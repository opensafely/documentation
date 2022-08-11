# ehrQL tutorial

---8<-- 'includes/data-builder-danger-header.md'

## Audience

This tutorial is aimed at:

* **new users of Data Builder**
  who wish to write dataset definitions
  to extract data from OpenSAFELY backends
* **developers involved in operating data backends**
  who wish to understand more about how OpenSAFELY backends
  are accessed by users

!!! tip
    There is no requirement for approval or access to OpenSAFELY to follow this tutorial.
    This tutorial uses artificial data throughout.

## What this tutorial covers: writing and running ehrQL queries with Data Builder

ehrQL is a query language for electronic health records.
The [introduction to ehrQL](ehrql-intro.md) has more information.

Data Builder is a program that takes ehrQL queries,
converts them to underlying database queries
and submits them to OpenSAFELY backends.
The [introduction to Data Builder](data-builder-intro) has more information.

This tutorial will introduce you to:

* writing a dataset definition in ehrQL
* running that dataset definition with Data Builder

### Requirements

#### Background knowledge

The current implementation of ehrQL is based on Python,
but the syntax used is relatively simple.

This tutorial assumes that you have a little familiarity with:

* programming or scripted data analysis,
  whether that is in Python, R, Stata or any other language.
* querying databases or other data stores

Familiarity with:

* OpenSAFELY
* How [electronic healthcare records are structured](data-sources/intro.md)

would also be helpful,
but is *not* essential.

#### Software requirements

To try running or modifying the examples in this tutorial,
you will need to install Data Builder.

##### Operating system

Data Builder runs on Windows, macOS, and Linux.

##### Installing Data Builder

We suggest two ways of getting Data Builder running.

=== "Docker (recommended)"

    This is the simplest way to run Data Builder.

    If you do not have Docker installed,
    refer to our [installation guides](install-intro.md) for guidance.

    !!! todo

        Test if running from Docker works for example CSVs.

=== "Python (for confident Python users)"

    If you are unable to run Data Builder via Docker,
    you can try installing Data Builder directly using Python.

    As Python configurations vary between operating systems,
    and how users have Python configured,
    we will not give detailed instructions.

    You will need to:

    * have a suitable Python version installed (currently Python 3.9)
    * configure a suitable virtual environment to run Data Builder
      for example with `conda` or `venv`
    * install the Data Builder package into that virtual environment;
      currently you will have to do something like:
      `pip install git+https://github.com/opensafely-core/databuilder@main#egg=databuilder`

    !!! todo

        Are we going to ever publish Data Builder to PyPI?

    !!! important
        **Commands listed in this tutorial are given for the Docker installation.**

        To make those commands work with Python, replace the start of any command:

        ```
        docker run --rm ghcr.io/opensafely-core/databuilder:v0
        ```

        with:

        ```
        databuilder
        ```

        For example,

        ```
        docker run --rm ghcr.io/opensafely-core/databuilder:v0 --help
        ```

        becomes:

        ```
        databuilder --help
        ```

!!! todo

    Consider adding Gitpod or similar.

**Commands in this tutorial will assume you are running Docker.**

##### Text editor

You can edit examples in any text editor.

You may find it useful to use a text editor or integrated development environment
that supports Python syntax.

If you have no preference already,
[Visual Studio Code](https://code.visualstudio.com) is a reasonable, free-of-charge choice
that runs on Windows, macOS and Linux.

## Running the tutorial code examples

### Downloading the tutorial examples

!!! todo

    Consider improving this process.

1. Download the [documentation source code](https://github.com/opensafely/documentation/archive/refs/heads/main.zip)
   that contains these examples.
2. Open the `.zip` file.
3. Extract the `databuilder/ehrql-tutorial-examples` somewhere.
4. You will need to navigate to the directory that you extracted
   when working in a terminal.

### Running the sample data

!!! todo

    Explain how to load that sample data.

    This is probably just running the initial dataset definition.

## A minimal dataset definition

We provide Data Builder with a dataset definition to extract data from an OpenSAFELY backend.

This is a minimal, but still valid, dataset definition:

!!! todo

    May need to fix up how this code is included.

```python
---8<-- "databuilder/ehrql-tutorial-examples/1_minimal_dataset_definition.py"
```

### Explanation of the dataset definition

#### Use `import` to use Data Builder components

Lines of the format `from… import…` specify which of Data Builder's code and features
to use in our dataset definition.
Here, we import two components of Data Builder:

* `Dataset` as provided by the query language, to create a dataset
* the `patients` table, which is one of several data tables that ehrQL gives access to

#### Creating a `Dataset`

A valid dataset definition must contain a dataset assigned to the name `dataset`.

A usual first step in writing a dataset definition is to create this empty dataset.
In subsequent steps,
we specify the data from the available data tables
that we wish to add to the dataset.

!!! warning

    The dataset used as the basis of an ehrQL query
    is the dataset that is last to be given the name `dataset`.

    A simple way to make your dataset definition clear is to
    only use the name `dataset` for the query's dataset.

!!! todo

    Would it be simpler here to say:
    "you probably should only have one dataset".
    Are there cases where you might need multiple datasets within a definition?

!!! todo

    Consider using code annotations to describe the code.

### Running the dataset definition

!!! todo

    Complete this section.

    The instructions should:

    * specify sample data
    * show the expected output
    * specify how to run the sample data against Data Builder

#### What happens when Data Builder generates a dataset?

When the dataset definition is used by Data Builder to generate a dataset:

1. The dataset definition is validated
   to ensure that the resulting database query would be valid.
2. A database query suitable for the specified database is created.
3. The query is submitted to the database.
4. Provided the query is successful, the results are output.

In writing a *dataset definition* then,
what we are really writing is a *database query*.
Data Builder transforms the dataset definition into the appropriate database query,
for the specific database.

!!! note

    You can see the database query that a dataset definition will generate
    via `databuilder --dump-dataset-sql`.

That database might be:

* a local database used for testing,
  such as in this tutorial
* an OpenSAFELY backend,
  when submitting jobs to OpenSAFELY

There are two important implications of how this Data Builder's process works:

1. **Queries do not have to be written in a specific query language tailored to a specific database.**
   The compatibility of a dataset definition depends only
   on whether all the data tables used are available in the database being queried.
2. **All the data processing requested happens at the database
   after the dataset definition is processed in its entirety.**
   This is different from a more typical interactive data analysis in Python, Stata or R
   where you load some data,
   then perform computations on that data as each line of the analysis code runs.

## Ideas and concepts to include
