## Overview

[SystmOne](https://www.tpp-uk.com/products/systmone) is a primary care clinical information system run by TPP (Leeds), used by roughly one third of GP practices in England, with records for approximately 44% of the English population. Its primary purpose is patient management, though the data may be used for research.

It captures symptoms, test results, diagnoses, prescriptions, onward referrals, demographic and social characteristics, etc. Essentially this is everything about a patient that is electronically recorded or accessed by GPs.

## The OpenSAFELY-TPP database

The SystmOne database contains various tables for events, medications, registrations, and so on, which have been processed, pseudonymised, and made available within the OpenSAFELY-TPP database. Some additional custom tables are also created, for instance to make administrative and geographic grouping information available (like household membership) without disclosing of identifiable patient data (like addresses).

Clinical, referral, and consultation events are coded in SystmOne using an augmented version of CTV3 Read codes. These are available in the OpenSAFELY-TPP database in the `CodedEvent` table. Each row is made up of a patient identifier, an event code, an event date, and an additional interaction identifier linking the event to a specific patient&ndash;service interaction, such as a GP consultation, getting bloods, receiving test results, updating contact details, and so on (perhaps confusingly, this is called the "consultation" identifier). There may also be an additional numeric value stored, for instance if the code relates to a physiological measurement.

Medications are coded using DM+D codes, and are available in the `MedicationIssue` table which is structured similarly to `CodedEvent`.

The `Vaccination` table contains information on administered vaccinations, identified using either the target disease (e.g., influenza), or the vaccine product (e.g., Optaflu). 

Only coded or other structured data can be accessed in OpenSAFELY &mdash; we do not have access to free text data.

### SARS-CoV-2 test results

SARS-CoV-2 test result data is incorporated into SystmOne and uses the following CTV3 codes:

* **Y20d1** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result positive_
* **Y20d2** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result negative_
* **Y23f6** _SARS-CoV-2 (severe acute respiratory syndrome coronavirus 2) RNA (ribonucleic acid) detection result unknown_

These are coded in response to data flowing from Pillar 1 and Pillar 2. (At the time of writing, Dec 2020, Moonshot community tests are also planned to be incorporated).

!!! note "National coronavirus testing data are also available from SGSS"
    We recommend you use linked [SGSS](dataset-sgsscovid.md) data for SARS-CoV-2 test results.

### Dates

All coded events should be accompanied by an event date.
However, invalid or unusual dates are possible and may occur for a number of reasons; for instance, when a GP is coding an important event in the patient's medical history but the exact date is not known.

## Additional derived data

### Geographic and administrative groupings
A patient registers with a practice using their home address.
The postcode from this address is mapped to an Output Area, from which other larger geographic representations such as LSOA, MSOA, CCG, and STP can be derived (see [various](https://geoportal.statistics.gov.uk/search?q=Beginners%20Guide%20to%20UK%20Geographies) [ONS publications](https://www.ons.gov.uk/methodology/geography/ukgeographies) for more detail).

#### MSOA
According to our identifiable data minimisation principles, only representations as large or larger than MSOA are available to be extracted into a study cohort for analysis.
Of ~36 million active patient addresses, less than 55,000 have no MSOA code set. These are a split of no postcode entered, an invalid postcode entered, and no fixed abode.

#### IMD
IMD (the English Index of Multiple Deprivation) is a ranking of LSOAs based on various characteristics of the areas.
The original ranking ranges from 1 to around 33,000 (the number of LSOAs in England),
where 1 is the most deprived area.
However, the original ranking is rounded to the nearest 100 in the OpenSAFELY-TPP database,
so that individual LSOAs cannot be identified.
Consequently, the rounded ranking ranges from 0 to around 33,000,
where 0 is the most deprived 49 areas.

IMD rankings are recalculated every 3 or 4 years.
Consequently, there is no original ranking for some newly built residences.
In these cases, the rounded ranking is -1.

---8<-- 'includes/imd-warning-header.md'

Occasionally a patient has multiple active registrations on a given date.
If so, the postcode is chosen as follows: choose the registration with the latest start date; if this is not unique, then choose the registration with the latest end date; if this is not unique, choose at random.

If a patient's postcode is not recorded, then these geographic variables are not available for analysis.

### Household membership

Content to be written.


## Externally linked data

Patient records from external datasets are imported and matched to the core primary care data as follows:

* Patient records from other external sources are matched to SystmOne records on NHS numbers via a [salted](https://en.wikipedia.org/wiki/Salt_(cryptography)) [hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function):
	* Usually this is done by the data controllers of the external dataset &mdash; that is, hashed NHS numbers for patients in OpenSAFELY are sent to the external data controller, they identify all the matching records in their dataset, and then send only those records back to OpenSAFELY.
	* For some datasets (ICNARC), OpenSAFELY receives the hashed NHS numbers from the external dataset and the matching occurs inside OpenSAFELY. The matched IDs are then sent back and the matched records are returned to OpenSAFELY.
* No other identifiers (names, postcodes, DOBs etc) are used for matching, though this may change in future.
* No patient identifiers are imported from external datasets.
* Only records for patients with matching NHS numbers are imported to OpenSAFELY (i.e., `left_join(SystmOne, External, by='NHSNumber')`).

Matching quality is dependent on the quality of NHS numbers (they're good but not infallible).
Currently there is no direct evaluation of linkage quality because by design (minimisation of the transfer of sensitive data) we don't have access to direct identifiers from external datasets; nor do we know in general if we should be expecting a match or not.

When TPP receive data from external data sources (eg ONS), the tables are completely replaced.

## OpenSAFELY-TPP database builds
The OpenSAFELY-TPP database is typically built once per week.
In essence, this involves refreshing the database records so that the following groups are available for analysis:

1. All patients currently registered[^1] at a TPP practice
2. All patients registered at any time from 2009-01-01 onwards, but having since de-registered
3. All patients registered at any time from 2009-01-01 onwards, but having since died.

These three groups constitute the patient population available for analysis within the OpenSAFELY-TPP database.
Note that any primary care events occurring in de-registered patients after the de-registration date will not be available in the TPP patient record, though any events recorded in external linked datasets (such as hospitals admissions or deaths) will be visible.

Every time the database is re-built there will differences, either due to new registrations or changes to patient records that include/exclude them from the study cohort.
Old database builds cannot be recovered, and due to the differences between successive database builds, old study populations are unlikely to be re-extracted exactly as before.

For those with access to the OpenSAFELY database, the latest database build time is available in the `LatestBuildTime` table, and the history of builds for each dataset is available in the `BuildInfo` table.




## OpenSAFELY-TPP database coverage and metadata

- [Most recent coverage of records in SystmOne and external datasets](https://reports.opensafely.org/reports/opensafely-tpp-database-builds/)
- [Historical coverage of records in SystmOne and external datasets](https://github.com/opensafely/database-notebooks/blob/master/notebooks/database-history.ipynb)
- [OpenSAFELY-TPP database schema](https://reports.opensafely.org/reports/opensafely-tpp-database-schema/)
- [OpenSAFELY-TPP database table examples (based on dummy data)](https://github.com/opensafely/tpp-sql-notebook/blob/master/notebooks/tpp-schema.ipynb)


[^1]:
    "Registered" here means a patient with a full "GMS" (General Medical Services) registration. Patients with temporary registrations are not included.

---8<-- 'includes/glossary.md'
