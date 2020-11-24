## Overview

[SystmOne](https://www.tpp-uk.com/products/systmone) is the primary care clinical information system run by The Phoenix Partnership, used by roughly one third of GP practices in England, with records for approximately 44% of the English population. It's primary purpose is patient management, though the data may be used for research. 
It captures symptoms, test results, diagnoses, prescriptions, onward referrals, demographic and social characteristics, etc. Essentially everything about a patient that is electronically recorded or accessed by GPs.
SystmOne uses an augmented version of CTV3 Read Codes and only data that is associated with a Read Code can be accessed in OpenSAFELY &mdash; we do not have access to free text data. 

The SystmOne database contains various tables for events, medications, registrations, and so on, and some additional custom tables have been created specifically for OpenSAFELY.

## Events and event dates

<!--
The main event data is in the `CodedEvent` dataset, which is formatted as follows:

| Patient ID | Consultation ID | Event code (CTV3) | Value | Event Date | 
| --- | --- | --- | --- | --- |
| 1 | 123 | Xa1kG | 0.0 | 2019-04-24 10:50:00 |
| 1 | 456 | Xa1kG | 0.0 | 2019-04-26 15:20:00 |
| 2 | 789 | G.... | 0.0 | 2004-02-04 08:14:46 |
| 2 | 246 | Ub0Qd | -1.0 | 2010-08-25 14:07:07 |
| 2 | 369 | Y2619 | 0.0 | 2011-07-12 09:18:35 |

* **Patient ID** is the unique identifier for each patient.
* **Consultations ID** is the unique identifier for the coded event. "Consultations" has a different meaning to GP consultations in the usual sense of an actual consultation with a healthcare professional. Rather here it is an abstract concept for any interaction with GP practice, e.g., getting a blood test, receiving test results, updating contact details.
* **Event code** is a TPP-augmented CTV3 code.
* **Value** is the value associated with the recorded event, where relevant. For instance, a blood pressure reading.
* **Event date** is the date associated with the recorded event.
-->

All coded events should be accompanied by an event date. However, unknown dates are possible and may occur for a number of reasons. For instance, when a GP is coding an important event in the patient's medical history but the exact date is not known. 

## Geographic and administrative regions
A patient registers with a practice using their home address.
The postcode from this address is mapped to an Output Area, from which other larger geographic representations such as LSOA, MSOA, CCG, and STP can be derived (see https://geoportal.statistics.gov.uk/search?q=Beginners%20Guide%20to%20UK%20Geographies and https://www.ons.gov.uk/methodology/geography/ukgeographies for more detail). 

Only representations as large or larger than MSOA can be extracted into a study cohort for analysis.

IMD (the English Index of Multiple Deprivation) is a ranking of LSOAs based on various characteristics of the region. 
The ranking ranges from 1 to around 33000 (the number of LSOAs in England), but is rounded to the nearest 100 so that the exact LSOA cannot be derived. 
IMD rankings are redone every 3 or 4 years. For some newly built residences, there is no associated IMD rank, and so IMD is not defined in that case.

Occasionally a patient has multiple active registrations on a given date. 
The chosen postcode is chosen as follows: choose the registration with the latest start date; if this is not unique, then choose the registration with the latest end date; if this is not unique, choose at random. 

If a patient's postcode is not recorded, then these geographic variables are not available for analysis.

