This section introduces some tricks for working more efficiently with the study definition API, by helping you to avoid copy-and-pasting chunks of code unnecessarily. 

## Create a variable for each code in a codelist

Say we have a codelist and want to return the number of times each code in that codelist was used, then a variable is needed for each code within the codelist. The standard way to create these variables would be as follows:

```py
study = StudyDefinition(

    ...

    count_code1 = patients.with_these_clinical_events(
        codelist(code1, system="snomed"),
        on_or_after="index_date",
        returning = "number_of_matches_in_period",
        return_expectations={
            "incidence": 0.1,
            "int": {"distribution": "normal", "mean": 3, "stddev": 1}
        }
    ),

    count_code2 = patients.with_these_clinical_events(
        codelist(code2, system="snomed"),
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

A neater way of doing this is to wrap the variable signature in a function and loop that function over each code in the codelist:

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

This function is then invoked inside the `StudyDefinition` call for example as follows:

```py
study = StudyDefinition(

    ...
	
    **loop_over_codes(diabetes_codes),
	
    ...
)

```

This pattern can be used for any type of variable that uses codelists. For instance to extract the first admission date for a set of diagnoses in a codelist, use the following variable signature function:

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

Example code: https://github.com/opensafely/long-covid/blob/master/analysis/study_definition_cohort.py

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
This is ok for 5 events, but if you need more it becomes quite cumbersome. An alternative is to wrap the variable signature in a function and loop that signature over the number of events required:


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

* This does not make for efficient SQL queries. It is creating a new query for each event, rather than a query for each set of events. This will slow down extraction time considerably.
* The dummy data won't necessarily appear in date order. It may be possible to tinker with the function to make this work. Another workaround is to reorder the columns post-extraction, for example here: https://github.com/opensafely/covid-vaccine-effectiveness-research/blob/be747894e1fadf525e391c01477a8ac532613b42/analysis/R/data_process.R#L229 
* It's likely that you'll want to to convert this wide-formatted data to long format, 

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

However, if the number of categories is large, for instance small geographical regions like MSOAs, then it's a pain to have to write out all these by hand. An alternative is to create an external file containing the category levels, import this as a python dict, and pass this dict to the `return_expectations` argument. For example:

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

If the category levels are named with a predictable structure for example (`["stage 1", "stage 2", ...]`, or [`100, 200, 300, ...`]) then a dict comprehension can be used to create the levels, without having to import them. For example for IMD ranks rounded to the nearest 100:

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

## Common variables
For using the same set of variables across different study definitions, see the [common variables section]( https://docs.opensafely.org/study-def/#sharing-common-study-definition-variables) of the documentation.