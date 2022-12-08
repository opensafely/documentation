# ehrQL tutorial: Working with multiple tables

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 2a: Working with multiple tables

By the end of this tutorial, you should be able:

* to write a dataset definition that access multiple tables
* to look up the details of data tables that you can access via Data Builder
* to run a simple query of event-level data

### Full Example

OpenSAFELY backends provide several different collections of related data on patients. As you might expect if you have worked with databases before,
each collection is made available via Data Builder's *tables*.

For the purposes of this tutorial, each individual table is stored in a single CSV file, where the CSV filename indicates the table name. This is the simulate a real backend with multiple tables available. 

In the previous definitions, we accessed just a single table. This dataset definition accesses multiple tables
and also demonstrates some of the querying that ehrQL permits.

???+ example "Dataset definition: `2a_multiple_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/2a_multiple_dataset_definition.py"
    ```

As explained above, this definition needs two tables to query. Below shows the data available in the patient table and the prescriptions table. Our dataset definition will combine data from both tables to generate one dataset. 

???+ example "Data table: `multiple/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple/patients.csv') }}

???+ example "Data table: `multiple/prescriptions.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple/prescriptions.csv') }}

When we run the dataset definition against these tables, we should get this result. 

???+ example "Output dataset: `outputs/2a_multiple_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/2a_multiple_dataset_definition.csv') }}

## Line by line explanation

Most of this dataset definition will be familiar from the previous examples. There are only two changes. 

### Import statements
We import `prescriptions` as well as `patients`. 

The `prescriptions` table differs from `patients`
in that `prescriptions` is an *event-level table*,
while `patients` is a *patient table*. We will cover the difference between these more later.
For now, it is sufficient to understand that `prescriptions` may contain multiple entries per patient.

### Query the prescription table
The final line of dataset definition finds the most recently prescribed Dictionary of Medicines and Devices code for a patient.

This is done by sorting the table by `processing_date` and picking the last entry for a patient.
You can see the `sort_by` method described in the [ehrQL reference](ehrql-reference.md#212-sort-by-column-pick-last).

We will see more on working with dates in a later tutorial.

It is worth noting that the order in which columns are added to the `dataset` in the dataset definition is the order in which they appear in the output.

## Your turn
Run the dataset definition. 

!!! question

    Can you modify the dataset definition so that the output shows:

    1. The earliest DMD code prescribed 
    2. Reorder the columns so dmd prescription comes first, followed by sex
    3. The set_population only contains Males born in or after 2000
