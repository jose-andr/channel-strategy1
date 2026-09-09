---
title: "Off-Platform Search — Test Register"
source_system: confluence
confluence_page_id: "1511325716"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1511325716/Off-Platform+Search+Test+Register"
confluence_version: "2"
repository_path: "off-platform-search/ops-discover/off-platform-search-test-register/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Off-Platform Search — Test Register

**Status:** In progress   
**Workstream:** Channel Strategy Y2 — Off-Platform Search   
**Phase:** Discover   
**Artefact type:** Test register

---

## 1.1. Purpose

Use this register to track Off-Platform Search test cycles over time.

The register provides a simple record of:

- what was tested;
- when it was tested;
- which platforms were included;
- which methodology version applied;
- whether the test is directly comparable with earlier results;
- where detailed evidence is stored; and
- what decision or question the test was intended to support.

Detailed test definitions and evidence remain in their own artefacts.

---

## 1.2. Comparison principle

Repeated testing is intended to show how individual experience dimensions change over time.

To preserve comparability:

- keep the core platform-result dimensions stable;
- keep assessment thresholds stable;
- reuse customer intents and queries where practical;
- record material changes in platforms or test conditions;
- keep source readability separate from platform-result performance;
- record methodology changes explicitly; and
- do not treat results as directly comparable where a material change prevents a like-for-like comparison.

A new platform can be added without redefining the core assessment framework.

---

## 1.3. Test register

| Test | Purpose | Platforms | Test set | Methodology | Comparison status | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Test 01 — Google Search + AI Mode Baseline | Establish the first Off-Platform Search baseline | Google Search; Google AI Mode | 5 priority services + 5 priority contact reasons | Six core platform-result dimensions + separate AI browser readability diagnostic | Baseline | Planned / In progress | `test-01-google-search-ai-mode-baseline.md` |

Add a new row only when a distinct test cycle is planned or completed.

Do not create placeholder entries for tests that have not been justified.

---

## 1.4. Test cycle record

For each new test cycle, record the following.

### 1.4.1. Test identification

| Field | Detail |
| --- | --- |
| Test ID |  |
| Test name |  |
| Test date / period |  |
| Test purpose |  |
| Decision or question supported |  |
| Platforms |  |
| Number of customer intents |  |
| Number of planned executions |  |
| Number of completed executions |  |
| Test definition |  |
| Evidence location |  |
| Results summary |  |

---

## 1.5. Methodology record

| Field | Detail |
| --- | --- |
| Core platform-result dimensions changed | Yes / No |
| Assessment thresholds changed | Yes / No |
| Failure-layer model changed | Yes / No |
| High-risk approach changed | Yes / No |
| Evidence confidence approach changed | Yes / No |
| AI browser readability criteria changed | Yes / No |
| Evidence capture materially changed | Yes / No |
| Other methodology change |  |

### 1.5.1. Methodology notes

> Record only material changes that could affect interpretation or comparison.

Do not treat changes to platform-specific evidence fields as methodology changes where the underlying assessment framework remains unchanged.

---

## 1.6. Test-set comparison

Record whether the customer intents and queries remain comparable with an earlier test.

| Field | Detail |
| --- | --- |
| Previous test used for comparison |  |
| Same customer intents | Yes / Partial / No |
| Same customer-language queries | Yes / Partial / No |
| Same authoritative sources | Yes / Partial / No |
| Material service or pathway changes | Yes / No |
| Material source-content changes | Yes / No |
| Material platform changes | Yes / No |
| Material test-condition changes | Yes / No |

### 1.6.1. Comparison judgement

**Comparison status:**

- **Directly comparable**
- **Comparable with caveats**
- **Not directly comparable**
- **New baseline**

**Reason:**

> Explain the material factor affecting comparison.

---

## 1.7. Platform changes

Off-platform products may change independently of City of Melbourne.

For each test cycle, record material platform changes known to affect interpretation.

Examples include:

- a new result format;
- changes to generated answers;
- changes to source citation behaviour;
- changes to ranking or result presentation;
- changes to account or personalisation behaviour;
- platform feature availability;
- major product renaming; or
- a platform being discontinued.

| Platform | Material change | Effect on comparison |
| --- | --- | --- |
|  |  |  |

Do not assume that an observed result difference is caused by a platform change unless the evidence supports that conclusion.

---

## 1.8. Source and pathway changes

A result may change because the authoritative source or service pathway changed rather than because the off-platform platform improved or deteriorated.

Record material changes such as:

- page content updates;
- URL or redirect changes;
- service naming changes;
- eligibility changes;
- fee or deadline changes;
- pathway changes;
- form or transaction changes;
- information architecture changes; or
- dynamic interaction changes.

| Source / pathway | Change | Relevant test intent | Comparison implication |
| --- | --- | --- | --- |
|  |  |  |  |

Where a source has materially changed, determine whether its existing AI browser readability assessment remains reusable.

---

## 1.9. Readability comparison

Source readability remains separate from platform-result comparison.

For repeated readability assessments:

| Field | Detail |
| --- | --- |
| Source / pathway |  |
| Previous readability assessment |  |
| Current readability assessment |  |
| Same relevant page state | Yes / No |
| Material content change | Yes / No |
| Material structural change | Yes / No |
| Material interaction change | Yes / No |
| Assessment conditions comparable | Yes / Partial / No |
| Reassessment required | Yes / No |

Do not infer source improvement or deterioration from platform-result changes alone.

---

## 1.10. Baseline relationship

Each test should identify its relationship to prior evidence.

Use one of the following:

### 1.10.1. New baseline

Use where:

- no comparable earlier test exists;
- the methodology has materially changed; or
- the platform, service or source has changed enough that earlier results are not meaningfully comparable.

### 1.10.2. Direct comparison

Use where:

- the customer intent is equivalent;
- the query is equivalent or meaningfully unchanged;
- the core methodology is unchanged; and
- material test conditions are sufficiently comparable.

### 1.10.3. Comparison with caveats

Use where comparison remains useful but one or more material differences need to be visible.

### 1.10.4. Not comparable

Use where changes are significant enough that presenting a trend would be misleading.

---

## 1.11. Test outcome reference

The register should not duplicate the detailed results summary.

For each completed test, record only:

**Primary finding:**

> One sentence.

**Material high-risk finding:**

> One sentence or `None identified`.

**Key comparison finding:**

> One sentence or `Not applicable`.

**Decision / next step:**

> One sentence.

Detailed dimension-level evidence should remain in the relevant results summary and evidence records.

---

## 1.12. Version discipline

When the test framework changes materially:

1. record the change in this register;
2. identify the first test using the revised methodology;
3. state whether earlier results remain directly comparable;
4. avoid silently rescoring previous evidence;
5. preserve the original evidence and methodology reference; and
6. establish a new baseline where direct comparison would otherwise be misleading.

The objective is to preserve useful evidence over time rather than force continuity where the methodology has genuinely changed.

---

## 1.13. Current register status

### 1.13.1. Test 01 — Google Search + AI Mode Baseline

**Purpose:**   
Establish the first repeatable baseline for priority Off-Platform Search customer intents.

**Platforms:**

- Google Search
- Google AI Mode

**Test set:**

- 5 priority services
- 5 priority contact reasons
- 10 customer intents
- 20 planned platform executions

**Framework:**

- Discoverability
- Authority
- Accuracy
- Currency
- Understandability
- Actionability

**Separate diagnostics:**

- AI browser readability
- failure layer
- High Risk
- evidence confidence

**Comparison status:**   
New baseline

**Test definition:**   
`test-01-google-search-ai-mode-baseline.md`

**Evidence template:**   
`evidence-capture-template.md`

**Results summary:**   
`baseline-results-summary.md`

**AI browser readability method:**   
`ai-browser-readability-criteria.md`
