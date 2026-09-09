---
title: "OPS - Discover"
source_system: confluence
confluence_page_id: "1348337680"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1348337680/OPS+-+Discover"
confluence_version: "5"
repository_path: "off-platform-search/ops-discover/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# OPS - Discover

# OPS - Discover

## Page status

| Field | Details |
| --- | --- |
| Parent page | Off-Platform Search |
| Workstream | Off-Platform Search |
| Phase | Discover |
| Status | In progress |
| Owner | Jose Andrade |
| Contributors | CX, Digital, Content, SEO, Knowledge, Service Owners, Data, Risk / Legal, Privacy |
| Related Y2 outcome | Search-as-channel improvements and service information architecture foundations |
| Related Jira deliverable | Off-Platform Search - Discovery |

---

## Discovery purpose

Off-Platform Search Discovery examines what customers experience when they begin a service journey outside City of Melbourne-owned channels.

The work is intended to establish a repeatable way to understand:

- whether customers can find information relevant to their intent;
- whether authoritative City of Melbourne information is recognised or preferred;
- whether information presented off-platform is accurate and current;
- whether customers can understand the information;
- whether the appropriate next action is clear;
- whether underlying City of Melbourne sources are sufficiently readable by emerging AI-enabled browsers and agents; and
- where failures or friction are occurring so improvements can be prioritised.

The methodology is designed to remain useful across different off-platform experiences and repeated testing over time.

It does not produce a single aggregated numerical score.

The dimensions are kept independent so that strength in one area does not hide a material weakness or high-risk failure in another.

---

## Current sprint focus

The current sprint will establish the first lightweight Off-Platform Search baseline.

The initial test uses:

- Google Search; and
- Google AI Mode.

This is the first application of the methodology, not the boundary of the methodology itself.

Future testing may apply the same core assessment framework to other off-platform search or AI-mediated experiences where there is a useful reason to do so.

The immediate focus is to:

- use a deliberately small set of priority customer intents;
- test those intents using realistic customer language;
- capture the conditions under which each test is run;
- record what the off-platform experience presents;
- validate material information against the authoritative City of Melbourne source;
- assess the customer result using stable dimensions;
- assess source readability separately where relevant;
- identify likely failure layers;
- flag high-risk outcomes separately;
- preserve uncertainty and evidence limitations; and
- identify findings that may influence Intelligent Front Door, Information Architecture or other Channel Strategy Y2 work.

The detailed queries, execution method and evidence capture for the first test are maintained in the separate Google Search + AI Mode test artefact.

---

## Key activities

| Activity | Description | Outcome |
| --- | --- | --- |
| Define the off-platform test approach | Establish a reusable method based on customer intent, stable assessment dimensions and consistent evidence capture | Reusable test framework |
| Define the initial test set | Select a manageable set of priority services and customer reasons for the first baseline | Initial test set |
| Run the first baseline | Apply the methodology to Google Search and Google AI Mode | Current-state baseline |
| Validate authoritative information | Compare material off-platform information with the relevant City of Melbourne source | Source-aligned evidence |
| Assess platform results | Assess what the customer receives against the stable platform-result dimensions | Dimension-level baseline |
| Assess source readability | Apply the dedicated AI browser readability method where the underlying source is relevant | Source readability evidence |
| Identify failure layers | Diagnose where Partial or Fail outcomes appear to originate | Failure-layer view |
| Identify high-risk outcomes | Flag cases where inaccurate or outdated information could materially affect a customer | High-risk view |
| Identify source dependencies | Record authoritative and competing sources that appear relevant to the result where they can be established | Initial source dependency view |
| Identify evidence gaps | Capture variable results, unclear provenance, tool limitations or insufficient evidence | Evidence gap summary |
| Connect findings to Y2 workstreams | Identify implications for Intelligent Front Door, Information Architecture and related work without duplicating their evidence | Cross-workstream implications |
| Assess next Discovery activity | Determine what additional testing is justified by the evidence | Updated Discovery priorities |

---

## Current sprint outputs

The current sprint is expected to establish an initial baseline rather than complete every possible Off-Platform Search discovery activity.

| Output | Sprint expectation |
| --- | --- |
| Test methodology | Confirm and apply the reusable assessment framework |
| First test artefact | Google Search + Google AI Mode test definition and evidence method |
| Platform-result baseline | Initial dimension-level assessment for the selected customer intents |
| Source readability evidence | Readability assessments for relevant City of Melbourne sources where required |
| Failure-layer view | Initial diagnosis of where observed problems occur |
| High-risk view | Separate visibility of materially risky outcomes |
| Source dependency view | Sources identifiable from the baseline |
| Evidence gap summary | Uncertainty, variability and missing evidence |
| Improvement signals | Initial opportunities for source, content, pathway or information architecture improvement |
| Cross-workstream implications | Findings relevant to other Channel Strategy Y2 work |
| Next Discovery priorities | Decision on what testing or investigation is justified next |

A comprehensive SEO, content or remediation backlog is not required at this stage.

Opportunities should initially be captured as evidence-backed signals.

---

## Test framework

The Off-Platform Search methodology separates three things:

1. **the customer intent being tested;**
2. **the result presented by the off-platform experience;** and
3. **the readability of the underlying authoritative source where relevant.**

This separation is important for maintaining comparison between different platforms and across repeated testing.

A poor customer result should not automatically be assumed to be a City of Melbourne content problem.

Likewise, a readable authoritative source does not guarantee that an off-platform experience will surface or represent it correctly.

---

## Core platform-result dimensions

The core dimensions assess the result presented to the customer by the off-platform experience.

These dimensions are intended to remain stable across platforms and over time.

| Dimension | Stable assessment question |
| --- | --- |
| Discoverability | Is information relevant to the customer's intent surfaced clearly enough to be found or recognised? |
| Authority | Can the customer recognise an appropriate authoritative source or pathway? |
| Accuracy | Is the information materially consistent with the authoritative source? |
| Currency | Does the information reflect the current authoritative source? |
| Understandability | Can the customer understand what the information means without needing organisational or specialist terminology? |
| Actionability | Does the off-platform result make the appropriate customer next step clear? |

Assess each dimension independently as:

- **Pass** — the dimension is satisfactorily met;
- **Partial** — the result is usable but contains a meaningful gap, ambiguity or weakness;
- **Fail** — the dimension is materially absent, incorrect, misleading or unusable; or
- **Unable to assess** — available evidence does not support a meaningful assessment.

The definitions and thresholds should remain stable between platforms and testing cycles.

Platform-specific evidence capture may differ without changing the underlying assessment dimensions.

---

## Source readability diagnostic

Source readability is assessed separately from the core platform-result dimensions.

Where a City of Melbourne webpage is relevant to the test, use the dedicated **AI browser readability criteria** to assess whether the underlying source can be understood and used by an AI-enabled browser or agent.

### Working definition

**AI browser readability** is the extent to which an AI-enabled browser can access, interpret and act on the underlying structure and content of a webpage sufficiently to understand the service and identify the appropriate next step.

The assessment focuses on machine interpretation of the live webpage rather than visual presentation alone.

---

## AI browser readability criteria

The dedicated readability assessment examines the following criteria.

### 1. Content is available in the page structure

Can the agent access the important customer-facing information through the page HTML and DOM?

Good readability means:

- important service information appears as accessible page content;
- headings, body content and instructions can be extracted;
- key information is not available only through an image or visual treatment; and
- dynamically generated content becomes available to the browser after the page loads.

**Result:** Yes / Partial / No

### 2. Page structure communicates meaning

Can the agent understand how the information is organised?

Good readability means:

- headings provide a meaningful hierarchy;
- related information is grouped logically;
- lists, sections and labels provide useful context;
- the main service purpose can be distinguished from navigation, promotional or supporting content; and
- information order supports interpretation of the customer task.

**Result:** Yes / Partial / No

### 3. Important elements can be identified

Can the agent distinguish important page elements from surrounding content?

This may include:

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

**Result:** Yes / Partial / No

### 4. Interactive controls have understandable purpose

Can the agent determine what interactive elements do?

Good readability means:

- links have meaningful destinations or labels;
- buttons communicate their action;
- form fields and controls can be associated with their purpose;
- actions do not depend entirely on visual position, styling or iconography; and
- the intended next step can be distinguished from secondary actions.

**Result:** Yes / Partial / No

### 5. Dynamic behaviour remains understandable

Can the browser understand the page after JavaScript and network activity have changed its state?

Good readability means:

- essential information loads successfully;
- dynamically revealed information becomes available in the DOM;
- network-driven content does not leave the agent with an incomplete view;
- state changes can be detected; and
- the agent can recognise when an interaction has succeeded, failed or requires another step.

**Result:** Yes / Partial / No

### 6. Text can be selected and extracted meaningfully

Can important information be isolated and extracted without losing its meaning?

Good readability means:

- relevant text can be selected or extracted;
- extracted content retains enough context to be interpreted correctly;
- headings and labels remain associated with the content they describe; and
- important caveats are not separated from the information they qualify.

**Result:** Yes / Partial / No

### 7. Non-text information has interpretable meaning

Where information is presented through SVGs, icons, diagrams or other visual elements, can the agent still understand its meaning?

Good readability means:

- important information is not dependent solely on graphics;
- visual elements have sufficient structural or textual context;
- icons do not carry essential meaning without labels; and
- diagrams or graphics supplement rather than replace critical service information.

**Result:** Yes / Partial / No

### 8. The customer task is actionable

Can the agent determine what the customer should do next from the underlying webpage?

The agent should be able to identify:

- the appropriate next action;
- where that action starts;
- any prerequisite information;
- conditions that affect the pathway; and
- whether human assistance is required instead.

**Result:** Yes / Partial / No

### 9. The pathway remains readable across steps

If the agent follows the next action, does the resulting state or page remain understandable?

Good readability means:

- the next page or state loads;
- the purpose of the new step is clear;
- context is not unexpectedly lost;
- the agent can recognise progression through the task; and
- errors and exceptions provide understandable information.

**Result:** Yes / Partial / No

### 10. The page does not depend on unsupported browser behaviour

Does the experience rely on functionality that an emerging agent browser may not support reliably?

Possible signals include:

- persistent authenticated sessions;
- complex browser fingerprinting or bot challenges;
- WebGL or rich media dependencies;
- unusual JavaScript execution requirements; and
- interaction patterns that require pixel-perfect rendering.

These should initially be classified as compatibility observations rather than automatically treated as City of Melbourne content failures.

**Result:** No issue / Possible issue / Blocking issue

---

## Overall readability classification

### Good

The agent can understand the main service information, identify important conditions and determine the appropriate next action from the underlying webpage structure.

### Partial

The page is technically accessible but the agent has difficulty interpreting some important information, controls, dynamic behaviour or pathway logic.

### Poor

The agent cannot reliably understand the service, important conditions or next action from the available webpage structure.

### Unable to assess

A browser or tool limitation prevents a meaningful assessment.

---

## Readability interpretation rule

A page should not fail simply because it renders differently from Chromium or another conventional browser.

The assessment is concerned with whether the agent can **understand and use the service pathway**, not whether the page achieves pixel-perfect visual fidelity.

Where a readability result is unclear, distinguish between:

- **content readability issue**;
- **structural or interaction issue**;
- **agent-browser compatibility issue**; and
- **tool limitation**.

These classifications describe the source or assessment environment.

They should not automatically be treated as failures of the off-platform platform that surfaced the source.

---

## Minimum AI readability success criteria

For the initial methodology, a page demonstrates good AI readability when an agent can:

1. access the important customer-facing content;
2. understand the main purpose of the page;
3. identify the important conditions or instructions;
4. distinguish the relevant next action;
5. understand dynamically loaded information where it is required; and
6. continue the customer task without depending primarily on visual interpretation.

---

## Readability scope boundary

The AI browser readability assessment is not:

- an SEO audit;
- an accessibility audit;
- a technical standards audit;
- an AI optimisation standard;
- a browser compatibility certification; or
- an assessment of every possible AI agent.

It is a Discovery method for identifying whether current service information and pathways are sufficiently machine-readable to support emerging AI-mediated customer journeys.

---

## Actionability distinction

Actionability exists at two different levels and should not be combined.

### Platform-result Actionability

**Question:** Does the off-platform result make the appropriate customer next step clear?

This assesses what the off-platform experience communicates to the customer.

### AI-readability customer-task actionability

**Question:** Can an AI-enabled browser determine the appropriate next action from the underlying webpage?

This assesses whether the City of Melbourne source itself exposes sufficient structure and information for the task to be interpreted and continued.

A platform may therefore pass one assessment and fail the other.

---

## Reuse of readability evidence

Readability is a property of the source and relevant pathway state rather than of the platform that surfaced it.

An existing readability assessment may be reused where:

- the same authoritative source is being assessed;
- the relevant page content and structure have not materially changed;
- the same relevant pathway or interaction state applies;
- dynamic behaviour relevant to the task has not materially changed; and
- assessment conditions remain sufficiently comparable.

Do not assume that the same URL always represents the same readability state.

Repeat the assessment where the page structure, content, pathway, interaction behaviour or relevant browser conditions have materially changed.

---

## Diagnostic overlays

The following information should be recorded alongside the core assessment without becoming additional performance dimensions.

### Failure layer

Where a platform-result dimension is **Partial** or **Fail**, identify the most likely point at which the customer experience breaks.

| Failure layer | Meaning |
| --- | --- |
| Discovery failure | Relevant authoritative information was not surfaced |
| Source-selection failure | A weaker, inappropriate or third-party source was preferred |
| Content interpretation failure | The correct source was available but its information was misunderstood or misrepresented |
| Currency failure | Returned information does not reflect the current authoritative source |
| Actionability failure | The off-platform result does not provide a sufficiently clear or correct next step |
| Source readability issue | A separately recorded source-readability issue contributes to the observed customer result |
| Tool limitation | Platform or assessment-tool behaviour prevents a meaningful assessment |

A source readability issue should reference the dedicated readability assessment rather than replace it.

Do not automatically classify every Partial or Poor readability result as a platform failure.

### High-risk flag

Separately flag a test where inaccurate, outdated or misleading information could materially affect the customer.

The High Risk flag does not change the definitions of Pass, Partial or Fail.

It indicates that:

- the consequence of failure is greater;
- stronger evidence may be needed before relying on the result; and
- remediation may warrant higher priority.

### Evidence confidence

Record evidence confidence separately where results are variable, incomplete or difficult to reproduce.

Confidence describes the strength of the evidence supporting the assessment.

It does not describe the quality of the customer experience and should not be treated as an assessment dimension.

---

## Comparison rule

To preserve comparison across platforms and over time:

- keep the six core platform-result dimensions stable;
- keep their assessment questions and thresholds stable;
- use the same customer intent and query where practical;
- record material differences in test conditions;
- assess each platform result independently;
- keep AI browser readability as a separate source-level diagnostic;
- preserve the native readability criteria and classifications;
- distinguish platform-result Actionability from webpage task Actionability;
- do not convert readability classifications into platform-result scores;
- do not count source readability as an additional platform-performance dimension;
- record failure layer, High Risk and evidence confidence as overlays rather than dimensions; and
- document future framework changes before comparing results collected under materially different versions.

Platform-specific evidence capture can evolve without changing the underlying comparison framework.

---

## Connection to Intelligent Front Door Define

Off-Platform Search should support, but not duplicate, Intelligent Front Door Define.

Use the baseline to identify whether off-platform discovery contributes evidence about:

- how customers express and interpret their need before reaching an owned channel;
- whether customers are directed toward the correct pathway;
- whether information gaps may contribute to avoidable contact;
- whether external results create expectations that conflict with the owned-channel experience;
- whether source-of-truth issues affect the front-door experience;
- whether source structure creates barriers for emerging AI-mediated journeys; and
- whether Information Architecture improvements could strengthen both owned and off-platform discovery.

Relevant findings can inform Intelligent Front Door opportunity statements.

Detailed Off-Platform Search evidence and analysis should remain in this workstream.

---

## Current sprint completion check

The current sprint activity is complete enough when:

- the initial priority customer intents have been agreed;
- realistic customer-language queries have been documented;
- the test method and evidence capture approach have been established;
- the first baseline has been run across the selected Google experiences;
- platform-result dimensions have been assessed consistently;
- material information has been validated against authoritative City of Melbourne sources;
- relevant source readability assessments have been completed or referenced;
- material failure layers are visible;
- high-risk outcomes are identified separately;
- evidence limitations and variable results are explicit;
- relevant implications for Intelligent Front Door or Information Architecture are identified; and
- the team can decide what Off-Platform Search discovery is worth doing next.

This sprint does **not** need to complete the full Discovery exit criteria unless the evidence genuinely supports doing so.
