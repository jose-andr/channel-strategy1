---
title: "Test 01: Evidence Capture Template"
source_system: confluence
confluence_page_id: "1510670340"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1510670340/Test+01+Evidence+Capture+Template"
confluence_version: "6"
repository_path: "off-platform-search/ops-discover/test-01-google-search-ai-mode-baseline/test-01-evidence-capture-template/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Test 01: Evidence Capture Template

# 1. Off-Platform Search — Evidence Capture Template

**Status:** In progress   
**Workstream:** Channel Strategy Y2 — Off-Platform Search   
**Phase:** Discover   
**Artefact type:** Reusable test evidence template

---

## 1.1. Purpose

Use this template to record evidence from an individual Off-Platform Search test execution.

Create one record for each:

**customer intent × platform**

The template separates:

1. test conditions;
2. observed platform evidence;
3. authoritative-source validation;
4. core platform-result assessment;
5. diagnostic overlays; and
6. source readability evidence where relevant.

This structure should remain stable enough to support comparison between platforms and repeated testing over time.

Do not combine the assessment dimensions into a single numerical score.

---

## 1.2. Test identification

| Field | Record |
| --- | --- |
| Test ID |  |
| Test definition |  |
| Customer intent |  |
| Customer-language query |  |
| Service / contact reason |  |
| Platform |  |
| Test date |  |
| Test time |  |
| Tester |  |

---

## 1.3. Test conditions

Record the conditions that could materially influence the result.

| Field | Record |
| --- | --- |
| Device |  |
| Browser |  |
| Signed into platform | Yes / No |
| Private / incognito mode | Yes / No |
| Relevant platform feature available | Yes / No |
| Location or localisation relevant | Yes / No / Unknown |
| Other relevant condition |  |

Do not attempt to eliminate all platform variability.

Record enough context to understand whether materially different conditions may affect later comparison.

---

## 1.4. Observed platform result

Record what was actually presented before interpreting its quality.

### 1.4.1. Result summary

**Observed result:**

> Add concise factual description.

### 1.4.2. Platform evidence

| Field | Record |
| --- | --- |
| Relevant City of Melbourne information surfaced | Yes / Partial / No |
| City of Melbourne identified | Yes / No / Unclear |
| City of Melbourne source / page |  |
| Other sources presented or cited |  |
| Result position, where applicable |  |
| Result title, where applicable |  |
| Displayed source / domain, where applicable |  |
| Returned URL, where applicable |  |
| Generated answer / summary, where applicable |  |
| Important conditions or qualifications presented |  |
| Recommended next action |  |
| Competing source or pathway observations |  |

Capture platform-specific evidence without changing the underlying assessment dimensions.

---

## 1.5. Authoritative-source validation

Do not treat the off-platform answer itself as the source of truth.

| Field | Record |
| --- | --- |
| Authoritative City of Melbourne source |  |
| Source URL |  |
| Source checked | Yes / No |
| Source appears current | Yes / No / Unclear |
| Material information required for this intent |  |
| Important conditions / qualifications |  |
| Correct customer next action |  |

### 1.5.1. Validation notes

> Record any material difference between the platform result and the authoritative source.

Do not infer source provenance where it cannot be established.

---

## 1.6. Core platform-result assessment

Assess each dimension independently.

### 1.6.1. Discoverability

**Question:**   
Is information relevant to the customer's intent surfaced clearly enough to be found or recognised?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

### 1.6.2. Authority

**Question:**   
Can the customer recognise an appropriate authoritative source or pathway?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

### 1.6.3. Accuracy

**Question:**   
Is the information materially consistent with the authoritative source?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

### 1.6.4. Currency

**Question:**   
Does the information reflect the current authoritative source?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

### 1.6.5. Understandability

**Question:**   
Can the customer understand what the information means without needing organisational or specialist terminology?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

### 1.6.6. Actionability

**Question:**   
Does the off-platform result make the appropriate customer next step clear?

**Result:**   
Pass / Partial / Fail / Unable to assess

**Evidence:**

> Add evidence supporting the result.

---

## 1.7. Dimension summary

| Dimension | Result |
| --- | --- |
| Discoverability |  |
| Authority |  |
| Accuracy |  |
| Currency |  |
| Understandability |  |
| Actionability |  |

Do not calculate an average or aggregated score.

---

## 1.8. Diagnostic overlays

### 1.8.1. Failure layer

Complete where one or more core dimensions are Partial or Fail.

**Most likely failure layer:**

- Discovery failure
- Source-selection failure
- Content interpretation failure
- Currency failure
- Actionability failure
- Source readability issue
- Tool limitation
- Not applicable
- Unclear

**Evidence:**

> Explain why this appears to be the most likely point of failure.

A failure layer is diagnostic and does not replace the individual dimension results.

---

### 1.8.2. High-risk flag

**High Risk:**   
Yes / No

**Reason:**

> Record the potential consequence if the information is inaccurate, outdated or misleading.

The High Risk flag does not alter the Pass / Partial / Fail thresholds.

---

### 1.8.3. Evidence confidence

**Confidence:**   
High / Medium / Low

**Reason:**

> Record relevant reproducibility, source, provenance or tool limitations.

Confidence describes the strength of the evidence, not the quality of the customer experience.

---

## 1.9. Source readability

Complete this section only where a source-readability assessment is relevant to interpreting the test outcome.

Do not score source readability as an additional platform-result dimension.

### 1.9.1. Readability evidence

**Readability assessment required:**   
Yes / No

**Existing assessment reusable:**   
Yes / No / Not applicable

**Readability assessment reference:**

> Add page or evidence reference.

**Overall readability:**   
Good / Partial / Poor / Unable to assess

**Issue type, where relevant:**

- Content readability issue
- Structural or interaction issue
- Agent-browser compatibility issue
- Tool limitation
- None

### 1.9.2. Relationship to this test

> Explain whether and how the source-readability result contributes to the observed platform outcome.

A Partial or Poor source-readability result does not automatically mean the off-platform platform has failed.

---

## 1.10. Test outcome summary

### 1.10.1. What happened?

> Summarise the observed customer experience in one or two sentences.

### 1.10.2. What matters?

> Identify the most important finding or risk.

### 1.10.3. Where does the experience appear to break?

> Record the most likely failure layer or state that no material failure was observed.

### 1.10.4. What should be investigated or changed?

> Record an evidence-backed improvement signal, or state that no action is currently justified.

---

## 1.11. Cross-workstream implication

Record only where the finding has a meaningful implication outside Off-Platform Search.

**Relevant workstream:**

- Intelligent Front Door
- Information Architecture
- Knowledge Management System
- Other
- None

**Implication:**

> Record the implication without duplicating the underlying evidence.

---

## 1.12. Evidence references

Record links or references required to validate the finding.

- Platform result:
- City of Melbourne authoritative source:
- Competing source:
- Readability assessment:
- Screenshot / evidence artefact:
- Other:

Do not store customer personal information, credentials or sensitive operational data in this record.

---

## 1.13. Completion check

Before treating the record as complete, confirm:

- [ ] customer intent and exact query are recorded;
- [ ] platform and test conditions are recorded;
- [ ] observed evidence is separated from interpretation;
- [ ] authoritative-source validation has been completed where required;
- [ ] all six core dimensions are assessed independently;
- [ ] evidence supports each material Partial or Fail result;
- [ ] no aggregate score has been created;
- [ ] failure layer is recorded where relevant;
- [ ] High Risk is recorded separately;
- [ ] evidence confidence is recorded separately;
- [ ] source readability is referenced separately where relevant;
- [ ] platform behaviour and source problems have not been conflated;
- [ ] uncertainty is explicit; and
- [ ] any improvement signal is supported by the evidence.
