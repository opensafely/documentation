# ehrQL tutorial: Operations on tables

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 3a: Operations on tables

### Learning objectives

* Understand some simple operations that can be performed with ehrQL tables.
* Understand more about the importance of data types.
* Understand the difference between patient-level and event-level tables.

### The dataset definition we will work with

???+ example "Dataset definition: `3a_multiple2_dataset_definition.py`"

    ```python title="3a_multiple2_dataset_definition.py"
    ---8<-- "databuilder/ehrql-tutorial-examples/3a_multiple2_dataset_definition.py"
    ```

### The `multiple2` data source

???+ example "Data table: `multiple2/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/patients.csv') }}

???+ example "Data table: `multiple2/hospitalisations.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/hospitalisations.csv') }}

???+ example "Data table: `multiple2/patient_address.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/patient_address.csv') }}

### Dataset definition 3a output

???+ example "Output dataset: `outputs/3a_multiple2_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a_multiple2_dataset_definition.csv') }}

### Explanation of the dataset definition

#### Summary

This dataset definition finds the patients whose data meet all of the following conditions:

* born before the year 2000
* *and* matching at least one of the following
    * with a most recent patient address in a location with an index of multiple deprivation greater than 5000
    * where the index of multiple deprivation has increased from the earliest address to the latest

For those patients, the output dataset shows:

* patient sex
* whether the patient has ever been hospitalised

#### How the dataset definition works

Selecting the year of birth is as we've seen in previous dataset definitions.

We set the population with a more complex condition than in previous tutorials.
Instead of solely considering the year of birth for each patient,
we look for specific details of the index of multiple deprivation (IMD)
where patients live.

First, we find the earliest and most recent IMDs for each patient.
Both of these can be thought of as single-column tables,
like this one for the earliest IMD:

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a1_multiple2_dataset_definition.csv') }}

!!! todo
    Is single-column table a good term for a series?
    We don't just have the values only,
    like in an array,
    but indexed by patient identifier.

We have defined "earliest" IMD by sorting the address details by the date a patient stopped living there.

!!! todo
    In this exercise, we deliberately do not have a notion of the "current" address.
    Would this require a null value or a `9999-12-31`?
    If a `9999` date, should we use that?
    It would be better to not complicate with null values right now.
    Otherwise do we explain the simplifying assumption
    that we are avoiding missing values?

##### Comparing values

To compare the earliest and latest IMD values we have,
we can use comparison operators you might be familiar with, such as `<`, `>`, `==`.

We do two kinds of comparison here.
First, values of the two IMD *columns* are compared for each patient row.

This comparison can be thought of as a new single-column table,
indicating whether the IMD has increased from earliest to latest date,
represented by one of the Boolean values, `True` or `False`:

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a2_multiple2_dataset_definition.csv') }}

The other kind of comparison is between row,
and a fixed numeric value.

In this case, we compare the "latest" IMD to the *integer* `5000`.
Integers in ehrQL are written as numbers without a decimal point.

!!! warning
    Python has two types of numbers relevant to ehrQL:

    * `int`: to represent integers
    * `float`: to represent real numbers

    ehrQL is currently strict when comparing numeric types:
    only integers can be compared to integers,
    and floating point numbers ("floats") to other floats.

    Data Builder will give an error
    if you try to compare incompatible types in your dataset definition.

    The [Contracts reference](contracts-reference.md) tells you
    which data type each table column has.
    This tells you what kinds of values and columns you can directly compare with.

    If you need to convert values in columns,
    as a temporary fix,
    then you can use: `.as_int()` and `.as_float()`.

!!! todo
    This behaviour is expected to change in future
    to be more flexible:
    <https://github.com/opensafely-core/databuilder/issues/540>

    We should be able to remove this warning.

##### Logical operators

Logical operators combine Boolean values together to give a single Boolean value.
ehrQL has the following logical operators that you might already be familiar with:

* `&` to represent `AND`
    * `a & b` is `True` when both `a` and `b` are `True`
* `|` to represent `OR`
    * `a | b` is `True` when either or both of `a` and `b` are `True`
* `¬` to represent `NOT`
    * `¬a` is `True` when `a` is `False`.

With ehrQL,
these, like the comparison operators, are applied per table row,
resulting in a table as output.

!!! todo
    Can we improve the explanation of "per table" row?
    It's not necessarily "per patient".

In this tutorial dataset definition, we combine multiple logical expressions.
The parentheses around each logical expression make the intent clearer.
The parentheses also ensure the order of evaluation:
each expression in parentheses is evaluated before combining them together.

!!! todo
    Do we have a reference or specification for the order of evaluation?
    As written, this is a little vague.

The logical operators are used to combine the criteria
for patients to include in the population,
as mentioned above in the [summary](#summary).
In this dataset definition, we use:

* `|` to specify that we want either an increased IMD,
  or an IMD greater than a specified value.
* `&` to then specify we want to match the previous IMD criteria
  *and* certain values of year of birth.

##### Adding columns to our dataset

Finally, we add multiple columns to our dataset,
as we have done in previous dataset definitions.

We are interested in if a patient ever has been admitted to hospital.
This is inferred by the presence of a row in the `hospitalisations` table.
To check for the presence of a row,
we can use the `exists_for_patient()` method on a table.
This results in a Boolean column indicating whether any rows exist.

### Event and patient-level tables

When working with ehrQL, there are two distinct kinds of tables:

* event-level tables can contain many rows per patient
* patient-level tables can contain only one row per patient

!!! todo
    Decide on how to refer to one row/many rows tables.
    Do we continue to use "one row"/"many rows"
    or event-level/patient-level?

The table passed to `set_population` must be a patient-level table with a single Boolean column.
This table then defines which patients are included in the final dataset.

!!! todo
    Does it have to contain one row for *every* patient in the data?
    Or can there be effectively zero rows for a patient?

### Frames and series: the underlying ehrQL query model

!!! todo
    Include this section here,
    or move to another page?

!!! todo
    Do we even need to refer to frames and series at all?
    Or is it sufficient for a user to just refer to any of these as simply "tables".

    Current hunch:
    include, because:
    * it is probably in error logs
    * it is in the source
    * there are possible subtle distinction in the rules for combining frames and series

    This is possibly a more advanced detail.

!!! todo
    Clear up uses of "table", "frame", "series".
    Perhaps "tables" are collections of data
    that are internally represented as frames or series.

When working with data in ehrQL,
the underlying data structures representing each table are *series* and *frames*:

* ehrQL frames represent a collection of rows and columns.
* ehrQL series represent a single column: a sequence of values.

!!! todo
    In practice, can each of these can be thought of as a table?

Both frames and series can be classified into one of two kinds,
depending on the maximum number of rows that can exist for any patient:

* those containing at most, one row for every patient
* those that can contain many rows per patient

In this example,
we can see that:

* the `patients` table is a *frame*
  containing *one row per patient*
* the `hospitalisations` and `patient_address` tables are *frames*
  containing *many rows per patient*
* `earliest_imd` and `latest_imd` are *series*
  containing *one row per patient*
* if we had selected `patient_address.index_of_multiple_deprivation`,
  then we would have had a `series`
  containing *many rows per patient*

To be included in a dataset,
a series must contain one row per patient.

#### Rules for combining frames and series

We have seen in this dataset definition
that we can compose data from different tables:
by combining series.
This also extends to frames too.

Combining frames and series is a useful tool when writing more complex ehrQL queries.
However, there are subtleties that can arise
when combining "many rows per patient" data
to ensure a meaningful result is produced.

For now, it is sufficient to know that Data Builder checks your ehrQL dataset definition for you,
before a query is submitted to any data backend.
You will get an explicit error
if you try to combine frames and series
in a way that ehrQL does not support.

The full details are out of scope for this tutorial.
When you have completed the tutorial,
you may wish to review the [more detailed explanation](ehrql-combining-series-and-frames.md).

!!! todo
    This is currently on its own page.
    Is that the most appropriate place?

### Mathematical operations on frames and series

There are also more advanced ways to combine data with Data Builder,
which we will not cover in this tutorial.

!!! todo
    Review this statement.
    It is possible we could include this in a subsequent dataset definition.

For example,
you can perform simple mathematical operations on column (series) values
including combining with other column values for a patient,
or combining with some other value specified or computed in the dataset definition.

See ["Combining series"](ehrql-reference.md/#5-combining-series) in the ehrQL reference.

!!! todo
    Review this URL.
    It is fragile due to how we construct fragment identifiers.
    We can currently only verify the link is correct manually.

### Tutorial exercises

!!! question
    1. What do you think would if you compare the IMD values for patients
       to the floating point value `5000.0`,
       instead of the integer value `5000`?
       Modify the dataset definition to check if you are correct.
    2. Can you further restrict the population to those patients who have a postcode?
    3. Can you change a single line of this dataset definition
       so that the patient population selection is *inverted*?
       Specifically, all patients previously selected are now not selected,
       and all patients previously unselected are now selected.
