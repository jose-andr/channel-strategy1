---
title: "Test 01: Google Search + AI Mode Baseline"
source_system: confluence
confluence_page_id: "1510539273"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1510539273/Test+01+Google+Search+AI+Mode+Baseline"
confluence_version: "2"
repository_path: "off-platform-search/ops-discover/test-01-google-search-ai-mode-baseline/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Test 01: Google Search + AI Mode Baseline

**Status:** Draft   
**Workstream:** Channel Strategy Y2 — Off-Platform Search   
**Stage:** Discover   
**Test type:** Baseline diagnostic   
**Platforms:** Google Search and Google AI Mode   
**Test set:** 5 priority services + 5 priority contact reasons   
**Total executions:** 10 intents × 2 platforms = 20 test executions

---

## 1.1. Purpose

This first test establishes a repeatable baseline for how well customers can find and use City of Melbourne information when they begin outside owned channels.

The test applies the broader Off-Platform Search methodology to:

- Google Search; and
- Google AI Mode.

The purpose is to understand where friction occurs, where failures originate and where inaccurate or outdated information may create material customer risk.

The test deliberately does **not** produce a single aggregated numerical score.

Instead, each result is assessed independently across stable customer-result dimensions so that future tests can compare:

- the same customer intent over time;
- different off-platform experiences;
- different services or contact reasons; and
- changes following improvements to content, pathways or source information.

Strong performance in one dimension should not compensate for a material failure in another.

---

## 1.2. Test objective

Starting with Google, test whether a customer can:

1. find relevant City of Melbourne information;
2. recognise an authoritative source;
3. receive accurate and current information;
4. understand the answer in customer language; and
5. identify the correct next action.

Where a City of Melbourne webpage is relevant to the result, source readability may also be assessed separately using the dedicated AI browser readability method.

---

## 1.3. Scope

### 1.3.1. In scope

- Google Search results;
- Google AI Mode results;
- 5 priority services; and
- 5 priority contact reasons.

### 1.3.2. Out of scope

- other AI assistants;
- other search engines;
- Digital Assistant;
- internal search;
- site navigation; and
- end-to-end transaction completion.

This scope applies to Test 01 only.

It does not redefine the broader Off-Platform Search methodology.

---

## 1.4. Test set

### 1.4.1. Priority services

| ID | Service | Customer-language query | Key risk |
| --- | --- | --- | --- |
| A01 | Apply for a parking permit | How do I apply for a residential parking permit in Melbourne? | Generic parking information instead of the correct permit pathway |
| A02 | Request an infringement review | How do I request a review of a parking fine? | Incorrect legal or process information, or a third-party source, could materially misdirect the customer |
| A03 | Pay a parking fine | How do I pay a parking fine in Melbourne? | Unofficial or incorrect payment pathway |
| A04 | Pay rates | How do I pay my council rates in Melbourne? | Incorrect payment information, outdated options or non-authoritative sources |
| A05 | Report a missed waste collection | My bin wasn't collected. What do I do? | Wrong council or general waste information instead of the correct reporting pathway |

### 1.4.2. Priority contact reasons

| ID | Contact reason | Customer-language query | Key risk |
| --- | --- | --- | --- |
| B01 | General enquiry / triage | I'm not sure what service I need. Can you point me in the right direction? | Generic contact information instead of useful triage |
| B02 | Infringement Review | Can I appeal a parking fine in Melbourne? | Customer language is not mapped to the formal infringement review pathway |
| B03 | Parking Permit | Can I get a parking permit for my apartment in Melbourne? | Application pathway surfaced without necessary eligibility or location conditions |
| B04 | Graffiti Removal | How do I report graffiti for removal in City of Melbourne? | General policy or third-party reporting service instead of the actionable Council pathway |
| B05 | Driver Nomination | How do I nominate another driver for a parking fine in Melbourne? | Customer directed toward review, payment or generic contact instead of driver nomination |

Some services and contact reasons intentionally overlap.

The **service test** asks whether a customer who broadly knows the service can find the correct pathway.

The **contact-reason test** asks whether Google can interpret the customer's underlying need when it is expressed in normal customer language.

---

## 1.5. Test case structure

Each test case consists of:

| Element | Meaning |
| --- | --- |
| Customer intent | The underlying thing the customer is trying to achieve |
| Customer-language query | The words a customer might naturally type without needing to know City of Melbourne service terminology |
| Platform | Google Search or Google AI Mode |
| Result | What Google presents in response to the query |
| Source | The organisation or webpage Google relies on or cites |
| Interpretation | Whether the result correctly represents the authoritative source and can be understood by the customer |
| Next action | Whether the customer is given a clear, correct and usable next step |

---

## 1.6. Test method

### 1.6.1. Step 1 — Establish conditions

Before each test session, record:

- Test date
- Test time
- Tester
- Device
- Browser
- Signed into Google: Yes / No
- Incognito / private mode: Yes / No
- Google Search available: Yes / No
- Google AI Mode available: Yes / No
- Other relevant condition

Test conditions are recorded because results may vary by session, device, account state and product availability.

---

### 1.6.2. Step 2 — Run in Google Search

Enter the query **exactly as written**.

Record:

- whether relevant City of Melbourne information is surfaced;
- result position;
- result title;
- displayed source/domain;
- result snippet;
- returned URL;
- competing sources above the City of Melbourne result; and
- any prominent Google-generated answer.

Do not add:

- `site:melbourne.vic.gov.au`;
- internal service terminology;
- a known page title; or
- additional keywords after seeing the result.

---

### 1.6.3. Step 3 — Run in Google AI Mode

Enter the query **exactly as written**.

Record:

- the answer provided;
- whether City of Melbourne is cited;
- which City of Melbourne page is cited;
- other sources cited;
- whether the answer accurately represents City of Melbourne information;
- whether important conditions or qualifications are preserved; and
- the next action recommended.

---

### 1.6.4. Step 4 — Validate against the authoritative source

Where required:

1. open the relevant City of Melbourne source;
2. determine what the authoritative page actually says; and
3. do not treat the Google answer itself as the source of truth.

Do not infer source provenance where it cannot be established.

---

## 1.7. Platform-result assessment

Each Google result is assessed independently across the six stable Off-Platform Search dimensions.

These dimensions assess the result presented to the customer.

They are not specific to Google and should retain the same meaning when the methodology is applied to other platforms in future.

### 1.7.1. Discoverability

**Question:** Is information relevant to the customer's intent surfaced clearly enough to be found or recognised?

- **Pass:** The appropriate information or pathway is readily discoverable.
- **Partial:** Relevant information appears but is weak, buried or ambiguous.
- **Fail:** Relevant information is absent or materially difficult to identify.
- **Unable to assess:** Platform behaviour prevents a meaningful conclusion.

### 1.7.2. Authority

**Question:** Can the customer recognise an appropriate authoritative source or pathway?

- **Pass:** The authoritative source is clearly identifiable and appropriately represented.
- **Partial:** An authoritative source appears but its authority is ambiguous or competing sources dominate.
- **Fail:** An inappropriate, unofficial or misleading source is preferred or represented as authoritative.
- **Unable to assess:** Source authority cannot be determined from the available evidence.

### 1.7.3. Accuracy

**Question:** Is the information materially consistent with the authoritative source?

- **Pass:** Materially accurate.
- **Partial:** Broadly correct but omits, simplifies or ambiguously represents an important point.
- **Fail:** Incorrect or materially misleading.
- **Unable to assess:** Available evidence is insufficient to validate the information.

### 1.7.4. Currency

**Question:** Does the information reflect the current authoritative source?

- **Pass:** Current.
- **Partial:** Currency cannot be confidently established or minor stale information appears.
- **Fail:** Materially outdated.
- **Unable to assess:** Available evidence is insufficient to determine currency.

### 1.7.5. Understandability

**Question:** Can the customer understand what the information means without needing organisational or specialist terminology?

- **Pass:** Clear in customer language.
- **Partial:** Understandable but contains meaningful ambiguity, jargon or unnecessary complexity.
- **Fail:** Difficult or misleading to interpret.
- **Unable to assess:** The result does not provide enough information to assess understandability.

### 1.7.6. Actionability

**Question:** Does the off-platform result make the appropriate customer next step clear?

- **Pass:** The correct next action is clear.
- **Partial:** Direction is provided but an important prerequisite, condition or step is unclear.
- **Fail:** No usable next step is provided or the next step is incorrect.
- **Unable to assess:** The result does not provide enough evidence for assessment.

---

## 1.8. Assessment rule

Assess each dimension independently.

Do not:

- average the six dimensions;
- calculate a combined quality score;
- allow strength in one dimension to compensate for failure in another; or
- change the assessment threshold because a test is considered high risk.

The platform-result dimensions and their definitions should remain stable across repeated tests.

---

## 1.9. Source readability diagnostic

AI browser readability is a separate source-level assessment.

It should not be treated as a seventh platform-result dimension.

Where a City of Melbourne webpage is relevant to the test, the dedicated readability method may be used to assess whether an AI-enabled browser or agent can understand and use the underlying source.

### 1.9.1. Working definition

**AI browser readability** is the extent to which an AI-enabled browser can access, interpret and act on the underlying structure and content of a webpage sufficiently to understand the service and identify the appropriate next step.

The assessment focuses on machine interpretation of the live webpage rather than visual presentation alone.

### 1.9.2. Readability criteria

The dedicated assessment examines:

1. content availability in the page structure;
2. whether page structure communicates meaning;
3. whether important elements can be identified;
4. whether interactive controls have understandable purpose;
5. whether dynamic behaviour remains understandable;
6. whether text can be selected and extracted meaningfully;
7. whether non-text information has interpretable meaning;
8. whether the customer task is actionable from the webpage;
9. whether the pathway remains readable across steps; and
10. whether the page depends on unsupported browser behaviour.

Criterion-level results use:

- **Yes**
- **Partial**
- **No**

Compatibility observations use:

- **No issue**
- **Possible issue**
- **Blocking issue**

Overall readability uses:

- **Good**
- **Partial**
- **Poor**
- **Unable to assess**

Do not convert these classifications into the platform-result Pass / Partial / Fail scale.

---

## 1.10. Actionability distinction

Actionability is assessed at two different levels.

### 1.10.1. Platform-result Actionability

**Question:** Does the off-platform result make the appropriate customer next step clear?

This assesses what Google communicates to the customer.

### 1.10.2. AI-readability customer-task actionability

**Question:** Can an AI-enabled browser determine the appropriate next action from the underlying webpage?

This assesses the City of Melbourne source itself.

A Google result may therefore pass Actionability while the underlying source has a readability problem, or vice versa.

---

## 1.11. Readability interpretation

Where a readability result is Partial, Poor or unclear, distinguish between:

- **content readability issue**;
- **structural or interaction issue**;
- **agent-browser compatibility issue**; and
- **tool limitation**.

A page should not be classified poorly simply because it renders differently from a conventional browser.

The assessment is concerned with whether an agent can understand and use the service pathway.

---

## 1.12. Reuse of readability evidence

An existing source readability assessment may be referenced across test executions where:

- the same authoritative source is being assessed;
- relevant page content and structure have not materially changed;
- the same relevant pathway or interaction state applies;
- dynamic behaviour relevant to the task has not materially changed; and
- assessment conditions remain sufficiently comparable.

Do not assume that the same URL always represents the same readability state.

Repeat the assessment where the relevant source, pathway or interaction behaviour has materially changed.

---

## 1.13. Failure-layer diagnosis

Where a platform-result dimension is **Partial** or **Fail**, record the most likely point at which the experience breaks.

| Failure layer | Meaning |
| --- | --- |
| Discovery failure | Relevant authoritative information was not surfaced |
| Source-selection failure | A weaker, inappropriate or third-party source was preferred |
| Content interpretation failure | The correct source was available but its information was misunderstood or misrepresented |
| Currency failure | Returned information does not reflect the current authoritative source |
| Actionability failure | The off-platform result does not provide a sufficiently clear or correct next step |
| Source readability issue | A separately recorded source-readability issue contributes to the observed result |
| Tool limitation | Platform or assessment-tool behaviour prevents a meaningful assessment |

Failure layer is diagnostic.

It does not replace the dimension-level assessment.

A source readability issue should reference the separate readability assessment rather than being treated as a platform score.

---

## 1.14. High-risk flag

Separately flag a test where inaccurate, outdated or misleading information could materially affect the customer.

For this initial test set, this is particularly relevant to:

- infringement review;
- driver nomination;
- parking fine payment; and
- rates payment.

The High Risk flag does **not** change the definitions or thresholds of Pass, Partial or Fail.

It indicates that:

- the consequence of an incorrect result is greater;
- stronger evidence may be required before relying on the finding; and
- remediation may warrant higher priority.

---

## 1.15. Evidence confidence

Record evidence confidence separately where results are:

- variable;
- incomplete;
- difficult to reproduce;
- dependent on unclear source provenance; or
- affected by platform or tool behaviour.

Confidence describes the strength of the evidence supporting an assessment.

It does not describe the quality of the customer experience and should not be treated as an assessment dimension.

Suggested labels:

- **High** — result is clear, reproducible and well supported by authoritative evidence;
- **Medium** — result is usable but contains some variability or evidence limitation;
- **Low** — result is difficult to reproduce or insufficiently supported for a strong conclusion.

---

## 1.16. Evidence capture template

Use one record per customer query per platform.

| Field | Record |
| --- | --- |
| Test ID |  |
| Customer intent |  |
| Customer-language query |  |
| Platform |  |
| Test date / time |  |
| Tester |  |
| Device / browser |  |
| Signed into Google |  |
| Incognito / private mode |  |
| Result / answer observed |  |
| City of Melbourne surfaced / cited |  |
| City of Melbourne source |  |
| Other sources |  |
| Result position, where applicable |  |
| Returned URL |  |
| Important conditions preserved |  |
| Recommended next action |  |
| Discoverability | Pass / Partial / Fail / Unable to assess |
| Authority | Pass / Partial / Fail / Unable to assess |
| Accuracy | Pass / Partial / Fail / Unable to assess |
| Currency | Pass / Partial / Fail / Unable to assess |
| Understandability | Pass / Partial / Fail / Unable to assess |
| Actionability | Pass / Partial / Fail / Unable to assess |
| Failure layer |  |
| High-risk flag | Yes / No |
| Evidence confidence | High / Medium / Low |
| Readability assessment reference, where relevant |  |
| Evidence / notes |  |

---

## 1.17. Comparison rule

To preserve comparison across platforms and over time:

- keep the six core platform-result dimensions stable;
- keep their definitions and thresholds stable;
- use the same customer intent and query where practical;
- record material differences in test conditions;
- assess each platform result independently;
- keep source readability as a separate diagnostic;
- preserve the native readability classifications;
- distinguish platform Actionability from webpage task Actionability;
- do not convert readability classifications into platform-result scores;
- record failure layer, High Risk and evidence confidence as overlays rather than dimensions; and
- document any future framework change before comparing results collected under materially different versions.

Platform-specific evidence capture can evolve without changing the underlying comparison framework.

---

## 1.18. First-test outputs

Test 01 should produce:

1. 20 completed test executions;
2. dimension-level results across the six core platform-result dimensions;
3. a view of recurring failure layers;
4. a separate view of high-risk cases;
5. evidence confidence for material findings;
6. source readability assessments or references where relevant;
7. examples of recurring customer friction;
8. evidence of differences between Google Search and Google AI Mode; and
9. a prioritised set of improvement signals for the next Off-Platform Search decision point.

---

## 1.19. Interpretation rule

When reporting Test 01:

- show dimension-level results before any overall narrative;
- do not create a single aggregated quality score;
- keep high-risk cases visible;
- preserve evidence confidence;
- identify the failure layer for Partial and Fail results;
- distinguish platform behaviour from source readability problems;
- validate material claims against authoritative City of Melbourne sources;
- preserve uncertainty where results vary;
- treat readability as a separate source diagnostic; and
- treat the first test as a baseline for future comparison rather than a definitive assessment of Google as a whole.
