This section introduces some tricks for working more efficiently with the study definition API, by helping you to avoid copy-pasting chunks of code unnecessarily. 

A study definition is a Python script which uses some friendly OpenSAFELY functions to specify the data that you want to extract from the database. But it's still just a Python script, so you can push beyond this API to run other bits of Python code such as importing additional libraries and data, or creating functions and loops. The examples below do exactly this. For users without any Python experience these tricks could be hard to understand and adapt, so you should only incorporate them into your own study definition if you are confident about what they do. If unsure, ask for a code review.

If you have devised a trick of your own then please share it with us. It helps us to understand how people are using OpenSAFELY and whether there are any commonly-used patterns that could be intergrated into the framework. 

## Create a variable for each code in a codelist

Say we have a codelist and want to return the number of times each code in that codelist was used, then a variable is needed for each code within the codelist. The standard way to create these variables would be as follows:

```py
study = StudyDefinition(

    ...

    count_code1 = patients.with_these_clinical_events(
        codelist(["code1"], system="snomed"),
        on_or_after="index_date",
        returning = "number_of_matches_in_period",
        return_expectations={
            "incidence": 0.1,
            "int": {"distribution": "normal", "mean": 3, "stddev": 1}
        }
    ),

    count_code2 = patients.with_these_clinical_events(
        codelist(["code2"], system="snomed"),
        on_or_after="index_date",
        returning = "number_of_matches_in_period",
        return_expectations={
            "incidence": 0.1,
            "int": {"distribution": "normal", "mean": 3, "stddev": 1},
        }
    ),

    ...
	
)

```

A neater way of doing this is to wrap the variable in a function and loop that function over each code in the codelist:

```py

def loop_over_codes(code_list):

    def make_variable(code):
        return {
            f"count_{code}": (
                patients.with_these_clinical_events(
                    codelist([code], system="snomed"),
                    on_or_after="index_date",
                    returning="number_of_matches_in_period",
                    return_expectations={
                         "incidence": 0.1,
                         "int": {"distribution": "normal", "mean": 3, "stddev": 1},
                    },
                )
            )
        }

    variables = {}
    for code in code_list:
        variables.update(make_variable(code))
    return variables

```

This function can be invoked inside the `StudyDefinition` section as follows:

```py
study = StudyDefinition(

    ...
	
    **loop_over_codes(diabetes_codes),
	
    ...
)

```

This pattern can be used for any type of variable that uses codelists. For instance to extract the first admission date for a set of diagnoses in a codelist, use the following function:

```py
def make_variable(code):
    return {
        f"date_of_first_{code}": (
            patients.admitted_to_hospital(
                with_these_primary_diagnoses = codelist([code], system="icd10"),
                on_or_before="index_date",
		find_first_match_in_period=True,
                returning="date_admitted",
		return_expectations={
		    "incidence": 0.1,
                    "date": {"2015-01-01": "index_date"}}
                },
            )
        )
    }
```

An example of this can be seen in the [long-covid repository](https://github.com/opensafely/long-covid/blob/5923ebc09b898fac132c39ae7c980bf11d821e4d/analysis/study_definition_cohort.py).

## Extracting a series of consecutive events

Say we wanted to extract the first 5 coding events that occurred after a study start date. We could do this using:

```py
admission_date1 = patients.with_these_clinical_events(
                    codelist,
                    returning="date",
                    on_or_after="index_date",
                    date_format="YYYY-MM-DD",
                    find_first_match_in_period=True,
		    return_expectations = {...}
                ),
				
admission_date2 = patients.with_these_clinical_events(
                    codelist,
                    returning="date",
                    on_or_after="admission_date1 + 1 day",
                    date_format="YYYY-MM-DD",
                    find_first_match_in_period=True,
                    return_expectations = {...}
                ),
				
...

admission_date5 = patients.with_these_clinical_events(
                    codelist,
                    returning="date",
                    on_or_after="admission_date4 + 1 day",
                    date_format="YYYY-MM-DD",
                    find_first_match_in_period=True,
                    return_expectations = {...}
                ),
```
This is ok for 5 events, but if you need more it becomes quite cumbersome. An alternative is to wrap the variable in a function and loop it over the number of events required:


```py
def with_these_clinical_events_date_X(name, codelist, index_date, n, return_expectations):
    
    def var_signature(name, codelist, on_or_after, return_expectations):
        return {
            name: patients.with_these_clinical_events(
                    codelist,
                    returning="date",
                    on_or_after=on_or_after,
                    date_format="YYYY-MM-DD",
                    find_first_match_in_period=True,
                    return_expectations=return_expectations
	    ),
        }
    variables = var_signature(f"{name}_1", codelist, index_date, return_expectations)
    for i in range(2, n+1):
        variables.update(var_signature(f"{name}_{i}", codelist, f"{name}_{i-1} + 1 day", return_expectations))
    return variables
```

This can then be used inside a study definition for example as follows:


```py
study = StudyDefinition(

	...
	
	**with_these_clinical_events_date_X(
		name = "probable_covid_date", 
		codelist = probable_codes, 
		returning="date",
		on_or_after = "index_date",
		n = 5, 
		return_expectations = {
			"date": {"earliest": "2020-05-01", "latest": "2021-06-01"},
			"rate": "uniform",
			"incidence": 0.05,
		},
	),
	
	...
)
```

This can be used for any variable where you want to return information for a series of consecutive events. 

The will create `n` columns in the dataset. A few things to be aware of:

* Behind the scenes, this creates a new SQL query for each variable rather than a single query for everything. This can be inefficient and could slow down extraction time considerably. You should therefore only extract the minimum `n` events needed for your study.
* The dummy data won't appear in date order. You could write a more sophisticated function, with different expectations for each `i`. Or you could reorder the columns post-extraction, for example in [covid-vaccine-effectiveness-research repository](https://github.com/opensafely/covid-vaccine-effectiveness-research/blob/be747894e1fadf525e391c01477a8ac532613b42/analysis/R/data_process.R#L229). 
* Many routines for analysing this sort of data, for example in R or Stata, require the data to be in long-form, not wide-form as they are returned here. In that case, you'll need to reshape the columns. 

## Better dummy data for categorical variables
For categorical variables with a small number of categories, the standard way of creating dummy data is easy to use, for example:

```py
sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    )
```

However, if the number of categories is large, for instance small geographical regions like MSOAs, then it's a pain to have to write out all these by hand. An alternative is to create an external file containing the category levels, import this as a python [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) (or "dict"), and pass this to the `return_expectations` argument. For example:

```py
import pandas as pd

STPs = pd.read_csv(
    filepath_or_buffer = './lib/STPs.csv'
)

dict_stp = { stp : 1/len(STPs.index) for stp in STPs['stp_id'].tolist() }

study = StudyDefinition(
 
    ...

    stp = patients.registered_practice_as_of(
        index_date,
        returning="stp_code",
        return_expectations={
            "category": {"ratios": dict_stp},
        },
    ),
    
    ....

)

```

If the category levels are named with a predictable structure for example (`["stage 1", "stage 2", ...]`, or [`100, 200, 300, ...`]) then a [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) [comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) can be used to create the levels, without having to import them. For example for IMD ranks rounded to the nearest 100:

```py
 imd=patients.address_as_of(
        "index_date",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "category": {"ratios": {c: 1/320 for c in range(100,32100, 100)}}
        }
    )
```

See [this issue](https://github.com/opensafely-core/cohort-extractor/issues/312) for further discussion about how this functionality might be improved in future.

## Sharing common study definition variables
When using multiple study definitions, there's often a lot of common variables between them, with just the population and maybe a couple of other variables that differ.
This means you have to separately specify the common variables in each definition, and it's easy to make an error, particularly when something needs changing.
To avoid this, you can use the following approach to share common variables between study definitions:

Make a Python script called `common_variables.py` containing the following code:

```py
from cohortextractor import patients

from codelists import *
```

In this script, define your common variables in a dictionary (`dict`) rather than in a `StudyDefinition`.
In this case we use age and sex.

`common_variables.py`
```py
common_variables = dict(
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

Within each `study_definition_*.py`, add the line `from common_variables import common_variables` near the top with the other imports.
You then add `**common_variables` just before the final closing brackets at the end of the script.
This approach can also use different index dates, that are then passed to variables in `common_variables.py`.

`study_definition_copd.py`
```py
from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    combine_codelists,
)

from common_variables import common_variables
from codelists import *

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },
    # define the study index date
    index_date="2020-01-01",

    # STUDY POPULATION
    population=patients.all(),

    # COPD
    copd=patients.with_these_clinical_events(
        copd_codes, find_first_match_in_period=True, date_format="YYYY-MM",
    ),
    **common_variables
)
```

## Extracting ethnicity at multiple index dates

Extracting ethnicity can take a long time, as a large number of codes must be mapped to a small number of categories.
[This codelist](https://www.opencodelists.org/codelist/opensafely/ethnicity/2020-04-27/#full-list), for example, maps 270 codes to both 16 categories and six categories.

If you are extracting variables at multiple index dates (e.g. by week or by month), then extracting a variable like ethnicity, which we don't expect to change over time, is inefficient:
The codes will be mapped to the categories for each index date, when we don't expect them to change from index date to index date.
Instead, we can:

* Extract ethnicity once
* Extract the other variables once for each index date
* Join each index date's extract to the ethnicity extract

The following study definition (`analysis/study_definition_ethnicity.py`) demonstrates how we would extract ethnicity once:

```python
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # We extract ethnicity once for all patients, to ensure we don't exclude
    # any patients.
    population=patients.all(),

    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,  # the codelist
        returning="category",
        find_last_match_in_period=True,  # most recent code
        return_expectations={
            "category": {"ratios": {"1": 0.2, "2": 0.2, "3": 0.2, "4": 0.2, "5": 0.2}},
            "incidence": 0.75,
        },
    ),
)
```

The following [scripted action](actions-scripts.md) (`analysis/join_ethnicity.py`) demonstrates how we would join each index date's extract to the ethnicity extract:

```python
import pathlib

import pandas


path_to_output = pathlib.Path("output")

input_ethnicity = pandas.read_feather(path_to_output / "input_ethnicity.feather")

for path in path_to_output.iterdir():
    if not path.name.startswith("input") or path.name == "input_ethnicity.feather":
        continue

    input_other = pandas.read_feather(path)
    input_other = input_other.merge(input_ethnicity, how="left", on="patient_id")

    # If the old path was "output/input_2021-01-01.feather", then the new
    # path will be "output/input_2021-01-01_merged.feather".
    new_path = path_to_output / f"{input_other.stem}_merged{input_other.suffix}"
    input_other.to_feather(new_path)
```

You can find a Python example in [this repo](https://github.com/opensafely/sro-template) and an R example in [this repo](https://github.com/opensafely/sro-template).
