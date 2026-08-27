---
title: "Off-Platform Search — Initial Search Test Script"
source_system: confluence
confluence_page_id: "1430552580"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1430552580/Off-Platform+Search+Initial+Search+Test+Script"
confluence_version: "2"
repository_path: "off-platform-search/ops-discover/off-platform-search-initial-search-test-script/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Off-Platform Search — Initial Search Test Script

## 1.1. Purpose

Define a lightweight and repeatable method for testing how City of Melbourne information performs in off-platform search and AI-mediated browsing.

This first script does **not** define the final test set.

Its purpose is to establish:

- the assessment workflow;
- the success criteria;
- the evidence to capture;
- the test conditions;
- the treatment of uncertainty;
- the distinction between search visibility, AI answer quality and agent-browser readability.

The validated method can then be applied to a demand-led test set derived from Intelligent Front Door priority services and contact reasons.

## 1.2. Test objective

Determine whether a customer starting outside City of Melbourne-owned channels can:

1. find relevant City of Melbourne information;
2. identify an authoritative source;
3. receive information that is accurate and current;
4. understand what to do next; and
5. where agent-browser testing is used, navigate the service pathway sufficiently to continue the task.

## 1.3. Assessment model

Use the following assessment sequence:

**Customer intent**  
→ **Off-platform discovery**  
→ **Source selection**  
→ **Information interpretation**  
→ **Actionability**  
→ **Agent-browser navigation, where applicable**

These stages should be assessed separately.

A successful search result does not automatically mean the information is readable or actionable.

Similarly, an AI-generated answer may be useful even when the underlying service pathway is difficult for an agent to navigate.

## 1.4. Test workflow

### 1.4.1. Establish the test condition

Record:

- date and time;
- tool or search environment;
- signed-in or signed-out state where relevant;
- location or geography setting where relevant;
- whether live web access is enabled;
- browser or agent-browser environment;
- any material configuration that could influence the result.

### 1.4.2. Run the test input

Use the agreed customer-like query or task instruction.

Do not modify the wording during the initial run.

Record the exact input used.

### 1.4.3. Observe off-platform discovery

Capture:

- whether City of Melbourne information appears;
- which source is presented;
- whether the source appears authoritative;
- whether competing or third-party sources are presented more prominently;
- whether the result is clearly relevant to the customer intent.

### 1.4.4. Assess information quality

Assess whether the surfaced information is:

- accurate;
- current;
- relevant;
- understandable;
- sufficiently complete for the customer need;
- appropriately caveated where the answer depends on conditions.

### 1.4.5. Assess actionability

Determine whether the customer is given a clear next step.

Examples of a next step may include:

- visiting an authoritative page;
- starting a transaction;
- checking eligibility;
- reporting an issue;
- requesting support;
- checking status;
- contacting the correct service.

Assess the pathway, not just whether a link exists.

### 1.4.6. Assess agent-browser readability, where applicable

Where an agent-oriented browser such as Kitesurf is used, assess whether the browser or agent can:

- access the relevant content;
- identify the main purpose of the page;
- interpret important service information;
- recognise meaningful controls or links;
- identify the appropriate next action;
- navigate sufficiently to continue the task.

Do not treat agent-browser compatibility as equivalent to customer experience quality.

### 1.4.7. Record outcome and confidence

Record the result using:

- **Yes**
- **Partial**
- **No**
- **Not tested**

Also record:

- confidence: High / Medium / Low;
- material observation;
- known limitation or test condition;
- whether further investigation is required.

## 1.5. Success criteria

The method should consider an outcome successful when the evidence shows that:

### 1.5.1. Discoverability

The relevant City of Melbourne source can be found from the customer intent.

### 1.5.2. Authority

The result clearly identifies or relies on an appropriate City of Melbourne source.

### 1.5.3. Accuracy

The surfaced information is materially consistent with the authoritative source.

### 1.5.4. Currency

There is no observable indication that the information is outdated or superseded.

### 1.5.5. Understandability

The customer can reasonably understand the answer or service information without needing internal organisational knowledge.

### 1.5.6. Actionability

The result provides a clear and appropriate next step.

### 1.5.7. Agent readability

Where tested, the agent browser can access and interpret the important service information.

### 1.5.8. Agent navigability

Where tested, the agent can identify and follow the intended service pathway sufficiently to continue the task.

## 1.6. Result classification

Use a simple classification rather than a weighted score.

### 1.6.1. Pass

The result is authoritative, materially accurate, understandable and actionable.

### 1.6.2. Partial

The result is usable but contains a meaningful gap, ambiguity, incomplete pathway or confidence issue.

### 1.6.3. Fail

The result is materially inaccurate, outdated, misleading, non-authoritative or does not provide a usable pathway.

### 1.6.4. Unable to assess

The test environment or tool behaviour prevents a meaningful conclusion.

## 1.7. Risk flag

Flag the test as **High risk** where an incorrect or outdated answer could materially affect the customer.

Potential risk characteristics include:

- statutory or legal obligations;
- enforcement or penalties;
- financial amounts;
- deadlines;
- individual eligibility;
- safety or urgent situations;
- sensitive circumstances;
- personal case or status information.

High-risk results should require stronger evidence of authoritative sourcing and accuracy.

## 1.8. Failure interpretation

Where a test fails, identify the likely failure layer before recommending action.

Possible layers include:

**Discovery failure**  
The relevant City of Melbourne information was not surfaced.

**Source-selection failure**  
A weaker, outdated or third-party source was preferred.

**Content interpretation failure**  
The correct source was found but the information was misunderstood.

**Currency failure**  
The surfaced information does not reflect the current authoritative source.

**Actionability failure**  
The answer is informative but does not provide a usable next step.

**Agent-readability failure**  
The page can be used by a person but important information is not readily interpretable by the agent.

**Agent-navigation failure**  
The agent can understand the information but cannot identify or operate the next service step.

**Tool limitation**  
The observed failure appears to result from the search or agent-browser environment rather than the City of Melbourne source.

Do not automatically attribute every failed test to City of Melbourne content.

## 1.9. Repeatability rule

AI and agent-mediated results may vary between runs.

The assessment should therefore record observed behaviour rather than claim universal behaviour.

Repeat a test only when:

- the result is materially ambiguous;
- a tool failure is suspected;
- a high-risk result requires confirmation; or
- comparison is needed to distinguish source failure from tool limitation.

## 1.10. Minimum evidence record

For each future test, capture:

| Field | Required |
| --- | --- |
| Test input | Yes |
| Customer intent | Yes |
| Test environment | Yes |
| Date/time | Yes |
| Source surfaced | Yes |
| Authoritative source identified | Yes |
| Accuracy | Yes |
| Currency | Yes |
| Understandability | Yes |
| Actionability | Yes |
| Agent readability | Where applicable |
| Agent navigability | Where applicable |
| Risk | Yes |
| Overall result | Yes |
| Confidence | Yes |
| Observation / caveat | Yes |

## 1.11. Method success criteria

This initial methodology is considered viable for the wider Off-Platform Search discovery if the team can:

1. run the same workflow consistently across different search or AI environments;
2. distinguish discovery, answer-quality and agent-browser issues;
3. compare surfaced information with an authoritative source;
4. identify whether the customer receives a usable next step;
5. record uncertainty and tool limitations without overclaiming;
6. apply the method without specialist technical tooling for every test; and
7. use the resulting evidence to support subsequent design or content decisions.

## 1.12. Current scope boundary

This script defines the **test method only**.

It does not yet define:

- specific priority services;
- final customer queries;
- target URLs;
- the number of tests;
- a fixed AI tool set;
- a fixed agent-browser tool;
- a scoring or benchmarking model;
- remediation actions.

Those should be confirmed when the demand-led test set is created from Intelligent Front Door priority services and contact reasons.
