Because OpenSAFELY doesn't allow direct access to individual patient records, researchers must use *dummy data* for developing their analytic code on their own computer.

OpenSAFELY requires you to define *expectations* in your study definition: these describe the properties of each variable, and are used to generate random data that match the expectations.

## Defining `return_expectations`

Every variable in a study definition must have a `return_expectations` argument defined (with the exception of the `population` variable).
This defines the general shape or distribution of the variables in the dummy data used for developing the code.  It is currently relatively unsophisticated; each variable is generated independently of all others. This is sufficient for testing that it is possible to run your study from start to finish in most cases, but sometimes not. You can find (and contribute to!) discussions on improving the dummy data framework [here](https://github.com/opensafely/cohort-extractor/issues/221)

### Specifying default distributions

All variables use a default defined at the top of the study definition, with the `default_expectations` argument, as follows:

```py
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations = {
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
		"incidence": 0.5
    },
    ...

```

In this case, we are saying that:

* Events dates are expected to be distributed between 1900 and today, with exponentially-increasing frequenc, with events occurring for 50% of patients.
* Values for binary variables are expected to be positive 50% of the time.
* Values for categorical variables are expected to be present (i.e., non-missing) 50% of the time.
* Values for numeric variables are expected to be present (i.e., non-missing) 50% of the time.

### Specifying variable-specific distributions
If the defaults need to be overridden, then use the `return_expectations` argument within the variable extractor function, for example as follows:

```py
    copd = patients.with_these_clinical_events(
		copd_codes,
		returning = "binary_flag",
		find_first_match_in_period = True,
		between = [index_date, "today"],
		return_expectations = {"incidence": 0.2},
    ),
```
This overrides the 50% default incidence for the binary variable `copd` to be 20% instead.


### All options
The following options are currently available for dummy data:

**integers**

* `{"int" : {"distribution": "normal", "mean": 25, "stddev": 5}, "incidence" : 0.5}`
* `{"int" : {"distribution": "population_ages"}, "incidence" : 1}`

**numeric**

* `{"float" : {"distribution": "normal", "mean": 25, "stddev": 5}, "incidence" : 0.75}`

**binary**

* `{"incidence": 0.33}`

**categorical**

* `{"category": {"ratios": {"cat1": 0.1, "cat2": 0.2, "cat3": 0.7}}, "incidence" : 1}`

**date**

*	`{"date": {"earliest": "1900-01-01", "latest": "today"}, "rate" : "exponential_increase"}`
*	`{"date": {"earliest": "1900-01-01", "latest": "today"}, "rate" : "uniform"}`

Note that `"incidence"` is used either for the actual incidence of a binary variable (`returning="binary_flag"`), or to indicate non-missingness for other variable types.
`"rate"` is used for the distribution of date values (with either `"exponential_increase"` or `"uniform"`), but can also be used as an alias for `incidence=1` by specifying `rate="universal"` for non-date values.

`population_ages` samples from the distribution of ages in the UK taken from [the Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/tablea21principalprojectionukpopulationinagegroups).
