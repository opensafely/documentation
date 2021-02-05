## What is a Study Definition?

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

The OpenSAFELY framework case use a single study definition to query different
vendor EHR databases, and saves the results to the secure server in a CSV file
of tabular data.

A study definition also allows a researcher to define the shape of the values they *expect* to get back from the vendor data.
This allows the framework to generate dummy data which the researcher can use to develop and test their analysis scripts, without ever having to touch real patient data.

When you generate a study population from your study definition, the framework reads a study definition from the python script (usually `analysis/study_definition.py`), and writes the output data frame in a tabular CSV file (usually `output/input.csv`).
In a production environment this file will contain real data; in a development environment this will be dummy data.

Currently the framework supports one row per patient datasets.

## `study_definition.py` structure

### Importing code building blocks

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

This essentially says we want to import the some functions from the `cohortextractor` package which will be used throughout the script.

### A simple example

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
In this case, we expect event dates to be between `1970-01-01` and today's date, uniformly distributed in that period, and to be recorded for 20% of patients (returning empty `""` values otherwise).
See [Defining dummy data](#defining-dummy-data) for more details.
* `index_date=` is used to set the index date against which all other dates can be defined.
See [Defining time periods](#defining_time_periods) for more details on how the index date is used.
* `population=` is where the population is defined.
In this case, we want all patients available in the OpenSAFELY database and so we use the method `all()` to indicate this.
See the [study population section]() for more details on how to select a specific subset of patients in the OpenSAFELY database.

The `default_expectations`, `index_date`, and `population` arguments are reserved names within `StudyDefinition()`.
All other names are used to define the variables that will appear in the outputted dataset, using _variable extractor functions_ of the form `patients.function_name`.

`age=` is a simple example of an extractor function in use.
The `patients.age_as_of()` function returns the age of each patient as of the date provided (in this case the `index_date`).

All other variables are defined similarly.
To see the full list of currently available extractor functions, see [Study definition variables reference](study-def-variables.md).



## Codelists

For more information about how to create and edit codelists on the [OpenSAFELY Codelists](https://codelists.opensafely.org) website, see [Codelists](codelist-intro.md).

### Pulling Codelists into your Study Definition

Many functions for defining variables take *codelists* as arguments.
Codelists live as CSV files in the `codelists/` directory, and are loaded into variables like this:

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

### Combining codelists

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



## Defining time periods

### Index Dates

If you define an `index_date` on a study definition then everywhere that you might normally supply a date you can now supply a "date expression".

Here is a simple example:

```py
study = StudyDefinition(
    index_date = "2015-06-01",
    population = patients.with_these_clinical_events(
        copd_codes,
        between = [
            "first_day_of_year(index_date) - 2 years",
            "last_day_of_year(index_date)",
        ],
    ),
    age = patients.age_as_of("index_date"),
)
```

This can make it easier to change the index date of a study by making sure it is only defined in once place.

The simplest date expression is just `index_date`, which gets replaced by whatever the index date is set to.

It's also possible to apply various functions to the index date.
The available options (hopefully self-explanatory) are:

```py
first_day_of_month(index_date)
last_day_of_month(index_date)
first_day_of_year(index_date)
last_day_of_year(index_date)
```

Intervals of time can be added or subtracted from the index date (or from a function applied to the index date).
The available units are `year(s)`, `month(s)` and `day(s)`.
For example:

```py
index_date + 90 days
first_day_of_month(index_date) + 9 months
index_date - 1 year
```

Note that if the index date is 29 February and you add or subtract some number of years which doesn't lead to a leap year, then an error will be thrown.
An error will also be show if adding or subtracting months leads to a month with no equivalent day e.g. adding 1 month to 31 January to produce 31 February.

### Dynamic index dates

Index dates can also be dynamic, different for each patient based on another criteria, rather than a common fixed value. For example, we may want to define an index date by the first occurence of a positive test result. In this case we define the dynamic index date as a variable in the study definition, then refer to this variable name as the index date.
For example:

```py
study = StudyDefinition(
    first_pos_index_date = patients.with_test_result_in_sgss(
       pathogen="SARS-CoV-2",
       test_result="positive",
       find_first_match_in_period=True,
       returning="date",
       date_format="YYYY-MM-DD",
    
    age = patients.age_as_of("first_pos_index_date"),
)
```

Here the index date is defined as the first SARS-CoV-2 positive test result in SGSS, which will differ for each patient. The age variable is now defined relative to this dynamic date, i.e. age is age at the time of the positive SARS-CoV-2 test.

Where the dynamic index date is null, in this case when a patient doesn't have a positive test result, any variables that reference the dynamic date will take the null value for their variable type (0 for continuous variables; an empty string for string variables).

### Time periods

Most variable extractor functions have arguments for specifying the date range over which you want to retrieve information.
Most commonly this is `on_or_before=`, `on_or_after=`, or `between=` (see the [variable reference](study-def-variables.md) for full documentation).
You must use at most one.
If no option is given then it will use all dates (including possibly future dates).

As well as specifying dates explicitly with e.g., `on_or_before="2019-12-31"`, you can use the date expressions discussed above.


## Defining and extracting variables

All variables that you want to include in your dataset are declared within the `StudyDefinition()` function, using functions of the form `patients.function_name()`.

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
The meaning of these values will depend on the data source, and this should be documented in the [dataset documentation](dataset-intro.md).


### Variables that return value-date pairs

Some functions will produce two variables: a value and the corresponding date.
In this case, expectations for both the value and the date can be specified, for example as follows:

```py
sbp = patients.mean_recorded_value(
	systolic_blood_pressure_codes,
	on_most_recent_day_of_measurement = True,
	include_measurement_date = True,
	on_or_after = index_date,
	date_format = "YYYY-MM-DD",
	return_expectations = {
		"incidence" : 0.8,
		"float" : {"distribution": "normal", "mean": 110, "stddev": 20},
		"date" : {"earliest": index_date, "latest": "today"},
		"rate" : "uniform"
	},
)
```
This says that we expect the returned systolic blood pressure values to be normally distributed and available for 80% of patients, at dates between the `index_date` and `"today"`'s date. The date of the most recent measurement is distributed uniformly between those dates.


## Defining dummy data

Every variable in a study definition must have a `return_expectations` argument defined (with the exception of the `population` variable).
This defines the general shape or distribution of the variables in the dummy data used for developing the code.  It is currently relatively unsophisticated; each variable is generated independently of all others. This is sufficient for testing that it is possible to run your study from start to finish in most cases, but sometimes not. You can find (and contribute to!) discussions on improving the dummy data framework [here](https://github.com/opensafely/cohort-extractor/issues/221)

### Specifying default distributions

All variables use a default defined at the top of the study definition, with the `default_expectations` argument, as follows:

```py
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations = {
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
		"incidence": 0.5
    },
    ...

```

In this case, we are saying that:
* Events dates are expected to be distributed between 1900 and today, with exponentially-increasing frequenc, with events occurring for 50% of patients.
* Values for binary variables are expected to be positive 50% of the time.
* Values for categorical variables are expected to be present (i.e., non-missing) 50% of the time.
* Values for numeric variables are expected to be present (i.e., non-missing) 50% of the time.

### Specifying variable-specific distributions
If the defaults need to be overridden, then use the `return_expectations` argument within the variable extractor function, for example as follows:

```py
    copd = patients.with_these_clinical_events(
		copd_codes,
		returning = "binary_flag",
		find_first_match_in_period = True,
		between = [index_date, "today"],
		return_expectations = {"incidence": 0.2},
    ),
```
This overrides the 50% default incidence for the binary variable `copd` to be 20% instead.


### All options
The following options are currently available for dummy data:

**integers**

* `{"int" : {"distribution": "normal", "mean": 25, "stddev": 5}, "incidence" : 0.5}`
* `{"int" : {"distribution": "population_ages"}, "incidence" : 1}`

**numeric**

* `{"float" : {"distribution": "normal", "mean": 25, "stddev": 5}, "incidence" : 0.75}`

**binary**

* `{"incidence": 0.33}`

**categorical**

* `{"category": {"ratios": {"cat1": 0.1, "cat2": 0.2, "cat3": 0.7}}, "incidence" : 1}`

**date**

*	`{"date": {"earliest": "1900-01-01", "latest": "today"}, "rate" : "exponential_increase"}`
*	`{"date": {"earliest": "1900-01-01", "latest": "today"}, "rate" : "uniform"}`

Note that `"incidence"` is used either for the actual incidence of a binary variable (`returning="binary_flag"`), or to indicate non-missingness for other variable types.
`"rate"` is used for the distribution of date values (with either `"exponential_increase"` or `"uniform"`), but can also be used as an alias for `incidence=1` by specifying `rate="universal"` for non-date values.

`population_ages` samples from the distribution of ages in the UK taken from [the Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/tablea21principalprojectionukpopulationinagegroups).

## Defining study populations

Most commonly, you will want to include only patients with certain characteristics, rather than every patient in the database.

### Using variables to define your population

To define a study population with one particular characteristic, you need to define the characteristic within the study
population.

```py
population = patients.with_these_clinical_events(
    copd_codes,
    on_or_before = "2017-03-01",
)
```

### Using time registered in one practice

Researchers often want to exclude patients who have switched practice recently and hence may have an incomplete record of their conditions as it can take some time for their records to come from their previous practice.

```py
population = patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
)
```

### Combining population criteria

Population criteria may need to be combined.
Here we have combined both COPD and registration details to find only patients who have COPD and have been registered at a practice for more than a year.

```py

population = patients.satisfying(
    "has_follow_up AND has_copd",
    has_copd=patients.with_these_clinical_events(
        copd_codes,
		on_or_before = "2017-03-01"
    ),
    has_follow_up = patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
)
```

If a variable has been defined elsewhere in `StudyDefinition()`, then that variable can be used in the `patients.satisfying()` function without needing to be defined again.
For example,

```py
study = StudyDefinition(
	population = patients.satisfying(
		"""
		has_follow_up AND
		(sex = "M" OR sex = "F")
		""",
		has_follow_up = patients.registered_with_one_practice_between(
			"2019-03-01", "2020-03-01"
		),
	)
	sex = patients.sex(
		"incidence" : 1,
		returning_expectations={"category": {"ratios": {"M": 0.49, "F": 0.51}}}
	),
)
```

Here `sex` is _defined_ outside of `patients.satisfying()` but can still be _used_ inside of it.
In this case, it's being used to exclude patients without a "valid" sex category (`"M"` or `"F"`) from the study population.

### Dummy data versus real data

The `population=` argument has no bearing at all on the dummy data. It is just used to select patients in the real data.
If in the example above we had `"incidence" : 0.95`, then 5% of patients in the dummy data would have missing sex values, but 0% of patients in the real data would have missing sex values because they have been excluded with `population=`.
It's important therefore to match the dummy data with what you would expect to see _conditional on_ the chosen patient population, rather than in the data as a whole.

## Multiple study definitions

### Naming

A `study_definition.py` will produce a file called `input.csv`.
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

You should reflect this by creating two cohortextractor actions in the [`project.yaml`](pipelines.md), one for each study definition:

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

### Sharing common study definition variables
When using multiple study definitions, there's often a lot of common variables between them, with just the population and maybe a couple of other variables that differ.
This means you have to separately specify the common variables in each definition, and it's easy to make an error, particularly when something needs changing.
To avoid this, there is a way to share these common variables between study definitions:


Make a file called `common_variables.py` containing the following code:

```py
from cohortextractor import patients

from codelists import *

```

You can then define your common variables in a dictionary (`dict`) rather than in a `StudyDefinition`.
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

### Define the specific study definitions

Within each `study_definition_*.py`, add the line `from common_variables import common_variables` near the top with the other imports.
You then add `**common_variables` just before the final closing brackets at the end of the file.
This approach can also use different index dates, that are then passed to variables in `common_variables.py`.

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
    # define the study index date
    index_date = "2020-01-01"

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
### Identical study definitions with different index dates
Though the `common_variables` approach described above can be used to make cohorts using different index dates, if you want two cohorts that are entirely identical except for the index date, we can do this more simply.
We start by using just one study definition, then within the [`project.yaml`](https://docs.opensafely.org/en/latest/pipelines/#projectyaml-format) we define two actions, one for each index date you want to use. We then borrow the `--index-date-range` argument from the [measures](https://docs.opensafely.org/en/latest/measures/#extract-the-data) function to specify the index dates:
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


---8<-- 'includes/glossary.md'
