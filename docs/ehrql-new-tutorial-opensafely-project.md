# Using Data Builder in an OpenSAFELY project

---8<-- 'includes/data-builder-danger-header.md'

!!! todo

    We should consider moving all the examples to be project based
    and covering some of the topics here earlier on.

## The relationship between Data Builder and OpenSAFELY projects

### Learning objectives

By the end of this tutorial, you should know how to:

* Create an OpenSAFELY project that uses Data Builder.
* Run that project to generate the dataset definition output.

### Running Data Builder via an OpenSAFELY project

So far in this tutorial,
we have run dataset definitions entirely via Data Builder.

This is fine for learning purposes in this tutorial.
However, to run against an OpenSAFELY backend,
we must create an OpenSAFELY project.

To create an OpenSAFELY project,
there are three steps:

1. Create the dataset definition,
   as we have already covered in these tutorial examples.
2. Create an OpenSAFELY project that uses Data Builder,
   by writing a `project.yaml` file.
3. Use the OpenSAFELY CLI to run that `project.yaml` file.

### Requirements

In addition to the previous requirements,
you will also need the [OpenSAFELY CLI](opensafely-cli.md) installed.

### The dataset definition we will work with

We will use a simple dataset definition that we have already seen.


???+ example "Dataset definition: `1a_minimal_dataset_definition.py`"

    ```python title="1a_minimal_dataset_definition.py"
    ---8<-- "databuilder/ehrql-tutorial-examples/1a_minimal_dataset_definition.py"
    ```

### The `minimal` data source

???+ example "Data table: `minimal/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/minimal/patients.csv') }}

### The `project.yaml`

!!! todo

    Make this work, and check that it works.
    It requires the OpenSAFELY CLI to be able to run the `project.yaml` correctly.
    It also requires the correct options adding to this YAML file.

A `project.yaml` file configures how analytic code is run for OpenSAFELY projects.

Using Data Builder in a `project.yaml` is much like working with other OpenSAFELY used by other OpenSAFELY actions.

???+ example "Project pipeline: `project.yaml`"

    ```yaml"
    ---8<-- "databuilder/ehrql-tutorial-examples/project.yaml"
    ```

### Running the `project.yaml`

!!! todo

    Add any extra details that are required.
    It may be that the `DATABASE_URL` or similar must be specified by environment variable.

Running a `project.yaml` which contains a Data Builder action
is much the same as for any other OpenSAFELY project.

Use [`opensafely run`](opensafely-cli.md/#run) to run the `project.yaml`:

1. In your terminal, change directory to where you have the example `project.yaml` file.
2. Run `opensafely run run_all`
3. The OpenSAFELY CLI should run Data Builder with the dataset definition
   and you should find the output in the relative path shown under `outputs` in the `project.yaml`.

### Tutorial exercises

!!! todo

    What is required to create a new OpenSAFELY project?
    Do you need a Git repository configured?

!!! question

    1. Can you create an OpenSAFELY project
       for one of the other dataset definitions we have covered in these tutorials?
    2. Try running that project
       and confirm that the outputs are the same
       as running the dataset definition directly with Data Builder.
