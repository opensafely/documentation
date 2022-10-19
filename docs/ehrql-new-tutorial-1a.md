# ehrQL tutorial: A minimal dataset definition

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 1a: A minimal dataset definition

### Learning objectives

By the end of this tutorial, you should know how to:

* Write a very simple dataset definition
* Run that dataset definition with Data Builder

### The dataset definition we will work with

This is a minimal, but still valid, dataset definition:

!!! todo

    May need to fix up how this code is included.
    Can we have code annotations?
    What's the best way of jumping between input, output and dataset
    definition? Maybe that's a case for having one example per tutorial
    page?

???+ example "Dataset definition: `1a_minimal_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/1a_minimal_dataset_definition.py"
    ```

It finds the patients whose year of birth is 2000 or later.

### The `minimal` data source

???+ example "Data table: `minimal/patient_demographics.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/minimal/patient_demographics.csv') }}

### Dataset definition 1a output

!!! todo

    Do we need to clarify that the filename corresponds to the outputs already created?
    And that you'll overwrite these if you use this as a filename?

???+ example "Output dataset: `outputs/1a_minimal_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1a_minimal_dataset_definition.csv') }}

### Explanation of the dataset definition

#### Specify the Data Builder components in use with `import` statements

Lines of the format `from… import…` specify which of Data Builder's code and features
to use in our dataset definition.
Here, we import two components of Data Builder:

* `Dataset` as provided by the query language, to create a dataset
* the `patient_demographics` table, which is one of several data tables that ehrQL gives access to

!!! todo

    Consider using snippets or code annotations instead of copy-pasting lines.

!!! warning
    For the purposes of the tutorial,
    we are accessing tables from `databuilder.tables.examples.tutorial`.

    Different backends support access to different tables.
    To access tables on real backends,
    refer to the [Contracts reference](contracts-reference.md)
    (to be renamed)
    to look up the correct import statement
    that specifies the backend and table name.

#### Give names to values using Python's assignment operator, `=`

Like in many other languages,
the `=` operator is used to assign a *value*, on the right-hand side,
to a *name*, on the left-hand side.

#### Create a `Dataset`

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

!!! warning

    Likewise, if you accidentally include multiple calls to `set_population()`,
    it is the call that appears closest to the end of the dataset definition
    that takes effect.

    In future, calling `set_population()` more than once will cause a dataset definition to fail;
    see the associated [Data Builder](https://github.com/opensafely-core/databuilder/issues/775) issue.

!!! todo

    Would it be simpler here to say:
    "you probably should only have one dataset".
    Are there cases where you might need multiple datasets within a definition?

!!! todo

    Consider using code annotations to describe the code.

#### What happens when Data Builder generates a dataset?

When the dataset definition is used by Data Builder to generate a dataset:

1. The dataset definition is validated
   to ensure that the resulting database query would be valid.
2. A database query suitable for the specified database is created.
3. The query is submitted to the database.
4. Provided the query is successful, the query creates an output.

In writing a *dataset definition* then,
what we are really writing is a *database query*.
Data Builder transforms the dataset definition into the appropriate database query,
for the specific database.

!!! note

    You can see the database query that a dataset definition will generate
    via the `databuilder --dump-dataset-sql` command.

    For the minimal example `1a_minimal_dataset_definition.py` above,
    the underlying SQL query generated is:

    ```sql
    SELECT patient_demographics.patient_id AS patient_id
    FROM patient_demographics
    WHERE CAST(STRFTIME('%Y', patient_demographics.date_of_birth) AS INTEGER) >= 2000;
    ```

    !!! todo

        This SQL should be kept updated.

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
