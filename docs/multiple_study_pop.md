When using multiple study definitions, there's often a lot of common variables between them, with just the population and maybe a couple of other variables that differ. This means you have to separately specify the common variables in each definition, and it's easy to make an error, particularly when something needs changing. To avoid this, there is a way to share these common variables between study definitions:

## Define a common study definition 

Make a file called `common_variables.py` containing the following code:

```py
from cohortextractor import patients

from codelists import *

```

You can then define your common variables in a dictionary (`dict`) rather than in a `StudyDefinition`. In this case 
we use age and sex. 

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

## Define the specific study definitions
Within each `study_definition_*.py`, add the line `from common_variables import common_variables` near the top with the 
other imports. You then need just before the final closing brackets at the end of the file, add `**common_variables`

`study_definition_copd.py`
```py 
from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    combine_codelists
)

from common_variables import common_variables
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

    **common_variables 
)
```
