# Study Definitions

## Overview

A _study definition_ describes all of the features of your study: the
codelists, the population definitions, the dates, and the variables.

It is written in a custom format which is intended to be readable and
reviewable by anyone with epidemiological knowledge.  The OpenSAFELY
framework uses the study definition to query different vendor EHR
databases, and returns the results in a CSV file of tabular data.

A study definition also allows a researcher to define the shape of the
values they *expect* to get back from the vendor data. This allows the
framework to generate dummy data which the researcher can user to test
models their models during development, without ever having to touch
real patient data.


## Naming study definitions

When you run `cohortextractor generate_cohort`, the framework reads a
study definition at `analysis/study_definition.py`, and writes the
output dataframe to `output/input.csv`.  In a production environment
this will be real data; in a development environment this will be
dummy data.

Multiple study definition files can be specified using a suffix like:
```
study_definition_copd.py
study_definition_asthma.py
```

And all the corresponding output files will have the same suffix e.g.
```
input_copd.csv
input_asthma.csv
```

## Codelist definitions

Many functions for defining covarites take *codelists* as arguments.  Codelists live in CSV files in the `codelists/` directory, and are loaded into variables like this:


```py
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)
```
They can also be combined, like this:

```py
from datalab_cohorts import combine_codelists

all_cardiac_disease_codes = combine_codelists(chronic_cardiac_disease_codes, acute_cardiac_disease_codes)
```

### Defining and recording codelists

The canonical source for codelists in OpenSAFELY is [codelists.opensafely.org](https://codelists.opensafely.org).

Over time, these lists may change, as mistakes are noticed, or new
conditions or medicines are added.  Therefore, your study definition
must contain a snapshot of the specific version of each codelist that
it uses at the time the analysis is run.

As such, codelists should not be added or edited by hand.  Instead:

* Go to [the openSAFELY codelists admin](https://codelists.opensafely.org/admin) (you will need an editor account)
* Create or update the codelist.
  * Copy/paste the CSV data into the `csv_data field`
  * Set the `version_str` to today's date in `YYYY-MM-DD`
  * Click "Save"
* Update the file `codelists/codelists.txt`, which is a list of codelists that your study needs
* From the root of this repo, run `cohortextractor update_codelists`
* Check the git diff for sense
* Commit the changes and make a PR


## Population definitions

Most commonly, you will want to include only patients with a continuous history of (say) 12 months, so that you exclude patients who have switched practice recently and hence may have an incomplete record of their conditions.

```py

population=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
)
```

::: cohortextractor.patients.registered_with_one_practice_between

You can combine this with other criteria thus:

```py

population=patients.satisfying(
    "has_follow_up AND has_asthma",
    has_asthma=patients.with_these_clinical_events(
        asthma_codes, on_or_before="2017-03-01"
    ),
    has_follow_up=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
)
```

To retrieve all patients currently available in OpenSAFELY in your study cohort, use:

```py
population=patients.all()
```




## Variable definitions

All available functions for defining variables within a study definition can be viewed in [`patients.py`](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/patients.py) in the [`cohort-extractor`](https://github.com/opensafely/cohort-extractor) repository. New functions (or changes to existing functions) that are currently under consideration can be found on the `cohort-extractor` [issues page](https://github.com/opensafely/cohort-extractor/issues).


### Clinical Events

The most common kind of variable query. It allows you to flag
patients matching lists of codes.  The flag is typically a date, but
can be a binary variable or a count.


Returning a date, rounded to nearest month:

```py
copd=patients.with_these_clinical_events(
    copd_codes,
    return_first_date_in_period=True,
    date_format="YYYY-MM",
)
```

Returning a count:

```py
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    between=["2001-12-01", "2002-06-01"],
    returning="number_of_matches_in_period",
),
```

If you want to return a count *and* a date, you can reuse the former
definition in a date definition like this:

```py
asthma_count_date=patients.date_of("asthma_count", date_format="YYYY-MM"),
```

#### Counting episodes

We currently provide a single way to define an "episode": a continuous
chain of coded events each of which are no more than a certain number
of days apart:


```py
study = StudyDefinition(
    population=patients.all(),
    copd_episode_count=patients.with_these_clinical_events(
        copd_codes,
        on_or_before="2020-01-01",
        returning="number_of_episodes",
        episode_defined_as="series of events each <= 14 days apart",
    ),
)
```
##### Exclusions

For some definitions of "episode", you want to exclude some kinds of
consultation. For example, a consultation that includes a COPD coding
should only count towards the definition of "episode" if it's not
coded as part of a routine annual review.


```py
study = StudyDefinition(
    population=patients.all(),
    copd_episode_count=patients.with_these_clinical_events(
        copd_codes,
        on_or_before="2020-01-01",
        returning="number_of_episodes",
        episode_defined_as="series of events each <= 14 days apart",
        ignore_days_where_these_codes_occur=copd_annual_review_codes,
    ),
)
```

A similar approach works with medications:

```py
study = StudyDefinition(
    population=patients.all(),
    episode_count=patients.with_these_medications(
        oral_steroid_codes,
        on_or_before="2020-01-01",
        ignore_days_where_these_clinical_codes_occur=annual_review_codes,
        returning="number_of_episodes",
        episode_defined_as="series of events each <= 14 days apart",
    ),
)
```

### Adding date columns to existing variables

If you have already defined a variable, for which you also want to
add a date column, you can wrap a definition with `date_of`.

For example, given this definition which returns matching codes:

```py
latest_smoking_code=patients.with_these_clinical_events(
    smoking_codes,
    find_last_match_in_period=True,
    returning="code",
)
```

You can additionally request a date, thus:


```py
latest_smoking_date=patients.date_of(
    "latest_smoking_code", date_format="YYYY-MM"
)
```

### with_tpp_vaccination_record

This is TPP-specfic, so the method name reflects that; it will not
work against other backends.

An example query might be:

```py
recent_flu_vaccine = patients.with_tpp_vaccination_record(
    target_disease_matches="INFLUENZA",
    on_or_after="2018-01-01",
    find_last_match_in_period=True,
    returning="date",
)
```

or

```py
recent_flu_vaccine = patients.with_tpp_vaccination_record(
    product_name_matches=["Optaflu", "Madeva"],
    on_or_after="2018-01-01",
    find_last_match_in_period=True,
    returning="date",
)
```

Apart from the standard arguments this function takes two optional query
parameters: `target_disease_matches` and `product_name_matches`.

`target_disease_matches` returns all vaccinations that target a
particular disease/pathogen, bearing in mind that a single product
(e.g.  MMR) can target multiple diseases. The values this takes are
all-caps strings drawn from TPP's internal list and should be checked
against the contents of the *live* (not dummy) `VaccinationReference`
table during development.

`product_name_matches` matches against the product name TPP use which,
again, should be checked against the `VaccinationReference` table.

Both arguments can either take either a single string or a list of
strings, in which case it returns results matching _any_ of the items in
the list.

### Care Homes

TPP have attempted to match patient addresses to care homes as stored in
the CQC database. At its most simple the `care_home_status` query
returns a boolean indicating whether the patient's address (as of the
supplied time) matched with a care home.

It is also possible to return a more complex categorisation based on
attributes of the care homes in the CQC database, which can be freely
downloaded here:
https://www.cqc.org.uk/about-us/transparency/using-cqc-data

At present the only imported fields are `LocationRequiresNursing` and
`LocationDoesNotRequireNursing`, but we can ask for more fields to be
imported if needed.

The `categorised_as` argument acts in effectively the same way as for
the `categorised_as` function (q.v.) except that the only columns that
can be referred to are those belonging to the care home table
(i.e. the two nursing fields above) and the boolean
`IsPotentialCareHome`.

Example queries:
```py
is_in_care_home=patients.care_home_status_as_of("2020-01-01")

care_home_type=patients.care_home_status_as_of(
    "2020-01-01",
    categorised_as={
        "PC": """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='Y'
          AND LocationRequiresNursing='N'
        """,
        "PN": """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='N'
          AND LocationRequiresNursing='Y'
        """,
        "PS": "IsPotentialCareHome",
        "U": "DEFAULT",
    },
)
```

### SGSS

This allows us to check COVID test results in the Second Generation
Surveillance System. Example queries are:

```py
study = StudyDefinition(
    population=patients.all(),
    positive_covid_test_ever=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive"
    ),
    negative_covid_test_ever=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="negative"
    ),
    tested_for_covid=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="any",
        on_or_before="2020-05-01"
    ),
    first_positive_test_date=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD",
    ),
)
```

Only SARS-CoV-2 results are included in our data extract so this will
throw an error if the specified pathogen is anything other than
"SARS-CoV-2".

`test_result` must be one of: "positive", "negative" or "any"

The date used is the date the specimen was taken. Where a patient has
multiple positive results only the date of the earliest specimen that
tested positive is recorded. (See docstring for a more detailed explanation.)

The data we receive has an Organism_Species_Name field which is always
"SARS-CoV-2 CORONAVIRUS (Covid-19)" in the case of a positive result and
"NEGATIVE SARS-CoV-2 (COVID-19)" in the case of a negative result. The
code will throw an error if anything else is ever found in this field.

### Consultations

In OpenSAFELY, a "consultation" means a GP-patient interactions, either
in person or via phone/video call. However, the concept of a
"consultation" in EHR systems is generally broader and might include
things like updating a phone number with the receptionist.

Because of this, it's possible that we might have a full medical
history for a patient (imported via GP2GP) but not have an exact
record of which of their imported consultations should be considered
as GP-patient interactions.

There are, therefore, two methods for querying consultations:
`with_gp_consultations` and
`with_full_gp_consultation_history_between`.  The boolean predicate
`with_full_gp_consultation_history_between` allows us to identify
patients where we _do_ have a reliable history.


Example queries:
```py
...
consultation_count=patients.with_gp_consultations(
    between=["2010-01-01", "2015-01-01"],
    find_last_match_in_period=True,
    returning="number_of_matches_in_period",
),
latest_consultation_date=patients.date_of(
    "consultation_count", date_format="YYYY-MM"
),
has_history=patients.with_complete_gp_consultation_history_between(
    "2010-01-01", "2015-01-01"
),
...
```

### Households

OpenSAFELY can return information about the household to which the
patient belonged as of a reference date. This is inferred from address
data using an algorithm developed by TPP (to be documented soon) so the
results are not 100% reliable but are apparently pretty good.

Options for `returning` are:

```
    pseudo_id: An integer identifier for the household which has no meaning
               other than to identify individual members of the same
               household (0 if no household information available)

    household_size: the number of individuals in the household (0 if no
                    household information available)
```

Examples:

```
household_id=patients.household_as_of(
    "2020-02-01", returning="pseudo_id"
)

household_size=patients.household_as_of(
    "2020-02-01", returning="household_size"
),
```

### Missing values

If a query returns no matching record for a patient &mdash; for example if there are no blood pressure values recorded in a given period, or if there is no death date because the patient hasn't died, or if there is no household size available &mdash; then a default value will be returned. For strings and dates, the default value is the empty string `""`. For booleans, integers, or floats, the default value is `0`. There is no universal `null` value outputted to `input.csv` because these may be handled inconsistently across different programs.

## Expectations

Every element in a study definition must have `expectations` defined:
that is, the general shape of the expected output data.

All elements use a default defined at the top of the study definition. In this case, events are expected to be distributed with exponentially-increasing frequency from 1900 to today:


```py
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
    },
    ...

```

Individual elements can extend or override the defaults. This column will show dates getting exponentially more frequent over time, but only applying to 20% of the population:

```py
    chronic_cardiac_disease=patients.with_these_clinical_events(
        chronic_cardiac_disease_codes,
        returning="date",
        find_first_match_in_period=True,
        include_month=True,
        return_expectations={"incidence": 0.2},
    ),
```

Here, we state that we expect the values returned to be numbers, normally distributed around the value of 8, with values for 60% of the population:

```py
    recent_salbutamol_count=patients.with_these_medications(
        salbutamol_codes,
        between=["2018-02-01", "2020-02-01"],
        returning="number_of_matches_in_period",
        return_expectations={
            "incidence": 0.6,
            "int": {"distribution": "normal", "mean": 8, "stddev": 2},
        },
    ),
```

For elements that return categories, we can define expected proportions:

```py

    rural_urban=patients.address_as_of(
        "2020-02-01",
        returning="rural_urban_classification",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"rural": 0.1, "urban": 0.9}},
        },
    ),

```

There is also a custom distribution matching a typical population-age distribution for the UK:

```
    age=patients.age_as_of(
        "2020-02-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
```

## Index Dates

If you define an `index_date` on a study definition then everywhere that you might normally supply a date you can now supply a "date expression". Here is a simple example:

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

Finally, intervals of time can be added or subtracted from the index date (or from a function applied to the index date). The available units are `year(s)`, `month(s)` and `day(s)`. For example:
```
index_date + 90 days
first_day_of_month(index_date) + 9 months
index_date - 1 year
```

Note that if the index date is 29 February and you add or subtract some number of years which doesn't lead to a leap year, then an error will be thrown. Similarly, if adding or subtracting months leads to a month with no equivalent day e.g. adding 1 month to 31 January to produce 31 February.


### Flowcharts (temporary workaround)

Many studies will require a flowchart to show inclusion/exclusion of patients in the study. Eventually the numbers of patients excluded/included will be summarised automatically following cohort extract, but for now, a slightly manual approach is required:

 - Make a copy of the study definition (called `study_definition_flow_chart.py`). The `population=patients.satisfying()` function should be replaced with `population=patients.all()`. Then all variables except for those that appeared in the population definition logic should be removed (this will mean that it runs much faster than the main study definition). An example of such a study definition is [here](https://github.com/opensafely/nsaids-covid-research/pull/24).
  - Then make a Stata .do file that reads the `input_flow_chart.csv` and then sequentially drops each of the variables and counts the remaining population, in whatever order you'd like to report them. For example [here](https://github.com/opensafely/nsaids-covid-research/blob/flowchart/analysis/flowchart_numbers.do)


### Common variables when using multiple study definitions

When using multiple study definitions, there's often a lot of common variables between them, with just the population and maybe a couple of other variables that differ. This means you have to separately specify the common variables in each definition, and it's easy to make an error, particularly when something needs changing. To avoid this, there is a way to share these common variables between study definitions:
1. Make a file called `common_variables.py` containing the following code
```py
from cohortextractor import patients
from codelists import *
common_variables = dict(
    # LIST OF ALL COMMON VARIABLES IN THE SAME FORMAT THEY WOULD BE IN A NORMAL STUDY DEFINITION, E.G.
    age=patients.age_as_of(
        "2020-02-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
)
```
2. Within each `study_definition.py`, add the line `from common_variables import common_variables` near the top with the other imports
3. Just before the final closing brackets at the end of the file, add `**common_variables`
An example of how this should look is [here](https://github.com/opensafely/post-covid-thrombosis-research/tree/4cc8bfcef94137e2aa65f9cd1d50fa9c9de8ce12)
