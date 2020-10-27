Most commonly, you will want to include only patients with certain characteristics.

## Using variables to define your population 

To define a study population with one particular characteristic, you need to define the characteristic within the study 
population. 

```py 
population = patients.with_these_clinical_events(
    copd_codes, 
    on_or_before="2017-03-01",
)
```

## Using time registered in one practice 

Researchers often want to exclude patients who have switched practice recently and hence may have an incomplete record 
of their conditions as it can take some time for their records to come from their previous practice. 

```py

population=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
)
```

::: cohortextractor.patients.registered_with_one_practice_between


## Combining population criteria

Population criteria may need to be combined. Here we have combined both COPD and registration details to find only
patients who have COPD and have been registered at a practice for more than a year. 

```py

population=patients.satisfying(
    "has_follow_up AND has_copd",
    has_copd=patients.with_these_clinical_events(
        copd_codes, on_or_before="2017-03-01"
    ),
    has_follow_up=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
)
```

## Index Dates

If you define an `index_date` on a study definition then everywhere that you might normally supply a date 
you can now supply a "date expression". Here is a simple example:

```py
study = StudyDefinition(
    index_date="2015-06-01",
    population=patients.with_these_clinical_events(
        copd_codes,
        between=[
            "first_day_of_year(index_date) - 2 years",
            "last_day_of_year(index_date)",
        ],
    ),
    age=patients.age_as_of("index_date"),
)
```

This can make it easier to change the index date of a study by making sure it is only defined in once place.

The simplest date expression is just the string `index_date`, which gets replaced by whatever the index date is set to.

It's also possible to apply various functions to the index date. The available options (hopefully self-explanatory) are:
```
first_day_of_month(index_date)
last_day_of_month(index_date)
first_day_of_year(index_date)
last_day_of_year(index_date)
```

Finally, intervals of time can be added or subtracted from the index date (or from a function applied to 
the index date). The available units are `year(s)`, `month(s)` and `day(s)`. For example:
```
index_date + 90 days
first_day_of_month(index_date) + 9 months
index_date - 1 year
```

Note that if the index date is 29 February and you add or subtract some number of years which doesn't lead to a 
leap year, then an error will be thrown. Similarly, if adding or subtracting months leads to a month with no equivalent 
day e.g. adding 1 month to 31 January to produce 31 February.

