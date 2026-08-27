---
title: "Support mode model and priority service mapping"
source_system: confluence
confluence_page_id: "1427865606"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1427865606/Support+mode+model+and+priority+service+mapping"
confluence_version: "5"
repository_path: "intelligent-front-door/ifd-discover/support-mode-model-and-priority-service-mapping/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Support mode model and priority service mapping

| Field | Detail |
| --- | --- |
| **Status** | Draft |
| **Owner** | [Owner] |
| **Last updated** | 11 August 2026 |
| **Artefact** | Yes |
| **Artefact type** | Model |
| **Related Jira** | CFT-2716 |
| **Discovery area** | Intelligent Front Door |
| **Related pages** | IFD - Discover; Current-state interaction flows |
| **Evidence inputs** | CFT-2712 Priority Service Analysis; CFT-2713 Contact Reason Analysis |

## 1.1. Purpose

Define a reusable interaction-mode model and apply it to priority Intelligent Front Door services and customer tasks.

The model is intended to support two needs:

1. provide enough specificity to progress the current priority services into Define and Design
2. establish a reusable classification approach that can later be applied to other City of Melbourne services

The model separates:

- **customer intent** — what the customer is trying to do
- **interaction mode** — how much support the interaction requires
- **support pattern** — the type of support required
- **channel** — where or how the interaction is delivered

The current evidence baseline is drawn from:

- CFT-2712 — Priority Service Analysis
- CFT-2713 — Contact Reason Analysis
- CFT-2716 — Support Mode Mapping

## 1.2. Interaction mode framework

The primary interaction modes are:

**Routine → Guided → Assisted**

The modes represent increasing:

- complexity
- support need
- sensitivity
- judgement
- context dependency
- continuity requirement

### 1.2.1. Mode criteria

| Criterion | Routine | Guided | Assisted |
| --- | --- | --- | --- |
| Predictability | Standard, repeatable | Conditional or variable | Uncertain or exceptional |
| Complexity | Few steps, simple rules | Multiple steps or choices | Interdependent or specialist |
| Customer support need | Independent completion | Guidance or triage helps | Active human support needed |
| Sensitivity / risk | Low | Moderate | High |
| Context required | Minimal | Some context | Rich history / context |
| Continuity / ownership | Little or none | Context should carry | Clear ownership required |

## 1.3. Support subcategories

### 1.3.1. Routine

- Inform
- Transact
- Track
- Report

### 1.3.2. Guided

- Identify
- Diagnose
- Assess eligibility
- Navigate
- Complete with help

### 1.3.3. Assisted

- Resolve
- Specialist
- Sensitive
- Coordinated
- Exception

## 1.4. Mapping from original support categories

| Original CFT-2716 category | Refined interpretation |
| --- | --- |
| Self-service | Most commonly Routine — Inform / Transact / Track / Report |
| Guided self-service | Guided — Identify / Diagnose / Assess / Navigate |
| Assisted digital | Guided — Complete with help, or Assisted where judgement / continuity is required |
| Phone support | Channel / delivery option, not an interaction mode |
| Specialist support | Assisted — Specialist |
| Exception handling | Assisted — Exception |

Phone, digital, face-to-face and other channels are treated separately from interaction mode.

## 1.5. Priority service and task mapping

| Service | Topic / task | Contact reason | Interaction mode | Support subcategory | Evidence basis | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Parking Permit | Parking Permit Application | Apply | Guided | Assess eligibility / Navigate | CFT-2713 | High |
| Parking Permit | Disabled / Medical Parking enquiry | Apply | Guided | Assess eligibility / Navigate | CFT-2713 | High |
| Parking Permit | Reserved Parking enquiry | Apply | Guided | Assess eligibility / Navigate | CFT-2713 | High |
| Parking Infringement Review | Internal Review | Apply | Assisted | Resolve / Specialist | CFT-2713 | High |
| Parking Infringement Nomination | Driver nomination | Comply | Routine | Transact | CFT-2713 | High |
| Parking Enforcement | Low-priority officer request | Report an Issue | Routine | Report | CFT-2713 | High |
| Parking Enforcement | High-priority officer request | Report an Issue | Assisted | Specialist / Exception | CFT-2713 | High |
| Construction | Space Occupancy Permit | Apply | Guided | Assess eligibility / Navigate | CFT-2713 | High |
| Graffiti Removal | General graffiti report | Report an Issue | Routine | Report | CFT-2713 | High |
| Illegally Dumped Rubbish | Investigation request | Report an Issue | Guided | Diagnose / Report | CFT-2713 | High |
| Illegally Dumped Rubbish | Rapid response | Report an Issue | Assisted | Specialist / Exception | CFT-2713 | High |
| Property Rates | Copy of rates notice | Get Information | Routine | Inform / Retrieve | CFT-2713 | High |
| Property Rates | Update account details | Transact | Guided | Navigate / Complete with help | CFT-2713 | High |
| Property Rates | Rates amount / valuation query | Get Information | Assisted | Specialist / Resolve | CFT-2713 | High |
| Ratepayer Waste | Missed collection | Report an Issue | Routine | Report | CFT-2713 | High |

The interaction mode should be assigned at **task level**, not service level or contact-reason level.

For example:

**Apply**

- Parking Permit Application → Routine
- Construction Permit → Guided
- Infringement Review → Assisted

**Report an Issue**

- Graffiti → Routine
- Dumped rubbish investigation → Guided
- Rapid response → Assisted

## 1.6. Strong Routine / self-service opportunities

Current evidence suggests strong opportunities for direct fulfilment or low-support interaction patterns in:

- Parking Permit Application
- Parking Infringement Nomination
- Parking fine payment
- standard parking information
- Graffiti Removal reporting
- Ratepayer Waste reporting
- standard infrastructure reporting
- rates notice retrieval
- balance / payment confirmation

These are candidates for:

- direct information
- direct transaction
- standard reporting
- status visibility
- simple confirmations

This does not mean all customers must use self-service.

Accessibility, language, non-digital preference and failed digital journeys may require an alternative support pathway.

## 1.7. Guided and Assisted needs

### 1.7.1. Guided

Strong Guided patterns include:

- specialised parking permit enquiries
- construction permits
- eligibility checks
- conditional waiver / refund pathways
- dumped rubbish investigation
- Land Information Certificate enquiries
- account detail changes

Typical needs:

- intent recognition
- eligibility checks
- diagnosis
- decision support
- routing
- assisted completion

### 1.7.2. Assisted

Strong Assisted patterns include:

- Parking Infringement Reviews
- high-priority parking enforcement
- rapid-response dumped rubbish
- rates valuation enquiries
- sensitive or safety-related infrastructure issues

Typical needs:

- specialist judgement
- context retention
- structured handover
- clear ownership
- escalation
- continuity

## 1.8. Accessibility, language and non-digital considerations

Accessibility, language and non-digital needs are treated as **mode-changing conditions**, not separate interaction modes.

A Routine interaction may require Guided or Assisted delivery where the customer:

- needs accessibility support
- requires language or interpreter support
- cannot use the digital pathway
- has failed to complete self-service
- has a vulnerability or sensitive circumstance
- requires additional help to understand the process

The customer intent may stay the same while the required support level changes.

## 1.9. Confidence and assumptions

### 1.9.1. Confidence levels

**High**

- clear task
- explicit CFT-2713 mode
- meaningful volume
- stable pathway

**Medium**

- likely mode is clear
- task contains multiple intents or known ambiguity
- some service-owner validation is required

**Low**

- task or intent remains unresolved
- evidence is insufficient to assign a mode safely

### 1.9.2. Current assumptions

- CFT-2713 reaction mode is used as the current evidence baseline.
- Interaction mode does not determine channel.
- Digital origin does not imply Routine.
- Phone contact does not imply Assisted.
- Accessibility and vulnerability may change the required support level.
- Service owners retain authority over final service rules and escalation conditions.

## 1.10. Intelligent Front Door opportunities

### 1.10.1. Routine

**ANSWER / TRANSACT**

- direct authoritative information
- direct transactions
- standard reporting
- status and confirmation

### 1.10.2. Guided

**UNDERSTAND / GUIDE / ROUTE**

- identify intent
- ask minimum questions
- assess eligibility
- clarify pathway
- capture context once

### 1.10.3. Assisted

**RECOGNISE / CONNECT / PRESERVE CONTEXT**

- identify when specialist support is needed
- preserve relevant customer context
- support structured handover
- minimise repetition
- maintain continuity

## 1.11. CFT-2716 acceptance criteria

| Acceptance criterion | Status | Evidence |
| --- | --- | --- |
| Priority contact reasons reviewed | Met | CFT-2712 + CFT-2713 priority mappings |
| Likely support mode assigned where evidence allows | Met | Priority task mapping |
| Original support categories addressed | Met | Original-to-refined taxonomy mapping |
| Simple repeatable self-service opportunities identified | Met | Routine opportunities section |
| Assisted, specialist and exception needs visible | Met | Guided and Assisted needs section |
| Accessibility, language and non-digital needs considered | Met | Accessibility and equity section |
| Assumptions and confidence levels documented | Met | Confidence and assumptions section |
| Support mode model added to IFD Discover | Met when page is published / linked | This Confluence page |
