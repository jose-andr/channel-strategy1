---
title: "IFD - Discover - mid_sprint connection summary"
source_system: confluence
confluence_page_id: "1414070273"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1414070273/IFD+-+Discover+-+mid_sprint+connection+summary"
confluence_version: "4"
repository_path: "decision-log/ifd-discover-mid-sprint-connection-summary/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# IFD - Discover - mid_sprint connection summary

## 1.1. Mid-sprint connection summary

**Date:** 5 August 2026  
**Purpose:** Align the team on the Intelligent Front Door discovery approach, priority services, customer modes and the work required to complete the sprint.

## 1.2. Executive summary

The team agreed to progress practical improvements as opportunities emerge rather than wait for a complete future-state solution. This should follow a test-and-learn approach, provided each action remains aligned with the broader objectives of connected customer interactions.

The discovery will continue to focus on the seven priority service areas already identified, with parking-related services and rates providing the main starting points. The next level of analysis should move below broad service categories into the specific reasons customers make contact.

Customer modes—such as **apply, transact and access information**—will be used as internal design lenses. They will help define the preferred response, pathway, channel and level of support for a customer need. They are not intended to become customer-facing website categories.

The team also identified an important gap in the current thinking: most journey work assumes a customer is contacting Council for the first time. Follow-up interactions, open cases, complaints and requests for status information require separate consideration.

## 1.3. Confirmed direction

### 1.3.1. Progress does not need to wait for a “big bang”

The team supported taking action where evidence and confidence are sufficient.

Early opportunities—such as improving priority web pages, information structures, metadata and back-end content—can be progressed while discovery continues. These changes should be treated as iterative and may need to evolve as more is learned.

The methodology should guide the work without unnecessarily slowing delivery.

### 1.3.2. Maintain a shared objective

Speed should not result in disconnected improvements.

The team needs a shared understanding of:

- the customer and organisational outcomes being pursued;
- the priority customer needs;
- what a good interaction looks like;
- the preferred pathway or response; and
- how improvements across web, phone, CRM, knowledge and search connect.

Without this alignment, there is a risk of reproducing the current fragmented experience in a more polished form.

### 1.3.3. Retain the current priority service areas

The group was broadly comfortable retaining the seven priority service areas identified through the existing analysis.

The work is currently concentrated around:

- parking-related services;
- infringement-related interactions;
- rates; and
- services dominated by applying, paying or transacting.

Libraries were excluded from the core Intelligent Front Door focus because customers generally intend to contact a specific library location rather than Council as a broader organisation.

### 1.3.4. Move from broad services to reasons for contact

The broad service categories are useful for prioritisation, but they are not sufficiently granular for designing an Intelligent Front Door.

The next step is to identify the leading reasons for contact within each priority service. For example, “parking permits” may include distinct needs such as:

- checking eligibility;
- understanding how to apply;
- submitting an application;
- renewing a permit;
- following up an existing application; and
- resolving a problem.

Mapping customer modes at this level will make the design implications clearer.

## 1.4. Customer modes

Customer modes describe what the customer is trying to achieve. Examples discussed included:

- access or obtain information;
- apply;
- transact or pay;
- report an issue;
- follow up an existing request;
- complain or seek resolution.

A service may contain more than one mode. For example, an infringement review may begin as an application and lead to a payment pathway if the application is unsuccessful.

For the first iteration, the team will identify a **dominant mode** for each reason for contact while recognising that secondary modes may also exist.

## 1.5. How modes should be used

Modes should function as internal service-design logic rather than customer-facing navigation labels.

They can help define:

- the preferred response;
- the preferred channel;
- the level of assistance required;
- authentication requirements;
- the information that must be presented;
- the system or workflow destination;
- handover and routing rules; and
- the intended outcome.

The same mode may require different responses depending on the service context.

For example:

- a routine parking permit application may be suited to a straight-through self-service pathway;
- a rates hardship application may require access to assisted support;
- an infringement review may require a written application pathway even when customers frequently attempt to resolve it by phone.

The mode provides a reusable pattern, but the service context determines how that pattern is applied.

## 1.6. New versus existing interactions

The discussion identified a significant distinction between:

### 1.6.1. New interactions

The customer is attempting to begin a task, understand eligibility, apply, pay or report something for the first time.

### 1.6.2. Existing or in-flight interactions

The customer already has an application, request or case and wants to:

- check progress;
- understand a status;
- provide more information;
- resolve a delay;
- escalate an issue; or
- speak with someone who understands the existing context.

Current service structures and the “apply, pay, report” page largely assume a new interaction. The return-customer experience is not sufficiently visible.

A possible future pattern is a clear **check or follow up an existing request** pathway. This could request authentication or a case reference, provide available status information and only route the customer to assisted support when self-service cannot resolve the need.

For the immediate discovery, the team agreed to begin with the primary or “happy” path, while recording follow-up, complaint and exception pathways for subsequent design.

## 1.7. Information architecture opportunity

The existing “apply, pay, report” page may provide a useful test case for applying the discovery findings.

Potential improvements include:

- clearer grouping of customer tasks;
- separation of information needs from transactional actions;
- a pathway for checking an existing request or case;
- improved terminology;
- better links between related services; and
- removal of internal organisational complexity from the customer experience.

The customer should continue to navigate according to their task or service need—not according to an internal customer-mode framework.

## 1.8. Connected work

The Intelligent Front Door work has dependencies and opportunities across:

- website information architecture;
- IVR and contact-centre routing;
- Salesforce and CRM workflows;
- service information and knowledge;
- metadata and schema;
- Google and AI-based search;
- status information;
- authentication; and
- customer account context.

Margot’s work on large-language-model readiness, metadata, schema and back-end information structures appears strongly aligned with the Intelligent Front Door and Off-Platform Search discovery.

A walkthrough should be arranged so the team can understand the proposed back-end changes and confirm how they support the wider connected-interactions framework.

## 1.9. Risks and cautions

### 1.9.1. Over-engineering

Adding too many segmentation variables or journey layers too early may make the model difficult to test and use.

Demographic or customer-segment information should initially be used as a validation lens rather than the primary organising structure. Broad distinctions such as resident, business and third party may still be relevant where they materially change eligibility or service treatment.

### 1.9.2. Designing around internal categories

Customer modes must not become another internal taxonomy imposed on customers.

Customers should continue to enter through recognisable tasks, services and plain-language needs.

### 1.9.3. Treating all interactions as first contact

Ignoring follow-up and in-flight interactions would miss a major source of contact demand, particularly general enquiries about existing cases.

### 1.9.4. Assuming the preferred channel matches customer behaviour

A service may have a preferred written or digital pathway while customers continue to phone. The design must determine how to redirect, support or resolve these contacts without simply removing access.

### 1.9.5. Expanding scope too early

Proactive services, account-based personalisation and anticipatory communications are relevant opportunities, but the team should first establish the core discovery logic and agreed priority journeys.

## 1.10. Actions

| Action | Owner | Status |
| --- | --- | --- |
| Validate and expand the customer contact-reason analysis using a larger set of conversations. | Tom | In progress |
| Add the validated analysis to the shared Miro board. | Tom | Pending validation |
| Identify the leading reasons for contact beneath each priority service. | Tom and discovery team | Next step |
| Map each priority contact reason to a dominant customer mode and preferred response. | Discovery team | Next step |
| Continue developing the draft journey and mode illustrations, including infringement review. | José | In progress |
| Arrange a walkthrough of the large-language-model, metadata, schema and back-end information work. | Margot | Planned |
| Include Alicia in the walkthrough and connect her page-prototyping work with the back-end work. | Margot | Planned |
| Record the need for an existing-request or case-follow-up pathway when reviewing “apply, pay, report.” | Discovery team | Recorded |
| Use the remaining sprint to confirm the priority journeys, contact reasons and initial response-mode logic. | Discovery team | Current sprint |

## 1.11. Open questions

- What are the top reasons for contact within each priority service?
- Which customer mode is dominant for each reason?
- When are secondary modes important enough to represent?
- What should count as a separate response mode—for example, follow-up, complaint or escalation?
- Which interactions should be straight-through self-service, assisted or hybrid?
- When is authentication required?
- What status information can be provided before routing to a staff member?
- How should the same service logic appear across web, IVR and contact-centre pathways?
- Which early improvements can proceed now without creating future rework?
- What criteria will determine whether an opportunity remains within the agreed Intelligent Front Door scope?

## 1.12. Recommended sprint outcome

By the end of discovery, the team should have:

1. a confirmed set of priority services;
2. the leading reasons for contact within those services;
3. an initial dominant customer mode for each reason;
4. a draft preferred-response pattern;
5. a small number of representative journey flows;
6. documented gaps covering follow-up, complaints and exceptions; and
7. a clear recommendation on which use cases should progress into definition or testing.
