For more information on all supported variable extractor functions, see the [patients.py](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/patients.py) script for skeleton documentation, and see [tpp_backend.py](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/tpp_backend.py) for how the SQL created by these functions for querying the OpenSAFELY database.

This section will updated soon.

## Missing data

If a query returns no matching record for a patient &mdash; for example if there are no blood pressure values recorded in a given period, or if there is no death date because the patient hasn't died, or if there is no household size available &mdash; then a default value will be returned. 
For strings and dates, the default value is the empty string `""`. 
For booleans, integers, or floats, the default value is `0`. 
There is no universal `null` value outputted to `input.csv` because these may be handled inconsistently across different programs.