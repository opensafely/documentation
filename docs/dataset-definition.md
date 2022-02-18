# Writing a dataset definition

---8<-- 'includes/data-builder-danger-header.md'

## What is a dataset definition?

A _dataset definition_ is a formal specification of the data that you want to extract from the OpenSAFELY database. This includes:

* the patient population (dataset rows)
* the variables (dataset columns)

The OpenSAFELY framework:

* Uses a single dataset definition to query different vendor-specific EHR databases or locally provided dummy data.
* Reads your dataset definition from the Python script (usually `analysis/dataset_definition.py`)
* Writes the output data frame in a tabular CSV file (usually `output/input.csv`).
    * For queries to vendor databases, the results are stored on a [secure server](releasing-files.md).

!!! note
    Currently the framework only supports datasets with one row per patient.

### Dataset definitions are written in ehrQL

Dataset definitions are written in a language designed for OpenSAFELY:
ehrQL. ehrQL runs on Python, but ehrQL is designed to be easily written,
read, and reviewed by anyone with some epidemiological knowledge.

A simple example of a dataset definition is given below.

!!! note
    Other documentation pages discuss [ehrQL in more depth](ehrql-intro.md).

## `dataset_definition.py` structure

Before writing a dataset definition, add [Data
Builder](data-builder-intro/#adding-data-builder-to-a-project) to your
OpenSAFELY project.

### Importing code building blocks

At the start of the dataset definition, we first *import* some code from
the Data Builder package. Put the following codeblock at the top of your
`dataset_definition.py` file:

--8<-- 'examples/src-imports.md'

!!! note
    This is a simple example. You may need different imports depending
    on your dataset definition.

### A simple example

The `Cohort()` class (imported above) is used to define both the data population and the variables.

--8<-- 'examples/src-dataset-definition.md'

---8<-- 'includes/glossary.md'
