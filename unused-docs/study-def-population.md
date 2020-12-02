Most commonly, you will want to include only patients with certain characteristics, rather than every patient in the database.

## Using variables to define your population 

To define a study population with one particular characteristic, you need to define the characteristic within the study 
population. 

```py 
population = patients.with_these_clinical_events(
    copd_codes, 
    on_or_before = "2017-03-01",
)
```

## Using time registered in one practice 

Researchers often want to exclude patients who have switched practice recently and hence may have an incomplete record of their conditions as it can take some time for their records to come from their previous practice. 

```py
population=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
)
```

::: cohortextractor.patients.registered_with_one_practice_between


## Combining population criteria

Population criteria may need to be combined. 
Here we have combined both COPD and registration details to find only patients who have COPD and have been registered at a practice for more than a year. 

```py

population = patients.satisfying(
    "has_follow_up AND has_copd",
    has_copd=patients.with_these_clinical_events(
        copd_codes, on_or_before="2017-03-01"
    ),
    has_follow_up = patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
)
```

If a variable has been defined elsewhere in `StudyDefinition()`, then that variable can be used in the `patients.satisfying()` function without needing to be defined again. 
For example,

```py
study = StudyDefinition(
	population = patients.satisfying(
		"""
		has_follow_up AND 
		(sex = "M" OR sex = "F")
		""",
		has_follow_up = patients.registered_with_one_practice_between(
			"2019-03-01", "2020-03-01"
		),
	)
	sex = patients.sex(
		"incidence" : 1,
		returning_expectations={"category": {"ratios": {"M": 0.49, "F": 0.51}}}
	),
)
```

Here `sex` is _defined_ outside of `patients.satisfying()` but can still be _used_ inside of it. 
In this case, it's being used to exclude patients without a "valid" sex category (`"M"` or `"F"`) from the study population.

## Dummy data versus real data

The `population=` argument has no bearing at all on the dummy data. It is just used to select patients in the real data. 
If in the example above we had `"incidence" : 0.95`, then 5% of patients in the dummy data would have missing sex values, but 0% of patients in the real data would have missing sex values because they have been excluded with `population=`. 
It's important therefore to match the dummy data with what you would expect to see _conditional on_ the chosen patient population, rather than in the data as a whole.

