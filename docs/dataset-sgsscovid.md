_The Second Generation Surveillance System (SGSS) is an application that stores and manages data on laboratory isolates and notifications, and is the preferred method for capturing routine laboratory surveillance data on infectious diseases and antimicrobial resistance from laboratories across England._ 
[PHE Laboratory Reporting Guidelines, page 6](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/739854/PHE_Laboratory_Reporting_Guidelines.pdf#page=6)

SGSS data currently available in OpenSAFELY is for SARS-COV-2 test results from the UK's pillar 1 and pillar 2 tests.
Some SARS-CoV-2 testing info also flows directly into the primary care record from SGSS (see below).

## Metadata

**Data provider** Public Health England

**Participation / Coverage** Unclear, and varies over time

**Provenance** PHE and NHS hospital testing labs

**Update frequency in OpenSAFELY** Approximately monthly

**Delay between event occurring and event appearing in OpenSAFELY** Approximately 1-2 weeks.

**Collected information** Earliest specimen date, lab report date, age, sex, county, test result, source ("pillar 2" or "other")

## Glossary
* **Pillar 1** swab testing in Public Health England (PHE) labs and NHS hospitals for those with a clinical need, and health and care workers
* **Pillar 2** swab testing for the wider population, as set out in government guidance (in practice this is testing conducted by commercial partners)
* **Pillar 3** serology testing to show if people have antibodies from having had COVID-19
* **Pillar 4** serology and swab testing for national surveillance supported by PHE, ONS, Biobank, universities and other partners to learn more about the prevalence and spread of the virus and for other testing research purposes, for example on the accuracy and ease of use of home testing

## Overview
SGSS contains Information on patients receiving a swab test for SARS-CoV-2, from pillar 1 (NHS and PHE labs) and pillar 2 (commercial partners).

It includes "earliest specimen date" (when the sample was taken); "lab report date" (when the result was uploaded to SGSS system); pillar 2 or "other"; result (pos/neg); some demographics.

The are two tables, one for positive tests and one for negative tests.

Multiple tests for the same person are treated as a single 'infection episode', no matter how far apart, and so the system will only return the earliest test (sample date and report date), and all subsequent tests are dropped. 
'Infection episodes' are split by test results, so SGSS will in theory return data for both the earliest positive test, and the earliest negative test. 
However, negative testing data appears to be incomplete. 
Other viruses/organisms may have a finite episode length, so that any tests occurring within say the first 14 days of the first test are dropped, but for coronavirus the episode length is indefinite, though this may change in future.

Negative test data is unreliable &mdash; DO NOT USE

SARS-CoV-2 test result data also available in SystmOne and use the following Read v3 (ctv3) codes:

* **Y20d1** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result positive_
* **Y20d2** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result negative_
* **Y23f6** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result unknown_

These codes can be queried in primary care data separately. 



## More information

[Regarding lab-confirmed cases](https://coronavirus.data.gov.uk/about#total-and-daily-uk-cases)
[National COVID-19 surveillance reports](https://www.gov.uk/government/publications/national-covid-19-surveillance-reports)
[Testing methodology](https://www.gov.uk/government/publications/coronavirus-covid-19-testing-data-methodology/covid-19-testing-data-methodology-note)
[Testing strategy]https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/878121/coronavirus-covid-19-testing-strategy.pdf#page=8)