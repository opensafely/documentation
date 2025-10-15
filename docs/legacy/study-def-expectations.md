---
search:
  exclude: true
---
---8<-- 'includes/cohort-extractor-deprecated.md'

Because OpenSAFELY doesn't allow direct access to individual patient records, researchers must use *dummy data* for developing their analytic code on their own computer.

OpenSAFELY requires you to define *expectations* in your study definition: these describe the properties of each variable, and are used to generate random data that match the expectations.

You can also [provide your own dummy data](#providing-your-own-dummy-data).

## Defining `return_expectations`

Every variable in a study definition must have a `return_expectations` argument defined (with the exception of the `population` variable).
This defines the general shape or distribution of the variables in the dummy data used for developing the code.  It is currently relatively unsophisticated; each variable is generated independently of all others. In most cases, dummy data is good enough to test that it is possible to run your study from start to finish, but sometimes not. You can find (and contribute to!) discussions on improving the [dummy data framework](https://github.com/opensafely-core/cohort-extractor/issues/221).

### Specifying default distributions

All variables use a default defined at the top of the study definition, with the `default_expectations` argument, as follows:

```py
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
        "incidence": 0.5,
    },
    ...
)
```

These defaults apply to *all* subsequently defined variables. `incidence` and `rate` have slightly different meanings depending on the variable type.

In this case, we are saying that:

* Events dates are expected to be distributed between 1900 and today, with exponentially-increasing frequency, with events occurring for 50% of patients.
* Values for binary variables are expected to be positive 50% of the time.
* Values for categorical variables are expected to be present (i.e., non-missing) 50% of the time.
* Values for numeric variables are expected to be present (i.e., non-missing) 50% of the time.

### Specifying variable-specific distributions
If the defaults need to be overridden, then use the `return_expectations` argument within the variable extractor function, for example as follows:

```py linenums="1" hl_lines="6 14"
    study = StudyDefinition(
        # Configure the expectations framework
        default_expectations = {
            "date": {"earliest": "1900-01-01", "latest": "today"},
            "rate": "exponential_increase",
            "incidence": 0.5
        },
        ...
        copd = patients.with_these_clinical_events(
            copd_codes,
            returning = "binary_flag",
            find_first_match_in_period = True,
            between = [index_date, "today"],
            return_expectations = {"incidence": 0.2},
        ),
    )
```
This overrides the 50% default incidence specified in the `default_expecations` argument at the start of the StudyDefinition() with 20% for the `copd` variable.

### All options
The following options are currently available for dummy data (note numeric values are shown as examples only):

**integers**

* `{"int" : {"distribution": "normal", "mean": 25, "stddev": 5}, "incidence" : 0.5}`
* `{"int" : {"distribution": "poisson", "mean": 5}, "incidence" : 0.6}`
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


### Notes on parameters/variables

**Incidence**

* For binary variables, `{"incidence": 0.5}` means we expect values to be `1` in 50% of cases and `0` in 50% of cases.
* For integer, float, and categorical variables, `{"incidence": 0.5}` means we expect values to occur in 50% of cases and not to occur (i.e. to be missing) in 50% of cases.

**Rate**

* For date variables, rate describes the distribution and can be either `"exponential_increase"` or `"uniform"`.
* For binary variables rate can be `"universal"`, which means we expect values to be `1` in all cases.
  This is an alias for `{"incidence": 1.0}`.
* For integer, float, and categorical variables rate can be `"universal"`, which means we expect values to occur in all cases.
  This is an alias for `{"incidence": 1.0}`.

**Distribution**

* `"normal"` means we expect a normal distribution.
* `"poisson"` means we expect a poisson distribution - better for variables that are counts.
* `"population_ages"`: means we expect the distribution to match that of the distribution of ages in the UK from [the Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/).

## Providing your own dummy data

If the expectations framework does not offer enough control over the dummy data that is generated, you can provide your own.

In your `project.yaml`, you can add a `dummy_data_file` value to a `cohortextractor` action.

For instance:

```
generate_cohort:
  run: cohortextractor:latest generate_cohort --output-format csv.gz
  dummy_data_file: test-data/dummy-data.csv.gz
  outputs:
    highly_sensitive:
      cohort: output/input.csv.gz

```

The dummy data file must be committed to the repo.
You should generate the dummy data using a script, and commit the script to the repo.

!!! warning
You must not use real clinical data for dummy data!
