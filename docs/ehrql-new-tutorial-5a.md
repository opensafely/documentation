# ehrQL tutorial: Handling missing values

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 5a: Handling missing values

### Learning objectives

* Understand how missing values are represented
* Understand how to check for missing values
* Understand how to replace missing values

### Missing values

In the tutorial examples so far,
all the data rows have been fully populated with values.
There have been no missing values.

This is a somewhat idealised situation.
In the real world,
data is often incomplete with some values missing.
Missing data values in ehrQL are represented with a special "null" value.

We will explore how ehrQL's null values work in the below dataset definition
and some approaches to dealing with missing values.

!!! note
    Null values in the inputs and outputs in this documentation are represented as blanks in the tables.

### The dataset definition we will work with

???+ example "Dataset definition: `5a_multiple3_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/5a_multiple3_dataset_definition.py"
    ```

### The `multiple3` data source

???+ example "Data table: `multiple3/hospitalisations.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple3/hospitalisations.csv', keep_default_na=False) }}

???+ example "Data table: `multiple3/patient_address.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple3/patient_address.csv', keep_default_na=False) }}

### Dataset definition 5a output

???+ example "Output dataset: `outputs/5a_multiple3_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/5a_multiple3_dataset_definition.csv') }}

### Explanation of the dataset definition

#### Summary

This dataset definition:

* sets the population to be those patients with a hospitalisation entry
* adds the most recent hospitalisation date for a patient to the dataset
* adds details of the index of multiple deprivation

#### Initial selection of data

As we have seen before,
we can sort and select an entry per patient
with methods like `sort_by()`, and `first_for_patient()`.

We use these methods to create two separate ehrQL frames:

* one containing the latest hospitalisation entry for each patient
* one containing the lowest value of index of multiple deprivation (IMD) for each patient

#### Replacing nulls: null hospitalisation coding system values

Reading through the provided data manually,
can you figure out which of the rows selected in the dataset definition have missing hospitalisation coding system values?

Instead of leaving the value as missing,
we can specify a replacement value for nulls
as we have done in this dataset definition.

This is via the `if_null_then()` method.

The result is that the dataset contains `UnknownCodeSystem` in the data in place of the nulls.

##### Sorting with nulls: null IMD values

Reading through the provided data manually,
can you find which of the rows selected in the dataset definition have a null IMD value?

You might reasonably think that,
since we selected the lowest value of index of multiple deprivation,
that this lowest value would be a non-null value.

However, ehrQL sorts null values *before* non-null values.
If a patient has null and non-null values,
then the `first_for_patient()` will be a null value.

!!! todo
    Is the sort order defined where there are multiple null values?
    And, if so, how?

This results in the "lowest" IMD value in some cases being null.

In the dataset definition,
we replace the missing values with a known invalid value of the correct type (`-1`);
IMD values are integers starting at 1.

##### Checking null values

We can also check,
as we have,
if values are null or not.

Here, we checked that values were not null with the `is_not_null()` method.
You can use the `is_null()` method to check if values are null.
In both cases, the result is a Boolean `True` or `False` for each row.

#### Advice for working with data without access to it directly

!!! todo
    We should have some kind of warning that we can see all the underlying data in the tutorial.
    When working with OpenSAFELY backends,
    by design,
    you are not able to view the data.
    Should users assume that nulls are always possible?
    Or does it depend on the specifics of the contract?

### Tutorial exercises

!!! question
    1. Can you modify the dataset definition
       to eliminate the IMD value nulls?
       (Hint: you may find `drop()` useful to filter out unwanted rows.)
    2. Even with that modification,
       we still get a null IMD value in the dataset?
       Why?
       (Hint: look at the patient ID values.)
    3. Can you further modify the dataset definition
       to add an extra criterion in `set_population()` to remove this row entirely?
       (Hint: you may find the table operators covered earlier useful.)
