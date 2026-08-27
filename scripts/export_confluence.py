#!/usr/bin/env python3
"""
Export a Confluence Cloud page tree to Markdown.

Purpose
-------
Create a one-way, Git-friendly snapshot of a Confluence page hierarchy.

Confluence remains the source of truth unless governance is explicitly changed.
Generated Markdown retains source provenance so content can be traced back to
its Confluence page.

Environment variables
---------------------
Required:
    CONFLUENCE_BASE_URL
        Example: https://your-domain.atlassian.net

    CONFLUENCE_EMAIL
        Atlassian account email used for API authentication.

    CONFLUENCE_API_TOKEN
        Atlassian API token. Never commit this value.

    CONFLUENCE_ROOT_PAGE_ID
        ID of the Confluence page whose tree should be exported.

Optional:
    CONFLUENCE_OUTPUT_DIR
        Default: exported-confluence

    CONFLUENCE_DOWNLOAD_ATTACHMENTS
        true / false
        Default: false

    CONFLUENCE_ATTACHMENT_EXTENSIONS
        Comma-separated allow-list.
        Default: pdf,png,jpg,jpeg,svg,gif

Install
-------
    pip install requests beautifulsoup4 markdownify

Run
---
    python scripts/export_confluence.py

Security
--------
Do not commit credentials, tokens, raw customer data, sensitive operational
extracts, or controlled material to the destination repository.
"""

from __future__ import annotations

import html
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as to_markdown
from requests.auth import HTTPBasicAuth


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.getenv("CONFLUENCE_EMAIL", "")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
ROOT_PAGE_ID = os.getenv("CONFLUENCE_ROOT_PAGE_ID", "")

OUTPUT_DIR = Path(
    os.getenv("CONFLUENCE_OUTPUT_DIR", "exported-confluence")
)

DOWNLOAD_ATTACHMENTS = (
    os.getenv("CONFLUENCE_DOWNLOAD_ATTACHMENTS", "false").lower() == "true"
)

ATTACHMENT_EXTENSIONS = {
    ext.strip().lower().lstrip(".")
    for ext in os.getenv(
        "CONFLUENCE_ATTACHMENT_EXTENSIONS",
        "pdf,png,jpg,jpeg,svg,gif",
    ).split(",")
    if ext.strip()
}

REQUEST_TIMEOUT = 30
RETRY_COUNT = 3
PAGE_LIMIT = 100


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

@dataclass
class PageNode:
    id: str
    title: str
    parent_id: str | None = None


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_config() -> None:
    missing = []

    if not BASE_URL:
        missing.append("CONFLUENCE_BASE_URL")
    if not EMAIL:
        missing.append("CONFLUENCE_EMAIL")
    if not API_TOKEN:
        missing.append("CONFLUENCE_API_TOKEN")
    if not ROOT_PAGE_ID:
        missing.append("CONFLUENCE_ROOT_PAGE_ID")

    if missing:
        print(
            "Missing required environment variables:\n- "
            + "\n- ".join(missing),
            file=sys.stderr,
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

session = requests.Session()
session.auth = HTTPBasicAuth(EMAIL, API_TOKEN)
session.headers.update(
    {
        "Accept": "application/json",
        "User-Agent": "confluence-markdown-export/1.0",
    }
)


def request(
    method: str,
    url: str,
    **kwargs: Any,
) -> requests.Response:
    """
    Make an authenticated Confluence request with simple retries.
    """
    for attempt in range(1, RETRY_COUNT + 1):
        response = session.request(
            method,
            url,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )

        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", "2"))
            time.sleep(retry_after)
            continue

        if response.status_code >= 500 and attempt < RETRY_COUNT:
            time.sleep(attempt * 2)
            continue

        response.raise_for_status()
        return response

    raise RuntimeError(f"Request failed after {RETRY_COUNT} attempts: {url}")


def api_url(path: str) -> str:
    return f"{BASE_URL}/wiki/api/v2/{path.lstrip('/')}"


def get_paginated(
    first_url: str,
    params: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """
    Retrieve all results from a Confluence v2 cursor-paginated endpoint.
    """
    results: list[dict[str, Any]] = []
    next_url: str | None = first_url
    first_request = True

    while next_url:
        response = request(
            "GET",
            next_url,
            params=params if first_request else None,
        )
        payload = response.json()

        results.extend(payload.get("results", []))

        next_link = payload.get("_links", {}).get("next")

        if next_link:
            next_url = urljoin(BASE_URL, next_link)
        else:
            next_url = None

        first_request = False

    return results


# ---------------------------------------------------------------------------
# Confluence retrieval
# ---------------------------------------------------------------------------

def get_page(page_id: str) -> dict[str, Any]:
    response = request(
        "GET",
        api_url(f"pages/{page_id}"),
        params={
            "body-format": "storage",
            "include-version": "true",
        },
    )
    return response.json()


def get_direct_child_pages(page_id: str) -> list[PageNode]:
    """
    Retrieve direct child content and retain pages only.

    Confluence's direct-children endpoint can also return folders,
    databases, embeds and whiteboards.
    """
    children = get_paginated(
        api_url(f"pages/{page_id}/direct-children"),
        params={"limit": PAGE_LIMIT},
    )

    page_children: list[PageNode] = []

    for child in children:
        if child.get("type") != "page":
            continue

        page_children.append(
            PageNode(
                id=str(child["id"]),
                title=child.get("title", f"page-{child['id']}"),
                parent_id=page_id,
            )
        )

    return page_children


def get_attachments(page_id: str) -> list[dict[str, Any]]:
    return get_paginated(
        api_url(f"pages/{page_id}/attachments"),
        params={"limit": PAGE_LIMIT},
    )


# ---------------------------------------------------------------------------
# Naming
# ---------------------------------------------------------------------------

def slugify(value: str) -> str:
    """
    Create stable, filesystem-safe lowercase names.
    """
    value = html.unescape(value)
    value = value.strip().lower()

    # Remove common numeric Confluence ordering prefixes.
    value = re.sub(r"^\d+[\.\-_ ]+", "", value)

    # Normalise punctuation.
    value = value.replace("&", "and")
    value = re.sub(r"[—–]", "-", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value)

    return value.strip("-") or "untitled"


def safe_filename(filename: str) -> str:
    """
    Keep attachment extensions while removing unsafe filename characters.
    """
    path = Path(filename)
    stem = slugify(path.stem)
    suffix = path.suffix.lower()
    return f"{stem}{suffix}"


# ---------------------------------------------------------------------------
# Confluence storage -> Markdown
# ---------------------------------------------------------------------------

def simplify_confluence_markup(storage_html: str) -> str:
    """
    Reduce common Confluence-specific markup before Markdown conversion.

    The goal is readable source material, not pixel-perfect reproduction.
    Complex macros are deliberately represented conservatively.
    """
    soup = BeautifulSoup(storage_html or "", "html.parser")

    # Remove script/style content if present.
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    # Convert Confluence structured macros into readable placeholders
    # while retaining visible text where possible.
    for macro in soup.find_all(
        lambda tag: getattr(tag, "name", "") in {
            "ac:structured-macro",
            "ac:macro",
        }
    ):
        macro_name = (
            macro.get("ac:name")
            or macro.get("name")
            or "confluence-macro"
        )

        text = macro.get_text(" ", strip=True)

        replacement = soup.new_tag("div")
        replacement.string = (
            f"[Confluence macro: {macro_name}]"
            + (f" {text}" if text else "")
        )

        macro.replace_with(replacement)

    # Replace Confluence user mentions with readable text where possible.
    for mention in soup.find_all(
        lambda tag: getattr(tag, "name", "") == "ri:user"
    ):
        account_id = (
            mention.get("ri:account-id")
            or mention.get("account-id")
            or "user"
        )
        mention.replace_with(f"@{account_id}")

    return str(soup)


def storage_to_markdown(storage_html: str) -> str:
    cleaned_html = simplify_confluence_markup(storage_html)

    markdown = to_markdown(
        cleaned_html,
        heading_style="ATX",
        bullets="-",
        strip=["style", "script"],
    )

    # Reduce excessive blank lines.
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)

    return markdown.strip()


# ---------------------------------------------------------------------------
# Provenance
# ---------------------------------------------------------------------------

def page_source_url(page: dict[str, Any]) -> str:
    links = page.get("_links", {})

    webui = links.get("webui")
    if webui:
        return urljoin(BASE_URL, webui)

    return f"{BASE_URL}/wiki/pages/viewpage.action?pageId={page['id']}"


def yaml_escape(value: Any) -> str:
    text = str(value or "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def build_frontmatter(
    page: dict[str, Any],
    relative_path: Path,
) -> str:
    version = page.get("version") or {}

    lines = [
        "---",
        f"title: {yaml_escape(page.get('title', 'Untitled'))}",
        "source_system: confluence",
        f"confluence_page_id: {yaml_escape(page.get('id', ''))}",
        f"confluence_space_id: {yaml_escape(page.get('spaceId', ''))}",
        f"confluence_status: {yaml_escape(page.get('status', ''))}",
        f"confluence_url: {yaml_escape(page_source_url(page))}",
        f"confluence_version: {yaml_escape(version.get('number', ''))}",
        f"repository_path: {yaml_escape(relative_path.as_posix())}",
        "generated: true",
        "---",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Attachments
# ---------------------------------------------------------------------------

def should_download_attachment(filename: str) -> bool:
    extension = Path(filename).suffix.lower().lstrip(".")
    return bool(extension and extension in ATTACHMENT_EXTENSIONS)


def download_page_attachments(
    page_id: str,
    destination: Path,
) -> list[Path]:
    if not DOWNLOAD_ATTACHMENTS:
        return []

    attachments = get_attachments(page_id)

    if not attachments:
        return []

    destination.mkdir(parents=True, exist_ok=True)

    downloaded: list[Path] = []

    for attachment in attachments:
        filename = attachment.get("title") or attachment.get("filename")

        if not filename:
            continue

        if not should_download_attachment(filename):
            print(f"  skip attachment: {filename}")
            continue

        download_link = (
            attachment.get("downloadLink")
            or attachment.get("_links", {}).get("download")
        )

        if not download_link:
            print(f"  no download link: {filename}")
            continue

        output_path = destination / safe_filename(filename)

        response = request(
            "GET",
            urljoin(BASE_URL, download_link),
            allow_redirects=True,
        )

        output_path.write_bytes(response.content)
        downloaded.append(output_path)

        print(f"  attachment: {output_path}")

    return downloaded


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------

def page_body_storage(page: dict[str, Any]) -> str:
    body = page.get("body") or {}
    storage = body.get("storage") or {}
    return storage.get("value") or ""


def write_page(
    page: dict[str, Any],
    destination: Path,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)

    relative_path = destination.relative_to(OUTPUT_DIR)

    markdown = storage_to_markdown(page_body_storage(page))
    frontmatter = build_frontmatter(page, relative_path)

    notice = (
        "> **Source note:** Generated from Confluence. "
        "Do not edit directly while Confluence remains the source of truth."
    )

    content = (
        f"{frontmatter}\n\n"
        f"{notice}\n\n"
        f"# {page.get('title', 'Untitled')}\n\n"
        f"{markdown}\n"
    )

    destination.write_text(content, encoding="utf-8")


def export_page_tree(
    page_id: str,
    directory: Path,
    *,
    is_root: bool = False,
) -> None:
    page = get_page(page_id)
    title = page.get("title", f"page-{page_id}")

    if is_root:
        page_directory = directory
        markdown_path = directory / "README.md"
    else:
        page_directory = directory / slugify(title)
        markdown_path = page_directory / "README.md"

    print(f"export: {title}")
    print(f"  -> {markdown_path}")

    write_page(page, markdown_path)

    download_page_attachments(
        page_id,
        page_directory / "assets",
    )

    children = get_direct_child_pages(page_id)

    for child in children:
        export_page_tree(
            child.id,
            page_directory,
            is_root=False,
        )


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def write_generated_gitignore() -> None:
    gitignore = OUTPUT_DIR / ".gitignore"

    if gitignore.exists():
        return

    gitignore.write_text(
        "\n".join(
            [
                "# Local/export artefacts",
                ".DS_Store",
                "__pycache__/",
                "*.pyc",
                "",
            ]
        ),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    validate_config()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Confluence -> Markdown export")
    print(f"Root page: {ROOT_PAGE_ID}")
    print(f"Output:    {OUTPUT_DIR.resolve()}")
    print(
        "Attachments: "
        + ("enabled" if DOWNLOAD_ATTACHMENTS else "disabled")
    )
    print()

    export_page_tree(
        ROOT_PAGE_ID,
        OUTPUT_DIR,
        is_root=True,
    )

    write_generated_gitignore()

    print()
    print("Export complete.")
    print()
    print("Review the generated repository before committing it.")
    print("Recommended next commands:")
    print(f"  cd {OUTPUT_DIR}")
    print("  git init")
    print("  git add .")
    print('  git commit -m "Initial Confluence export"')


if __name__ == "__main__":
    main()