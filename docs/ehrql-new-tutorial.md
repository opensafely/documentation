# ehrQL tutorial

---8<-- 'includes/data-builder-danger-header.md'

!!! todo
    Consider whether we want to break this up into multiple pages
    to make it less intimidating.

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

This tutorial assumes that you have some familiarity with
programming or scripted data analysis, whether that is in Python, R,
Stata or any other language.

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

        You may also need to adjust file paths; check this.

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

!!! tip
    Because dataset definitions are Python files,
    you can use auxiliary developer tools to keep the files tidy.

    For instance, the dataset definitions in this tutorial are checked with the following tools:

    * [black](https://github.com/psf/black), to format dataset definitions automatically
    * [flake8](https://github.com/PyCQA/flake8), to suggest coding style improvements
    * [isort](https://github.com/PyCQA/isort), to order `import` statements consistently

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

### Loading a dataset definition into Data Builder

#### CSV data

Typically, we provide Data Builder with a dataset definition
to extract data from an OpenSAFELY backend.

To simplify the examples in this tutorial,
we will instead specify a directory of CSV files
that contain artificial data,
and query that data instead of a backend.

Each CSV represents a database table.
Data Builder's CSV loader uses the filename of the CSV
to determine which Data Builder table it represents.
For example, a file named `patients.csv` is interpreted as the Data Builder `patients` table.

!!! todo
    Add information about loading CSVs elsewhere.

#### Using Data Builder's command-line interface

This section explains how to load dataset definitions into Databuilder.

Each dataset definition used in this tutorial has a filename of the form:

```
IDENTIFIER_DATASOURCENAME_dataset_definition.py
```

For example, for

```
1a_minimal_dataset_definition.py
```

the identifier is `1a` and the data source name is `minimal`.

!!! todo

    Check how compatible this is cross-platform.

To run this dataset definition with Data Builder,

1. In a terminal, enter the `ehrql-tutorial-examples` directory that you extracted
   from the sample data.
2. Run this command:

   ```
   docker run --rm ghcr.io/opensafely-core/databuilder:v0 --env DATABASE_URL "example-data/minimal/" generate-dataset "./1a_minimal_dataset_definition.py --output "outputs.csv"
   ```
3. You should see Data Builder run without error
   and find the `outputs.csv` file in the `ehrql-tutorial-examples` directory
   that you were working in.

!!! tip

    In general, the Docker command to run a dataset defintion looks like:

    ```
    docker run --rm ghcr.io/opensafely-core/databuilder:v0 --env DATABASE_URL "example-data/DATASOURCENAME/" generate-dataset "./IDENTIFIER_DATASOURCENAME_dataset_definition.py --output "outputs.csv"
    ```

    You need to substitute `DATASOURCENAME` with the appropriate dataset name,
    and `IDENTIFIER_DATASOURCENAME_dataset_definition.py` to match the specific dataset definition
    that you want to run.

!!! tip

    The output in this example is called `outputs.csv`,
    but you can choose any valid filename.

## Example dataset definition 1a: A minimal dataset definition

This is a minimal, but still valid, dataset definition:

!!! todo

    May need to fix up how this code is included.
    Can we have code annotations?
    What's the best way of jumping between input, output and dataset
    definition? Maybe that's a case for having one example per tutorial
    page?

```python title="1a_minimal_dataset_definition.py"
---8<-- "databuilder/ehrql-tutorial-examples/1a_minimal_dataset_definition.py"
```

It finds the patients whose year of birth is 2000 or later.

### The `minimal` data source

`minimal/patients.csv`:

{{ read_csv('databuilder/ehrql-tutorial-examples/example-data/minimal/patients.csv') }}

### Dataset definition 1a output

!!! todo

    Do we need to clarify that the filename corresponds to the outputs already created?
    And that you'll overwrite these if you use this as a filename?

`outputs/1a_minimal_dataset_definition.csv`

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1a_minimal_dataset_definition.csv') }}

### Explanation of the dataset definition

#### Specify the Data Builder components in use with `import` statements

Lines of the format `from… import…` specify which of Data Builder's code and features
to use in our dataset definition.
Here, we import two components of Data Builder:

* `Dataset` as provided by the query language, to create a dataset
* the `patients` table, which is one of several data tables that ehrQL gives access to

!!! todo

    Consider using snippets or code annotations instead of copy-pasting lines.

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
    SELECT patients.patient_id AS patient_id
    FROM patients
    WHERE CAST(STRFTIME('%Y', patients.date_of_birth) AS INTEGER) >= 2000;
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

## Example dataset definition 1b: Adding an extra output column from a minimal data source

This dataset definition uses the same [data source](#the-minimal-data-source).

```python title="1b_minimal_dataset_definition.py"
---8<-- "databuilder/ehrql-tutorial-examples/1b_minimal_dataset_definition.py"
```

The main addition here is the additional output column.

### Dataset definition 1b output

`outputs/1b_minimal_dataset_definition.csv`

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1b_minimal_dataset_definition.csv') }}

### Explanation of the dataset definition

This dataset definition is slightly modified from the previous example.

The difference is that an extra column, `sex` is added in the output.

We can see, logically, there are three stages to creating our dataset,
and we have split this dataset definition into these three logical stages.

1. Create an empty `Dataset()`
2. Specify that dataset's patient population of interest.
3. Add relevant columns.

!!! tip

    In the same way as you might use paragraphs to separate ideas in conventional writing,
    it can be useful to use vertical space in this way
    to help a reader of the code.

    (That reader may be your future self.)

#### Using the dot operator `.` to access attributes on values

In Python code,
like in many other languages,
the dot operator, `.`, appears frequently.

Generally, `.` is used when you want to access something
that is part of, or belongs to a value.

That "something" is typically either a data attribute (itself a value),
or a method (a function).

Here, the dot operator is used in several specific ways to:

* Identify which of the Python source files (modules) in Data Builder
  that we want to use via the `import` statement.
* Access the `.set_population()` method on the `Dataset` that we created.
* Access data from the `patients` tables.
* Set a column in the output via `dataset.column_name`

Sometimes that attribute accessed by dot notation may have useful attributes,
which can lead to "chaining" of the dot notation.
In this dataset definition example,
chained dot notation is used in `patients.date_of_birth.year`

#### `set_population()`

The `set_population()` method of a `Dataset` controls which patient rows will be included in the output.
It requires an argument to be passed to it.

This argument can be thought of as an expression or function
that can use data from one or multiple tables
and gives a true, false or missing result for any given patient.
Patients for which this argument evaluates to true are then included in the dataset.

!!! note
    Alternatively you could imagine creating a table
    which has each patient identifier in one column,
    and the result of this argument in another.
    The rows with a "true" result are then the patient identifiers
    included in the table.

    Data Builder does not actually create this intermediate table:
    it generates a single query that is submitted at the end.
    But this can be a useful way to imagine the process.

#### Tutorial exercises

!!! info

    These exercise sections are optional.
    They are prompts for you to practise writing your own ehrQL queries.

!!! question

    Can you modify the dataset definition so that the output shows:

    1. Patients that were born before 1980?
    2. Both `date_of_birth` and `sex` columns?
    3. `year_of_birth` instead of `date_of_birth`?

!!! todo

    Ways that we could polish this.

    1. We could:

        * provide known good outputs
        * provide a script for running Data Builder against the script
        * validate the outputs with pytest or similar

        The difficulty here is that, above,
        we invite people to use Docker to run Data Builder.
    2. Provide a solution in a dropdown,
       (and also test that solution).

## Example dataset definition 2: Working with multiple Data Builder tables

OpenSAFELY backends often provide data covering several healthcare domains.

### OpenSAFELY's data contracts

!!! todo

### The different data types

!!! todo

## Example dataset definition 3: `Frame`s and `Series`

### What `Frame`s and `Series` represent

!!! todo

### Operators on `Frame`s and `Series`

!!! todo

## Example dataset definition 4: Data special cases

### Date handling

!!! todo

### Missing values

!!! todo

## Example dataset definition 5: Codelists

### Loading a codelist

!!! todo

### Checking if a code is in a codelist

!!! todo

## Example dataset definition 6: Filtering and aggregation

### Filtering values

!!! todo

### Aggregating values

!!! todo

### Combining everything together

!!! todo

## Conclusion

!!! todo

    This should:

    * wrap up the tutorial
    * briefly summarise what has been covered
    * point to other information that a reader might want next

## Ideas and concepts to include

!!! todo

    Perhaps give some simple exercises for users to try to solve?
    Maybe with need to use the reference?

!!! todo

    Is there some way of templating the filenames for dataset definitions and CSVs?
    So that we have a single reference to update?
