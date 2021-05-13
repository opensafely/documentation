Admitted Patient Care (APC) is the national data set for hospital admissions.
APCS is part of Hospital Episode Statistics (HES) and is provided to OpenSAFELY via NHS Digital's Secondary Use Service (SUS).

## Metadata

* **Data provider** NHS England.
* **Participation / Coverage** In-hospital patient admissions in NHS Trusts in England.
* **Update frequency in OpenSAFELY** Approximately monthly.
* **Delay between event occurring and event appearing in OpenSAFELY** Approximately 1-2 months.
* **Collected information** Admission and discharge dates; admission and discharge locations; reason for admission; diagnoses; treatments; discharge destination.

Diagnoses are coded using ICD-10. Procedures are coded in OPCS-4.

Each row is a in-hospital spell. In-hospital episodes cannot be queried.

* An **episode** is a period of continuous care under a single responsible consultant.
* A **spell** is a period of continuous care within a single trust.

Essentially, a spell is a collection of episodes (often just one episode) denoting the entirety of a patient's stay in hospital from admission to discharge or death. An episode denotes time within a spell spent under the responsibility of a single consultant. So for example if within your hospital stay you are transferred from a medical to surgical ward, or transferred to another site (within the same trust), there will be at least two episodes within your spell.

The dataset does not include any patients who have not been discharged (i.e., patients who have an incomplete spell) at the data extraction date. In other words, the data will be missing admissions of the patients with the longest stay for the most recent admissions.

## More information

* [Notebook showing breakdown of ethnicity codes](https://github.com/opensafely/rapid-reports/blob/master/notebooks/ethnicity-codes.ipynb) - (private, pending review & publication)
* [NHS Digital SUS site](https://digital.nhs.uk/services/secondary-uses-service-sus/secondary-uses-services-sus-guidance)
* [NHS Digital HES site](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics)
* [Hospital APC Activity reports](https://digital.nhs.uk/data-and-information/publications/statistical/hospital-admitted-patient-care-activity)
* [NHS Digital APC data dictionary](https://datadictionary.nhs.uk/data_sets/cds_v6-2/cds_v6-2_type_130_-_admitted_patient_care_-_finished_general_episode_cds.html)
* [Data resource profile: Hospital Episode Statistics Admitted Patient Care (HES APC)](https://doi.org/10.1093/ije/dyx015)
* [CLOSER Understanding Hospital Episode Statistics](https://www.closer.ac.uk/wp-content/uploads/CLOSER-resource-Understanding-HES.pdf)


---8<-- 'includes/glossary.md'
