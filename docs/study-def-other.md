

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
