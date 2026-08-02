---
title: "**Fit-for-Purpose Systems and Computerised Systems Validation**"
layout: default
---

# **Fit-for-Purpose Systems and Computerised Systems Validation**

English Version

# Fit-for-Purpose Systems and Computerised Systems Validation

**Learn how ICH E6(R3) replaces one-size-fits-all validation with a fit-for-purpose approach, where system requirements and validation effort scale with data criticality and risk.**

---


## From Universal Templates to Proportionate Validation

There was a time when computerised system validation meant one thing: exhaustive documentation. Every system, regardless of its role in the trial, received the same treatment. The electronic data capture system holding primary endpoint data? Full validation package. The scheduling tool for monitoring visits? Full validation package. The system tracking office supplies? Well, perhaps not that one, but the principle was clear: validation meant doing everything, everywhere, always.
This approach was never quite right. It spread validation resources thin, applied identical rigour to systems with vastly different impacts, and often resulted in thick binders that demonstrated compliance without ensuring quality. A sponsor might possess immaculate validation documentation for a system that captured exploratory biomarkers while the system holding pivotal safety data received the same — but no more — attention.
ICH E6(R3) offers a different path. The guideline does not abandon validation; it refines it. The question is no longer “Did we validate?” but “Did we validate appropriately for what this system does and the criticality of its data?”
This is the fit-for-purpose standard: **validation effort proportionate to purpose**.

---


## What You Will Learn

By the end of this lesson, you will be able to:
1. Apply the fit-for-purpose standard as E6(R3)’s quality criterion for computerised systems
1. Implement risk-based approaches to computerised systems validation
1. Define system requirements based on data criticality and intended use
1. Develop user requirements and functional specifications appropriate to system purpose
1. Maintain systems through ongoing change control proportionate to risk

---


## Fit-for-Purpose as the Quality Standard

The phrase “fit for purpose” appears throughout E6(R3), and its meaning is precise. A system is fit for purpose when it reliably performs its intended functions under the conditions of actual use. Not when it meets some abstract standard of perfection. Not when it has been validated according to a universal template. When it works for what it is meant to do.
> **Sub-principle 9.3**
“Computerised systems used in clinical trials should be fit for purpose (e.g., through risk-based validation, if appropriate), and factors critical to their quality should be addressed in their design or adaptation for clinical trial purposes to ensure the integrity of relevant trial data.”
This language carries several implications worth examining.
**“Fit for purpose”** establishes a functional standard. The question is not whether the system has been subjected to a particular validation methodology, but whether it can be trusted to perform its intended role. A system capturing primary endpoint data has a different purpose than a system managing site correspondence. Both require validation, but the nature and extent of that validation should differ.
**“Through risk-based validation, if appropriate”** names the mechanism. E6(R3) does not prescribe a universal validation methodology. Instead, it points to risk-based validation as the means by which fitness for purpose is established — applying validation effort proportionate to the system’s role and the risks associated with its failure.
**“Factors critical to their quality should be addressed in their design or adaptation”** requires that quality be built into systems from the outset, not bolted on afterward. During system design or when adapting existing systems for clinical trial use, those responsible must identify and address the factors most critical to reliable performance. This shifts validation from a retrospective checklist exercise to a prospective design activity.
**“To ensure the integrity of relevant trial data”** states the objective plainly. The purpose of fit-for-purpose validation is not to generate documentation; it is to ensure that the data produced by the system can be trusted. This outcome-oriented focus distinguishes fit-for-purpose validation from checklist-driven compliance.
> **Key Distinction: Fit-for-Purpose vs. One-Size-Fits-All**
Under traditional approaches, sponsors often applied identical validation protocols regardless of system criticality. Fit-for-purpose validation requires different questions: What does this system do? How critical is that function? What are the consequences if the system fails? The answers to these questions drive the validation approach — more intensive for high-stakes systems, more streamlined for lower-risk applications.

---


## Risk-Based Approach to Validation

Risk-based validation is not about doing less work. It is about doing the right work. The goal is to focus validation effort where it matters most: on the functions and data elements that could, if they failed, harm participants or compromise the reliability of trial results.

### Assessing System Risk

The first step in risk-based validation is understanding what a system does and what could go wrong. Section 4.3.4(a) of E6(R3) provides the framework for this assessment, specifying that the approach to validation should be “based on a risk assessment that considers the intended use of the system; the purpose and importance of the data/record that are collected/generated, maintained and retained in the system; and the potential of the system to affect the well-being, rights and safety of trial participants and the reliability of trial results.”
**Data criticality** asks: What type of data does this system handle? Primary endpoint data that will determine whether the product receives approval? Safety data that protects participants? Administrative data with minimal impact on trial conclusions? The more critical the data, the more rigorous the validation requirements.
**Impact of failure** asks: What happens if this system malfunctions? Could it lead to incorrect dosing? Delayed safety reporting? Lost efficacy data? Or would it merely inconvenience the study team without affecting data integrity? Systems where failure has serious consequences require more intensive validation.
**Complexity and novelty** considers whether the system uses proven technology with an established track record or represents a new application with unknown failure modes. Novel systems may require more extensive testing because their behaviour under various conditions is less predictable.
**Integration points** examines how the system connects with other systems. A standalone application presents fewer risks than a system that feeds data to other applications or receives data from multiple sources. Interfaces introduce opportunities for data corruption or loss.

### Proportionate Validation Effort

Once risk is assessed, validation effort scales accordingly. This does not mean a simple “high/medium/low” categorisation leading to predetermined validation packages. It means thoughtful consideration of which validation activities provide value for each specific system.

### Reference Table: Validation Intensity by System Criticality


| System Characteristic | Validation Focus | Documentation Depth |
| --- | --- | --- |
| **Primary endpoint capture** | Extensive functional testing, data integrity verification, audit trail validation, comprehensive user acceptance testing | Complete validation documentation with detailed test scripts and traceability matrices |
| **Safety data management** | Rigorous workflow testing, timing verification, escalation procedures, integration with safety databases | Thorough documentation emphasising safety-critical functions |
| **Randomisation and treatment assignment** | Algorithm verification, blinding integrity, emergency unblinding procedures | Focus on functions that could introduce bias or reveal treatment |
| **Secondary endpoint collection** | Appropriate functional testing, data entry controls, query management | Proportionate documentation covering key functions |
| **Site communication tools** | Basic functionality verification, access controls, record retention | Streamlined documentation focused on essential capabilities |


---


## Defining System Requirements Based on Data Criticality

Before validating any system, sponsors and investigators must understand what the system needs to do. This understanding is captured in requirements documentation — but the depth and formality of that documentation should itself be proportionate to system criticality.

### User Requirements

User requirements describe what the system must accomplish from the perspective of those who will use it. These are not technical specifications but functional needs. “The system must capture the date and time of drug administration” is a user requirement. “The system must use a MySQL database with timestamp fields” is a technical specification.
For high-criticality systems, user requirements should be:
- **Specific:** Clear enough that compliance can be objectively assessed
- **Complete:** Covering all intended uses and expected scenarios
- **Traceable:** Linked to business or regulatory needs that justify them
- **Testable:** Stated in ways that permit verification
For lower-criticality systems, user requirements may be more streamlined — perhaps a functional overview rather than itemised specifications — provided they adequately describe expected system behaviour.
> **Practical Example: EDC System Requirements**
For an electronic data capture system handling primary endpoint data, user requirements might include: “The system must prevent entry of dates in the future,” “The system must require electronic signature for form completion,” “The system must maintain a complete audit trail of all data entries and modifications.” Each requirement is specific, testable, and traceable to data integrity objectives. For a site file management system, requirements might be simpler: “The system must allow document upload, storage, and retrieval with access limited to authorised users.”

### Involving Participants and Healthcare Professionals in Design

E6(R3) introduces a recommendation that reflects the increasing role of participant-facing technology in clinical trials. The introductory paragraph of Section 4.3 states:
> “It is recommended that representatives of intended participant populations and healthcare professionals are involved in the design of the system, where relevant, to ensure that computerised systems are suitable for use by the intended user population.”
This is not a mere suggestion buried in regulatory boilerplate. When a sponsor deploys an ePRO application that a 72-year-old participant with limited smartphone experience must use daily, the usability of that application directly affects data quality. When an eConsent platform presents complex trial information through a digital interface, participants must be able to navigate it meaningfully — not just technically.
User-centred design involves engaging representative end-users during the requirements and design phases. For participant-facing technologies — ePRO systems, eConsent platforms, wearable devices, patient-facing mobile applications — this means testing prototypes with individuals who reflect the target population’s age range, technical literacy, and physical capabilities. For healthcare professional-facing systems, it means involving the clinicians and coordinators who will actually use the system in their daily workflow, not just IT specialists who understand the technical architecture.
The practical consequence: systems designed without end-user input risk low compliance rates, increased data entry errors, and ultimately compromised data quality — precisely the outcomes that validation is intended to prevent.

### Functional Specifications

Functional specifications translate user requirements into descriptions of how the system will meet those requirements. If user requirements say *what* the system must do, functional specifications say *how* it will do it.
For critical systems, functional specifications should address:
- How each user requirement will be implemented
- System configuration settings and their rationale
- Interface behaviours and validation rules
- Error handling and exception processing
- Audit trail generation and storage
For less critical systems, functional specifications may be abbreviated or combined with user requirements in a single document. The key is that someone — whether the sponsor, the system vendor, or both — has documented the intended system behaviour with sufficient clarity to support validation testing.

### Requirements Traceability

For high-criticality systems, a traceability matrix links user requirements to functional specifications to test cases. This chain ensures that every requirement is addressed in system design and verified in testing. Nothing is forgotten. Nothing is assumed.
For moderate-criticality systems, traceability may take simpler forms — perhaps a documented crosswalk rather than a formal matrix. For lower-criticality systems, traceability may be implicit in the testing approach, provided that approach demonstrably covers intended functionality. As Section 4.3.4(e) recognises, “different degrees of validation may be needed for bespoke systems, systems designed to be configured or systems where no alterations are needed.”
> **The Traceability Principle**
Regardless of documentation format, the principle remains constant: validation testing should verify that requirements have been met. The depth of traceability documentation should match the risk of gaps going undetected. A missing test case for a critical function is a serious oversight; a missing test case for a minor administrative function is less consequential.

---


## Ongoing Maintenance and Change Control

Validation is not a moment; it is a lifecycle. A system validated in January may require updates in March, new configurations in July, and security patches throughout the year. Each change has the potential to affect validated functions. Managing these changes is as important as the initial validation.

### Change Control Principles

Change control ensures that modifications to validated systems are evaluated, approved, tested, and documented before implementation. The rigour of this process should, like initial validation, be proportionate to system criticality and the nature of the change.
**Impact assessment** asks: Which validated functions could this change affect? A software update that modifies the user interface may have different implications than one that changes how data are stored or transmitted. Changes affecting critical data flows require more careful evaluation than cosmetic modifications.
**Testing requirements** flow from impact assessment. If a change could affect validated functions, those functions must be re-tested. The scope of testing should match the scope of potential impact. A minor configuration change may require only targeted testing; a major software upgrade may require comprehensive regression testing.
**Documentation** captures what changed, why, who approved it, what testing was performed, and what the results showed. This documentation provides evidence that changes were controlled and that the system remains fit for purpose after modification.
> **Categories of Change**
Changes to validated systems typically fall into several categories:
- **Planned updates:** Vendor-released software versions, scheduled enhancements
- **Corrective changes:** Fixes for identified defects or non-conformances
- **Emergency changes:** Urgent modifications to address security vulnerabilities or critical failures
- **Configuration changes:** Modifications to system settings, workflows, or user access
Each category may have different procedures, but all require documented evaluation and appropriate testing before implementation.

### Periodic System Review

Beyond change-by-change evaluation, sponsors should periodically review computerised systems to confirm they remain fit for purpose. As Section 4.3.4(d) states, “periodic review may be appropriate to ensure that computerised systems remain in a validated state throughout the life cycle of the system.” Technology evolves. Vendor support status changes. New vulnerabilities are discovered. A system that was fit for purpose two years ago may face new challenges today.
Periodic reviews consider:
- Whether the system continues to meet user requirements
- Whether any changes have accumulated that warrant comprehensive re-validation
- Whether vendor support remains adequate
- Whether security controls remain effective against current threats
- Whether the system’s role has changed in ways that alter its criticality
The frequency and depth of these reviews should, again, be proportionate. Critical systems warrant more frequent and thorough review than administrative tools.

---


## Key Takeaways

- Fit-for-purpose validation asks whether a system reliably performs its intended functions, not whether it has been subjected to a universal validation template
- Risk-based approaches focus validation effort where it matters most — on systems where failure could harm participants or compromise data reliability
- System criticality assessment considers data criticality, failure impact, complexity, and integration points to determine appropriate validation intensity
- User requirements describe what the system must accomplish; functional specifications describe how it will accomplish it
- Requirements traceability ensures that validation testing verifies each requirement, with documentation depth proportionate to system criticality
- Change control maintains validated state throughout the system lifecycle, with evaluation and testing proportionate to the nature and impact of changes
- Periodic review confirms that systems remain fit for purpose as technology and circumstances evolve

---


## Looking Ahead

This lesson introduced the validation principles established by Sub-principle 9.3 and detailed in Section 4.3.4 of E6(R3). Validation effort is expected to scale with system criticality — more intensive for systems handling primary endpoints and safety data, more streamlined for lower-risk applications.
Module 8 builds on this foundation, addressing the additional operational requirements of Section 4.3: procedures for system use (4.3.1), training (4.3.2), security controls and data backup (4.3.3), system release procedures (4.3.5), contingency planning for system failures (4.3.6), technical support (4.3.7), and user access management (4.3.8). Together with the validation principles covered here, these requirements form the complete framework for computerised systems in clinical trials.
What you take from this lesson is the mindset: validation exists to ensure the integrity of relevant trial data, and the path to integrity runs through proportionate, risk-based attention to what matters most.

---


## Key Terms

**Fit for purpose (computerised systems):** The E6(R3) standard requiring that a system reliably perform its intended functions under conditions of actual use; established through risk-based validation rather than a universal template.
**Risk-based validation:** An approach in which validation effort is scaled to the system’s role, the criticality of its data, and the consequences of its failure (Section 4.3.4(a)).
**Data criticality:** The importance of the data a system handles — primary endpoint and safety data being most critical, administrative data least — a key determinant of validation intensity.
**User requirements:** Functional statements of what a system must accomplish from the perspective of those who will use it; distinct from technical specifications.
**Functional specifications:** Documentation translating user requirements into descriptions of how the system will implement them, including configuration, interface behaviours, validation rules, error handling, and audit trail generation.
**Traceability matrix:** Documentation linking user requirements to functional specifications to test cases, ensuring every requirement is designed for and verified; depth should be proportionate to criticality.
**User-centred design:** The practice, recommended in Section 4.3, of involving representatives of intended participant populations and healthcare professionals in system design to ensure suitability for the intended user population.
**Change control:** The process by which modifications to a validated system are evaluated, approved, tested, and documented before implementation, preserving the validated state.
**Regression testing:** Comprehensive re-testing of previously validated functions following a change, to confirm that the change has not disrupted them.
**Periodic system review:** Scheduled reassessment (per Section 4.3.4(d)) confirming that a system remains in a validated state and fit for purpose throughout its lifecycle.
**Section 4.3.4:** The portion of ICH E6(R3) Annex 1 detailing computerised systems validation requirements, including the risk assessment framework (a), periodic review (d), and degrees of validation for bespoke, configurable, and unaltered systems (e).

---

Source: [https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation](https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation)
Burmese Version


---

Source: [https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation](https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation)
Translated by **Google Gemini (3.5 Flash)**

