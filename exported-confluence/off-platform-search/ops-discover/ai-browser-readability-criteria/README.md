---
title: "AI Browser Readability Criteria"
source_system: confluence
confluence_page_id: "1431535627"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1431535627/AI+Browser+Readability+Criteria"
confluence_version: "2"
repository_path: "off-platform-search/ops-discover/ai-browser-readability-criteria/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# AI Browser Readability Criteria

## 1.1. Purpose

Define a lightweight set of criteria for assessing whether a City of Melbourne webpage is readable and usable by an AI-enabled browser or agent.

These criteria are intended for the initial Off-Platform Search test methodology.

They do not define which services, pages or customer queries will be tested.

## 1.2. Working definition

**AI browser readability** is the extent to which an AI-enabled browser can access, interpret and act on the underlying structure and content of a webpage sufficiently to understand the service and identify the appropriate next step.

The assessment focuses on machine interpretation of the live webpage rather than visual presentation alone.

## 1.3. Readability criteria

### 1.3.1. Content is available in the page structure

**Question**

Can the agent access the important customer-facing information through the page HTML and DOM?

**Good readability means**

- important service information appears as accessible page content;
- headings, body content and instructions can be extracted;
- key information is not available only through an image or visual treatment;
- dynamically generated content becomes available to the browser after the page loads.

**Test result**

Yes / Partial / No

---

### 1.3.2. Page structure communicates meaning

**Question**

Can the agent understand how the information is organised?

**Good readability means**

- headings provide a meaningful hierarchy;
- related information is grouped logically;
- lists, sections and labels provide useful context;
- the main service purpose can be distinguished from navigation, promotional or supporting content;
- information order supports interpretation of the customer task.

**Test result**

Yes / Partial / No

---

### 1.3.3. Important elements can be identified

**Question**

Can the agent distinguish important page elements from surrounding content?

**Good readability means**

The agent can identify elements such as:

- service name;
- eligibility or conditions;
- fees;
- deadlines;
- instructions;
- warnings;
- contact information;
- status information;
- relevant links;
- next actions.

**Test result**

Yes / Partial / No

---

### 1.3.4. Interactive controls have understandable purpose

**Question**

Can the agent determine what interactive elements do?

**Good readability means**

- links have meaningful destinations or labels;
- buttons communicate their action;
- form fields and controls can be associated with their purpose;
- actions do not depend entirely on visual position, styling or iconography;
- the intended next step can be distinguished from secondary actions.

**Test result**

Yes / Partial / No

---

### 1.3.5. Dynamic behaviour remains understandable

**Question**

Can the browser understand the page after JavaScript and network activity have changed its state?

**Good readability means**

- essential information loads successfully;
- dynamically revealed information becomes available in the DOM;
- XHR or other network-driven content does not leave the agent with an incomplete view;
- state changes can be detected;
- the agent can recognise when an interaction has succeeded, failed or requires another step.

**Test result**

Yes / Partial / No

---

### 1.3.6. Text can be selected and extracted meaningfully

**Question**

Can important information be isolated and extracted without losing its meaning?

**Good readability means**

- relevant text can be selected or extracted;
- extracted content retains enough context to be interpreted correctly;
- headings and labels remain associated with the content they describe;
- important caveats are not separated from the information they qualify.

**Test result**

Yes / Partial / No

---

### 1.3.7. Non-text information has interpretable meaning

**Question**

Where information is presented through SVGs, icons, diagrams or other visual elements, can the agent still understand its meaning?

**Good readability means**

- important information is not dependent solely on graphics;
- visual elements have sufficient structural or textual context;
- icons do not carry essential meaning without labels;
- diagrams or graphics supplement rather than replace critical service information.

**Test result**

Yes / Partial / No

---

### 1.3.8. The customer task is actionable

**Question**

Can the agent determine what the customer should do next?

**Good readability means**

The agent can identify:

- the appropriate next action;
- where that action starts;
- any prerequisite information;
- conditions that affect the pathway;
- whether human assistance is required instead.

**Test result**

Yes / Partial / No

---

### 1.3.9. The pathway remains readable across steps

**Question**

If the agent follows the next action, does the resulting state or page remain understandable?

**Good readability means**

- the next page or state loads;
- the purpose of the new step is clear;
- context is not unexpectedly lost;
- the agent can recognise progression through the task;
- errors and exceptions provide understandable information.

**Test result**

Yes / Partial / No

---

### 1.3.10. The page does not depend on unsupported browser behaviour

**Question**

Does the experience rely on functionality that an emerging agent browser may not support reliably?

**Possible signals**

- persistent authenticated sessions;
- complex browser fingerprinting or bot challenges;
- WebGL or rich media dependencies;
- unusual JavaScript execution requirements;
- interaction patterns that require pixel-perfect rendering.

These should initially be classified as **compatibility observations**, not automatically as City of Melbourne content failures.

**Test result**

No issue / Possible issue / Blocking issue

## 1.4. Overall readability classification

### 1.4.1. Good

The agent can understand the main service information, identify important conditions and determine the appropriate next action from the underlying webpage structure.

### 1.4.2. Partial

The page is technically accessible but the agent has difficulty interpreting some important information, controls, dynamic behaviour or pathway logic.

### 1.4.3. Poor

The agent cannot reliably understand the service, important conditions or next action from the available webpage structure.

### 1.4.4. Unable to assess

A browser or tool limitation prevents a meaningful assessment.

## 1.5. Important interpretation rule

A page should not fail simply because it renders differently from Chromium.

The assessment is concerned with whether the agent can **understand and use the service pathway**, not whether the page achieves pixel-perfect visual fidelity.

Where a result is unclear, distinguish between:

- **content readability issue**;
- **structural or interaction issue**;
- **agent-browser compatibility issue**; and
- **tool limitation**.

## 1.6. Minimum success criteria

For the initial methodology, a page demonstrates good AI readability when an agent can:

1. access the important customer-facing content;
2. understand the main purpose of the page;
3. identify the important conditions or instructions;
4. distinguish the relevant next action;
5. understand dynamically loaded information where it is required; and
6. continue the customer task without depending primarily on visual interpretation.

## 1.7. Current scope boundary

This is a **readability assessment**, not:

- an SEO audit;
- an accessibility audit;
- a technical standards audit;
- an AI optimisation standard;
- a browser compatibility certification; or
- an assessment of every possible AI agent.

It is a Discovery method for identifying whether current service information and pathways are sufficiently machine-readable to support emerging AI-mediated customer journeys.
