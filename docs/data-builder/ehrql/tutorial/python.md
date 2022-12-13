# Installing Data Builder with Python

---8<-- 'includes/data-builder-danger-header.md'

!!! warning
    We recommend that you use Data Builder with the [OpenSAFELY CLI](opensafely-cli.md)
    as instructed in the [ehrQL tutorial](ehrql-new-tutorial-intro.md).

## Limitations

This option is a fall back if:

* you are a competent Python user,
* and you understand how to install Python packages yourself with `pip`

This installation option will allow you to run ehrQL dataset definitions only.
You will not be able to run a full OpenSAFELY project via a [`project.yaml` pipeline](actions-pipelines.md).

If you are unable to run Data Builder via Docker,
you can try installing Data Builder directly using Python.

As Python configurations vary between operating systems,
and how users have Python configured,
we will not give detailed instructions.

!!! warning
    This option may not work on Windows currently:
    <https://github.com/opensafely-core/databuilder/issues/790>

!!! todo
    Can we fix that issue?

## Requirements

You will need to:

* have a suitable Python version installed (currently Python 3.9)
* configure a suitable virtual environment to run Data Builder
  for example with `conda` or `venv`
* install the Data Builder package into that virtual environment;

## Installation

Install the latest version of Data Builder into your new virtual environment with `pip`

```
pip install git+https://github.com/opensafely-core/databuilder@main#egg=opensafely-databuilder`
```

!!! todo
    It's probably better to advocate installing the same version we're using to build the definitions.
    This will be a tagged version in `databuilder/requirements.prod.in`.

!!! todo

    Are we going to ever publish Data Builder to PyPI?

### Checking the installation

Make sure that you can run Data Builder's "help" command:

```
databuilder --help
```

If that command succeeds,
you should see some help text
and Data Builder should be correctly installed.

## Using Data Builder's command-line interface

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
