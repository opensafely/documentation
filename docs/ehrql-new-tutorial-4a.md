# ehrQL tutorial: Date handling

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 4a: Date handling

### Learning objectives

By the end of this tutorial, you should be able:

* to specify dates in dataset definitions
* to explain date operations
* to use the key word `take` in dataset definitions

### Full Example

???+ example "Dataset definition: `4a_multiple2_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/4a_multiple2_dataset_definition.py"
    ```
In this section, we will be building up even more complex dataset definitions, in particular concentrating on date operations. We will be using 2 different tables, patients and hospitalisations. For the sake of brevity, the tables will not be displayed here but can be reviewed in the `example-data/multiple2/` folder.  

The output of the query above should generate a table with sex, year of birth, and last day of month before first hospitalisation as columns. 

???+ example "Output dataset: `outputs/4a_multiple2_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/4a_multiple2_dataset_definition.csv') }}

## Line by line explanation
This dataset definition finds the patients whose data meet all of the following conditions:

* born before the 1st of January, 2000.
* *and* hospitalised in a given date range.

For each of these patients,
we extract sex,
year of birth,
and the last day of the month
prior to when the patient was first hospitalised in that date range.

### Import Statements
Similar to the previous sections, we are importing the tables that we wish to work with. In this case, we only need two tables: patients and hospitalisations. 

Remember that hospitalisations is an event level data table. This means that it captures information at an event level of hospitalisation where each row represents a hospitalisation episode. Patients can have many hospitalisations. This is in contrast to patient level tables such as patients where each row represents one patient. 

### Specifying dates in a dataset definition

In this dataset definitions, we specify dates of interest
with strings written in the ISO8601 format: YYYY-MM-DD.

We are creating a start date and an end date of the study. We will use these dates with the hospitalisation variable to restrict the population to only those with hospitalisations inclusive of this date range. 

### Hospitalisations within a range

We select the hospitalisation rows that match a condition
with the `take` method.

This restricts the hospitalisation data to data that matches the condition passed into the `take()` function - i.e. what is in the brackets. In this case we are passing in a condition that the date column in the hospitalisation table is on or after the start date created above, and is before the end date created above. This creates a subset of the hospitalisation data. 

To be clear here, we could use the dates directly i.e. pass in `2020-03-01` rather than `start_date` and that would not be wrong. Here there is a question of readability and reusability. It is easier to see the start date as a variable in its own line rather than it get lost in the middle of another variable definition. It also allows us to reuse the start date. In other more complicated studies, we might want to create several variables that in some way reference the start date and this allows us to create the start date just once, rather than having to manually add dates in several places.

### Set the population 
Now we have the hospitalisation subset of data we can use this to create our dataset. Just the same as the date of birth examples we saw before in previous tutorials, we can also perform basic comparisons on dates
to check equality or to determine if one date is before or after another.

With string provided dates, we can use Python's standard comparison operators like: `<`, `>=`, `!=`.

We are using a special function called `exists_for_patient()` to restrict the population. This checks if a row exists for a patient and if it does it passes back a True. In this case we are restricting the population by only those with hospitalisation, i.e. have a row in the hospitalisation subset. 

### Extracting components of data

Next, we restrict the population to patients
who meet our [criteria](ehrql-new-tutorial-4a.md#summary).

We then add `sex` and `year_of_birth` to the dataset.

As we have done in previous dataset definitions,
and we do here,
we can extract individual components — year, month, day — of a date.

### First Hospitalisation in range
The aim here is to find the last date of the month that immediately proceeded the first hospitalisation of a patient. 

First of all, we need to find the first date of hospitalisation. We have already created the subset of hospitalisation in range as a variable for use in setting the population. We can reuse this subset to find the first date of hospitalisation. 

We do this by sorting the hospitalisation for each patient by date(remember this is event level data so patients can have many hospitalisations and hence rows of data). We then use `first_for_patient()` to take the first of these values. This means we will take the first date. 

Now we need to find the proceding month and the last date of this month. The easiest way to do this is to get the first of the month for the hospitalisation date and then subtract 1 day to get the last day of the proceding month. This allows us to account for varying lengths of months, rather than setting it at 28th of the month. To do this, we:

1. Add the variable to the dataset with `dataset.last_day_of_month_before_first_hospitalisation` 
2. Round the date down to the first of the month (`to_first_of_month()`)
3. Subtract 1 day (`subtract_days(1)`) to get the last date of the proceeding month. 

This function `subtract_days()` is an example of the type of date operations that can be carried out on the dates. See the documentation for further information. 

## Your Turn
Run the dataset definition. 

!!! question
    1. Can you modify the date conditions in this dataset definition
       to _include_ both dates in the range,
       instead of excluding the specified end date?
       See the [ehrQL reference](ehrql-reference.md) for the operations and methods on dates.
    2. Can you modify the dataset definition
       to find the date seven days after hospitalisation?
    3. Can you modify the dataset definition to find the 15th of the month of hospitalisation?
    4. Can you add a new column to get the date of the last hospitalisation for each patient? 
