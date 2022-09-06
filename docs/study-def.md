## What is a Study Definition?

(Know what you're doing and just looking for a quick reference? Go to the [variable reference](study-def-variables.md))

A _study definition_ is a formal specification of the data that you want to extract from the OpenSAFELY database. This includes:

* the patient population (dataset rows)
* the variables (dataset columns)
* the expected distributions of these variables for use in dummy data

It is written in the Python programming language, using an OpenSAFELY-specific
format which is intended to be easily written, read, and reviewed by anyone with
some epidemiological knowledge.

!!! note "Some knowledge of python is helpful!"

    The following documentation should get you through most cases, but
    some will make little sense to a non-Python programmer.  It is on our
    roadmap to replace the Python-based approach with a configuration-based
    approach which is more secure, and can be driven from a graphical user interface.

The OpenSAFELY framework uses a single study definition to query different
vendor EHR databases, and saves the results to the secure server in a CSV file
of tabular data.

A study definition also allows a researcher to define the shape of the values they *expect* to get back from the vendor data.
This allows the framework to generate dummy data which the researcher can use to develop and test their analysis scripts, without ever having to touch real patient data.

When you generate a study population, the framework reads your study definition from the python script (usually `analysis/study_definition.py`), and writes the output data frame in a tabular CSV file (usually `output/input.csv`).
In a production environment this file will contain real data; in a development environment this will be dummy data.

Currently the framework supports one row per patient datasets.

## `study_definition.py` structure

### Importing code building blocks

To create the study definition, we first need to import the functions and code to create this.
You will need to put this codeblock at the top of your python file.

```py
from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)
```

This essentially says we want to import some functions from the `cohortextractor` package which will be used throughout the script.

### A simple example

The `StudyDefinition()` function (imported above) is used to define both the study population and the variables.

```py
study = StudyDefinition(
    # define default dummy data behaviour
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # define the study index date
    index_date="2020-01-01",

    # define the study population
    population=patients.all(),

    # define the study variables
    age=patients.age_as_of("index_date")

    # more variables ...
)
```

* `default_expectations=` is used to set default behaviour for the dummy data that is generated.
In this case, we expect event dates to be between `1970-01-01` and today's date, uniformly distributed in that period, and to be recorded for 20% of patients (returning empty `""` values otherwise).
See [Dummy data and expectations](study-def-expectations.md) for more details.
* `index_date=` is used to set the index date against which all other dates can be defined.
See [Working with dates](study-def-dates.md) for more details on how the index date is used.
* `population=` is where the population is defined.
In this case, we want all patients available in the OpenSAFELY database and so we use the method `all()` to indicate this.
See the [study population section](#defining-the-study-population) for more details on how to select a specific subset of patients in the OpenSAFELY database.

The `default_expectations`, `index_date`, and `population` arguments are reserved names within `StudyDefinition()`.
All other names are used to define the variables that will appear in the outputted dataset, using _variable extractor functions_ of the form `patients.function_name`.

`age=` is a simple example of an extractor function in use.
The `patients.age_as_of()` function returns the age of each patient as of the date provided (in this case the `index_date`).

All other variables are defined similarly.
To see the full list of currently available extractor functions, see [Study Definition variables reference](study-def-variables.md).


## Defining and extracting variables

All the variables that you want to include in your dataset are declared within the `StudyDefinition()` function, using functions of the form `patients.function_name()`.

To see the full documentation for all the variables that can be extracted with queries to the OpenSAFELY database, see [Study Definition variable reference](study-def-variables.md).

### Missing values and unmatched records

If a query returns no matching record for a patient &mdash; for example if there are no blood pressure values recorded in a given period, or if there is no death date because the patient hasn't died, or if there is no household size available &mdash; then a default value will be returned.
For strings and dates, the default value is the empty string `""`.
For booleans, integers, or floats, the default value is `0`.

There is no universal `null` value outputted to `input.csv` because these may be handled inconsistently across different programs.

It's possible that a record is matched, but the value is not valid.
In this case, the value will be returned as-is.
For example, a date set to `"9999-99-99"` or a blood pressure reading set to `-1`.
These will indicate missing / unknown / unrecorded / not applicable values in the source dataset.
The meaning of these values will depend on the data source, and this should be documented in the [dataset documentation](data-sources/intro.md).

In some instances, 0s will be returned for missing values when there are also numeric values of 0. Distinguishing true 0s from missing values can't be done 100% reliably within TPPs data model as, as stated above, the numeric value isn't nullable. Possible workarounds for this include:

1. For values which are normally expected to be associated with comparators (i.e. lab data values), fetch the comparator into a separate column. If that comparator column is empty, you can assume that there is no associated value.
2. For values not associated with comparators, a similar result could be achieved using the `date_of()` function to pull the date (even just the year) of the value into a separate column. If there is no associated year, then you know that it was not a true zero.

## Defining the study population

Each study definition must have a `population` variable defined. This is a special variable used to select all the patients for whom you want to extract information. Most likely, there will be multiple criteria used to include or exclude your study population, in which case you'll need to combine information from multiple different variables. We can do this using the [`patients.satisfying()`](study-def-variables.md#cohortextractor.patients.satisfying) function.

For example, here we have combined both COPD and registration details to find only patients who have COPD and have been registered at a practice for more than a year.

```py
study = StudyDefinition(
    population=patients.satisfying(
        "has_follow_up AND has_copd",
        has_follow_up=patients.registered_with_one_practice_between(
            "2019-03-01", "2020-03-01"
        ),
        has_copd=patients.with_these_clinical_events(
            copd_codes, on_or_before="2017-03-01"
        ),
    ),
    ...
)
```

The first argument to `patients.satisfying()` is a string defining the population of interest using elementary logic syntax.
Acceptable operators in this string are currently `=`, `!=`, `<`, `<=`, `>=`, `>`, `AND`, `OR`, `NOT`, `+`, `-`, `*`, `/`.
All subsequent arguments are variable definitions. These are used just as you would use them in the higher-level `StudyDefinition()` call, except that there's no need to define `return_expectations` arguments since these variables are extracted explicitly.

If a variable has been defined elsewhere in `StudyDefinition()`, then that variable can be used in the `patients.satisfying()` function without needing to be defined again.
For example,

```py
study = StudyDefinition(
    population=patients.satisfying(
        'has_follow_up AND (sex = "M" OR sex = "F")',
        has_follow_up=patients.registered_with_one_practice_between(
            "2019-03-01", "2020-03-01"
        ),
    ),
    sex=patients.sex(
        return_expectations={
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
            "incidence": 1,
        }
    ),
)
```

Here `sex` is _defined_ outside of `patients.satisfying()` but can still be _used_ inside of it.
In this case, it's being used to exclude patients without a "valid" sex category (`"M"` or `"F"`) from the study population.
To match the `population` definition, the `return_expectations` for `sex` only includes `"M"` and `"F"` (not `U` or `I`, the other two valid values that can be returned by `patients.sex()`).


### Using a single variables to define your population

If your population is defined by just one variable, you can use this variable directly instead of passing it through `patients.satisfying()`.
For example,

```py
    population=patients.with_these_clinical_events(
        copd_codes, on_or_before="2017-03-01",
    )
```

Again, there's no need here to use the `return_expectations` argument.

### Extracting data for all variables

Occasionally, it may be necessary to extract data for all patients available for analysis within the database. To do this, you can use

```py
    population=patients.all(),
```

Be aware that this will include a mix of registered, deregistered, and deceased patients.

### Dummy data versus real data

The `population=` argument has no bearing at all on the dummy data. It is just used to select patients in the real data.
If in the example above we had `"incidence" : 0.95`, then 5% of patients in the dummy data would have missing sex values, but 0% of patients in the real data would have missing sex values because they have been excluded with `population=`.
It's important therefore to match the dummy data with what you would expect to see _conditional on_ the chosen patient population, rather than in the data as a whole.

## Multiple study definitions

### File names

A study definition called `study_definition.py` will create a file called `input.csv`.
If you only require one study population, we recommend you stick with this.

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

You should then create two corresponding cohortextractor actions in the [`project.yaml`](actions-pipelines.md):

```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:

  generate_copd_cohort:
    run: cohortextractor:latest generate_cohort --study-definition study_definition_copd
    outputs:
      highly_sensitive:
        cohort: output/input_copd.csv

  generate_asthma_cohort:
    run: cohortextractor:latest generate_cohort --study-definition study_definition_asthma
    outputs:
      highly_sensitive:
        cohort: output/input_asthma.csv
```


### Parameterised study definitions

Parameterised study definitions allow you to create multiple study definitions that are structurally similar but differ in the values of a few parameters. This removes the need to create multiple similar study definition files.

First, set the relevant parameters in the action definition using the `--param` argument. For example, below we create two actions which use the same study definition but supply different values for `my_param`:

```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:

  generate_cohort_1:
    run: cohortextractor:latest generate_cohort
      --param my_param=value1
      --output-file output/input_1.csv
    outputs:
      highly_sensitive:
        cohort: output/input_1.csv

  generate_cohort_2:
    run: cohortextractor:latest generate_cohort
      --param my_param=value2
      --output-file output/input_1.csv
    outputs:
      highly_sensitive:
        cohort: output/input_2.csv
```

Note that each set of parameters requires a different output file name so we have to supply one using the `--output-file` argument.
This argument takes the full path of the output file which includes its output directory and the file extension which determines its format e.g.
```
--output-file output/results_1.feather
```

Inside `study_definition.py` you can access the values of parameters like so:
```py
from cohortextractor import params
...
my_param = params["my_param"]
```

Note that parameters are always supplied as strings. If you need to use other types such as integers or booleans you must explicitly convert them in Python e.g.
```py
my_int_param = int(params["my_int_param"])
my_bool_param = params["my_bool_param"] == "true"
```

Accessing parameters with the square bracket syntax above makes the parameters required: if you don't supply the appropriate `--param` arguments then the study defintion will fail with an error.

You can make parameters optional by using the `.get()` method and supplying a default e.g.
```py
my_param = params.get("my_param", "default_value")
```

You can use as many parameters as you like; just use the `--param` argument multiple times:
```
generate_cohort --param some_param=value1 --param other_param=value2 ...
```

If parameter values contain spaces you will need to quote them:
```
generate_cohort --param my_param='Value with spaces' ...
```

### Identical study definitions with different index dates
To parameterise index dates, there is a simpler alternative than using `--param`. Use the `--index-date-range` argument from the [measures](measures.md#extract-the-data) feature. `--index-date-range` can be given a single date, instead of a range.

We start by creating the study definition defining the variables you want to extract.
Then within the [`project.yaml`](actions-pipelines.md#projectyaml-format) we define two or more actions, one for each index date you want to use.
```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:

  generate_study_population_1:
    run: cohortextractor:latest generate_cohort --study-definition study_definition --index-date-range "2020-01-01"
    outputs:
      highly_sensitive:
        cohort: output/input-2020-01-01.csv

  generate_study_population_2:
    run: cohortextractor:latest generate_cohort --study-definition study_definition --index-date-range "2020-09-01"
    outputs:
      highly_sensitive:
        cohort: output/input-2020-09-01.csv
```
Currently the study definition called above must have the index date defined within the StudyDefinition (e.g. `index_date="2020-01-01"`), though the date defined is arbitrary and is replaced by the arguments defined above.

---8<-- 'includes/glossary.md'
