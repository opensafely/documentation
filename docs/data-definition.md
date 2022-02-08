---8<-- 'includes/data-builder-danger-header.md'

## What is a Data Definition?

A _data definition_ is a formal specification of the data that you want to extract from the OpenSAFELY database. This includes:

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

The OpenSAFELY framework uses a single data definition to query different
vendor EHR databases, and saves the results to the secure server in a CSV file
of tabular data.

A data definition also allows a researcher to define the shape of the values they *expect* to get back from the vendor data.
This allows the framework to generate dummy data which the researcher can use to develop and test their analysis scripts, without ever having to touch real patient data.

When you generate a data population, the framework reads your data definition from the python script (usually `analysis/data_definition.py`), and writes the output data frame in a tabular CSV file (usually `output/input.csv`).
In a production environment this file will contain real data; in a development environment this will be dummy data.

Currently the framework supports one row per patient datasets.

## `data_definition.py` structure

### Importing code building blocks

To create the data definition, we first need to import the functions and code to create this.
You will need to put this codeblock at the top of your python file.

--8<-- 'examples/src-imports.md'

This essentially says we want to import some functions from the `databuilder` package which will be used throughout the script.

### A simple example

The `Cohort()` class (imported above) is used to define both the data population and the variables.

--8<-- 'examples/src-data-definition.md'


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
