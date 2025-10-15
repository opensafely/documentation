---
search:
  exclude: true
---
---8<-- 'includes/cohort-extractor-deprecated.md'

In study definitions, dates are described in `"YYYY-MM-DD"` format; so, for example, the 3rd May 1995 would be written `"1995-05-03"`.


## Supplying time periods to functions

Most variable extractor functions have arguments for specifying the date range over which you want to retrieve information.
Most commonly this is `on_or_before=`, `on_or_after=`, or `between=` (see the [variable reference](study-def-variables.md) for full documentation).
You can set one or both of `on_or_before=` / `on_or_after=`; but these cannot be mixed with `between=` (which is equivalent to setting both `on_or_before=` AND `on_or_after=`).
If no option is given then it will use all dates (including possibly future dates).


As well as specifying dates explicitly with e.g., `on_or_before="2019-12-31"`, you can use the date expressions discussed [below](#index-dates).

### Setting date ranges to filter out 'impossible' dates

You should be aware that events can be recorded in clinical systems without a date:

- These default to `1900-01-01` in OpenSAFELY but other dates around and before this date are also possible.
- In some systems, null values for dates may be recorded with the ceiling value `9999-12-31`.
- These often relate to demographic information; and sometimes events or diagnoses (e.g. Asthma), which may have been imported from other systems, originally recorded on paper, or reported by patients relating to past experiences but not knowing the precise date.
- In addition, occasionally "impossible" dates may be recorded by accident; for example far in the future, or before a patient was born.

You should take this into account in your analysis; for example, you might want to discard blood pressure values that are in the future, but you might want to keep an ethnicity category which was recorded with no date, as these are less likely to change over time.

### Using dates with patients.satisfying

You should be aware that `patients.satisfying` does not treat `1900-01-01` as equivalent to `NULL`. In order to exclude an impossible date, such as 1900-01-01, you might want to add checks such as

```
study = StudyDefinition(
    ...
    nulldate = patients.fixed_value("1900-01-01"),
    ...
    THIS_GROUP = patients.satisfying(
        """
        date_variable AND date_variable > nulldate
        """,
        ...
    )
)
```

## Index Dates

If you define an `index_date` on a study definition then everywhere that you might normally supply a date you can now supply a "date expression".

Here is a simple example:

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

This can make it easier to change the index date of a study by making sure it is only defined in one place. (Note that if using `between`, ensure that the dates are given in chronological order as in the example above).

The simplest date expression is just `index_date`, which gets replaced by whatever the index date is set to.

It's also possible to apply various functions to the index date.
The available options (hopefully self-explanatory) are:

```py
"first_day_of_month(index_date)"
"last_day_of_month(index_date)"
"first_day_of_year(index_date)"
"last_day_of_year(index_date)"
"first_day_of_nhs_financial_year(index_date)"
"last_day_of_nhs_financial_year(index_date)"
"first_day_of_school_year(index_date)"
"last_day_of_school_year(index_date)"
```

Note:

* NHS financial (reporting) year runs from 1st April to 31st March
* English school year runs from 1st September to 31st August

Any `index_date` you've defined in your study definition can be overridden in your `project.yaml`, by providing an `--index-date-range` argument, like this:

```yaml
actions:

  generate_study_population_1:
    run: >
      cohortextractor:latest generate_cohort
        --study-definition study_definition
        --index-date-range "2020-01-01"
        --output-format csv.gz
    outputs:
      highly_sensitive:
        cohort: output/input-2020-01-01.csv.gz
```

This can also be used to define a range of dates over which to run the study definition, usually when working with [Measures](study-def-measures.md).


## Date arithmetic

Intervals of time can be added or subtracted from an index date, from a function applied to the index date, or from a [dynamic date](#dynamic-dates).

The available units are `year(s)`, `month(s)` and `day(s)`.
For example:

```py
"index_date + 90 days"
"first_day_of_month(index_date) + 9 months"
"index_date - 1 year"
```

Note that if the index date (or other starting date) is 29 February and you add or subtract some number of years which doesn't lead to a leap year, then an error will be thrown.

An error will also be thrown if adding or subtracting months leads to a month with no equivalent day e.g. adding 1 month to 31 January to produce 31 February.

When working with dynamic dates, be aware that null dates may be represented by the ceiling date, `9999-12-31`.  Adding one day to this date will result in a date outside of the valid range, and will throw an error.  This can be avoided by using `between` in the variable definition to set an upper limit on values that excludes the ceiling date.

For example, if there are patients will null (represented as "9999-12-31") entries for GP consultations, this will throw an error:
```py
contact_date = patients.with_gp_consultations(returning="date", on_or_after="index_date"),
next_contact_date = patients.with_gp_consultations(
    returning="date", on_or_after="contact_date + 1 day"
)
```

Instead, define the initial contact date with a `between` argument, with an end date far enough in the future to capture any valid dates:
```py
contact_date = patients.with_gp_consultations(
    returning="date", between=["index_date", "2100-12-31"]
),
next_contact_date = patients.with_gp_consultations(
    returning="date", on_or_after="contact_date + 1 day"
)
```

## Dynamic dates
Dates used in variable definitions can also be taken from date variables defined elsewhere in the study definition, rather than using a common fixed value.
For example, we may want to define a patient's age on their first positive test result, rather than a fixed index date. In this case we first define positive test date as a variable in the study definition, then refer to this variable name in the age definition:

```py
study = StudyDefinition(
    pos_test_date=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD",
    ),
    age=patients.age_as_of("pos_test_date"),
)
```

Here, the patient-specific date `pos_test_date` is defined as the first SARS-CoV-2 positive test result in SGSS, which will differ for each patient.
The age variable is now defined relative to this date, i.e. age is given at the time of the positive SARS-CoV-2 test. Note the need for the variable name to be passed as a string rather than unquoted.
We can also use date expressions on these dates, for example `"pos_test_date - 1 year"`

Wherever the inputted date is null, in this case when a patient doesn't have a positive test result, any variables that reference the date will take the [null value for their variable type](study-def.md#missing-values-and-unmatched-records) (0 for numeric variables; an empty string for character and date variables).

Take particular care that the dates are in the correct order if you are using `between` with dynammic dates, i.e. `[min, max]`, as it will not give the expected results if they are the opposite way around.

## Variables that return value-date pairs

Some functions will produce two variables: a value and the corresponding date.
In this case, expectations for both the value and the date can be specified, for example as follows:

```py
    sbp=patients.mean_recorded_value(
        systolic_blood_pressure_codes,
        on_most_recent_day_of_measurement=True,
        include_measurement_date=True,
        on_or_after="index_date",
        date_format="YYYY-MM-DD",
        return_expectations={
            "incidence": 0.8,
            "float": {"distribution": "normal", "mean": 110, "stddev": 20},
            "date": {"earliest": "index_date", "latest": "index_date + 1 year"},
            "rate": "uniform",
        },
    )
```

This says that we expect the returned systolic blood pressure values to be normally distributed and available for 80% of patients, at dates between the `index_date` and one year later. The date of the most recent measurement is distributed uniformly between those dates.
