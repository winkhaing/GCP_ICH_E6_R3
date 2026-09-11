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

# ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော စနစ်များနှင့် ကွန်ပျူတာစနစ်များ အတည်ပြုစိစစ်ခြင်း (Fit-for-Purpose Systems and Computerised Systems Validation)

**ICH E6(R3) သည် တစ်ပုံစံတည်း သုံးစွဲသည့် အတည်ပြုစိစစ်မှုကို ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော ချဉ်းကပ်မှုဖြင့် မည်သို့ အစားထိုးလိုက်သည်ကို လေ့လာပါ၊ ဤတွင် စနစ် လိုအပ်ချက်များနှင့် အတည်ပြုစိစစ်မှု အားထုတ်မှုများသည် အချက်အလက် အရေးပါမှုနှင့် ဘေးအန္တရာယ်တို့နှင့်အညီ ချိန်ညှိသွားကြသည်။**

---


## ယေဘုယျ ပုံစံခွက်များမှသည် အချိုးအစားကျသော အတည်ပြုစိစစ်မှုဆီသို့ (From Universal Templates to Proportionate Validation)

ကွန်ပျူတာစနစ် အတည်ပြုစိစစ်ခြင်း ဆိုသည်မှာ အရာတစ်ခုတည်းကို အဓိပ္ပာယ်ရသည့် ခေတ်ကာလတစ်ခု ရှိခဲ့ဖူးသည် - ကျယ်ပြန့်သော မှတ်တမ်းတင်မှု။ စနစ်တိုင်းသည် စမ်းသပ်မှုပါ ယင်း၏ ကဏ္ဍကို မထည့်တွက်ဘဲ တူညီသော ကိုယ်တွယ်မှုကို ရရှိခဲ့ကြသည်။ အဓိက အဆုံးသတ်တိုင်းတာချက် အချက်အလက်များကို ထိန်းသိမ်းထားသည့် အီလက်ထရောနစ် အချက်အလက် စုဆောင်းမှု စနစ်? ပြည့်စုံသော အတည်ပြုစိစစ်မှု အထုပ်။ စောင့်ကြည့်စစ်ဆေးမှု ခရီးစဉ်များအတွက် အချိန်ဇယားဆွဲရေး ကိရိယာ? ပြည့်စုံသော အတည်ပြုစိစစ်မှု အထုပ်။ ရုံးသုံး ပစ္စည်းများကို ခြေရာခံသည့် စနစ်? ကဲ၊ ထိုတစ်ခု မဟုတ်နိုင်သော်လည်း မူမှာ ရှင်းလင်းခဲ့သည် - အတည်ပြုစိစစ်ခြင်း ဆိုသည်မှာ အရာရာကို၊ နေရာတိုင်းတွင်၊ အစဉ်သဖြင့် ဆောင်ရွက်ခြင်း ဖြစ်သည်။
ဤချဉ်းကပ်မှုသည် မည်သည့်အခါမျှ မှန်ကန်မနေခဲ့ပါ။ ၎င်းသည် အတည်ပြုစိစစ်မှု အရင်းအမြစ်များကို ပါးလွှာအောင် ဖြန့်ကျက်လိုက်သည်၊ သိသာစွာ မတူညီသော သက်ရောက်မှုများ ရှိသည့် စနစ်များထံ တူညီသော တင်းကျပ်မှုကို အသုံးချခဲ့သည်၊ ထို့ပြင် အရည်အသွေးကို မသေချာစေဘဲ စည်းမျဉ်း လိုက်နာမှုကို ပြသသည့် ထူထဲသော ဖိုင်တွဲများကို မကြာခဏ ထွက်ပေါ်စေခဲ့သည်။ အဓိက ဘေးကင်းရေး အချက်အလက်များကို ထိန်းသိမ်းထားသည့် စနစ်သည် တူညီသော — သို့သော် ပိုမိုမပါရှိသော — အာရုံစိုက်မှုကို ရရှိစဉ် စပွန်ဆာတစ်ခုသည် စူးစမ်းလေ့လာမှုဆိုင်ရာ ဇီဝမှတ်တိုင်များကို ရယူသည့် စနစ်တစ်ခုအတွက် သန့်ရှင်းစင်ကြယ်သော အတည်ပြုစိစစ်မှု မှတ်တမ်းတင်မှုကို ပိုင်ဆိုင်ထားနိုင်သည်။
ICH E6(R3) က မတူညီသော လမ်းကြောင်းတစ်ခုကို ပေးအပ်သည်။ လမ်းညွှန်ချက်သည် အတည်ပြုစိစစ်ခြင်းကို စွန့်လွှတ်လိုက်ခြင်း မဟုတ်ပါ; ၎င်းကို သန့်စင်ပေးလိုက်ခြင်း ဖြစ်သည်။ မေးခွန်းမှာ “ငါတို့ အတည်ပြုစိစစ်ခဲ့ရဲ့လား” မဟုတ်တော့ပါ၊ “ဤစနစ် ဆောင်ရွက်သည့် အရာနှင့် ယင်း၏ အချက်အလက် အရေးပါမှုတို့အတွက် ငါတို့ သင့်လျော်စွာ အတည်ပြုစိစစ်ခဲ့ရဲ့လား” ဟု ဖြစ်လာသည်။
ဤသည်မှာ ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော စံနှုန်း ဖြစ်သည် - **ရည်ရွယ်ချက်နှင့် အချိုးအစားကျသော အတည်ပြုစိစစ်မှု အားထုတ်မှု**။

---


## သင်ဘာတွေ လေ့လာသင်ယူရမည်နည်း (What You Will Learn)

ဤသင်ခန်းစာပြီးဆုံးပါက သင်သည် အောက်ပါတို့ကို ဆောင်ရွက်နိုင်မည်ဖြစ်သည် -
၁။ ကွန်ပျူတာစနစ်များအတွက် E6(R3) ၏ အရည်အသွေး စံနှုန်းအဖြစ် ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော စံနှုန်းကို အသုံးချနိုင်ခြင်း
၂။ ကွန်ပျူတာစနစ်များ အတည်ပြုစိစစ်ခြင်းထံ ဘေးအန္တရာယ်အခြေပြု ချဉ်းကပ်မှုများကို အကောင်အထည်ဖော်နိုင်ခြင်း
၃။ အချက်အလက် အရေးပါမှုနှင့် ရည်ရွယ်ထားသော အသုံးပြုမှုတို့အပေါ် အခြေခံ၍ စနစ် လိုအပ်ချက်များကို အဓိပ္ပာယ်ဖွင့်ဆိုနိုင်ခြင်း
၄။ စနစ် ရည်ရွယ်ချက်နှင့် သင့်လျော်သော အသုံးပြုသူ လိုအပ်ချက်များနှင့် လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များကို ဖော်ထုတ်နိုင်ခြင်း
၅။ ဘေးအန္တရာယ်နှင့် အချိုးအစားကျသော စဉ်ဆက်မပြတ် ပြောင်းလဲမှု ထိန်းချုပ်မှုမှတစ်ဆင့် စနစ်များကို ထိန်းသိမ်းနိုင်ခြင်း

---


## အရည်အသွေး စံနှုန်းအဖြစ် ရည်ရွယ်ချက်နှင့် ကိုက်ညီခြင်း (Fit-for-Purpose as the Quality Standard)

“ရည်ရွယ်ချက်နှင့် ကိုက်ညီခြင်း” ဟူသော စကားစုသည် E6(R3) တစ်လျှောက် ပေါ်ပေါက်လာပြီး ယင်း၏ အဓိပ္ပာယ်မှာ တိကျသည်။ စနစ်တစ်ခုသည် လက်တွေ့ အသုံးပြုမှု အခြေအနေများအောက်တွင် ယင်း၏ ရည်ရွယ်ထားသော လုပ်ငန်းဆောင်တာများကို ယုံကြည်စိတ်ချစွာ ဆောင်ရွက်နိုင်သည့်အခါ ရည်ရွယ်ချက်နှင့် ကိုက်ညီသည်။ ပြည့်ဝစုံလင်မှုဆိုင်ရာ စိတ်ကူးယဉ် စံနှုန်းတစ်ခုခုနှင့် ကိုက်ညီသည့်အခါ မဟုတ်ပါ။ ယေဘုယျ ပုံစံခွက်တစ်ခုအရ အတည်ပြုစိစစ်ပြီးသည့်အခါ မဟုတ်ပါ။ ၎င်း ဆောင်ရွက်ရန် ရည်ရွယ်ထားသည့် အရာအတွက် အလုပ်လုပ်သည့်အခါ ဖြစ်သည်။
> **မူခွဲ ၉.၃**
“စက္ခုတို စမ်းသပ်မှုများတွင် အသုံးပြုသော ကွန်ပျူတာစနစ်များသည် ရည်ရွယ်ချက်နှင့် ကိုက်ညီရမည်ဖြစ်ပြီး (ဥပမာ - သင့်လျော်ပါက ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်းမှတစ်ဆင့်)၊ သက်ဆိုင်ရာ စမ်းသပ်မှု အချက်အလက်များ၏ စစ်မှန်မှုကို သေချာစေရန် စက္ခုတို စမ်းသပ်မှု ရည်ရွယ်ချက်များအတွက် ၎င်းတို့၏ ဒီဇိုင်း သို့မဟုတ် ပြုပြင်ဆန်းသစ်မှုတွင် ၎င်းတို့၏ အရည်အသွေးအတွက် အလွန်အရေးပါသောအချက်များကို ကိုင်တွယ်ရမည်။”
ဤဘာသာစကားသည် စိစစ်ရန် ထိုက်တန်သော အကျိုးဆက် အများအပြားကို ဆောင်ကြဉ်းပေးသည်။
**“ရည်ရွယ်ချက်နှင့် ကိုက်ညီခြင်း”** သည် လုပ်ငန်းဆောင်တာဆိုင်ရာ စံနှုန်းတစ်ခုကို ထူထောင်ပေးသည်။ မေးခွန်းမှာ စနစ်အား သီးခြား အတည်ပြုစိစစ်မှု နည်းလမ်းတစ်ခုခုအောက်သို့ သွတ်သွင်းခဲ့သလား မဟုတ်ပါ၊ ယင်း၏ ရည်ရွယ်ထားသော ကဏ္ဍကို ဆောင်ရွက်ရန် ယုံကြည်စိတ်ချနိုင်သလား ဟု ဖြစ်သည်။ အဓိက အဆုံးသတ်တိုင်းတာချက် အချက်အလက်များကို ရယူသည့် စနစ်တစ်ခုသည် စမ်းသပ်ရာနေရာ အပြန်အလှန် ဆက်သွယ်ရေးကို စီမံခန့်ခွဲသည့် စနစ်တစ်ခုနှင့် မတူညီသော ရည်ရွယ်ချက် ရှိသည်။ နှစ်ခုလုံးသည် အတည်ပြုစိစစ်မှု လိုအပ်သော်လည်း ထိုအတည်ပြုစိစစ်မှု၏ သဘောသဘာဝနှင့် အတိုင်းအတာတို့ ကွဲပြားသင့်သည်။
**“သင့်လျော်ပါက ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်းမှတစ်ဆင့်”** သည် ယန္တရားကို အမည်တပ်ပေးသည်။ E6(R3) သည် ယေဘုယျ အတည်ပြုစိစစ်မှု နည်းလမ်းကို ပြဋ္ဌာန်းမထားပါ။ ယင်းအစား ၎င်းသည် ရည်ရွယ်ချက်နှင့် ကိုက်ညီမှုကို ထူထောင်သည့် နည်းလမ်းအဖြစ် ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်းကို ညွှန်းဆိုသည် — စနစ်၏ ကဏ္ဍနှင့် ယင်း၏ ပျက်ကွက်မှုဆိုင်ရာ ဘေးအန္တရာယ်တို့နှင့် အချိုးအစားကျသော အတည်ပြုစိစစ်မှု အားထုတ်မှုကို အသုံးချခြင်း။
**“၎င်းတို့၏ အရည်အသွေးအတွက် အလွန်အရေးပါသောအချက်များကို ၎င်းတို့၏ ဒီဇိုင်း သို့မဟုတ် ပြုပြင်ဆန်းသစ်မှုတွင် ကိုင်တွယ်ရမည်”** က အရည်အသွေးကို စတင်ချိန်ကတည်းက စနစ်များအတွင်း ထည့်သွင်းတည်ဆောက်ရန် တောင်းဆိုသည်၊ နောက်မှ တပ်ဆင်ခြင်း မဟုတ်ပါ။ စနစ် ဒီဇိုင်းဆွဲစဉ် သို့မဟုတ် စက္ခုတို စမ်းသပ်မှု အသုံးပြုရန်အတွက် ရှိပြီးသား စနစ်များကို ပြုပြင်ဆန်းသစ်သည့်အခါ တာဝန်ရှိသူများသည် ယုံကြည်စိတ်ချရသော စွမ်းဆောင်ရည်အတွက် အရေးအကြီးဆုံး အချက်များကို ခွဲခြားသတ်မှတ်ပြီး ကိုင်တွယ်ရမည်။ ဤသည်မှာ အတည်ပြုစိစစ်ခြင်းအား အတိတ် နောက်ကြောင်းပြန် စိစစ်ရေး စာရင်း လေ့ကျင့်ခန်းမှသည် ကြိုတင်ပြင်ဆင်သော ဒီဇိုင်း လုပ်ဆောင်ချက်အဖြစ်သို့ ပြောင်းလဲလိုက်သည်။
**“သက်ဆိုင်ရာ စမ်းသပ်မှု အချက်အလက်များ၏ စစ်မှန်မှုကို သေချာစေရန်”** က ရည်ရွယ်ချက်ကို ရှင်းလင်းစွာ ဖော်ပြထားသည်။ ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော အတည်ပြုစိစစ်ခြင်း၏ ပန်းတိုင်မှာ မှတ်တမ်းတင်မှု ဖန်တီးရန် မဟုတ်ပါ; စနစ်က ထုတ်လုပ်လိုက်သော အချက်အလက်များကို ယုံကြည်စိတ်ချနိုင်ကြောင်း သေချာစေရန် ဖြစ်သည်။ ဤရလဒ်ကို အဓိကထားသည့် ဦးတည်ချက်သည် ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော အတည်ပြုစိစစ်ခြင်းအား စိစစ်ရေး စာရင်းအပေါ် အဓိပ္ပာယ်ရသော လိုက်နာမှုမှ ခွဲခြားပေးသည်။
> **အဓိက ခြားနားချက် - ရည်ရွယ်ချက်နှင့် ကိုက်ညီခြင်း နှင့် တစ်ပုံစံတည်း သုံးစွဲခြင်း (Key Distinction: Fit-for-Purpose vs. One-Size-Fits-All)**
ရိုးရာ ချဉ်းကပ်မှုများအောက်တွင် စပွန်ဆာများသည် စနစ် အရေးပါမှုကို မထည့်တွက်ဘဲ တူညီသော အတည်ပြုစိစစ်မှု ပရိုတိုကောများကို မကြာခဏ အသုံးချခဲ့ကြသည်။ ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော အတည်ပြုစိစစ်ခြင်းသည် မတူညီသော မေးခွန်းများကို တောင်းဆိုသည် - ဤစနစ်သည် မည်သည့်အရာ ဆောင်ရွက်သနည်း။ ထိုလုပ်ငန်းဆောင်တာသည် မည်မျှ အရေးကြီးသနည်း။ အကယ်၍ စနစ် ပျက်ကွက်ပါက မည်သည့် နောက်ဆက်တွဲကျရောက်မှုများ ရှိသနည်း။ ဤမေးခွန်းများ၏ အဖြေများသည် အတည်ပြုစိစစ်မှု ချဉ်းကပ်မှုကို ဦးဆောင်သည် — အရေးကြီးသော စနစ်များအတွက် ပိုမို အထူးကြပ်မတ်ပြီး၊ ဘေးအန္တရာယ် နည်းပါးသော အသုံးချမှုများအတွက် ပိုမို ရိုးရှင်းစေသည်။

---


## အတည်ပြုစိစစ်ခြင်းထံ ဘေးအန္တရာယ်အခြေပြု ချဉ်းကပ်မှု (Risk-Based Approach to Validation)

ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်း ဆိုသည်မှာ အလုပ် နည်းပါးစွာ ဆောင်ရွက်ခြင်း မဟုတ်ပါ။ ၎င်းသည် မှန်ကန်သော အလုပ်ကို ဆောင်ရွက်ခြင်း ဖြစ်သည်။ ပန်းတိုင်မှာ အတည်ပြုစိစစ်မှု အားထုတ်မှုကို အရေးအကြီးဆုံး နေရာများအပေါ် အာရုံစူးစိုက်ရန် ဖြစ်သည် - အကယ်၍ ပျက်ကွက်ခဲ့ပါက ပါဝင်သူများကို ထိခိုက်စေနိုင်သော သို့မဟုတ် စမ်းသပ်မှု ရလဒ်များ၏ ယုံကြည်စိတ်ချရမှုကို ထိခိုက်စေနိုင်သော လုပ်ငန်းဆောင်တာများနှင့် အချက်အလက် အစိတ်အပိုင်းများအပေါ်တွင် ဖြစ်သည်။

### စနစ် ဘေးအန္တရာယ်ကို အကဲဖြတ်ခြင်း (Assessing System Risk)

ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်း၏ ပထမအဆင့်မှာ စနစ်တစ်ခုက မည်သည့်အရာ ဆောင်ရွက်သည်၊ မည်သည့်အရာ မှားယွင်းသွားနိုင်သည်ကို နားလည်ခြင်း ဖြစ်သည်။ E6(R3) ၏ အပိုင်း ၄.၃.၄(a) က ဤအကဲဖြတ်မှုအတွက် မူဘောင်ကို ပေးစွမ်းပြီး၊ အတည်ပြုစိစစ်မှု ချဉ်းကပ်မှုသည် “စနစ်၏ ရည်ရွယ်ထားသော အသုံးပြုမှု၊ စနစ်တွင် စုဆောင်း/ထုတ်လုပ်၊ ထိန်းသိမ်းပြီး သိမ်းဆည်းထားသော အချက်အလက်/မှတ်တမ်း၏ ရည်ရွယ်ချက်နှင့် အရေးပါမှု၊ ထို့ပြင် စက္ခုတို စမ်းသပ်မှု ပါဝင်သူများ၏ သုခချမ်းသာ၊ အခွင့်အရေးနှင့် ဘေးကင်းရေးနှင့် စမ်းသပ်မှု ရလဒ်များ၏ ယုံကြည်စိတ်ချရမှုတို့အပေါ် ထိခိုက်စေနိုင်သည့် စနစ်၏ အလားအလာတို့ကို ထည့်သွင်းစဉ်းစားသော ဘေးအန္တရာယ် အကဲဖြတ်မှုအပေါ် အခြေခံရမည်” ဟု သတ်မှတ်ထားသည်။
**အချက်အလက် အရေးပါမှု** က မေးမြန်းသည် - ဤစနစ်သည် မည်သည့် အချက်အလက် အမျိုးအစားကို ကိုင်တွယ်သနည်း။ ထုတ်ကုန် အတည်ပြုချက် ရမရ ဆုံးဖြတ်ပေးမည့် အဓိက အဆုံးသတ်တိုင်းတာချက် အချက်အလက်များလား။ ပါဝင်သူများကို ကာကွယ်ပေးသည့် ဘေးကင်းရေး အချက်အလက်များလား။ စမ်းသပ်မှု ကောက်ချက်များအပေါ် သက်ရောက်မှု အနည်းဆုံးရှိသော အုပ်ချုပ်ရေးဆိုင်ရာ အချက်အလက်များလား။ အချက်အလက် ပိုမို အရေးကြီးလေ၊ အတည်ပြုစိစစ်မှု လိုအပ်ချက်များ ပိုမို တင်းကျပ်လေ ဖြစ်သည်။
**ပျက်ကွက်မှု၏ သက်ရောက်မှု** က မေးမြန်းသည် - အကယ်၍ ဤစနစ် မလျော်ကန်စွာ အလုပ်လုပ်ပါက မည်သည့်အရာ ဖြစ်ပျက်မည်နည်း။ ၎င်းသည် မမှန်ကန်သော ဆေးပမာဏ ရရှိခြင်းဆီသို့ ဦးတည်သွားနိုင်သလား။ နှောင့်နှေးသော ဘေးကင်းရေး အစီရင်ခံမှုလား။ လွတ်ကင်းသွားသော ထိရောက်မှု အချက်အလက်များလား။ သို့မဟုတ် အချက်အလက် စစ်မှန်မှုကို မထိခိုက်ဘဲ လေ့လာမှု အဖွဲ့ကို အဆင်မပြေမှုမျှသာ ဖြစ်စေမည်လား။ ပျက်ကွက်မှုတွင် ပြင်းထန်သော နောက်ဆက်တွဲကျရောက်မှုများ ရှိသည့် စနစ်များသည် ပိုမို အထူးကြပ်မတ်သော အတည်ပြုစိစစ်မှု လိုအပ်သည်။
**ရှုပ်ထွေးမှုနှင့် ဆန်းသစ်မှု** က စနစ်သည် ထူထောင်ပြီးသား မှတ်တမ်းရှိသော သက်သေပြပြီးသား နည်းပညာကို အသုံးပြုသလား သို့မဟုတ် မသိရသေးသော ပျက်ကွက်မှု ပုံစံများပါရှိသည့် အသုံးချမှုသစ်တစ်ခုကို ကိုယ်စားပြုသလား ဆိုသည်ကို ထည့်သွင်းစဉ်းစားသည်။ ဆန်းသစ်သော စနစ်များသည် အမျိုးမျိုးသော အခြေအနေများအောက်တွင် ၎င်းတို့၏ ပြုမူပုံကို ခန့်မှန်းရန် ခက်ခဲသောကြောင့် ပိုမို ကျယ်ပြန့်သော စမ်းသပ်မှုများ လိုအပ်နိုင်သည်။
**ပေါင်းစပ်မှု အမှတ်များ** က စနစ်သည် အခြား စနစ်များနှင့် မည်သို့ ချိတ်ဆက်နေကြောင်း စိစစ်သည်။ သီးခြား အသုံးချမှုတစ်ခုသည် အခြား အသုံးချမှုများထံ အချက်အလက် ပေးပို့သည့် သို့မဟုတ် မြောက်မြားစွာသော အရင်းအမြစ်များမှ အချက်အလက် လက်ခံရရှိသည့် စနစ်တစ်ခုထက် ဘေးအန္တရာယ် နည်းပါးသည်။ ချိတ်ဆက်မှုများသည် အချက်အလက် ပျက်စီးမှု သို့မဟုတ် ဆုံးရှုံးမှုအတွက် အခွင့်အလမ်းများကို စတင်စေသည်။

### အချိုးအစားကျသော အတည်ပြုစိစစ်မှု အားထုတ်မှု (Proportionate Validation Effort)

ဘေးအန္တရာယ်ကို အကဲဖြတ်ပြီးပါက အတည်ပြုစိစစ်မှု အားထုတ်မှုသည် ထိုအတိုင်း ချိန်ညှိသွားသည်။ ဤသည်မှာ ကြိုတင်သတ်မှတ်ထားသော အတည်ပြုစိစစ်မှု အထုပ်များဆီသို့ ဦးတည်သည့် ရိုးရှင်းသော “မြင့်/လတ်/နည်း” အမျိုးအစား ခွဲခြားခြင်းကို မဆိုလိုပါ။ ၎င်းသည် သီးခြား စနစ်တစ်ခုစီအတွက် မည်သည့် အတည်ပြုစိစစ်ရေး လုပ်ဆောင်ချက်များက တန်ဖိုး ပေးစွမ်းသည်ကို စေ့စပ်စွာ ထည့်သွင်းစဉ်းစားခြင်းကို အဓိပ္ပာယ်ရသည်။

### ကိုးကားဇယား - စနစ် အရေးပါမှုအလိုက် အတည်ပြုစိစစ်မှု အပြင်းအထန် ပမာဏ (Validation Intensity by System Criticality)


| စနစ် ဂုဏ်သတ္တိ (System Characteristic) | အတည်ပြုစိစစ်မှု အာရုံစိုက်မှု (Validation Focus) | မှတ်တမ်းတင်မှု နက်ရှိုင်းမှု (Documentation Depth) |
| --- | --- | --- |
| **အဓိက အဆုံးသတ်တိုင်းတာချက် ရယူမှု** | ကျယ်ပြန့်သော လုပ်ငန်းဆောင်တာ စမ်းသပ်ခြင်း၊ အချက်အလက် စစ်မှန်မှု စိစစ်ခြင်း၊ စစ်ဆေးမှု လမ်းကြောင်း အတည်ပြုစိစစ်ခြင်း၊ ဘက်စုံကျသော အသုံးပြုသူ လက်ခံရေး စမ်းသပ်ခြင်း | တိကျသော စမ်းသပ်မှု စာသားများနှင့် ခြေရာခံနိုင်မှု ဇယားများပါရှိသော ပြည့်စုံသော အတည်ပြုစိစစ်မှု မှတ်တမ်းတင်မှု |
| **ဘေးကင်းရေး အချက်အလက် စီမံခန့်ခွဲခြင်း** | စေ့စပ်သော လုပ်ငန်းစဉ် စမ်းသပ်ခြင်း၊ အချိန်ကာလ စိစစ်ခြင်း၊ တိုင်ကြားအကြောင်းကြားရေး လုပ်ထုံးလုပ်နည်းများ၊ ဘေးကင်းရေး အချက်အလက် အစုအဝေးများနှင့် ပေါင်းစပ်ခြင်း | ဘေးကင်းရေးအတွက် အရေးပါသော လုပ်ငန်းဆောင်တာများကို အဓိကထားသည့် စေ့စပ်သော မှတ်တမ်းတင်မှု |
| **စမ်းသပ်မှု အဖွဲ့ခွဲခြင်းနှင့် ကုသမှု တာဝန်ပေးအပ်ခြင်း** | ပရိုဂရမ် စိစစ်ခြင်း၊ မျက်ကွယ်ပြုမှု စစ်မှန်မှု၊ အရေးပေါ် မျက်ကွယ်ပြုမှု ဖော်ထုတ်ရေး လုပ်ထုံးလုပ်နည်းများ | ဘက်လိုက်မှုကို စတင်စေနိုင်သော သို့မဟုတ် ကုသမှုကို ဖော်ထုတ်နိုင်သော လုပ်ငန်းဆောင်တာများအပေါ် အာရုံစိုက်ခြင်း |
| **ဒုတိယဦးစားပေး အဆုံးသတ်တိုင်းတာချက် စုဆောင်းခြင်း** | သင့်လျော်သော လုပ်ငန်းဆောင်တာ စမ်းသပ်ခြင်း၊ အချက်အလက် ရိုက်ထည့်မှု ထိန်းချုပ်မှုများ၊ မေးခွန်း စီမံခန့်ခွဲခြင်း | အဓိက လုပ်ငန်းဆောင်တာများကို လွှမ်းခြုံထားသည့် အချိုးအစားကျသော မှတ်တမ်းတင်မှု |
| **စမ်းသပ်ရာနေရာ အပြန်အလှန် ဆက်သွယ်ရေး ကိရိယာများ** | အခြေခံ လုပ်ငန်းဆောင်တာ စိစစ်ခြင်း၊ ဝင်ရောက်ကြည့်ရှုခွင့် ထိန်းချုပ်မှုများ၊ မှတ်တမ်း ထိန်းသိမ်းခြင်း | မရှိမဖြစ် စွမ်းဆောင်ရည်များကို အဓိကထားသည့် ရိုးရှင်းသော မှတ်တမ်းတင်မှု |


---


## အချက်အလက် အရေးပါမှုအပေါ် အခြေခံ၍ စနစ် လိုအပ်ချက်များကို အဓိပ္ပာယ်ဖွင့်ဆိုခြင်း (Defining System Requirements Based on Data Criticality)

မည်သည့် စနစ်ကိုမဆို အတည်ပြုမစိစစ်မီ စပွန်ဆာများနှင့် သုတေသီများသည် စနစ်က မည်သည့်အရာ ဆောင်ရွက်ရန် လိုအပ်ကြောင်း နားလည်ရမည်။ ဤနားလည်မှုကို လိုအပ်ချက်များ မှတ်တမ်းတင်မှုတွင် ရယူထားသည် — သို့သော် ထိုမှတ်တမ်းတင်မှု၏ နက်ရှိုင်းမှုနှင့် တရားဝင်မှုတို့သည် ၎င်းတို့ကိုယ်တိုင် စနစ် အရေးပါမှုနှင့် အချိုးအစားကျရမည်။

### အသုံးပြုသူ လိုအပ်ချက်များ (User Requirements)

အသုံးပြုသူ လိုအပ်ချက်များသည် စနစ်အား အသုံးပြုမည့်သူများ၏ ရှုထောင့်မှ စနစ်က မည်သည့်အရာ အောင်မြင်အောင် ဆောင်ရွက်ရမည်ကို ဖော်ပြသည်။ ဤသည်တို့မှာ နည်းပညာဆိုင်ရာ သတ်မှတ်ချက်များ မဟုတ်ဘဲ လုပ်ငန်းဆောင်တာဆိုင်ရာ လိုအပ်ချက်များ ဖြစ်ကြသည်။ “စနစ်သည် ဆေးဝါး ပေးပို့သည့် ရက်စွဲနှင့် အချိန်ကို ရယူရမည်” သည် အသုံးပြုသူ လိုအပ်ချက် ဖြစ်သည်။ “စနစ်သည် အချိန်တံဆိပ် ကွက်များပါရှိသော MySQL အချက်အလက် အစုအဝေးကို အသုံးပြုရမည်” သည် နည်းပညာဆိုင်ရာ သတ်မှတ်ချက် ဖြစ်သည်။
အဆင့်မြင့် အရေးပါမှုရှိသော စနစ်များအတွက် အသုံးပြုသူ လိုအပ်ချက်များသည် -
- **တိကျရမည် -** လိုက်နာမှုကို ပမာဏအလိုက် အကဲဖြတ်နိုင်လောက်အောင် ရှင်းလင်းရမည်
- **ပြည့်စုံရမည် -** ရည်ရွယ်ထားသော အသုံးပြုမှု အားလုံးနှင့် မျှော်မှန်းထားသော အခြေအနေများကို လွှမ်းခြုံရမည်
- **ခြေရာခံနိုင်ရမည် -** ၎င်းတို့ကို အကြောင်းပြပေးသည့် စီးပွားရေး သို့မဟုတ် စည်းမျဉ်းဆိုင်ရာ လိုအပ်ချက်များထံ ချိတ်ဆက်ထားရမည်
- **စမ်းသပ်နိုင်ရမည် -** စိစစ်ခွင့်ပြုသည့် နည်းလမ်းများဖြင့် ဖော်ပြထားရမည်
ပိုမိုနည်းပါးသော အရေးပါမှုရှိသော စနစ်များအတွက် အသုံးပြုသူ လိုအပ်ချက်များသည် ပိုမို ရိုးရှင်းနိုင်သည် — အရာတစ်ခုစီအလိုက် သတ်မှတ်ချက်များထက် လုပ်ငန်းဆောင်တာ အထွေထွေ သုံးသပ်ချက် ဖြစ်နိုင်သည် — မျှော်မှန်းထားသော စနစ် ပြုမူပုံကို သင့်လျော်စွာ ဖော်ပြထားလျှင် ဖြစ်သည်။
> **လက်တွေ့ကျသော ဥပမာ - EDC စနစ် လိုအပ်ချက်များ (Practical Example: EDC System Requirements)**
အဓိက အဆုံးသတ်တိုင်းတာချက် အချက်အလက်များကို ကိုင်တွယ်သည့် အီလက်ထရောနစ် အချက်အလက် စုဆောင်းမှု စနစ်တစ်ခုအတွက် အသုံးပြုသူ လိုအပ်ချက်များတွင် ပါဝင်နိုင်သည် - “စနစ်သည် အနာဂတ် ရက်စွဲများ ရိုက်ထည့်ခြင်းကို တားဆီးရမည်”၊ “စနစ်သည် ပုံစံ ပြည့်စုံမှုအတွက် အီလက်ထရောနစ် လက်မှတ် လိုအပ်ရမည်”၊ “စနစ်သည် အချက်အလက် ရိုက်ထည့်မှုများနှင့် ပြင်ဆင်ချက်များ အားလုံး၏ ပြည့်စုံသော စစ်ဆေးမှု လမ်းကြောင်းကို ထိန်းသိမ်းရမည်”။ လိုအပ်ချက် တစ်ခုစီသည် တိကျသည်၊ စမ်းသပ်နိုင်သည်၊ ထို့ပြင် အချက်အလက် စစ်မှန်မှု ရည်မှန်းချက်များထံ ခြေရာခံနိုင်သည်။ စမ်းသပ်ရာနေရာ ဖိုင် စီမံခန့်ခွဲမှု စနစ်တစ်ခုအတွက် လိုအပ်ချက်များသည် ပိုမိုရိုးရှင်းနိုင်သည် - “စနစ်သည် ခွင့်ပြုချက်ရှိသော အသုံးပြုသူများထံ ကန့်သတ်ထားသော ဝင်ရောက်ကြည့်ရှုခွင့်ဖြင့် စာရွက်စာတမ်း တင်ပို့ခြင်း၊ သိုလှောင်ခြင်းနှင့် ပြန်လည်ထုတ်ယူခြင်းတို့ကို ခွင့်ပြုရမည်”။

### ဒီဇိုင်းရေးဆွဲရာတွင် ပါဝင်သူများနှင့် ကျန်းမာရေး ကျွမ်းကျင်သူများကို ပါဝင်စေခြင်း (Involving Participants and Healthcare Professionals in Design)

E6(R3) သည် စက္ခုတို စမ်းသပ်မှုများတွင် ပါဝင်သူနှင့် ထိတွေ့နေသော နည်းပညာ၏ တိုးတက်လာသော ကဏ္ဍကို ရောင်ပြန်ဟပ်သည့် အကြံပြုချက်တစ်ခုကို စတင်မိတ်ဆက်လိုက်သည်။ အပိုင်း ၄.၃ ၏ နိဒါန်း စာပိုဒ်တွင် ဖော်ပြထားသည်မှာ -
> “ကွန်ပျူတာစနစ်များသည် ရည်ရွယ်ထားသော အသုံးပြုသူ လူဦးရေက အသုံးပြုရန် သင့်လျော်ကြောင်း သေချာစေရန် သက်ဆိုင်ပါက စနစ်၏ ဒီဇိုင်းရေးဆွဲရာတွင် ရည်ရွယ်ထားသော ပါဝင်သူ လူဦးရေနှင့် ကျန်းမာရေး ကျွမ်းကျင်သူများ၏ ကိုယ်စားလှယ်များကို ပါဝင်စေရန် အကြံပြုထားသည်။”
ဤသည်မှာ စည်းမျဉ်းဆိုင်ရာ စာသားများအောက်တွင် မြှုပ်နှံထားသော ရိုးရိုး အကြံပြုချက်မျှ မဟုတ်ပါ။ စပွန်ဆာတစ်ခုသည် စမတ်ဖုန်း အတွေ့အကြုံ အနည်းငယ်သာရှိသော အသက် ၇၂ နှစ်ရှိ ပါဝင်သူတစ်ဦး နေ့စဉ် အသုံးပြုရမည့် ePRO အသုံးချမှုကို တပ်ဆင်လိုက်သောအခါ ထိုအသုံးချမှု၏ အသုံးပြုနိုင်စွမ်းသည် အချက်အလက် အရည်အသွေးကို တိုက်ရိုက် ထိခိုက်စေသည်။ eConsent မူဘောင်တစ်ခုသည် ဒစ်ဂျစ်တယ် ချိတ်ဆက်မှုမှတစ်ဆင့် ရှုပ်ထွေးသော စမ်းသပ်မှု သတင်းအချက်အလက်များကို တင်ပြသောအခါ ပါဝင်သူများသည် နည်းပညာအရ သာမကဘဲ အဓိပ္ပာယ်ရှိစွာ အသုံးပြုနိုင်ရမည်။
အသုံးပြုသူကို အဓိကထားသည့် ဒီဇိုင်းတွင် လိုအပ်ချက်များနှင့် ဒီဇိုင်း အဆင့်များအတွင်း ကိုယ်စားလှယ် အဆုံးသတ် အသုံးပြုသူများကို ပါဝင်စေခြင်း ပါဝင်သည်။ ပါဝင်သူနှင့် ထိတွေ့နေသော နည်းပညာများအတွက် — ePRO စနစ်များ၊ eConsent မူဘောင်များ၊ ဝတ်ဆင်နိုင်သော စက်ပစ္စည်းများ၊ လူနာနှင့် ထိတွေ့နေသော မိုဘိုင်း အသုံးချမှုများ — ဤသည်မှာ ပစ်မှတ် လူဦးရေ၏ အသက်အရွယ် အကန့်အသတ်၊ နည်းပညာ ကျွမ်းကျင်မှုနှင့် ရုပ်ပိုင်းဆိုင်ရာ စွမ်းဆောင်ရည်များကို ရောင်ပြန်ဟပ်သည့် တစ်ဦးချင်းစီနှင့်အတူ ပုံစံငယ်များကို စမ်းသပ်ခြင်းကို အဓိပ္ပာယ်ရသည်။ ကျန်းမာရေး ကျွမ်းကျင်သူနှင့် ထိတွေ့နေသော စနစ်များအတွက် ဤသည်မှာ နည်းပညာဆိုင်ရာ ဖွဲ့စည်းတည်ဆောက်ပုံကို နားလည်သော IT ကျွမ်းကျင်သူများတင်မကဘဲ ၎င်းတို့၏ နေ့စဉ် လုပ်ငန်းစဉ်တွင် စနစ်ကို အမှန်တကယ် အသုံးပြုမည့် ဆရာဝန်များနှင့် ပေါင်းစပ်ညှိနှိုင်းရေးမှူးများကို ပါဝင်စေခြင်းကို အဓိပ္ပာယ်ရသည်။
လက်တွေ့ကျသော နောက်ဆက်တွဲကျရောက်မှုမှာ - အဆုံးသတ် အသုံးပြုသူ၏ ပါဝင်အကြံပြုချက် မပါဘဲ ဒီဇိုင်းဆွဲထားသော စနစ်များသည် လိုက်နာမှုနှုန်း နည်းပါးခြင်း၊ အချက်အလက် ရိုက်ထည့်မှု အမှားများ တိုးတက်လာခြင်း၊ ထို့ပြင် နောက်ဆုံးတွင် အချက်အလက် အရည်အသွေး ထိခိုက်ခြင်းတို့၏ ဘေးအန္တရာယ်ရှိသည် — ဤသည်တို့မှာ အတည်ပြုစိစစ်ခြင်းက တားဆီးရန် ရည်ရွယ်ထားသည့် အတိအကျ ရလဒ်များ ဖြစ်ကြသည်။

### လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များ (Functional Specifications)

လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များသည် အသုံးပြုသူ လိုအပ်ချက်များကို စနစ်က ထိုလိုအပ်ချက်များနှင့် မည်သို့ ကိုက်ညီမည်ဆိုသည့် ဖော်ပြချက်များအဖြစ်သို့ ဘာသာပြန်ပေးသည်။ အကယ်၍ အသုံးပြုသူ လိုအပ်ချက်များက စနစ်က မည်သည့်အရာ ဆောင်ရွက်ရမည်ကို ပြောဆိုပါက၊ လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များသည် ၎င်းကို မည်သို့ ဆောင်ရွက်မည်ကို ပြောဆိုသည်။
အရေးပါသော စနစ်များအတွက် လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များသည် အောက်ပါတို့ကို ကိုင်တွယ်ရမည် -
- အသုံးပြုသူ လိုအပ်ချက် တစ်ခုစီကို မည်သို့ အကောင်အထည်ဖော်မည်
- စနစ် ပြင်ဆင်သတ်မှတ်မှု ဆက်တင်များနှင့် ၎င်းတို့၏ အကြောင်းပြချက်
- ချိတ်ဆက်မှု ပြုမူပုံများနှင့် အတည်ပြုစိစစ်မှု စည်းမျဉ်းများ
- အမှား ကိုင်တွယ်မှုနှင့် ကင်းလွတ်ခွင့် ပြုပြင်ဆောင်ရွက်မှု
- စစ်ဆေးမှု လမ်းကြောင်း ထုတ်လုပ်ခြင်းနှင့် သိုလှောင်ခြင်း
အရေးပါမှု နည်းပါးသော စနစ်များအတွက် လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များကို အတိုချုပ် ပြုလုပ်နိုင်သည် သို့မဟုတ် စာရွက်စာတမ်း တစ်ခုတည်းတွင် အသုံးပြုသူ လိုအပ်ချက်များနှင့် ပေါင်းစပ်နိုင်သည်။ အဓိက သော့ချက်မှာ တစ်ဦးတစ်ယောက်က — စပွန်ဆာ၊ စနစ် ရောင်းချသူ သို့မဟုတ် နှစ်ဦးလုံး ဖြစ်စေ — အတည်ပြုစိစစ်မှု စမ်းသပ်ခြင်းကို ထောက်ပံ့ရန် လုံလောက်သော ရှင်းလင်းမှုဖြင့် ရည်ရွယ်ထားသော စနစ် ပြုမူပုံကို မှတ်တမ်းတင်ထားခြင်း ဖြစ်သည်။

### လိုအပ်ချက်များ ခြေရာခံနိုင်မှု (Requirements Traceability)

အဆင့်မြင့် အရေးပါမှုရှိသော စနစ်များအတွက် ခြေရာခံနိုင်မှု ဇယားသည် အသုံးပြုသူ လိုအပ်ချက်များကို လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များထံ၊ ထိုမှတစ်ဆင့် စမ်းသပ်မှု ဖြစ်စဉ်များထံ ချိတ်ဆက်ပေးသည်။ ဤကွင်းဆက်သည် လိုအပ်ချက် တိုင်းကို စနစ် ဒီဇိုင်းတွင် ကိုင်တွယ်ထားကြောင်းနှင့် စမ်းသပ်ခြင်းတွင် စိစစ်ထားကြောင်း သေချာစေသည်။ မည်သည့်အရာမျှ မေ့လျော့မထားပါ။ မည်သည့်အရာကိုမျှ မယူဆထားပါ။
အလယ်အလတ် အရေးပါမှုရှိသော စနစ်များအတွက် ခြေရာခံနိုင်မှုသည် ပိုမိုရိုးရှင်းသော ပုံသဏ္ဌာန်များကို ယူဆောင်နိုင်သည် — တရားဝင် ဇယားတစ်ခုထက် မှတ်တမ်းတင်ထားသော ချိတ်ဆက်မှု ဖြစ်နိုင်သည်။ ပိုမိုနည်းပါးသော အရေးပါမှုရှိသော စနစ်များအတွက် ခြေရာခံနိုင်မှုသည် ချဉ်းကပ်မှုသည် ရည်ရွယ်ထားသော လုပ်ငန်းဆောင်တာများကို သက်သေပြနိုင်လောက်အောင် လွှမ်းခြုံထားလျှင် စမ်းသပ်မှု ချဉ်းကပ်မှုတွင် ကိန်းဝပ်နေနိုင်သည်။ အပိုင်း ၄.၃.၄(e) က အသိအမှတ်ပြုထားသည့်အတိုင်း “သီးသန့် ရေးဆွဲထားသော စနစ်များ၊ ပြင်ဆင်သတ်မှတ်ရန် ဒီဇိုင်းဆွဲထားသော စနစ်များ သို့မဟုတ် မည်သည့် ပြုပြင်ပြောင်းလဲမှုမျှ မလိုအပ်သော စနစ်များအတွက် မတူညီသော အတည်ပြုစိစစ်မှု အဆင့်များ လိုအပ်နိုင်သည်။”
> **ခြေရာခံနိုင်မှု မူ (The Traceability Principle)**
မှတ်တမ်းတင်မှု ပုံစံကို မထည့်တွက်ဘဲ မူမှာ ပြောင်းလဲမှု မရှိပါ - အတည်ပြုစိစစ်မှု စမ်းသပ်ခြင်းသည် လိုအပ်ချက်များ ပြည့်စုံကြောင်း စိစစ်ရမည်။ ခြေရာခံနိုင်မှု မှတ်တမ်းတင်မှု၏ နက်ရှိုင်းမှုသည် လစ်ဟာချက်များ မသိရှိဘဲ ကျန်ရှိနေမည့် ဘေးအန္တရာယ်နှင့် ကိုက်ညီရမည်။ အရေးပါသော လုပ်ငန်းဆောင်တာတစ်ခုအတွက် လွတ်ကင်းနေသော စမ်းသပ်မှု ဖြစ်စဉ်တစ်ခုသည် ပြင်းထန်သော သတိမမူမိခြင်း ဖြစ်သည်; သေးငယ်သော အုပ်ချုပ်ရေးဆိုင်ရာ လုပ်ငန်းဆောင်တာတစ်ခုအတွက် လွတ်ကင်းနေသော စမ်းသပ်မှု ဖြစ်စဉ်တစ်ခုသည် အကျိုးဆက် ပိုမို နည်းပါးသည်။

---


## စဉ်ဆက်မပြတ် ထိန်းသိမ်းမှုနှင့် ပြောင်းလဲမှု ထိန်းချုပ်မှု (Ongoing Maintenance and Change Control)

အတည်ပြုစိစစ်ခြင်းဆိုသည်မှာ ခဏတာ မဟုတ်ပါ; ၎င်းသည် သက်တမ်းတစ်ခု ဖြစ်သည်။ ဇန်နဝါရီလတွင် အတည်ပြုစိစစ်ထားသော စနစ်တစ်ခုသည် မတ်လတွင် မွမ်းမံမှုများ၊ ဇူလိုင်လတွင် ပြင်ဆင်သတ်မှတ်မှုအသစ်များ၊ ထို့ပြင် တစ်နှစ်လုံးတွင် လုံခြုံရေး ပြင်ဆင်ချက်များ လိုအပ်နိုင်သည်။ ပြောင်းလဲမှု တိုင်းသည် အတည်ပြုစိစစ်ထားသော လုပ်ငန်းဆောင်တာများကို ထိခိုက်စေနိုင်သည့် အလားအလာ ရှိသည်။ ဤပြောင်းလဲမှုများကို စီမံခန့်ခွဲခြင်းသည် အစောပိုင်း အတည်ပြုစိစစ်ခြင်းကဲ့သို့ပင် အရေးကြီးပါသည်။

### ပြောင်းလဲမှု ထိန်းချုပ်မှု မူများ (Change Control Principles)

ပြောင်းလဲမှု ထိန်းချုပ်မှုသည် အတည်ပြုစိစစ်ထားသော စနစ်များသို့ ပြုပြင်ပြောင်းလဲမှုများကို အကောင်အထည်မဖော်မီ အကဲဖြတ်ခြင်း၊ အတည်ပြုခြင်း၊ စမ်းသပ်ခြင်းနှင့် မှတ်တမ်းတင်ခြင်းတို့ကို သေချာစေသည်။ ဤလုပ်ငန်းစဉ်၏ တင်းကျပ်မှုသည် အစောပိုင်း အတည်ပြုစိစစ်ခြင်းကဲ့သို့ပင် စနစ် အရေးပါမှုနှင့် ပြောင်းလဲမှု၏ သဘောသဘာဝတို့နှင့် အချိုးအစားကျရမည်။
**သက်ရောက်မှု အကဲဖြတ်မှု** က မေးမြန်းသည် - ဤပြောင်းလဲမှုသည် မည်သည့် အတည်ပြုစိစစ်ထားသော လုပ်ငန်းဆောင်တာများကို ထိခိုက်စေနိုင်သနည်း။ အသုံးပြုသူ အပြန်အလှန် ဆက်သွယ်မှုကို ပြုပြင်ပြောင်းလဲသည့် ဆော့ဖ်ဝဲလ် မွမ်းမံမှုတစ်ခုသည် အချက်အလက်များ သိုလှောင်ပုံ သို့မဟုတ် ပေးပို့ပုံကို ပြောင်းလဲသည့် မွမ်းမံမှုတစ်ခုနှင့် မတူညီသော အကျိုးဆက်များ ရှိနိုင်သည်။ အရေးပါသော အချက်အလက် စီးဆင်းမှုများကို ထိခိုက်စေသည့် ပြောင်းလဲမှုများသည် ဟန်ပြ ပြုပြင်ပြောင်းလဲမှုများထက် ပိုမို စေ့စပ်သော အကဲဖြတ်မှု လိုအပ်သည်။
**စမ်းသပ်မှု လိုအပ်ချက်များ** သည် သက်ရောက်မှု အကဲဖြတ်မှုမှ ဆင်းသက်လာသည်။ အကယ်၍ ပြောင်းလဲမှုတစ်ခုသည် အတည်ပြုစိစစ်ထားသော လုပ်ငန်းဆောင်တာများကို ထိခိုက်စေနိုင်ပါက ထိုလုပ်ငန်းဆောင်တာများကို ပြန်လည် စမ်းသပ်ရမည်။ စမ်းသပ်မှု နယ်ပယ်သည် ဖြစ်နိုင်ချေရှိသော သက်ရောက်မှု နယ်ပယ်နှင့် ကိုက်ညီရမည်။ သေးငယ်သော ပြင်ဆင်သတ်မှတ်မှု ပြောင်းလဲမှုတစ်ခုသည် ပစ်မှတ်ထား စမ်းသပ်မှုသာ လိုအပ်နိုင်သည်; ကြီးမားသော ဆော့ဖ်ဝဲလ် အဆင့်မြှင့်တင်မှုတစ်ခုသည် ဘက်စုံကျသော ပြန်လည် စမ်းသပ်မှု (regression testing) လိုအပ်နိုင်သည်။
**မှတ်တမ်းတင်ခြင်း** က မည်သည့်အရာ ပြောင်းလဲခဲ့သည်၊ အဘယ်ကြောင့်၊ မည်သူက အတည်ပြုခဲ့သည်၊ မည်သည့် စမ်းသပ်မှု ဆောင်ရွက်ခဲ့သည်၊ ထို့ပြင် ရလဒ်များက မည်သည့်အရာ ပြသခဲ့သည်တို့ကို ရယူသည်။ ဤမှတ်တမ်းတင်ခြင်းသည် ပြောင်းလဲမှုများကို ထိန်းချုပ်ခဲ့ကြောင်းနှင့် စနစ်သည် ပြုပြင်ပြောင်းလဲပြီးနောက် ရည်ရွယ်ချက်နှင့် ဆက်လက် ကိုက်ညီနေကြောင်း သက်သေအထောက်အထား ပေးစွမ်းသည်။
> **ပြောင်းလဲမှု အမျိုးအစားများ (Categories of Change)**
အတည်ပြုစိစစ်ထားသော စနစ်များသို့ ပြောင်းလဲမှုများသည် ပုံမှန်အားဖြင့် အမျိုးအစား အများအပြားအောက်သို့ ကျရောက်ကြသည် -
- **စီမံကိန်းချထားသော မွမ်းမံမှုများ -** ရောင်းချသူက ထုတ်လုပ်လိုက်သော ဆော့ဖ်ဝဲလ် ဗားရှင်းများ၊ အချိန်ဇယားဆွဲထားသော အဆင့်မြှင့်တင်မှုများ
- **ပြင်ဆင်ရေး ပြောင်းလဲမှုများ -** ခွဲခြားသတ်မှတ်ထားသော ချို့ယွင်းချက်များ သို့မဟုတ် မကိုက်ညီမှုများအတွက် ပြင်ဆင်ချက်များ
- **အရေးပေါ် ပြောင်းလဲမှုများ -** လုံခြုံရေး ထိခိုက်လွယ်မှုများ သို့မဟုတ် အရေးပါသော ပျက်ကွက်မှုများကို ကိုင်တွယ်ရန် အရေးပေါ် ပြုပြင်ပြောင်းလဲမှုများ
- **ပြင်ဆင်သတ်မှတ်မှု ပြောင်းလဲမှုများ -** စနစ် ဆက်တင်များ၊ လုပ်ငန်းစဉ်များ သို့မဟုတ် အသုံးပြုသူ ဝင်ရောက်ကြည့်ရှုခွင့်သို့ ပြုပြင်ပြောင်းလဲမှုများ
အမျိုးအစား တစ်ခုစီတွင် မတူညီသော လုပ်ထုံးလုပ်နည်းများ ရှိနိုင်သော်လည်း အားလုံးသည် အကောင်အထည်မဖော်မီ မှတ်တမ်းတင်ထားသော အကဲဖြတ်မှုနှင့် သင့်လျော်သော စမ်းသပ်မှုတို့ လိုအပ်ကြသည်။

### ပုံမှန် စနစ် သုံးသပ်ခြင်း (Periodic System Review)

ပြောင်းလဲမှုအလိုက် အကဲဖြတ်ခြင်းထက် ကျော်လွန်၍ စပွန်ဆာများသည် ကွန်ပျူတာစနစ်များသည် ရည်ရွယ်ချက်နှင့် ဆက်လက် ကိုက်ညီကြောင်း အတည်ပြုရန် ပုံမှန် သုံးသပ်သင့်သည်။ အပိုင်း ၄.၃.၄(d) တွင် ဖော်ပြထားသည့်အတိုင်း “ကွန်ပျူတာစနစ်များသည် စနစ်၏ သက်တမ်းတစ်လျှောက် အတည်ပြုစိစစ်ထားသော အခြေအနေတွင် ဆက်လက် ရှိနေကြောင်း သေချာစေရန် ပုံမှန် သုံးသပ်ခြင်းသည် သင့်လျော်နိုင်သည်။” နည်းညာ ပြောင်းလဲတိုးတက်လာသည်။ ရောင်းချသူ ပံ့ပိုးမှု အခြေအနေ ပြောင်းလဲသွားသည်။ ထိခိုက်လွယ်မှုသစ်များကို တွေ့ရှိရသည်။ လွန်ခဲ့သော နှစ်နှစ်က ရည်ရွယ်ချက်နှင့် ကိုက်ညီခဲ့သော စနစ်တစ်ခုသည် ယနေ့တွင် စိန်ခေါ်မှုသစ်များနှင့် ရင်ဆိုင်ရနိုင်သည်။
ပုံမှန် သုံးသပ်မှုများသည် အောက်ပါတို့ကို ထည့်သွင်းစဉ်းစားသည် -
- စနစ်သည် အသုံးပြုသူ လိုအပ်ချက်များနှင့် ဆက်လက် ကိုက်ညီခြင်း ရှိမရှိ
- ဘက်စုံကျသော ပြန်လည် အတည်ပြုစိစစ်မှု ပြုလုပ်ရန် လိုအပ်လောက်အောင် ပြောင်းလဲမှုများ စုပုံလာခြင်း ရှိမရှိ
- ရောင်းချသူ ပံ့ပိုးမှု လုံလောက်စွာ ရှိနေဆဲ ရှိမရှိ
- လုံခြုံရေး ထိန်းချုပ်မှုများသည် လက်ရှိ ခြိမ်းခြောက်မှုများကို ဆက်လက် ကာကွယ်နိုင်ခြင်း ရှိမရှိ
- စနစ်၏ ကဏ္ဍသည် ယင်း၏ အရေးပါမှုကို ပြောင်းလဲစေသည့် နည်းလမ်းများဖြင့် ပြောင်းလဲသွားခြင်း ရှိမရှိ
ဤသုံးသပ်မှုများ၏ အကြိမ်ရေနှင့် နက်ရှိုင်းမှုတို့သည်လည်း ထိုအတိုင်း အချိုးအစားကျရမည်။ အရေးပါသော စနစ်များသည် အုပ်ချုပ်ရေးဆိုင်ရာ ကိရိယာများထက် ပိုမိုမကြာခဏ စေ့စပ်သော သုံးသပ်မှုကို ရရှိထိုက်သည်။

---


## အဓိက မှတ်သားဖွယ်ရာများ (Key Takeaways)

- ရည်ရွယ်ချက်နှင့် ကိုက်ညီသော အတည်ပြုစိစစ်ခြင်းသည် စနစ်အား ယေဘုယျ အတည်ပြုစိစစ်မှု ပုံစံခွက်တစ်ခုအောက်သို့ သွတ်သွင်းခဲ့သလား မဟုတ်ဘဲ စနစ်သည် ယင်း၏ ရည်ရွယ်ထားသော လုပ်ငန်းဆောင်တာများကို ယုံကြည်စိတ်ချစွာ ဆောင်ရွက်နိုင်သလားဟု မေးမြန်းသည်
- ဘေးအန္တရာယ်အခြေပြု ချဉ်းကပ်မှုများသည် အတည်ပြုစိစစ်မှု အားထုတ်မှုကို အရေးအကြီးဆုံး နေရာများအပေါ် အာရုံစူးစိုက်သည် — ပျက်ကွက်မှုက ပါဝင်သူများကို ထိခိုက်စေနိုင်သော သို့မဟုတ် အချက်အလက် ယုံကြည်စိတ်ချရမှုကို ထိခိုက်စေနိုင်သော စနစ်များအပေါ်တွင် ဖြစ်သည်
- စနစ် အရေးပါမှု အကဲဖြတ်ခြင်းသည် သင့်လျော်သော အတည်ပြုစိစစ်မှု အပြင်းအထန် ပမာဏကို ဆုံးဖြတ်ရန် အချက်အလက် အရေးပါမှု၊ ပျက်ကွက်မှု သက်ရောက်မှု၊ ရှုပ်ထွေးမှုနှင့် ပေါင်းစပ်မှု အမှတ်များကို ထည့်သွင်းစဉ်းစားသည်
- အသုံးပြုသူ လိုအပ်ချက်များသည် စနစ်က မည်သည့်အရာ အောင်မြင်အောင် ဆောင်ရွက်ရမည်ကို ဖော်ပြသည်; လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များသည် ၎င်းကို မည်သို့ အောင်မြင်အောင် ဆောင်ရွက်မည်ကို ဖော်ပြသည်
- လိုအပ်ချက်များ ခြေရာခံနိုင်မှုသည် အတည်ပြုစိစစ်မှု စမ်းသပ်ခြင်းက လိုအပ်ချက် တစ်ခုစီကို စိစစ်ကြောင်း သေချာစေသည်၊ စာရွက်စာတမ်း မှတ်တမ်းတင်မှု နက်ရှိုင်းမှုသည် စနစ် အရေးပါမှုနှင့် အချိုးအစားကျရမည်
- ပြောင်းလဲမှု ထိန်းချုပ်မှုသည် စနစ် သက်တမ်းတစ်လျှောက် အတည်ပြုစိစစ်ထားသော အခြေအနေကို ထိန်းသိမ်းပေးသည်၊ အကဲဖြတ်ခြင်းနှင့် စမ်းသပ်ခြင်းတို့သည် ပြောင်းလဲမှု၏ သဘောသဘာဝနှင့် သက်ရောက်မှုတို့နှင့် အချိုးအစားကျရမည်
- ပုံမှန် သုံးသပ်ခြင်းသည် နည်းပညာနှင့် အခြေအနေများ ပြောင်းလဲတိုးတက်လာသည်နှင့်အမျှ စနစ်များသည် ရည်ရွယ်ချက်နှင့် ဆက်လက် ကိုက်ညီကြောင်း အတည်ပြုပေးသည်

---


## အနာဂတ်ကို မျှော်ကြည့်ခြင်း (Looking Ahead)

ဤသင်ခန်းစာသည် မူခွဲ ၉.၃ က ထူထောင်ထားသော အတည်ပြုစိစစ်မှု မူများကို မိတ်ဆက်ခဲ့ပြီး E6(R3) ၏ အပိုင်း ၄.၃.၄ တွင် အသေးစိတ် ဖော်ပြခဲ့သည်။ အတည်ပြုစိစစ်မှု အားထုတ်မှုသည် စနစ် အရေးပါမှုနှင့်အညီ ချိန်ညှိရန် မျှော်လင့်ရသည် — အဓိက အဆုံးသတ်တိုင်းတာချက်များနှင့် ဘေးကင်းရေး အချက်အလက်များကို ကိုင်တွယ်သည့် စနစ်များအတွက် ပိုမို အထူးကြပ်မတ်ပြီး၊ ဘေးအန္တရာယ် နည်းပါးသော အသုံးချမှုများအတွက် ပိုမို ရိုးရှင်းစေသည်။
မော်ဂျူး ၈ သည် ဤအုတ်မြစ်အပေါ် အခြေခံ၍ တည်ဆောက်ထားပြီး၊ အပိုင်း ၄.၃ ၏ ထပ်ဆောင်း လုပ်ငန်းဆောင်ရွက်မှုဆိုင်ရာ လိုအပ်ချက်များကို ကိုင်တွယ်သည် - စနစ် အသုံးပြုမှုဆိုင်ရာ လုပ်ထုံးလုပ်နည်းများ (၄.၃.၁)၊ လေ့ကျင့်သင်ကြားမှု (၄.၃.၂)၊ လုံခြုံရေး ထိန်းချုပ်မှုများနှင့် အချက်အလက် အရန်သိမ်းဆည်းမှု (၄.၃.၃)၊ စနစ် ထုတ်လုပ်ဖြန့်ချိရေး လုပ်ထုံးလုပ်နည်းများ (၄.၃.၅)၊ စနစ် ပျက်ကွက်မှုများအတွက် အရေးပေါ် စီမံကိန်း ရေးဆွဲခြင်း (၄.၃.၆)၊ နည်းပညာဆိုင်ရာ ပံ့ပိုးမှု (၄.၃.၇)၊ ထို့ပြင် အသုံးပြုသူ ဝင်ရောက်ကြည့်ရှုခွင့် စီမံခန့်ခွဲခြင်း (၄.၃.၈)။ ဤနေရာတွင် လွှမ်းခြုံထားသော အတည်ပြုစိစစ်မှု မူများနှင့်အတူ ဤလိုအပ်ချက်များသည် စက္ခုတို စမ်းသပ်မှုများပါ ကွန်ပျူတာစနစ်များအတွက် ပြည့်စုံသော မူဘောင်ကို ဖန်တီးပေးသည်။
ဤသင်ခန်းစာမှ သင် ယူဆောင်သွားသည့် အရာမှာ အတွေးအခေါ် ဖြစ်သည် - သက်ဆိုင်ရာ စမ်းသပ်မှု အချက်အလက်များ၏ စစ်မှန်မှုကို သေချာစေရန် အတည်ပြုစိစစ်ခြင်း တည်ရှိနေပြီး၊ စစ်မှန်မှုဆီသို့ လမ်းကြောင်းသည် အရေးအကြီးဆုံး အရာများပေါ်တွင် အချိုးအစားကျသော၊ ဘေးအန္တရာယ်အခြေပြု အာရုံစိုက်မှုမှတစ်ဆင့် လျှောက်လှမ်းသွားသည်။

---


## အဓိက ဝေါဟာရများ (Key Terms)

**ရည်ရွယ်ချက်နှင့် ကိုက်ညီခြင်း (ကွန်ပျူတာစနစ်များ):** ယေဘုယျ ပုံစံခွက်တစ်ခုထက် ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်းမှတစ်ဆင့် ထူထောင်ထားသော၊ လက်တွေ့ အသုံးပြုမှု အခြေအနေများအောက်တွင် စနစ်တစ်ခုသည် ယင်း၏ ရည်ရွယ်ထားသော လုပ်ငန်းဆောင်တာများကို ယုံကြည်စိတ်ချစွာ ဆောင်ရွက်ရန် တောင်းဆိုသည့် E6(R3) စံနှုန်း။
**ဘေးအန္တရာယ်အခြေပြု အတည်ပြုစိစစ်ခြင်း (Risk-based validation):** အတည်ပြုစိစစ်မှု အားထုတ်မှုသည် စနစ်၏ ကဏ္ဍ၊ ယင်း၏ အချက်အလက်များ၏ အရေးပါမှု၊ ထို့ပြင် ယင်း၏ ပျက်ကွက်မှုဆိုင်ရာ နောက်ဆက်တွဲကျရောက်မှုတို့နှင့်အညီ ချိန်ညှိသွားသည့် ချဉ်းကပ်မှု (အပိုင်း ၄.၃.၄(a))။
**အချက်အလက် အရေးပါမှု (Data criticality):** စနစ်တစ်ခု ကိုင်တွယ်သည့် အချက်အလက်များ၏ အရေးပါမှု — အဓိက အဆုံးသတ်တိုင်းတာချက်နှင့် ဘေးကင်းရေး အချက်အလက်များသည် အရေးကြီးဆုံး ဖြစ်ပြီး၊ အုပ်ချုပ်ရေးဆိုင်ရာ အချက်အလက်များသည် အနည်းဆုံး ဖြစ်သည် — အတည်ပြုစိစစ်မှု အပြင်းအထန် ပမာဏ၏ အဓိက ဆုံးဖြတ်ချက် အချက်။
**အသုံးပြုသူ လိုအပ်ချက်များ (User requirements):** နည်းပညာဆိုင်ရာ သတ်မှတ်ချက်များနှင့် မတူဘဲ စနစ်အား အသုံးပြုမည့်သူများ၏ ရှုထောင့်မှ စနစ်က မည်သည့်အရာ အောင်မြင်အောင် ဆောင်ရွက်ရမည်ဆိုသည့် လုပ်ငန်းဆောင်တာဆိုင်ရာ ဖော်ပြချက်များ။
**လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များ (Functional specifications):** ပြင်ဆင်သတ်မှတ်မှု၊ ချိတ်ဆက်မှု ပြုမူပုံများ၊ အတည်ပြုစိစစ်မှု စည်းမျဉ်းများ၊ အမှား ကိုင်တွယ်မှုနှင့် စစ်ဆေးမှု လမ်းကြောင်း ထုတ်လုပ်ခြင်းတို့ အပါအဝင် စနစ်က ၎င်းတို့ကို မည်သို့ အကောင်အထည်ဖော်မည်ဆိုသည့် ဖော်ပြချက်များအဖြစ်သို့ အသုံးပြုသူ လိုအပ်ချက်များကို ဘာသာပြန်ပေးသည့် မှတ်တမ်းတင်မှု။
**ခြေရာခံနိုင်မှု ဇယား (Traceability matrix):** လိုအပ်ချက် တိုင်းကို ဒီဇိုင်းဆွဲထားကြောင်းနှင့် စိစစ်ထားကြောင်း သေချာစေရေးအတွက် အသုံးပြုသူ လိုအပ်ချက်များကို လုပ်ငန်းဆောင်တာဆိုင်ရာ သတ်မှတ်ချက်များထံ၊ ထိုမှတစ်ဆင့် စမ်းသပ်မှု ဖြစ်စဉ်များထံ ချိတ်ဆက်ပေးသည့် မှတ်တမ်းတင်မှု; နက်ရှိုင်းမှုသည် အရေးပါမှုနှင့် အချိုးအစားကျရမည်။
**အသုံးပြုသူကို အဓိကထားသည့် ဒီဇိုင်း (User-centred design):** ရည်ရွယ်ထားသော အသုံးပြုသူ လူဦးရေအတွက် သင့်လျော်မှု ရှိစေရန် စနစ် ဒီဇိုင်းတွင် ရည်ရွယ်ထားသော ပါဝင်သူ လူဦးရေနှင့် ကျန်းမာရေး ကျွမ်းကျင်သူများ၏ ကိုယ်စားလှယ်များကို ပါဝင်စေရေး အပိုင်း ၄.၃ တွင် အကြံပြုထားသော ကျင့်သုံးမှု။
**ပြောင်းလဲမှု ထိန်းချုပ်မှု (Change control):** အတည်ပြုစိစစ်ထားသော အခြေအနေကို ထိန်းသိမ်းထားရှိလျက်၊ အတည်ပြုစိစစ်ထားသော စနစ်တစ်ခုသို့ ပြုပြင်ပြောင်းလဲမှုများကို အကောင်အထည်မဖော်မီ အကဲဖြတ်ခြင်း၊ အတည်ပြုခြင်း၊ စမ်းသပ်ခြင်းနှင့် မှတ်တမ်းတင်ခြင်းတို့ကို ဆောင်ရွက်သည့် လုပ်ငန်းစဉ်။
**ပြန်လည် စမ်းသပ်ခြင်း (Regression testing):** ပြောင်းလဲမှုတစ်ခုက ၎င်းတို့အား အနှောင့်အယှက် မဖြစ်စေကြောင်း အတည်ပြုရန် ပြောင်းလဲမှုတစ်ခု ပြုလုပ်ပြီးနောက် ယခင် အတည်ပြုစိစစ်ထားသော လုပ်ငန်းဆောင်တာများကို ဘက်စုံကျစွာ ပြန်လည် စမ်းသပ်ခြင်း။
**ပုံမှန် စနစ် သုံးသပ်ခြင်း (Periodic system review):** နည်းပညာနှင့် အခြေအနေများ ပြောင်းလဲတိုးတက်လာသည်နှင့်အမျှ စနစ်တစ်ခုသည် အတည်ပြုစိစစ်ထားသော အခြေအနေတွင် ဆက်လက် ရှိနေကြောင်းနှင့် ယင်း၏ သက်တမ်းတစ်လျှောက် ရည်ရွယ်ချက်နှင့် ဆက်လက် ကိုက်ညီကြောင်း အတည်ပြုသည့် အချိန်ဇယားဆွဲထားသော ပြန်လည် အကဲဖြတ်မှု (အပိုင်း ၄.၃.၄(d) အရ)။
**အပိုင်း ၄.၃.၄ (Section 4.3.4):** ဘေးအန္တရာယ် အကဲဖြတ်မှု မူဘောင် (a)၊ ပုံမှန် သုံးသပ်ခြင်း (d)၊ ထို့ပြင် သီးသန့် ရေးဆွဲထားသော၊ ပြင်ဆင်သတ်မှတ်နိုင်သော၊ နှင့် ပြုပြင်ပြောင်းလဲမှု မရှိသော စနစ်များအတွက် အတည်ပြုစိစစ်မှု အဆင့်များ (e) တို့ အပါအဝင် ကွန်ပျူတာစနစ်များ အတည်ပြုစိစစ်မှု လိုအပ်ချက်များကို အသေးစိတ် ဖော်ပြထားသည့် ICH E6(R3) နောက်ဆက်တွဲ ၁ ၏ အပိုင်း။

---

Source: [https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation](https://www.freegcp.com/learn/ich-e6r3-gcp/reliable-results-roles-and-product-management/fit-for-purpose-systems-and-computerized-systems-validation)
Translated by **Google Gemini (3.5 Flash)**

