
## Index Dates

If you define an `index_date` on a study definition then everywhere that you might normally supply a date you can now supply a "date expression". 

Here is a simple example:

```py
study = StudyDefinition(
    index_date = "2015-06-01",
    population = patients.with_these_clinical_events(
        copd_codes,
        between = [
            "first_day_of_year(index_date) - 2 years",
            "last_day_of_year(index_date)",
        ],
    ),
    age = patients.age_as_of("index_date"),
)
```

This can make it easier to change the index date of a study by making sure it is only defined in once place.

The simplest date expression is just `index_date`, which gets replaced by whatever the index date is set to.

It's also possible to apply various functions to the index date.
The available options (hopefully self-explanatory) are:
```
first_day_of_month(index_date)
last_day_of_month(index_date)
first_day_of_year(index_date)
last_day_of_year(index_date)
```

Finally, intervals of time can be added or subtracted from the index date (or from a function applied to the index date). 
The available units are `year(s)`, `month(s)` and `day(s)`. 
For example:
```
index_date + 90 days
first_day_of_month(index_date) + 9 months
index_date - 1 year
```

Note that if the index date is 29 February and you add or subtract some number of years which doesn't lead to a leap year, then an error will be thrown. 
Similarly, if adding or subtracting months leads to a month with no equivalent day e.g. adding 1 month to 31 January to produce 31 February.

## Time periods

Most variable extractor functions have arguments for specifying the date range over which you want to retrieve information. 
Most commonly this is `on_or_before=`, `on_or_after=`, or `between=`. 
You must use at most one. 
If no option is given then it will use all dates (including possibly future dates).

As well as specifying dates explicitly with e.g., `on_or_before="2019-12-31"`, you can use the date expressions discussed above.
