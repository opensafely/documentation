


## Pulling Codelists into your Study Definition

Many functions for defining variables take *codelists* as arguments. 
Codelists live in CSV files in the `codelists/` directory, and are loaded into variables like this:

```py
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)
```

This code needs to come before your `StudyDefinition()`. 
You can do this in `analysis/study_definition.py` but we recommend that you put all your codelist definitions into a file called `codelists.py` and importing it in at the top of your file:

```py 
from codelists import *
```

This just keeps it cleaner and easier to read. 

You can read more about how to create and edit codelists in the [Codelists](codelist-intro.md) section, and you can read more about how to import codelists into your project folder using `cohortextractor` [here](cohortextractor.md#update_codelists).

## combining codelists

Codelists can be combined where appropriate. 
This has the advantage of keeping codeslists separate for some studies but easily combining them for others. 
This removes the need for manually combining two or more into a new codelist, and naming it and uploading it to [codelists.opensafely.org](https://codelists.opensafely.org).

Codelists can be combined using the `combine_codelist` function from `cohortextractor` for example as follows:

```py
from cohortextractor import combine_codelists

all_cardiac_disease_codes = combine_codelists(
    chronic_cardiac_disease_codes, 
    acute_cardiac_disease_codes
)
```
