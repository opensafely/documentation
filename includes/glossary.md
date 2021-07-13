*[Pillar 1]: swab testing in Public Health England (PHE) labs and NHS hospitals for those with a clinical need, and health and care workers
*[Pillar 2]: swab testing for the wider population, as set out in government guidance (in practice this is testing conducted by commercial partners)
*[Pillar 3]: serology testing to show if people have antibodies from having had COVID-19
*[Pillar 4]: serology and swab testing for national surveillance supported by PHE, ONS, Biobank, universities and other partners to learn more about the prevalence and spread of the virus and for other testing research purposes, for example on the accuracy and ease of use of home testing
*[study definition]: specifies the patients you want to include in your study and defines the variables that describe them. Study definitions are written in a Python script using a human-readable API.
*[cohort extractor]: a program that uses the study definition to create a dataset for analysis
*[codelist]: a collection of clinical codes that define a particular condition, event or diagnosis.
*[project pipeline]: defines how different scripts within the project’s analytic code should be run: in what order, with which versions of which software, etc; defined in a file named `project.yaml`
*[job runner]: runs the actions defined in the project pipeline using real data, in a secure environment
*[job server]: a website where you can request runs of all or some of your project pipeline outputs
*[PHE]: Public Health England
*[EHR]: Electronic Health Record
*[SGSS]: Second Generation Surveillance System: an application that stores and manages data on laboratory isolates and notifications. PHE's preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England
*[HES]: Hospital Episode Statistics - a database containing details of all admissions, A&E attendances and outpatient appointments at NHS hospitals in England - like SUS but more often used outside of NHS setting such as in research
*[SUS]: Secondary Uses Service - NHS hospital activity data pseudonymised and used for purposes other than direct care, such as analytics and service planning
*[ECDS]: Emergency Care Data Set - the national data set for urgent and emergency care
*[SNOMED-CT]: SNOMED Clinical Terms, a structured clinical vocabulary for use in an electronic health record, the current standard for coding in the NHS and many jurisdictions globally
*[SNOMED]: SNOMED Clinical Terms, a structured clinical vocabulary for use in an electronic health record, the current standard for coding in the NHS and many jurisdictions globally
*[CTV3]: Clinical Terms Version 3; a version of clinical coding that supercedes Read v2, used natively in TPP SystmOne
*[APC]: Admitted Patient Care is the national data set for hospital admissions. It is part of HES
*[ICD-10]: the 10th revision of the International Statistical Classification of Diseases and Related Health Problems (ICD), a medical classification list by the World Health Organization (WHO)
*[OPCS-4]: OPCS Classification of Interventions and Procedures version 4: coding system used in NHS hospitals, covering operations, procedures and interventions performed during in-patient stays, day case surgery and some out-patient treatments
*[ICNARC]: Intensive Care National Audit and Research Centre
*[ICNARC-CMP]: data on covid-related intensive care admissions in England
*[CPNS]: Covid-19 Patient Notification System - the route by which NHS England are informed of COVID-19-positive, deaths in hospital
*[ONS]: Office for National Statistics - the UK's largest independent producer of official statistics and the recognised national statistical institute of the UK
*[Level 3]: intermediate data, required for running a study, which may contain identifiable information, and which should never be considered for publication; usually a CSV produced from a study definition. Most OpenSAFELY users will not have (or need) permission to see this data directly
*[Level 4]: tables, figures, and other structured files produced as a result of the analysis of Level 3 data, for example summary statistics and statistical models. OpenSAFELY users with the appropriate permission can view this data, and publish it to the internet if they consider it safe to do so
*[TPP]: The company behind the SystmOne EHR
*[APCS]: Admitted Patient Care Statistics - the national data set for in-patient hospital admissions across England.
*[OPA]: Outpatient Attendances is the national data set for hospital outpatient appointments. It is part of HES
*[EMIS]: EMIS Health, formerly known as Egton Medical Information Systems
*[CLI]: Command-line interface, a text interface used by some computer software that is usually run via a "terminal" or "command-line shell".
*[2FA]: Two-factor authentication, a means of verifying a user is authorised to access a service by checking for something that only the user should know (e.g. a password) and something the user should have (e.g. an authenticator application installed on the user's phone).
