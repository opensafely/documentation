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


There is no requirement for approval or access to OpenSAFELY to follow this tutorial.
This tutorial uses artificial data throughout.

This tutorial assumes that you have some familiarity with
programming or scripted data analysis, whether that is in Python, R,
Stata or any other language.

Familiarity with:

* OpenSAFELY
* How [electronic healthcare records are structured](data-sources/intro.md)

would also be helpful,
but is *not* essential.

## How to work through this tutorial series
The tutorial is split into 7 sections that we recommend
you work through sequentially. Each section builds on previous knowledge. Throughout the tutorial series, you will see optional explanations and reading, that you might 
want to explore at the time or afterwards.

We recommend that you work through the tutorial by installing Data Builder, downloading the sample code, and 
running the code on your machine. 

### Learning objectives
This tutorial series will introduce you to writing and running 
ehrQL queries with Data Builder. 

By the end of the tutorials, you will be able:

* to install Data Builder
* to write a dataset definition in ehrQL
* to run a dataset definition with Data Builder
* to use electronic health record codelists in ehrQL
* to perform queries via selecting, filtering and aggregation

Each tutorial section will have its own learning objectives. 

## Installation 

To try running or modifying the examples in this tutorial,
you will need to install Data Builder and have a text 
editor. 

### Installing Data Builder

Data Builder runs on Windows, macOS, and Linux either via:

* the OpenSAFELY CLI (recommended)
* a manually installed Python package


#### OpenSAFELY CLI
The [OpenSAFELY CLI](opensafely-cli.md) requires a working Docker installation.
If you do not already have the OpenSAFELY CLI installed,
refer to the [instructions](opensafely-cli.md).
Once you have the OpenSAFELY CLI installed,
you are ready to use Data Builder.

#### Install via Python 
If you are unable to install Docker,
you can try Data Builder via Python.

A Python package install will still allow you to follow this tutorial,
but will not allow you to run full OpenSAFELY projects.

We will not cover the Python installation here.
Refer to the [separate page](ehrql-new-tutorial-python.md) on this.

### Text editor

You can edit dataset definitions in any text editor.

You may find it useful to use a text editor or integrated development environment
that supports Python syntax.

If you have no preference already,
[Visual Studio Code](https://code.visualstudio.com) is a reasonable, free-of-charge choice
that runs on Windows, macOS and Linux.

## How to download the tutorial code and data

Throughout this tutorial,
we will refer to code examples.

These examples are available for you
to run and to experiment with.

When working through each tutorial,
you may find it useful to open the relevant dataset definition and example CSV data in a text editor,
to refer along with.

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

## How to run the tutorial code
There are two ways to run the tutorial code:

1. Run the code directly using `opensafely exec`
2. Run the code via `project.yaml` file (this is how real 
OpenSAFELY projects get run)

### Run using `opensafely exec`
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

### Run via `project.yaml`
Each OpenSAFELY project has a `project.yaml` (see projects), where actions are defined. The `project.yaml`
file is run via the `opensafely run` command. 

For this tutorial, we have already defined individual actions in the `project.yaml` for each example, for convenience. 

To run this dataset definition with Data Builder: 

1. In a terminal, enter the `ehrql-tutorial-examples` directory that you extracted from the sample data.

2. Run this command:
   ```
   opensafely run extract_1a_minimal_population
   ```

3. The OpenSAFELY CLI now runs and should complete without error. This command runs the appropriate *action* in the `project.yaml` file.

4. You should be able to find the relevant output file in the `ehrql-tutorial-examples` directory that you were working in.
   The filename of the output is also specified in the `project.yaml`.

!!! tip

    In general, the command to run a dataset defintion looks like:

    ```
    opensafely run extract_IDENTIFIER_DATASOURCENAME_population
    ```

    You need to substitute `IDENTIFIER` with the appopriate dataset definition identifier and `DATASOURCENAME` with the appropriate data source name.
