# ehrQL tutorial Part 1: Minimal dataset definition
By the end of this tutorial, you should able:

* to write a very simple dataset definition
* to run that dataset definition with Data Builder

## Full Example

We start with a minimal dataset definition. This
finds the patients whose year of birth is 2000 or later.

???+ example "Dataset definition: `1a_minimal_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/1a_minimal_dataset_definition.py"
    ```

If we run this against the sample data provided (see below), it will
pick out only patients who were born in 2000 or later. 

???+ example "Original Data: `minimal/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/minimal/patients.csv') }}

In this case, patient 2, 5 and 7. 

???+ example "Output dataset: `outputs/1a_minimal_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1a_minimal_dataset_definition.csv') }}

## Line by line explanation

### Import statements

Lines of the format `from… import…` specify which of Data Builder's code and features
to use in our dataset definition.
Here, we import two components of Data Builder:

* `Dataset` as provided by the query language, to create a dataset
* the `patients` table, which is one of several data tables that ehrQL gives access to

### Create a `Dataset`

A valid dataset definition must contain a dataset assigned to the name `dataset`. Like many other programming languages, we use `=` to assign a value to a variable name. In this case, we have assigned `Dataset()` to the variable `dataset`. This creates an empty dataset. 
In subsequent steps,
we specify the data from the available data tables
that we wish to add to the dataset.

### Find year of birth
Next we define a year of birth. `date_of_birth` is in the patient table and therefore we can assign it to this new variable. We want to only capture the `year` of birth so we add the `.year` to the end of this variable assignment. 

### Set population
Finally we set the population of the dataset. We use the special method called `set_population()` and pass in the definition of the population. In this case, we want to use our previously created `year_of_birth` and say, if year of birth is equal to or greater than 2000, include in this dataset. 

## Your turn
Run the dataset definition by:

```
opensafely exec databuilder:v0 generate-dataset "1a_minimal_dataset_definition.py" --dummy-tables "example-data/minimal/" --output "outputs.csv"
```

or if you are using `project.yaml`:

```
opensafely run extract_1a_minimal_population
```

!!! question

    Can you modify the dataset definition so that the output shows:

    1. Patients that were born before 1980?
    2. Patient that were born between 1980 and 2000?
