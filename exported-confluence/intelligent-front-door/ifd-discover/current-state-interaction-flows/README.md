---
title: "Current-state interaction flows"
source_system: confluence
confluence_page_id: "1427046410"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1427046410/Current-state+interaction+flows"
confluence_version: "5"
repository_path: "intelligent-front-door/ifd-discover/current-state-interaction-flows/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# Current-state interaction flows

| Field | Detail |
| --- | --- |
| **Status** | Draft |
| **Owner** | [Owner] |
| **Last updated** | 12 August 2026 |
| **Artefact** | Yes |
| **Artefact type** | Map |
| **Related Jira** | CFT-2714 |
| **Discovery area** | Intelligent Front Door |
| **Related pages** | IFD - Discover; Support mode model and priority service mapping; Pain point summary |
| **Evidence inputs** | CFT-2712 Priority Service Analysis; CFT-2713 Contact Reason Analysis; Channel Strategy data analysis; current-state flow mapping |

## 1.1. Purpose

Document how priority customer interactions currently move from customer intent and entry point through information, self-service, support channels, systems and specialist handling.

This page focuses on the **current state**:

- where customers enter
- how they find or access a service
- which channels and systems are involved
- where support is introduced
- where handoffs occur
- where context may be lost
- where repeat contact or friction is visible
- what remains unknown or needs validation

This page does not define the future-state Intelligent Front Door.

Future-state routing, support logic and interaction design will be developed through Define and Design.

---

## 1.2. How this connects to the support mode model

The related **Support mode model and priority service mapping** page defines:

- Routine
- Guided
- Assisted

and the support subcategories beneath them.

This page shows the **current pathways that sit underneath those classifications**.

The two artefacts should be read together:

**Support mode model**  
→ what level and type of support the task needs

**Current-state interaction flows**  
→ how the customer currently moves through channels, systems and teams

Channel is treated separately from interaction mode.

A digital interaction is not automatically Routine, and a phone interaction is not automatically Assisted.

---

# 2. Current-state flow map

[Embed current-state interaction flow map here]

## 2.1. How to read the map

The map is read from left to right:

**Customer segment**  
→ **Customer intent / contact reason**  
→ **Task**  
→ **Entry point**  
→ **Information**  
→ **Self-service / transaction**  
→ **Support**  
→ **Internal handling**  
→ **Outcome**  
→ **Post-interaction**

Current-state channels and systems shown include:

- Google search
- notice / direct link
- City of Melbourne website
- information pages
- Service Account portal
- e-services
- Genesys telephony
- Salesforce CRM
- legacy CRM / workflow
- specialist teams

---

# 3. Current-state interaction signals

Use the following annotations consistently across the flow map and supporting notes.

| Signal | Meaning |
| --- | --- |
| **Routine / Guided / Assisted** | Current evidence-based interaction mode |
| **Volume** | Relative importance of the task |
| **Channel signal** | Current dominant or significant channel |
| **Friction** | Known point of failure, confusion or additional effort |
| **Repeat / chase** | Customer returns for status, clarification or unresolved need |
| **Handover** | Interaction crosses a team, channel or system boundary |
| **Context risk** | Customer or interaction context may not transfer cleanly |
| **Open** | Current-state evidence is incomplete or requires validation |

These annotations describe the current state only.

They should not be interpreted as confirmed future-state requirements.

---

# 4. Priority journeys

## 4.1. Residential parking permit application

**Service:** Parking Permit   
**Contact reason:** Apply   
**Interaction mode:** Routine   
**Primary support pattern:** Transact

### 4.1.1. Current pathway

Typical current pathway:

**Google search / permit renewal notice**  
→ City of Melbourne parking permit information  
→ Service Account portal  
→ permit application  
→ assessment / work order  
→ permit outcome

The current flow also allows customers to move into Contact Centre or expert support where the digital pathway does not resolve the need.

### 4.1.2. Current evidence

CFT-2713 identifies the standard Parking Permit Application as a high-volume **Routine** interaction and shows that the dominant origin is digital.

The same analysis also identifies distinct Guided permit enquiry patterns, including Disabled / Medical Parking and Reserved Parking enquiries.

### 4.1.3. Current-state observations

- the core permit application is a standard transactional pathway
- the same service contains enquiry types that require more guidance
- digital failure can cause customers to move into phone or expert support
- eligibility uncertainty can shift the interaction from Routine to Guided
- the customer may need to repeat information when moving from digital into assisted support

### 4.1.4. Friction / handoff signals

Potential signals to show on the map:

- **Friction:** digital completion failure
- **Repeat / chase:** application status, change, eligibility, cancelled / not received
- **Handover:** digital → Contact Centre
- **Context risk:** information already entered digitally may not transfer into assisted support

### 4.1.5. Open questions

- Which portal failure points are still active?
- What customer context transfers from the portal into Contact Centre support?
- Can application status be seen without contacting the Contact Centre?
- Which permit enquiry types are most frequently misrouted?

---

## 4.2. Parking infringement review

**Service:** Parking Infringement Review   
**Contact reason:** Apply   
**Interaction mode:** Assisted   
**Primary support pattern:** Resolve / Specialist

### 4.2.1. Current pathway

Typical current pathway:

**Fine notice / Google search**  
→ parking infringement information  
→ request review pathway  
→ webform submission  
→ internal assessment workflow  
→ specialist review team  
→ review outcome

Customers may also contact the Contact Centre or expert queue for help before, during or after the review process.

### 4.2.2. Current evidence

CFT-2713 classifies infringement review topics consistently as **Assisted**, including:

- Internal Review
- Infringement Review
- Point of Distribution Review
- Repeat Review
- Meter Fault Review

The interaction remains Assisted even where submission occurs through a digital form because the underlying service involves assessment and judgement.

### 4.2.3. Current-state observations

- digital submission is only the entry mechanism
- assessment and specialist judgement sit behind the digital pathway
- interaction history and supporting evidence matter
- customers may contact the organisation for clarification or status
- continuity is more important than for a standard transaction

### 4.2.4. Friction / handoff signals

- **Handover:** digital submission → internal assessment
- **Handover:** Contact Centre → expert / review team
- **Context risk:** review reason, supporting evidence and previous contact
- **Repeat / chase:** review progress or outcome
- **Open:** ownership visibility during assessment

### 4.2.5. Open questions

- What context is retained between submission and specialist assessment?
- What causes customers to contact the Contact Centre after submitting a review?
- Can customers see review status?
- Which review types create repeat contact?
- Where is ownership recorded and visible?

---

## 4.3. Parking infringement nomination

**Service:** Parking Infringement Nomination   
**Contact reason:** Comply   
**Interaction mode:** Routine   
**Primary support pattern:** Transact

### 4.3.1. Current pathway

Typical current pathway:

**Fine notice / direct link / website**  
→ nomination information  
→ driver nomination form  
→ submission  
→ confirmation

### 4.3.2. Current evidence

CFT-2713 classifies Parking Infringement Nomination as **Routine**.

### 4.3.3. Current-state observations

- this is materially different from infringement review
- the intent is clearer and more transactional
- the pathway is suitable for direct completion where the customer knows what they need to do
- support may still be needed where the customer cannot complete the form or does not understand the requirement

### 4.3.4. Friction / handoff signals

- **Friction:** form completion issue
- **Handover:** digital → Contact Centre if support is required
- **Context risk:** whether partially completed information transfers

### 4.3.5. Open questions

- What are the common reasons nomination customers seek support?
- Is status or confirmation sufficient after submission?
- Are there exception cases that require specialist handling?

---

## 4.4. Parking fine payment

**Service:** Parking   
**Contact reason:** Transact   
**Interaction mode:** Routine   
**Primary support pattern:** Transact

### 4.4.1. Current pathway

Typical current pathway:

**Fine notice / Google search**  
→ parking fines information  
→ e-services  
→ payment  
→ payment outcome

### 4.4.2. Current-state observations

- the core interaction is predictable and transactional
- standard payment should not require specialist intervention
- related needs such as waiver or refund can move into Guided support
- customers may contact the Contact Centre if payment information is unclear or the transaction fails

### 4.4.3. Friction / handoff signals

- **Friction:** payment failure or unclear payment state
- **Repeat / chase:** confirmation of payment
- **Handover:** failed transaction → Contact Centre

### 4.4.4. Open questions

- What proportion of support demand is caused by payment failure?
- Can payment confirmation be surfaced clearly?
- Are payment, waiver and refund intents separated early enough?

---

## 4.5. Rates payment and information

**Service:** Property Rates   
**Contact reason:** Transact / Get Information

Rates contains different interaction modes depending on task.

### 4.5.1. Current task patterns

| Task | Interaction mode | Support pattern |
| --- | --- | --- |
| Copy of rates notice / historical statement | Routine | Inform / Retrieve |
| Check balance / confirm payment received | Routine | Track |
| Update account details | Guided | Navigate / Complete with help |
| Land Information Certificate query | Guided | Identify / Navigate |
| Rates amount / valuation query | Assisted | Specialist / Resolve |

### 4.5.2. Current pathway

Typical payment pathway:

**Rates notice / Google search**  
→ rates information  
→ rates payment  
→ e-services  
→ payment outcome

Other rates enquiries may move directly into Contact Centre or specialist support.

### 4.5.3. Current-state observations

- standard payment and information tasks are Routine
- account changes and certificate enquiries require more guidance
- valuation-related questions require specialist interpretation
- the same service therefore spans all three interaction modes
- repeat contact can occur when customers need confirmation, explanation or account context

### 4.5.4. Friction / handoff signals

- **Repeat / chase:** payment confirmation
- **Friction:** account update / portal issue
- **Handover:** Contact Centre → rates specialist
- **Context risk:** account history and prior actions

### 4.5.5. Open questions

- Which rates tasks create the most repeat contact?
- What account context is available to the Contact Centre?
- What causes customers to move from digital into phone support?
- How are hardship or payment arrangement interactions identified and routed?

---

# 5. Cross-journey findings

## 5.1. Interaction mode is task-specific

The current-state evidence shows that interaction mode cannot be assigned at service level alone.

Examples:

**Apply**

- Parking Permit Application → Routine
- Construction Permit → Guided
- Infringement Review → Assisted

**Report an Issue**

- Graffiti → Routine
- Illegally Dumped Rubbish investigation → Guided
- Rapid Response → Assisted

This reinforces the need to design around:

**Service Group**  
→ **Contact Reason**  
→ **Task**  
→ **Interaction Mode**

---

## 5.2. Channel does not determine complexity

Current evidence shows that:

- Routine tasks can generate substantial phone demand
- Guided tasks can be completed digitally
- Assisted tasks can begin through digital forms

Therefore:

**digital ≠ Routine**

and:

**phone ≠ Assisted**

Channel describes where the interaction happens.

Interaction mode describes the support the interaction requires.

---

## 5.3. Digital failure can create assisted demand

Some customers begin in a digital pathway and contact the organisation only after the digital journey fails or becomes unclear.

This means some phone demand may represent:

- failed self-service
- unclear eligibility
- inability to find the right pathway
- inability to complete a transaction
- need for status or confirmation

Current-state mapping should therefore identify where support demand occurs **after an attempted digital interaction**.

---

## 5.4. Handoffs are a major discovery focus

Priority handoff points include:

- Google / direct link → website
- website → external or service portal
- portal → Contact Centre
- Contact Centre → expert queue
- Salesforce → legacy workflow
- specialist team → customer update

For each material handoff, discovery should ask:

- what information transfers?
- what does the customer need to repeat?
- who owns the next step?
- is current status visible?
- does the customer know what happens next?

---

## 5.5. Context requirements increase with support need

### 5.5.1. Routine

Usually needs:

- clear intent
- simple task data
- confirmation
- next action

### 5.5.2. Guided

Usually needs:

- customer intent
- answers to triage or eligibility questions
- pathway decision
- captured context that should not need to be repeated

### 5.5.3. Assisted

Usually needs:

- customer identity where required
- interaction history
- evidence / attachments
- current status
- ownership
- next action
- structured handover

---

# 6. Current-state friction themes

Use these as discovery tags rather than future-state requirements.

## 6.1. Findability

Customer cannot easily identify the correct service or task.

Examples:

- wrong page
- unclear terminology
- no obvious pathway
- search result does not match intent

## 6.2. Eligibility / pathway uncertainty

Customer knows what they want to do but not which pathway applies.

Examples:

- permit type
- eligibility
- waiver / refund
- assessment route

## 6.3. Digital completion failure

Customer finds the correct pathway but cannot complete it.

Examples:

- form error
- portal friction
- authentication issue
- transaction failure

## 6.4. Status / confirmation gap

Customer has completed an action but does not know:

- whether it was received
- current status
- what happens next
- when to expect an update

## 6.5. Handover / context loss

Customer moves between channels or teams and must repeat information.

## 6.6. Specialist boundary

Customer reaches general support for a need that requires specialist judgement.

---

# 7. Evidence gaps and validation

| Question | Status | Validation approach |
| --- | --- | --- |
| Which digital failure points remain active? | Open | Validate with platform and service owners |
| Which tasks create the most repeat contact? | Open | Contact reason / repeat-contact analysis |
| What context transfers from digital to Contact Centre? | Open | Current-state system / process review |
| What context transfers from Contact Centre to specialist teams? | Open | Workflow validation |
| Which outcomes and statuses are visible to customers? | Open | Journey and system review |
| Which pathways differ for accessibility needs? | Open | Accessibility discovery |
| Which pathways differ for language or interpreter support? | Open | Service and Contact Centre validation |
| Which Routine tasks become Guided or Assisted after failure? | Open | Journey / contact reason analysis |
| Which specialist handoffs have unclear ownership? | Open | Service-owner validation |

---

# 8. Current-state design signals

These are **signals for Define and Design**, not confirmed requirements.

## 8.1. Direct fulfilment signal

Routine tasks may benefit from:

- clearer information
- direct transaction
- standard issue reporting
- visible confirmation
- status visibility

## 8.2. Guidance signal

Guided tasks may benefit from:

- intent recognition
- eligibility checks
- diagnosis
- pathway selection
- assisted completion

## 8.3. Continuity signal

Assisted tasks may benefit from:

- retained context
- structured handover
- specialist routing
- visible ownership
- coordinated updates
- reduced repetition

---

# 9. What should move forward into Define

The current-state flow work should provide Define with:

1. confirmed priority tasks and pathways
2. validated points of friction
3. material handoff points
4. known context-loss risks
5. repeat-contact patterns
6. current support and specialist boundaries
7. unresolved evidence gaps
8. priority opportunities for:

   - direct fulfilment
   - guidance
   - better routing
   - continuity

The Define phase should decide which of these signals become future-state design principles or requirements.

---

# 10. Related artefacts

- Support mode model and priority service mapping
- CFT-2712 — Priority Service Analysis
- CFT-2713 — Contact Reason Analysis
- CFT-2716 — Support Mode Mapping
- Draft current-state flow map
- IFD - Discover
- Information Architecture - Discover
- Off-Platform Search - Discover

# 11. CFT-2714 acceptance criteria

| Acceptance criterion | Status | Evidence |
| --- | --- | --- |
| Priority services to be mapped are confirmed | Met for agreed mapped scope | Priority journeys are based on CFT-2712 and CFT-2713 evidence |
| Main customer entry points are identified | Met | Search, notices / direct links, website, forms, payments, phone and service-specific pathways are represented |
| Current movement from entry point to next channel, final channel or team is mapped | Met for mapped journeys | Current-state flow map and priority journey sections |
| Handoffs, escalations, redirects and channel switching are visible | Met | Journey sections and cross-journey handoff findings |
| Available evidence sources are documented | Met | Evidence inputs and journey-level evidence |
| Confidence is captured where possible | Met | Open questions, evidence gaps and validation status |
| Flow gaps, assumptions and unknowns are documented | Met | Evidence gaps and validation section |
| Findings are added or linked to IFD Discover | Met when linked | This artefact |

# 12. Completion note

This page is the durable Confluence evidence output for **CFT-2714 — Current-state channel movement**.

The available evidence is sufficient to describe the main current pathways, entry points, handoffs, channel switching and known gaps at a useful Discovery level.

Detailed system behaviour and context transfer are intentionally retained as validation items rather than blockers to Define.

## 12.1. Current validation note

The Channel Strategy data analysis notes that the **Request an Infringement Review** page was updated and live on **3 August 2026**.

Historic friction associated with that webpage should therefore be treated as:

**Needs post-change validation**

before being presented as a current issue.

This does not invalidate the broader current-state pathway or the Assisted interaction classification for infringement review.
