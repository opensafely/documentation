# ehrQL tutorial: Date handling

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 4a: Date handling

### Learning objectives

* Understand how to specify dates in dataset definitions
* Understand date operations

### The dataset definition we will work with

???+ example "Dataset definition: `4a_multiple2_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/4a_multiple2_dataset_definition.py"
    ```

### The `multiple2` data source

???+ example "Data table: `multiple2/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/patients.csv') }}

???+ example "Data table: `multiple2/hospitalisations.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/hospitalisations.csv') }}

???+ example "Data table: `multiple2/patient_address.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple2/patient_address.csv') }}

### Dataset definition 4a output

???+ example "Output dataset: `outputs/4a_multiple2_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/4a_multiple2_dataset_definition.csv') }}

### Explanation of the dataset definition

#### Summary

This dataset definition sets the population to patients:

* born before the 1st of January, 2000.
* *and* hospitalised in a given date range.

For each of these patients,
we extract `sex`,
year of birth,
and the last day of the month
prior to when the patient was first hospitalised in that date range.

#### Specifying dates in a dataset definition

In this dataset definitions,
we specify dates of interest
with strings written in the ISO8601 format: YYYY-MM-DD.

Although these are just Python strings,
Data Builder can compare these string dates to
date values in ehrQL series and frames
without any further step.

If you need more flexibility,
ehrQL also allows specifying dates as [Python `datetime` dates](https://docs.python.org/3/library/datetime.html#date-objects);
[see the ehrQL reference](ehrql-reference.md).

#### Comparing dates

We select the hospitalisation rows that match a condition
with the `take` method.

We will explain `take` more in a subsequent tutorial.

!!! todo
    The use of `take` here is because of
    <https://github.com/opensafely-core/databuilder/issues/757>
    — it's not possible to just combine the series
    and then check if a value exists.

    We could reorder to move this after `take` is explained.

This result is a new ehrQL frame,
based on the existing hospitalisation frame.
but only containing rows with hospitalisations
that fall within the given dates,
excluding the final date itself.

We can also perform basic comparisons on dates
to check equality
or to determine if one date is before or after another.

With string provided dates, we can use Python's standard comparison operators like: `<`, `>=`, '!=`.

There also equivalent methods for comparison
such as `.is_on_or_after()`
that are more versatile.
These comparisons do not only work with a specified date value,
but also work with entire ehrQL date series.
This is a powerful means to compare date values in different columns, per patient.

!!! todo
    Check: is it just string provided dates that work like this?
    Or do date series,
    and `datetime` objects work like this too?

#### Extracting components of dates

Next, we restrict the population to patients
who meet our [criteria](ehrql-new-tutorial-4a.md#summary).

We then add `sex` and `year_of_birth` to the dataset.

As we have done in previous dataset definitions,
and we do here,
we can extract individual components — year, month, day — of a date.

These components are represented as *integer* values.

#### Operations on dates

We can perform basic arithmetic operations on ehrQL date values.
Here we subtract the same number of days
from a given series of dates.

We also extract a more complicated variable related to the first hospitalisation date.
We extract the first hospitalisation date in the range
and shift this to the last day of the previous month.

### Tutorial questions

!!! question
    1. Can you modify the date conditions in this dataset definitions
       to _include_ both dates in the range,
       instead of excluding the specified end date?
       See the [ehrQL reference](ehrql-reference.md) for the operations and methods on dates.
    2. Can you modify the dataset definition
       to find the date seven days after hospitalisation?
