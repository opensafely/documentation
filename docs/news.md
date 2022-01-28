
This page lists significant improvements to the platform since June 2021, with the most recent at the top. We suggest you check it regularly.

* 2022-01-28: Added ability to query a patient's _place_of_death_ (TPP backend only) [docs](https://docs.opensafely.org/study-def-variables/#cohortextractor.patients.with_these_codes_on_death_certificate), [#728](https://github.com/opensafely-core/cohort-extractor/pull/728)
* 2022-01-27: Extended `mean_recorded_value` to support querying for mean recorded value across a full date range, as well as the most recent day of measurement. [docs](https://docs.opensafely.org/study-def-variables/#cohortextractor.patients.mean_recorded_value).
Added `min_recorded_value` to support querying for minimum recorded value. [docs](https://docs.opensafely.org/study-def-variables/#cohortextractor.patients.min_recorded_value) 
Added `max_recorded_value` to support querying for maximum recorded value. [docs](https://docs.opensafely.org/study-def-variables/#cohortextractor.patients.max_recorded_value) 
[#726](https://github.com/opensafely-core/cohort-extractor/pull/726)
 * 2022-01-24: Added support for querying by first and last day of the NHS financial (recording) year [docs](https://docs.opensafely.org/study-def-dates/), [#723](https://github.com/opensafely-core/cohort-extractor/pull/723)
* 2022-01-18: The OpenSAFELY command-line tool can now start a JupyterLab server. This allows you to easily develop code within the [OpenSAFELY Python environment](opensafely-cli.md#running-jupyterlab).
* 2022-01-14: Added support for [case-control studies](case-control-studies.md)
* 2021-09-06: Show how to extract cohortextractor output in compressed gzip (`csv.gz`) format - recommended to be used in all studies to minimise file storage size. (However, CSVs can still be used where Stata is used for analysis). This is now shown in all parts of documentation with cohortextractor steps e.g. [this page](/actions-cohortextractor/#generate_cohort)
* 2021-07-21: Added [support for users to provide their own dummy data](/study-def-expectations#providing-your-own-dummy-data)
* 2021-07-07: Added [a page](https://docs.opensafely.org/permissions) in the docs explaining (briefly) how permissions work [#303](https://github.com/opensafely/documentation/pull/303)
* 2021-06-11: Add ability to query a patient's _health care worker_ status in vaccination records (TPP backend only) [docs](https://docs.opensafely.org/study-def-variables/#cohortextractor.patients.with_healthcare_worker_flag_on_covid_vaccine_record), [#567](https://github.com/opensafely-core/cohort-extractor/pull/567)

---8<-- 'includes/glossary.md'
