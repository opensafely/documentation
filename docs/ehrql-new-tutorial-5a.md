# ehrQL tutorial: Handling missing values

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 5a: Handling missing values

### Learning objectives

By the end of this tutorial, you should be able to:

* describe how missing values are represented in ehrQL
* check for missing values
* replace missing values

In the tutorial examples so far,
all the data rows have been fully populated with values.
There have been no missing values.

This is a somewhat idealised situation.
In the real world,
data is often incomplete with some values missing.
Missing data values in ehrQL are represented with a special "null" value.

We will explore how ehrQL's null values work in the below dataset definition
and some approaches to dealing with missing values.

### Full example

???+ example "Dataset definition: `5a_multiple3_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/5a_multiple3_dataset_definition.py"
    ```

In this section, we will build up a dataset using data that has missing values.
We will use two different tables:

* `hospitalisations`
* `patient_address`

Both of these tables contain missing data:

* the `hospitalisations` table has a column called `system` with missing values
* the `patient address` table has a column called `index_of_multiple_deprivation_rounded`
  We came across this column before in a previous tutorial but this time, we have included some missing data.

For brevity,
the tables will not be displayed here
but can be reviewed in the `example-data/multiple3/` folder.

The output of the query above should generate the table below:

???+ example "Output dataset: `outputs/5a_multiple3_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/5a_multiple3_dataset_definition.csv') }}

## Line by line explanation

This dataset definition:

* sets the population to be those patients with a hospitalisation entry
* adds the most recent hospitalisation date for a patient to the dataset
* adds details of the index of multiple deprivation

We will handle the missing data as follows:

* Where `most_recent_hospitalisation_system` in the hospitalisation table is missing, we will replace this with `UnknownCodeSystem`
* Where `imd` is missing, we will replace this with a `-1`

### Most recent hospitalisation

As we have seen before,
we can sort and select an entry per patient
with methods like `sort_by()`, and `first_for_patient()`.

This time, we are sorting and taking the last hospitalisation for the patient with `last_for_patient()`.

### Lowest IMD address

This is similar to what we have done before.
In this case we sort rows by `index_of_multiple_deprivation_rounded`,
and take the first row for the patient.

### Set population

We are trying to capture patients who have a recent hospitalisation.
For this, we check if a patient has row in the `most_recent_hospitalisation` subset (created above).
We can use `exists_for_patient()` as we did in a previous tutorial.

### Find code for hospitalisation

We want to find the code that is associated with the hospitalisation.
This is directly accessible as a column in the hospitalisation table.

### Replacing nulls: null hospitalisation coding system values

We now need to deal with the missing data in the hospitalisation code.
We can specify a replacement value for nulls as we have done in this dataset definition.

This is via the `if_null_then()` method.

The result is that the dataset contains `UnknownCodeSystem` in the data in place of the nulls.

### Replacing nulls: IMD

We now need to deal with the missing data
in the patient address table in the column of `index_of_multiple_deprivation_rounded`.
You might reasonably think that,
since we selected the lowest value of index of multiple deprivation,
that this lowest value would be a non-null value.

However, ehrQL sorts null values *before* non-null values.
If a patient has null and non-null values,
then the `first_for_patient()` will be a null value.

This results in the "lowest" IMD value in some cases being null.

In the dataset definition,
we replace the missing values with a negative value known to be invalid,
but of the correct integer type (`-1`).
This is via the `if_null_then()` method.

### Check if lowest IMD is valid

We want to create a variable that checks if an IMD is valid.
If so, returns a True, and if not, returns a False.
We use `is_not_null()` to handle the nulls.

Here, we checked that values were not null with the `is_not_null()` method.
We could have also used the `is_null()` method to check if values are null.
In both cases, the result is a Boolean `True` or `False` for each row.

## Your Turn

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
