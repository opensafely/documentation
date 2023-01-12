# Writing a dataset definition

---8<-- 'includes/data-builder-danger-header.md'

## How is a dataset constructed?
The OpenSAFELY framework:

* Uses a single dataset definition to query different vendor-specific EHR databases or locally provided dummy data.
* Reads your dataset definition from the Python script (usually `analysis/dataset_definition.py`)
* Writes the output data frame in a tabular CSV file (usually `output/input.csv`).
    * For queries to vendor databases, the results are stored on a [secure server](../releasing-files.md).


## What is a dataset definition?

A _dataset definition_ is a formal specification of the data that you want to extract from the OpenSAFELY database. This includes:

* the patient population (dataset rows)
* the variables (dataset columns)

It is written in [ehrQL](ehrql/index.md). Dataset definitions are written in a language designed for OpenSAFELY:
ehrQL. ehrQL runs on Python, but ehrQL is designed to be easily written,
read, and reviewed by anyone with some epidemiological knowledge.

## `dataset_definition.py` structure

Before writing a dataset definition, add [Data
Builder](index.md#adding-data-builder-to-a-project) to your
OpenSAFELY project.

### Importing code building blocks

At the start of the dataset definition, we first *import* some code from
the Data Builder package. Put the following codeblock at the top of your
`dataset_definition.py` file:

```python
--8<-- 'databuilder/snippets/dsl.py:imports'
```

!!! note
    This is a simple example. You may need different imports depending
    on your dataset definition.

### A simple example

The `Cohort()` class (imported above) is used to define both the data population and the variables.

```python
--8<-- 'databuilder/snippets/dsl.py:datasetdefinition'
```

## How do Dataset definitions work?
1. **Dataset** is defined in the dataset definition
2. **Query transformation**: The researcher then loads that dataset
   definition into Data Builder. Provided the dataset definition is valid, Data Builder transforms
   the dataset definition into an internal representation of the query called the *query model*.
3. **Query submission**: Data Builder then translates the query model
   into the appropriate query language for the data backend being
   accessed. This means that the same dataset definition can be run against
   multiple backends which may have different structures or underlying software.

For a more indepth technical explanation of how this works, see [explaining the query engine](query-engine-explanation.md).

---8<-- 'includes/glossary.md'
