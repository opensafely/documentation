Admitted Patient Care (APC) is the national data set for hospital admissions.
Admitted Patient Care Spells (APCS) is part of Hospital Episode Statistics (HES) and is provided to OpenSAFELY via NHS Digital's Secondary Use Service (SUS).

## Metadata

* **Data provider** NHS England.
* **Participation / Coverage** In-hospital patient admissions in NHS Trusts in England.
* **Available from** Data are available from early 2016.
* **Update frequency in OpenSAFELY** Approximately monthly.
* **Delay between event occurring and event appearing in OpenSAFELY** Approximately 1-2 months.
* **Collected information** Admission and discharge dates; routes of admission; reason for admission; diagnoses; treatments; discharge destination.


## Basic Background

Each row is a in-hospital spell. In-hospital episodes cannot be queried.

* An **episode** is a period of continuous care under a single responsible consultant.
* A **spell** is a period of continuous care within a single trust.

Essentially, a spell is a collection of episodes (often just one episode) denoting the entirety of a patient's stay in hospital from admission to discharge or death. An episode denotes time within a spell spent under the responsibility of a single consultant. So for example if within your hospital stay you are transferred from a medical to surgical ward, or transferred to another site (within the same trust), there will be at least two episodes within your spell.

The dataset does not include any patients who have not been discharged (i.e., patients who have an incomplete spell) at the data extraction date. In other words, the data will be missing admissions of the patients with the longest stay for the most recent admissions.

### \* Notes on transfers:
- Sometimes it is desirable to exclude patients admitted via transfer from another provider, e.g. if we are looking for readmissions we probably want to exclude them because it was not the original admission date of the readmission.
- The post-transfer spell may have additional diagnoses or procedures of interest so it is often useful to include them.
- Transfers may occasionally come from private hospitals where a patient's condition worsened to require e.g. intensive care; if the initial spell was not NHS funded we would probably not have the original spell in our data.

## Reference tables

### Admission method reference table
Codes | Admission method
-- | --
11, 12, 13 | Elective (planned/booked/waiting list)
21 | Emergency Admission: from A&E | usually include
2A | Emergency Admission: from A&E of another provider
22, 23, 24, 25, 2D | Emergency Admission: other sources (e.g. GP, MH crisis team)
28 | Emergency Admission: Other - NB can include transfers and births
2B | Transfer (emergency)
81 | Transfer (non-emergency)
2C, 82, 83 | Birth of baby (in hospital or e.g. at home)
31, 32 | Maternity Admission: Mother admitted ante or post partum

### Source of admission reference table
code | Source of admission
-- | --
19 | Usual place of residence or no fixed abode (but should exclude care homes)
29 | Temporary place of residence (e.g. hotel, school)
54, 65, 85, 88 | Care Home / hospice
51 | NHS other Hospital Provider - ordinary (physical care) ward or A&E
49, 52, 53 | NHS other Hospital Provider - psychiatric accommodation, maternity ward/neonates or MH/LD ward
39, 40, 41, 42, 66 | Other (Penal establishment, Court, or Police Station / Police Custody Suite,  foster care)
79 | Babies born in or on the way to hospital
87 | Non NHS run hospital
98, 99 | Default/unknown

### Patient classification reference table
code | patient classification
-- | --
1 | Ordinary admission (all emergency admissions and elective admissions expected to last at least one night)
2 | Day case admission (patient admitted electively, not expected to stay overnight and who returns home on the same day as scheduled. If discharge does not occur same day as planned, this should be counted as an ordinary admission)
3, 4 | Regular day or night admission (part of a planned series of regular admissions for an on-going regime of broadly similar treatment. If the admission lasts 24 hours or more, such an admission should be classified as an ordinary admission)
5 | Mother and baby using delivery facilities only


### Discharge destination reference table

Code | Description
-- | --
19 | Usual place of residence unless listed below. It includes 'no fixed abode' but excludes care homes.
29 | Temporary place of residence (includes hotel, residential Educational Establishment)
51, 52 | Transfer: NHS other Hospital Provider - general ward or  maternity/ neonates
30, 49, 50, 53 | Transfer (other NHS):, mentally ill / Learning Disabilities, psychiatric units
48, 84, 87 | Transfer: Non-NHS run hospital or medium secure unit, Scotland high-secure unit
37, 38, 66 | Other: Court, Penal establishment, police station, foster care
54, 65, 85, 88 | Hospice / Care Home
79 | Not applicable - PATIENT died or stillbirth

#### Reference
[Link to lookup table](https://datadictionary.nhs.uk/attributes/discharge_destination.html?hl=discharge%2Cdestination)


## More information

* [Notebook showing breakdown of ethnicity codes](https://github.com/opensafely/rapid-reports/blob/master/notebooks/ethnicity-codes.ipynb) - (private, pending review & publication)
* [NHS Digital SUS site](https://digital.nhs.uk/services/secondary-uses-service-sus/secondary-uses-services-sus-guidance)
* [NHS Digital HES site](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics)
* [Hospital APC Activity reports](https://digital.nhs.uk/data-and-information/publications/statistical/hospital-admitted-patient-care-activity)
* [NHS Digital APC data dictionary](https://datadictionary.nhs.uk/data_sets/cds_v6-2/cds_v6-2_type_130_-_admitted_patient_care_-_finished_general_episode_cds.html)
* [Data resource profile: Hospital Episode Statistics Admitted Patient Care (HES APC)](https://doi.org/10.1093/ije/dyx015)
* [CLOSER Understanding Hospital Episode Statistics](https://www.closer.ac.uk/wp-content/uploads/CLOSER-resource-understanding-hospital-episode-statistics-2018.pdf)
