---
title: "AI Browser Readability Criteria"
source_system: confluence
confluence_page_id: "1431535627"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1431535627/AI+Browser+Readability+Criteria"
confluence_version: "5"
repository_path: "off-platform-search/ops-discover/ai-browser-readability-criteria/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# AI Browser Readability Criteria

# 1. AI Browser Readability Criteria

**Status:** In progress   
**Workstream:** Channel Strategy Y2 — Off-Platform Search   
**Phase:** Discover   
**Method type:** Source readability diagnostic

---

## 1.1. Purpose

Define a lightweight set of criteria for assessing whether a City of Melbourne webpage is readable and usable by an AI-enabled browser or agent.

These criteria support the Off-Platform Search discovery methodology.

They assess the underlying City of Melbourne source or pathway and are intentionally separate from the assessment of what an off-platform search or AI experience presents to a customer.

They do not define:

- which services will be tested;
- which customer intents or queries will be used;
- which off-platform platforms will be tested; or
- whether an off-platform result itself is successful.

Those decisions belong to the relevant test definition.

---

## 1.2. Relationship to the Off-Platform Search framework

The broader Off-Platform Search methodology separates:

1. the customer intent being tested;
2. the result presented by the off-platform experience; and
3. the readability of the underlying authoritative source where relevant.

The core platform-result dimensions are:

- Discoverability;
- Authority;
- Accuracy;
- Currency;
- Understandability; and
- Actionability.

AI browser readability is **not an additional platform-result dimension**.

It is a separate source-level diagnostic used to understand whether the structure, content and interaction design of an authoritative webpage can be interpreted reliably by an AI-enabled browser or agent.

This distinction protects comparison across platforms and over time.

A platform may surface the correct source but represent it poorly.

A source may also be highly readable while an off-platform experience fails to surface it.

The two assessments should therefore remain separate.

---

## 1.3. Working definition

**AI browser readability** is the extent to which an AI-enabled browser can access, interpret and act on the underlying structure and content of a webpage sufficiently to understand the service and identify the appropriate next step.

The assessment focuses on machine interpretation of the live webpage rather than visual presentation alone.

---

## 1.4. Readability criteria

### 1.4.1. Content is available in the page structure

**Question**

Can the agent access the important customer-facing information through the page HTML and DOM?

**Good readability means**

- important service information appears as accessible page content;
- headings, body content and instructions can be extracted;
- key information is not available only through an image or visual treatment; and
- dynamically generated content becomes available to the browser after the page loads.

**Test result**

Yes / Partial / No

---

### 1.4.2. Page structure communicates meaning

**Question**

Can the agent understand how the information is organised?

**Good readability means**

- headings provide a meaningful hierarchy;
- related information is grouped logically;
- lists, sections and labels provide useful context;
- the main service purpose can be distinguished from navigation, promotional or supporting content; and
- information order supports interpretation of the customer task.

**Test result**

Yes / Partial / No

---

### 1.4.3. Important elements can be identified

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
- relevant links; and
- next actions.

**Test result**

Yes / Partial / No

---

### 1.4.4. Interactive controls have understandable purpose

**Question**

Can the agent determine what interactive elements do?

**Good readability means**

- links have meaningful destinations or labels;
- buttons communicate their action;
- form fields and controls can be associated with their purpose;
- actions do not depend entirely on visual position, styling or iconography; and
- the intended next step can be distinguished from secondary actions.

**Test result**

Yes / Partial / No

---

### 1.4.5. Dynamic behaviour remains understandable

**Question**

Can the browser understand the page after JavaScript and network activity have changed its state?

**Good readability means**

- essential information loads successfully;
- dynamically revealed information becomes available in the DOM;
- network-driven content does not leave the agent with an incomplete view;
- state changes can be detected; and
- the agent can recognise when an interaction has succeeded, failed or requires another step.

**Test result**

Yes / Partial / No

---

### 1.4.6. Text can be selected and extracted meaningfully

**Question**

Can important information be isolated and extracted without losing its meaning?

**Good readability means**

- relevant text can be selected or extracted;
- extracted content retains enough context to be interpreted correctly;
- headings and labels remain associated with the content they describe; and
- important caveats are not separated from the information they qualify.

**Test result**

Yes / Partial / No

---

### 1.4.7. Non-text information has interpretable meaning

**Question**

Where information is presented through SVGs, icons, diagrams or other visual elements, can the agent still understand its meaning?

**Good readability means**

- important information is not dependent solely on graphics;
- visual elements have sufficient structural or textual context;
- icons do not carry essential meaning without labels; and
- diagrams or graphics supplement rather than replace critical service information.

**Test result**

Yes / Partial / No

---

### 1.4.8. The customer task is actionable

**Question**

Can the agent determine what the customer should do next from the underlying webpage?

**Good readability means**

The agent can identify:

- the appropriate next action;
- where that action starts;
- any prerequisite information;
- conditions that affect the pathway; and
- whether human assistance is required instead.

**Test result**

Yes / Partial / No

---

### 1.4.9. The pathway remains readable across steps

**Question**

If the agent follows the next action, does the resulting state or page remain understandable?

**Good readability means**

- the next page or state loads;
- the purpose of the new step is clear;
- context is not unexpectedly lost;
- the agent can recognise progression through the task; and
- errors and exceptions provide understandable information.

**Test result**

Yes / Partial / No

---

### 1.4.10. The page does not depend on unsupported browser behaviour

**Question**

Does the experience rely on functionality that an emerging agent browser may not support reliably?

**Possible signals**

- persistent authenticated sessions;
- complex browser fingerprinting or bot challenges;
- WebGL or rich media dependencies;
- unusual JavaScript execution requirements; and
- interaction patterns that require pixel-perfect rendering.

These should initially be classified as compatibility observations, not automatically as City of Melbourne content failures.

**Test result**

No issue / Possible issue / Blocking issue

---

## 1.5. Overall readability classification

### 1.5.1. Good

The agent can understand the main service information, identify important conditions and determine the appropriate next action from the underlying webpage structure.

### 1.5.2. Partial

The page is technically accessible but the agent has difficulty interpreting some important information, controls, dynamic behaviour or pathway logic.

### 1.5.3. Poor

The agent cannot reliably understand the service, important conditions or next action from the available webpage structure.

### 1.5.4. Unable to assess

A browser or tool limitation prevents a meaningful assessment.

---

## 1.6. Interpretation rule

A page should not fail simply because it renders differently from Chromium or another conventional browser.

The assessment is concerned with whether the agent can **understand and use the service pathway**, not whether the page achieves pixel-perfect visual fidelity.

Where a result is unclear, distinguish between:

- **Content readability issue** — important information is unavailable, inaccessible or loses necessary meaning when interpreted;
- **Structural or interaction issue** — page structure, controls, dynamic states or pathway logic cannot be reliably interpreted;
- **Agent-browser compatibility issue** — the experience relies on browser behaviour that an emerging agent browser may not support reliably; and
- **Tool limitation** — the assessment tool prevents a meaningful conclusion.

These classifications describe the source or assessment environment.

They should not automatically be treated as failures of the off-platform platform that surfaced the source.

---

## 1.7. Actionability distinction

Actionability appears in both the platform-result framework and the readability assessment, but they measure different things.

### 1.7.1. Platform-result Actionability

**Question**

Does the off-platform result make the appropriate customer next step clear?

This assesses what the off-platform experience communicates to the customer.

### 1.7.2. AI-readability customer-task actionability

**Question**

Can an AI-enabled browser determine the appropriate next action from the underlying webpage?

This assesses whether the City of Melbourne source itself exposes enough structure and information for the task to be interpreted and continued.

A platform may pass one assessment and fail the other.

The two results should not be merged.

---

## 1.8. Minimum success criteria

For the initial methodology, a page demonstrates good AI readability when an agent can:

1. access the important customer-facing content;
2. understand the main purpose of the page;
3. identify the important conditions or instructions;
4. distinguish the relevant next action;
5. understand dynamically loaded information where it is required; and
6. continue the customer task without depending primarily on visual interpretation.

---

## 1.9. Evidence reuse

Readability is a property of the source and relevant pathway state rather than of the platform that surfaced it.

An existing readability assessment may be reused where:

- the same authoritative source is being assessed;
- the relevant page content and structure have not materially changed;
- the same relevant pathway or interaction state applies;
- dynamic behaviour relevant to the task has not materially changed; and
- assessment conditions remain sufficiently comparable.

Do not assume that the same URL always represents the same readability state.

Repeat the assessment where:

- page content materially changes;
- page structure changes;
- important controls or interactions change;
- the relevant pathway changes;
- dynamic behaviour affecting the task changes; or
- assessment conditions are no longer sufficiently comparable.

---

## 1.10. Recording the assessment

For each assessed source, record at minimum:

| Field | Record |
| --- | --- |
| Source / page |  |
| URL |  |
| Related customer intent |  |
| Assessment date |  |
| Tester |  |
| Browser / agent |  |
| Relevant pathway state |  |
| Content available in page structure | Yes / Partial / No |
| Page structure communicates meaning | Yes / Partial / No |
| Important elements identifiable | Yes / Partial / No |
| Interactive controls understandable | Yes / Partial / No |
| Dynamic behaviour understandable | Yes / Partial / No |
| Text extractable with meaning preserved | Yes / Partial / No |
| Non-text information interpretable | Yes / Partial / No |
| Customer task actionable | Yes / Partial / No |
| Pathway readable across steps | Yes / Partial / No |
| Unsupported browser behaviour | No issue / Possible issue / Blocking issue |
| Overall readability | Good / Partial / Poor / Unable to assess |
| Issue type | Content readability / Structural or interaction / Agent-browser compatibility / Tool limitation |
| Evidence / observations |  |

Do not convert the criterion results or overall readability classification into the Off-Platform Search platform-result Pass / Partial / Fail scale.

---

## 1.11. Relationship to failure diagnosis

Where a source readability issue contributes to an observed off-platform result, the relevant test may record **Source readability issue** as a failure-layer diagnosis.

The detailed evidence should remain in this readability assessment.

A Partial or Poor readability result does not automatically mean that the platform that surfaced the source has failed.

Likewise, a platform-result failure should not automatically be attributed to source readability without supporting evidence.

---

## 1.12. Current scope boundary

This is a **readability assessment**, not:

- an SEO audit;
- an accessibility audit;
- a technical standards audit;
- an AI optimisation standard;
- a browser compatibility certification; or
- an assessment of every possible AI agent.

It is a Discovery method for identifying whether current service information and pathways are sufficiently machine-readable to support emerging AI-mediated customer journeys.

---

## 1.13. Comparison rule

To preserve the usefulness of readability evidence over time:

- keep the 10 criteria stable;
- preserve the criterion-level result scales;
- preserve the overall Good / Partial / Poor / Unable to assess classification;
- record the browser or agent used;
- record material differences in assessment conditions;
- distinguish compatibility issues from source readability problems;
- preserve the relevant page or pathway state;
- reassess when material source or interaction changes occur; and
- document any future methodology change before comparing results collected under materially different versions.

The detailed test implementation may evolve without changing the underlying readability criteria.
