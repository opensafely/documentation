Admitted Patient Care (APC) is the national data set for hospital admissions.
Admitted Patient Care Spells (APCS) is part of Hospital Episode Statistics (HES) and is provided to OpenSAFELY via NHS Digital's Secondary Use Service (SUS).

## Metadata

* **Data provider** NHS England.
* **Participation / Coverage** In-hospital patient admissions in NHS Trusts in England.
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

## Available filters and `returning` fields

- [Admission date](#admission_date)
- [Number of matches in period (number of spells)](#number_of_matches_in_period)
- [Discharge date](#discharge_date)
- [Diagnoses (primary or any)](#with_these_diagnoses-with_these_primary_diagnoses-primary_diagnosis)
- [Procedures](#with_these_procedures)
- [Admission method (planned vs emergency admissions / transfers)](#admission_method)
- [Source of admission](#source_of_admission)
- [Patient classification (ordinary/daycase/regular/maternity)](#patient_classification)
- [Discharge destination](#discharge_destination)
- [Administrative category (NHS vs private patients)](#administrative_category)
- [Admission TFC (specialty)](#admission_treatment_function_code)
- [Days in Critical Care](#days_in_critical_care)
- [Duration of elective wait (days)](#duration_of_elective_wait)


### `admission_date` 

#### Filtering
- Use `on_or_before` and/or `on_or_after`, or `between`.
- Optionally specify `find_first_match_in_period` (or last match). NB any ties (multiple same day admissions) are resolved using `APCS_Ident` which does not predictably give the earliest or latest admission on a given day. 
#### Returning
`returning="admission_date"`

### `number_of_matches_in_period`
#### Filtering
- Not currently available
#### Returning
- `returning="number_of_matches_in_period"`

### `discharge_date`
#### Filtering
- Not currently available
#### Returning
- `returning="discharge_date"`
#### Caution
- discharge date is present for patients who were transferred, or died, at the end of their spell
- patients who are still in hospital are not included in the dataset so this field is always complete but long-stay patients may be missing.

### `with_these_diagnoses` / `with_these_primary_diagnoses`/ `primary_diagnosis`
- Coding system: ICD-10.
#### Filtering 
- Filter using `with_these_diagnoses` / `with_these_primary_diagnoses`
#### Returning
- `returning="primary_diagnosis"`
#### Caution
- Primary diagnosis is not necessarily the primary reason for admission, and could represent an escalation/complication of initial reason for admission.

### `with_these_procedures`
Coding system: OPCS-4.
#### Filtering 
- Filter using `with_these_proecedures` 
#### Returning
- Not currently available

### `admission_method`
#### Filtering 
- Filter using `with_admission_method=` (supply either an individual code or a list)
#### Returning
- `returning="admission_method"`
#### Most useful for:
- identifying planned vs emergency admissions
- identifying/excluding transfers* (`'28', '2B', '81'`)
- excluding birth and maternity spells (`'2C', '82', '83', '31', '32'`)

#### Examples
```
# all normal admissions and transfers, excluding births and maternity admissions
with_admission_method = ['11', '12', '13', '21', '2A', '22', '23', '24', '25', '2D', '28', '2B', '81'] 
```
```
# all normal admissions excluding transfers, births and maternity admissions
with_admission_method = ['11', '12', '13', '21', '2A', '22', '23', '24', '25', '2D'] 
```

#### Brief Reference table
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


### `source_of_admission`
#### Filtering 
- Filter using `with_source_of_admission=` (supply either an individual code or a list)
#### Returning
- `returning="source_of_admission"`
#### Most useful for:
  - identifying patients admitted from care homes (`'54', '65', '85', '88'`)
  - excluding birth spells (`'79'`)
  - identifying transfers* - but this cannot distinguish transfers from wards vs patients arriving from the A&E dept of another provider (e.g. an MIU or smaller hospital which doesn't have a suitable ward) so `admission_method` is better for this purpose. 

#### Example
```
with_source_of_admission = ['19','29','54', '65', '85', '88', '39', '40', '41', '42', '66', '49', '52', '53', '87', '98', '99']
# all admissions except births (includes unknowns (98, 99))
```

#### Brief Reference table
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


### `patient_classification`

#### Most useful for:
- excluding regular admissions (i.e. where patient is admitted e.g. every week for chemotherapy or dialysis) 
- excluding mother and baby admissions (where using delivery facilities only)
- distinguishing elective day case admissions from ordinary admissions (day case admissions are for planned procedures not requiring overnight stays)

An potential advantage of this field is that it reflects what actually happened during the spell rather than what was planned. If a patient's treatment was not limited to the planned course, e.g. patient was expected to have their routine chemotherapy but illness arose which required further treatment and an overnight stay, this would be coded as `1` (ordinary admission) rather than as `3` (regular admission). 

#### Brief Reference table
code | patient classification
-- | --
1 | Ordinary admission (all emergency admissions and elective admissions expected to last at least one night)
2 | Day case admission (patient admitted electively, not expected to stay overnight and who returns home on the same day as scheduled. If discharge does not occur same day as planned, this should be counted as an ordinary admission)
3, 4 | Regular day or night admission (part of a planned series of regular admissions for an on-going regime of broadly similar treatment. If the admission lasts 24 hours or more, such an admission should be classified as an ordinary admission)
5 | Mother and baby using delivery facilities only


### `discharge_destination` 

#### Most useful for:
- Identifying/excluding patients who **died** at the end of their spell
- Identifying/excluding patients who **were transferred** at the end of their spell
- Identifying patients who were discharged to a care home (whether or not they were previously resident in one)

#### Example:
```
with_discharge_destination = ['19', '29', '51', '52', '30', '49', '50', '53', '48', '84', '87', '37', '38', '66', '54', '65', '85', '88', '98','99']
# everyone discharged alive or transferred to another provider (includes those with an unkown destination '98','99')
```
```
with_discharge_destination = ['19', '29', '30', '49', '50', '53', '48', '84', '87', '37', '38', '66', '54', '65', '85', '88']
# everyone discharged to the community, alive (excludes those with in unknown desination '98','99')
# excludes people transferred to other NHS providers of physical health care (51, 52)
# but includes patients transferred to psychiatric / secure units and non-NHS hospitals, because
# these post-transfer spells are most likely not present in SUS and any subsequent exacerbation 
# of physical symptoms would result in a new spell in SUS. 
```

Note - include `'79'` for patients who died (or were stillborn)
Include `98` and `99` for unknowns. There will also be some `null` values.  


#### Brief Reference table

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


### `administrative_category`
#### Most useful for:
- Identifying/excluding patients who were not undergoing NHS treatment
  
  
### `admission_treatment_function_code`
#### Most useful for:
- Identifying which specialty patients were admitted under (use with caution)


### `days_in_critical_care`
#### Most useful for:
- Enumerating how many days were spent in critical care

#### Caution
- Definition of critical care may vary between trusts
- This is counted in number of days (or part-days) not the number of nights as per normal "length of stay" calculations. E.g. a patient who was admitted on day 1 and discharged on day 2 and spent at least part of both days in critical care will have cc_days=2 but LOS=1. 


### `duration_of_elective_wait`
#### Most useful for:
- assessing how long patient was waiting for elective treatment (use with caution)

## More information

* [Notebook showing breakdown of ethnicity codes](https://github.com/opensafely/rapid-reports/blob/master/notebooks/ethnicity-codes.ipynb) - (private, pending review & publication)
* [NHS Digital SUS site](https://digital.nhs.uk/services/secondary-uses-service-sus/secondary-uses-services-sus-guidance)
* [NHS Digital HES site](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics)
* [Hospital APC Activity reports](https://digital.nhs.uk/data-and-information/publications/statistical/hospital-admitted-patient-care-activity)
* [NHS Digital APC data dictionary](https://datadictionary.nhs.uk/data_sets/cds_v6-2/cds_v6-2_type_130_-_admitted_patient_care_-_finished_general_episode_cds.html)
* [Data resource profile: Hospital Episode Statistics Admitted Patient Care (HES APC)](https://doi.org/10.1093/ije/dyx015)
* [CLOSER Understanding Hospital Episode Statistics](https://www.closer.ac.uk/wp-content/uploads/CLOSER-resource-Understanding-HES.pdf)


---8<-- 'includes/glossary.md'
