Every variable in a study definition must have `expectations` defined: that is, the general shape or distribution of the variables in the dummy data used for developing the code.

## Specifying default distributions

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

## Specifying variable-specific distributions
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


## All options
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

## Variable extractor functions returning value-date pairs

Some variable extractor functions will produce two variables: a value and the corresponding date. 
In this case, expectations for both the value and the date can be specified, for example as follows:

```py
sbp = patients.patients_mean_recorded_value(
	systolic_blood_pressure_codes,
	on_most_recent_day_of_measurement = True,
	include_measurement_date = True,
	on_or_after = index_date,
	date_format = "YYYY-MM-DD",
	return_expectations = {
		"incidence" : 0.8,
		"float" : {"distribution": "normal", "mean": 110, "stddev": 20},
		"date" : {"earliest": index_date, "latest": "today"},
		"rate" : "uniform"
	},
)
```
This says that we expect the returned systolic blood pressure values to be normally distributed and available for 80% of patients from the `index_date` and `"today"`'s date. The date of the most recent measurement is distributed uniformly between those dates.

