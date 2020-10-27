## Importing code building blocks

To create the study defintion, we first need to import the functions and code to create this. You will need
to put this codeblock at the top of your python file. 

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

## Basic Study Definition 

The StudyDefinition (imported above) is used to define both the study population and all the important
covariates.

```py
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # STUDY POPULATION
   population=patients.all(),
)
```

`default_expectations=` is needed to allow dummy data to be generated with some sensible dates. 

`population=` is where the population is defined. In this case, we want all patients and are using the method `all()`
to indicate this. 

See population section to see how this could be made more precise. 

## Pulling Codelists into your Study Definition

Many functions for defining covarites take *codelists* as arguments.  
Codelists live in CSV files in the `codelists/` directory, and are loaded into variables like this:


```py
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)
```

This code needs to come before your `StudyDefinition()`. You can do this in `analysis/study_definition.py`
but we recommend that you put all your codelist definitions into a file called `codelists.py` and import
it in at the top of your file:

```py 
from codelists import *
```

This just keeps it cleaner and easier to read. 

## Generating your variables 

Various variables are supported. Please see a list of all variables in variables section. 

Finding a clinical event is a common kind of variable query. It allows you to flag
patients matching lists of codes.  The flag is typically a date, but
can be a binary variable or a count.

This is added after the `population` is defined and before the final bracket. 

The code below, pulls in all the codes from a COPD codelist which is in the `codelist/` folder. 
It then returns a date for the first date that any code in this codelist appears in the 
patient record, rounded to the nearest month. 

```py
copd=patients.with_these_clinical_events(
    copd_codes,
    find_first_match_in_period=True,
    date_format="YYYY-MM",
)
```

## Putting it all together 

The below code is the same code detailed above but put together to show the format:

```py 
from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
)

from codelists import *

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # STUDY POPULATION
   population=patients.all(),

    # COPD 
    copd=patients.with_these_clinical_events(
    copd_codes,
    find_first_match_in_period=True,
    date_format="YYYY-MM",
    ),
)
```

This would produce a `input.csv` file with 2 columns. Note that no date in the copd column indicates no code
was found in that patient record. 

|patient_id|copd|
|---|---|
|177||
|183| 2002-02|
|323| 2014-06|

## Expectations

Every element in a study definition must have `expectations` defined:
that is, the general shape of the expected output data.

All elements use a default defined at the top of the study definition. In this case, events are expected to be 
distributed with exponentially-increasing frequency from 1900 to today:


```py
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
    },
    ...

```

In order to generate dummy data for developing the analytic code against, we need to make sure that 
there are values in the variable columns. In this case, we have taken our copd variable, and indicated 
that we expect 20% of all dummy patients (i.e. rows) to have a date generated for them in copd column. 

```py
    copd=patients.with_these_clinical_events(
    copd_codes,
    return_first_date_in_period=True,
    date_format="YYYY-MM",
    return_expectations={"incidence": 0.2},
    ),
```