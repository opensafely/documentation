## Overview

[SystmOne](https://www.tpp-uk.com/products/systmone) is a Primary Care clinical information system run by The Phoenix Partnership, used by roughly one third of GP practices in England, with records for approximately 44% of the English population. Its primary purpose is patient management, though the data may be used for research.

It captures symptoms, test results, diagnoses, prescriptions, onward referrals, demographic and social characteristics, etc. Essentially everything about a patient that is electronically recorded or accessed by GPs.

The SystmOne database contains various tables for events, medications, registrations, and so on, and some additional custom tables have been created specifically for OpenSAFELY. This is typically to make administrative and geographic grouping information available (like household membership) without disclosing of identifiable patient data (like addresses).

### Event coding

SystmOne uses an augmented version of CTV3 Read Codes to classify clinical events, and only data that is associated with a Read Code can be accessed in OpenSAFELY &mdash; we do not have access to free text data.

#### SARS-CoV-2 test results

SARS-CoV-2 test result data is incorporated into SystmOne and uses the following CTV3 codes:

* **Y20d1** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result positive_
* **Y20d2** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result negative_
* **Y23f6** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result unknown_

These are coded in response to data flowing from Pillar 1 and Pillar 2. (At the time of writing, Dec 2020, Moonshot community tests are also planned to be incorporated)

### Dates

All coded events should be accompanied by an event date.
However, invalid or highly unusual dates are possible and may occur for a number of reasons; for instance, when a GP is coding an important event in the patient's medical history but the exact date is not known.

## Additional derived data

### Geographic and administrative groupings
A patient registers with a practice using their home address.
The postcode from this address is mapped to an Output Area, from which other larger geographic representations such as LSOA, MSOA, CCG, and STP can be derived (see [various](https://geoportal.statistics.gov.uk/search?q=Beginners%20Guide%20to%20UK%20Geographies) [ONS publications](https://www.ons.gov.uk/methodology/geography/ukgeographies) for more detail).

#### MSOA
According to our identifiable data minimimisation principles, only representations as large or larger than MSOA are available to be extracted into a study cohort for analysis.
Of ~36 million active patient addresses, less than 55,000 have no MSOA code set. These are a split of no postcode entered, an invalid postcode entered, and no fixed abode.

#### IMD
IMD (the English Index of Multiple Deprivation) is a ranking of LSOAs based on various characteristics of the region.
The ranking ranges from 1 to around 33000 (the number of LSOAs in England), but is rounded to the nearest 100 so that the exact LSOA cannot be derived.
IMD rankings are redone every 3 or 4 years. For some newly built residences, there is no associated IMD rank, and so IMD is not defined in that case.

Occasionally a patient has multiple active registrations on a given date.
The chosen postcode is chosen as follows: choose the registration with the latest start date; if this is not unique, then choose the registration with the latest end date; if this is not unique, choose at random.

If a patient's postcode is not recorded, then these geographic variables are not available for analysis.

### Household membership

Content to be written


---8<-- 'includes/glossary.md'
