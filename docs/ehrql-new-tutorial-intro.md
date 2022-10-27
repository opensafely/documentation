# ehrQL tutorial

---8<-- 'includes/data-builder-danger-header.md'

## Table of contents

!!! todo

    Remove this.

    We should incorporate this as a full part of the documentation,
    so that it is easy to discover and follow on to the next page.

    This will be when this documentation is ready
    (or close to ready)
    for public use.

* [Introduction (this page)](ehrql-new-tutorial-intro.md)
* [Dataset definition 1a](ehrql-new-tutorial-1a.md)
* [Dataset definition 1b](ehrql-new-tutorial-1b.md)
* [Dataset definition 2a](ehrql-new-tutorial-2a.md)
* [Dataset definition 3a](ehrql-new-tutorial-3a.md)
* [Dataset definition 4a](ehrql-new-tutorial-4a.md)
* [Dataset definition 5a](ehrql-new-tutorial-5a.md)
* [Dataset definition 6a](ehrql-new-tutorial-6a.md)
* [Dataset definition 7a](ehrql-new-tutorial-7a.md)
* [Using ehrQL and Data Builder in an OpenSAFELY project](ehrql-new-tutorial-opensafely-project.md)
* [Conclusion](ehrql-new-tutorial-conclusion.md)

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

Data Builder is software that takes ehrQL queries,
converts them to underlying database queries
and submits them to OpenSAFELY backends.
The [introduction to Data Builder](data-builder-intro.md) has more information.

### Overall learning objectives

This tutorial will introduce you to:

* installing Data Builder
* writing a dataset definition in ehrQL
* running that dataset definition with Data Builder
* using electronic health record codelists in ehrQL
* performing queries via selecting, filtering and aggregation

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

Data Builder runs on Windows, macOS, and Linux either via:

* the OpenSAFELY CLI
* a manually installed Python package

##### Text editor

You can edit dataset definitions in any text editor.

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

#### Installing Data Builder

There are two ways that you can run Data Builder:

* Via the OpenSAFELY CLI (**recommended**)
* Via a Python package

!!! todo

    Consider adding Gitpod or similar.

The [OpenSAFELY CLI](opensafely-cli.md) requires a working Docker installation.
If you do not already have the OpenSAFELY CLI installed,
refer to the [instructions](opensafely-cli.md).
Once you have the OpenSAFELY CLI installed,
you are ready to use Data Builder.

If you are unable to install Docker,
you can try Data Builder via Python.

A Python package install will still allow you to follow this tutorial,
but will not allow you to run full OpenSAFELY projects.

!!! note
    We will not cover the Python installation here.
    Refer to the [separate page](ehrql-new-tutorial-python.md) on this.

!!! todo
    Consider specifying the Data Builder version (currently `v0`) via a variable,
    so we don't have to maintain it in multiple places.

    * <https://github.com/rosscdh/mkdocs-markdownextradata-plugin>
    * <https://github.com/fralau/mkdocs_macros_plugin>

**Commands in this tutorial will assume you are running with the OpenSAFELY CLI.**

## Running the tutorial code examples

Throughout this tutorial,
we will refer to code examples.

These examples are available for you
to run and to experiment with.

When working through each tutorial,
you may find it useful to open the relevant dataset definition and example CSV data in a text editor,
to refer along with.

### Learning objectives

By the end of this section, you should be able to:

* Run an existing dataset definition with Data Builder

### Downloading the tutorial examples

!!! todo

    Consider improving this process.

1. Download the [documentation source code](https://github.com/opensafely/documentation/archive/refs/heads/main.zip)
   that contains these examples.
2. Open the `.zip` file.
3. Extract the `databuilder/ehrql-tutorial-examples` somewhere.
4. In the `ehrql-tutorial-examples` directory that you extracted,
   delete the `outputs` directory.
   This contains outputs that have been generated already for the dataset definitions.
   We will regenerate these throughout this tutorial.
4. Navigate to the `ehrql-tutorial-examples` directory that you extracted
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

#### The OpenSAFELY CLI

With the OpenSAFELY CLI,
there are currently two ways of running the tutorial dataset definitions:

* `opensafely exec` where the Data Builder configuration is specified at the command line
* `opensafely run` where the Data Builder configuration is specified in the `project.yaml` file provided in `ehrql-tutorial-examples`

We explain both of these below.

!!! important
    You only need to use one of these two ways,
    though you are welcome to try both.
    We will likely favour the `opensafely exec` route
    for the tutorial in future
    and relegate the use of `project.yaml` to the tutorial page that discusses `project.yaml`.

    We are awaiting the improvements in
    <https://github.com/opensafely-core/opensafely-cli/issues/149>
    before doing so.

#### Using the OpenSAFELY CLI to run a dataset definition via `opensafely exec`

!!! warning
    This requires:
    * OpenSAFELY CLI version v1.32.1 or later
      (run `opensafely upgrade` to upgrade)
    * Data Builder Docker image v0.57.0 or later
      (run `opensafely pull` to update if you already have

!!! warning
    If you have installed with Python,
    see the [relevant guide](ehrql-new-tutorial-python.md)
    instead of following this section.

!!! todo
    Below paragraph is a near duplication of the Python page.
    Consider moving out into a shared Markdown source file.

This section explains how to load dataset definitions into Data Builder.

Each dataset definition used in this tutorial has a filename of the form:

```
IDENTIFIER_DATASOURCENAME_dataset_definition.py
```

For example, for

```
1a_minimal_dataset_definition.py
```

the identifier is `1a` and the data source name is `minimal`.
The identifier associates the dataset definition with a specific tutorial page.

!!! todo

    Check how compatible this is cross-platform.

To run this dataset definition with Data Builder,

1. In a terminal, enter the `ehrql-tutorial-examples` directory that you extracted
   from the sample data.
2. Run this command:

   ```
   opensafely exec databuilder:v0 generate-dataset "1a_minimal_dataset_definition.py" --dummy-tables "example-data/minimal/" --output "outputs.csv"
   ```
3. You should see Data Builder run without error
   and find the `outputs.csv` file in the `ehrql-tutorial-examples` directory
   that you were working in.

!!! tip

    In general, the command to run a dataset defintion looks like:

    ```
    opensafely exec databuilder:v0 generate-dataset "IDENTIFIER_DATASOURCENAME_dataset_definition.py --dummy-tables "example-data/DATASOURCENAME/" --output "outputs.csv"
    ```

    You need to substitute `DATASOURCENAME` with the appropriate dataset name,
    and `IDENTIFIER_DATASOURCENAME_dataset_definition.py` to match the specific dataset definition
    that you want to run.

!!! tip

    The output in this example is called `outputs.csv`,
    but you can choose any valid filename.

#### Using the OpenSAFELY CLI to run a dataset definition via `project.yaml`

!!! warning
    If you have installed with Python,
    see the [relevant guide](ehrql-new-tutorial-python.md)
    instead of following this section.

!!! todo
    Below paragraph is a duplication of the Python page.
    Consider moving out into a shared Markdown source file.

This section explains how to load dataset definitions into Data Builder.

Each dataset definition used in this tutorial has a filename of the form:

```
IDENTIFIER_DATASOURCENAME_dataset_definition.py
```

For example, for

```
1a_minimal_dataset_definition.py
```

the identifier is `1a` and the data source name is `minimal`.
The identifier associates the dataset definition with a specific tutorial page.

To run this dataset definition with Data Builder,

1. In a terminal, enter the `ehrql-tutorial-examples` directory that you extracted
   from the sample data.
2. Run this command:

   ```
   opensafely run extract_1a_minimal_population
   ```
3. The OpenSAFELY CLI now runs and should complete without error.
   This command runs the appropriate *action* in the `project.yaml` file.
   For this tutorial, we have already defined individual actions in the `project.yaml`
   for each example, for convenience.
4. You should be able to find the relevant output file in the `ehrql-tutorial-examples` directory that you were working in.
   The filename of the output is also specified in the `project.yaml`.

!!! tip

    In general, the command to run a dataset defintion looks like:

    ```
    opensafely run extract_IDENTIFIER_DATASOURCENAME_population
    ```

    You need to substitute `IDENTIFIER` with the appopriate dataset definition identifier and `DATASOURCENAME` with the appropriate data source name.
