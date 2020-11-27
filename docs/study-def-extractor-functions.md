This section describes each available function for creating variables within a study definition. 

The [tpp_backend.py](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/tpp_backend.py) python script is where these functions are actually defined &mdash; go there to see the SQL these functions generate for querying the OpenSAFELY backends.

## Primary Care Record

These variables are derived from data held in the patients' primary care records. 
&nbsp;

::: cohortextractor.patients.random_sample
&nbsp;

::: cohortextractor.patients.registered_as_of
&nbsp;

::: cohortextractor.patients.registered_with_one_practice_between
&nbsp;

::: cohortextractor.patients.date_deregistered_from_all_supported_practices
&nbsp;

::: cohortextractor.patients.with_complete_history_between
&nbsp;

::: cohortextractor.patients.with_complete_gp_consultation_history_between
&nbsp;

::: cohortextractor.patients.registered_practice_as_of
&nbsp;

::: cohortextractor.patients.address_as_of
&nbsp;

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

::: cohortextractor.patients.with_these_medications
&nbsp;

::: cohortextractor.patients.with_these_clinical_events
&nbsp;

::: cohortextractor.patients.with_death_recorded_in_primary_care
&nbsp;

### SystmOne only

These variables are only available from primary care data in OpenSAFELY-TPP.
&nbsp;

::: cohortextractor.patients.care_home_status_as_of
&nbsp;

::: cohortextractor.patients.with_tpp_vaccination_record
&nbsp;

::: cohortextractor.patients.household_as_of
&nbsp;
    
## APCS
These variables are derived from Admitted Patient Care Statistics (APCS) data on in-patient hospital admissions across England.
For more information, see the [APCS data section](dataset-apcs).
&nbsp;

::: cohortextractor.patients.admitted_to_hospital
&nbsp;

## ECDS
These variables are derived from Emergency Care Data Set (ECDS) data on emergency department attendances across England.
For more information, see the [ECDS data section](dataset-ecds).
&nbsp;

::: cohortextractor.patients.attended_emergency_care
&nbsp;

## ICNARC-CMP
These variables are derived from the Intensive Care National Audit and Research Centre Case-Mix Programme (ICNARC-CMP), which collects information on ICU admissions across England.
For more information, see the [ICNARC data section](dataset-icnarc).
&nbsp;

::: cohortextractor.patients.admitted_to_icu
&nbsp;

## SGSS
These variables are derived from Second Generation Surveillance System (SGSS) data which captures routine laboratory surveillance data on infectious diseases across England.
For more information, see the [SGSS data section](dataset-sgsscovid).
&nbsp;

::: cohortextractor.patients.with_test_result_in_sgss
&nbsp;


## CPNS

These variables are derived from the COVID-19 Patient Notification System (CPNS), which collects info on all in-hospital covid-related deaths.
For more information, see the [CPNS data section](dataset-cpns).
&nbsp;

::: cohortextractor.patients.with_death_recorded_in_cpns
&nbsp;

## ONS deaths
These variables are derived from the Death Registry data provided by the Office for National Statistics.
For more information, see the [ONS deaths section](dataset-onsdeaths).
&nbsp;

::: cohortextractor.patients.died_from_any_cause
&nbsp;

::: cohortextractor.patients.with_these_codes_on_death_certificate
&nbsp;


## Utility functions

These variables create new variable from existing variables. They do not extract any data directly.
&nbsp;

::: cohortextractor.patients.categorised_as
&nbsp;

::: cohortextractor.patients.satisfying
&nbsp;

::: cohortextractor.patients.date_of
&nbsp;

::: cohortextractor.patients.maximum_of
&nbsp;

::: cohortextractor.patients.maximum_of
&nbsp;


