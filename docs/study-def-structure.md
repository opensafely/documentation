

## Importing code building blocks

To create the study definition, we first need to import the functions and code to create this.
You will need to put this codeblock at the top of your python file. 

```py 
from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
)
```

This essentially says we want to import the some functions from the `cohortextractor` module which will be used throughout the script.

## Basic Study Definition 

The `StudyDefinition()` function (imported above) is used to define both the study population and the variables.

```py
study = StudyDefinition(

	# define default dummy data behaviour
	default_expectations = {
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },
	
	# define the study index date
	index_date = "2020-01-01"
	
	# define the study population
	population = patients.all(),
   
	# define the study variables
	
	age = patients.age_as_of(index_date)
   
	# more variables ...
   
)
```

* `default_expectations=` is used to set default behaviour for the dummy data that is generated. 
In this case, we want event dates to be between 1970-01-01 and today's date, uniformly distributed in that period, and occurring for 20% of patients (returning `""` values otherwise).
See the [dummy data section]() for more details.
* `index_date=` is used to set the index date against which all other dates can be defined. 
See [Defining time periods](study-def-time.md) for more details on how the index date is used. 
* `population=` is where the population is defined. 
In this case, we want all patients available in the OpenSAFELY database and so we use the method `all()` to indicate this. 
See the [study population section]() for more details on how to select a specific subset of patients in the OpenSAFELY database.

The `default_expectations`, `index_date`, and `population` arguments are reserved names within `StudyDefinition()`.
All other names are used to define the variables that will appear in the outputted dataset, using _variable extractor functions_ of the form `patients.function_name`.

`age=` is a simple example of an extractor function in use. 
The `patients.age_as_of()` function returns the age of each patient as of the date provided (in this case the `index_date`). 

All other variables are defined similarly. 
To see the full list of currently available extractor functions, see the [Variable Extractor Functions]() section.
