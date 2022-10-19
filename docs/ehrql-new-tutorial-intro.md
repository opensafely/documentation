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

Data Builder runs on Windows, macOS, and Linux.

##### Installing Data Builder

There are two ways that you can run Data Builder:

* With Python
* With the OpenSAFELY CLI

!!! todo
    Consider specifying the Data Builder version (currently `v0`) via a variable,
    so we don't have to maintain it in multiple places.

    * <https://github.com/rosscdh/mkdocs-markdownextradata-plugin>
    * <https://github.com/fralau/mkdocs_macros_plugin>

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
      `pip install git+https://github.com/opensafely-core/databuilder@main#egg=opensafely-databuilder`

    !!! warning
        At the moment, you will have to install the specific Data Builder version listed in the documentation repository at:

        `databuilder/requirements.prod.in`

        <https://github.com/opensafely/documentation/pull/959> should fix this.

    !!! todo

        Are we going to ever publish Data Builder to PyPI?

=== "OpenSAFELY CLI (not yet working)"

    !!! warning
        This does not yet work.
        We want to switch this to the OpenSAFELY CLI.

    This will be the simplest way to run Data Builder in future.

!!! todo

    Consider adding Gitpod or similar.

**Commands in this tutorial will assume you are running with Python.**

!!! todo
    Update this.

!!! note
    Before proceeding, make sure that you can run Data Builder's "help" command:

    ```
    databuilder --help
    ```

    If that command succeeds,
    you should see some help text
    and Data Builder should be correctly installed.

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
For example, a file named `patient_demographics.csv` is interpreted as the Data Builder `patient_demographics` table.

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
   databuilder generate-dataset "1a_minimal_dataset_definition.py" --dummy-tables "example-data/minimal/" --output "outputs.csv"
   ```
3. You should see Data Builder run without error
   and find the `outputs.csv` file in the `ehrql-tutorial-examples` directory
   that you were working in.

!!! tip

    In general, the command to run a dataset defintion looks like:

    ```
    databuilder generate-dataset "IDENTIFIER_DATASOURCENAME_dataset_definition.py --dummy-tables "example-data/DATASOURCENAME/" --output "outputs.csv"
    ```

    You need to substitute `DATASOURCENAME` with the appropriate dataset name,
    and `IDENTIFIER_DATASOURCENAME_dataset_definition.py` to match the specific dataset definition
    that you want to run.

!!! tip

    The output in this example is called `outputs.csv`,
    but you can choose any valid filename.
