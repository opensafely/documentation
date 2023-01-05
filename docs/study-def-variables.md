This section describes each available function for creating variables within a study definition.

For more information on the datasets contained within the OpenSAFELY database, see the [Data sources section](data-sources/intro.md).

For more information on writing a study definition, go to the [study definition section](study-def.md).


## Primary Care Record

These variables are derived from data held in the patients' primary care records.
&nbsp;

::: cohortextractor.patients.registered_as_of
&nbsp;

::: cohortextractor.patients.registered_with_one_practice_between
&nbsp;

::: cohortextractor.patients.date_deregistered_from_all_supported_practices
&nbsp;

::: cohortextractor.patients.with_complete_gp_consultation_history_between
&nbsp;

::: cohortextractor.patients.registered_practice_as_of
&nbsp;

::: cohortextractor.patients.address_as_of
&nbsp;

---8<-- 'includes/imd-warning-header.md'

::: cohortextractor.patients.with_gp_consultations
&nbsp;

::: cohortextractor.patients.sex
&nbsp;

::: cohortextractor.patients.age_as_of
&nbsp;

::: cohortextractor.patients.date_of_birth
&nbsp;

::: cohortextractor.patients.most_recent_bmi
&nbsp;

::: cohortextractor.patients.mean_recorded_value
&nbsp;

::: cohortextractor.patients.min_recorded_value
&nbsp;

::: cohortextractor.patients.max_recorded_value
&nbsp;

::: cohortextractor.patients.with_these_medications
&nbsp;

::: cohortextractor.patients.with_these_clinical_events
&nbsp;

::: cohortextractor.patients.comparator_from
&nbsp;

::: cohortextractor.patients.reference_range_lower_bound_from
&nbsp;

::: cohortextractor.patients.reference_range_upper_bound_from
&nbsp;

::: cohortextractor.patients.with_death_recorded_in_primary_care
&nbsp;

::: cohortextractor.patients.care_home_status_as_of
&nbsp;

::: cohortextractor.patients.with_tpp_vaccination_record
&nbsp;

::: cohortextractor.patients.household_as_of
&nbsp;

::: cohortextractor.patients.with_these_decision_support_values
&nbsp;

## ICNARC
!!! warning
    ICNARC data can only be used in collaboration with ICNARC researchers who must be involved in working on the study and writing it up.
    Please contact your co-pilot, or <team@opensafely.org> if you have any questions.

!!! warning
    Data from ICNARC were last imported on 21-Jan-2021, with no further imports currently planned. Alternative data on ICU admission can be gleaned from SUS (i.e. returning=days_in_critical_care).

These variables are derived from the Intensive Care National Audit and Research Centre Case-Mix Programme (ICNARC-CMP), which collects information on ICU admissions across England.
For more information, see the [ICNARC data section](data-sources/icnarc.md).
&nbsp;

::: cohortextractor.patients.admitted_to_icu
&nbsp;

## SGSS
These variables are derived from Second Generation Surveillance System (SGSS) data which captures routine laboratory surveillance data on infectious diseases across England.
For more information, see the [SGSS data section](data-sources/sgsscovid.md).
&nbsp;

::: cohortextractor.patients.with_test_result_in_sgss
&nbsp;


## CPNS

These variables are derived from the COVID-19 Patient Notification System (CPNS), which collects info on all in-hospital covid-related deaths.
For more information, see the [CPNS data section](data-sources/cpns.md). 

!!! note
    CPNS is restricted to in-hospital covid-related deaths only. For covid-related deaths in any setting, ONS-registered deaths where cause of death matches [COVID-19 coding in ICD-10](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) is generally more useful.
&nbsp;

::: cohortextractor.patients.with_death_recorded_in_cpns
&nbsp;


## ONS deaths
These variables are derived from the Death Registry data provided by the Office for National Statistics.
For more information, see the [ONS deaths section](data-sources/onsdeaths.md).
&nbsp;

::: cohortextractor.patients.died_from_any_cause
&nbsp;

::: cohortextractor.patients.with_these_codes_on_death_certificate
&nbsp;


## ISARIC
---8<-- 'includes/isaric-warning-header.md'

These variables are derived from data provided by the International Severe Acute Respiratory and Emerging Infection Consortium.

For more information, see the [ISARIC section](data-sources/isaric.md).
&nbsp;

::: cohortextractor.patients.with_an_isaric_record
&nbsp;


## ONS CIS
---8<-- 'includes/onscis-warning-header.md'

These variables are derived from the COVID-19 Infection Survey data provided by the Office for National Statistics.
For more information, see the [ONS CIS section](data-sources/onscis.md).
&nbsp;

::: cohortextractor.patients.with_an_ons_cis_record
&nbsp;


## High Cost Drugs
(Documentation on the source of this data will be forthcoming later.)

::: cohortextractor.patients.with_high_cost_drugs
&nbsp;


## SUS
These variables are derived from the Secondary Uses Services (SUS) data, and their underlying datasets:

* [APCS](data-sources/apc.md)
* [ECDS](data-sources/ecds.md)
* OPA

::: cohortextractor.patients.admitted_to_hospital
&nbsp;

::: cohortextractor.patients.attended_emergency_care
&nbsp;

::: cohortextractor.patients.with_ethnicity_from_sus
&nbsp;

::: cohortextractor.patients.outpatient_appointment_date
&nbsp;


## UK Renal Registry
Data on patients under secondary renal care (advanced chronic kidney disease stages 4 and 5, dialysis, and kidney transplantation) are held at the UK Renal Registry (UKRR).

::: cohortextractor.patients.with_record_in_ukrr
&nbsp;

## NHS England COVID-19 data store
(Documentation on the source of this data will be forthcoming later.)

:::cohortextractor.patients.with_healthcare_worker_flag_on_covid_vaccine_record



## Therapeutics

These variables are derived from forms submitted by clinicians to NHS England for 
patients assessed and approved to receive antivirals/nMABs for COVID-19 in inpatient or outpatient
settings.

For more information, see the [Therapeutics data section](data-sources/therapeutics.md).
&nbsp;

::: cohortextractor.patients.with_covid_therapeutics
&nbsp;


## Utility functions

These variables create new variable from existing variables. They do not extract any data directly.
&nbsp;

::: cohortextractor.patients.random_sample
&nbsp;

::: cohortextractor.patients.categorised_as
&nbsp;

::: cohortextractor.patients.satisfying
&nbsp;

::: cohortextractor.patients.date_of
&nbsp;

::: cohortextractor.patients.minimum_of
&nbsp;

::: cohortextractor.patients.maximum_of
&nbsp;

::: cohortextractor.patients.with_value_from_file
&nbsp;

::: cohortextractor.patients.which_exist_in_file
&nbsp;


---8<-- 'includes/glossary.md'
