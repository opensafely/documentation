A *Codelist* is a collection of clinical codes that classifies patients as having certain conditions or demographic properties. For example, in an clinical system, an asthma diagnosis may be indicated by [any of more than 100 codes](https://www.opencodelists.org/codelist/primis-covid19-vacc-uptake/ast/v1/#full-list).

Codelists must be stored as data within your study repository, from where they can be used in your study definition.

To help you create, edit, and manage codelists, OpenSAFELY provides a web-based tool called [OpenCodelists](https://www.opencodelists.org). For more information about how to create and edit codelists on the  website, see the [codelists documentation](codelist-intro.md).

## Pulling codelists into your study definition

Many functions for defining variables take *codelists* as arguments.

Codelists live as CSV files in the `codelists/` directory (see instructions in the [Adding codelists to a project](codelist-project.md) page).

Codelists are loaded into variables as follows:

```py
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)
```

You should put code that creates codelist variables before your `StudyDefinition()`, so it can refer to them, and users know where to look.

You can do this in `analysis/study_definition.py`, but we recommend that you put all your codelist definitions into a file called `codelists.py` and importing it in at the top of your file:

```py
from codelists import *
```

This keeps it cleaner and easier to read.

## Combining codelists

Codelists can be combined where appropriate.
This has the advantage of keeping codeslists separate for some studies but easily combining them for others.


Codelists can be combined using the `combine_codelist` function from `cohortextractor`, for example:

```py
from cohortextractor import combine_codelists

all_cardiac_disease_codes = combine_codelists(
    chronic_cardiac_disease_codes,
    acute_cardiac_disease_codes
)
```

## Using a single code

In some cases you may only want a variable to use a one or two codes, e.g you want to look at use of a single code within a codelist. You can create a codelist object directly as follows:

```py
weight_codes = codelist(
    ["27113001", "162763007"], system="snomed"
)
```

Whilst you can pass this a list of codes of any length, we recommend building or using existing codelists on OpenCodelists for ease of discoverability and reproducibility.
