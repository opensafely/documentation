# ehrQL tutorial: Filtering and aggregation

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 6a: Filtering and aggregation

### Learning objectives

* Understand more about how to filter rows
* Understand more about how to aggregate values

### The dataset definition we will work with

???+ example "Dataset definition: `6a_multiple4_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/6a_multiple4_dataset_definition.py"
    ```

### The `multiple4` data source

???+ example "Data table: `multiple4/patient_demographics.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple4/patient_demographics.csv', keep_default_na=False) }}

???+ example "Data table: `multiple4/clinical_events.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple4/clinical_events.csv', keep_default_na=False) }}

### Dataset definition 6a output

???+ example "Output dataset: `outputs/6a_multiple4_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/6a_multiple4_dataset_definition.csv', keep_default_na=False) }}

### Explanation of the dataset definition

#### Summary

In this dataset definition, we select details of patients who:

* have had a particular clinical event code recorded
* with an associated numeric value higher than a given threshold
* within a specified date range

We then extract:

* the patient's date of birth
* the maximum numeric value recorded for the patient for the specified
  clinical event code
* the number of matching clinical events that exceed the given threshold

#### Filtering values

The `take()` and `drop()` methods allow filtering of table rows:

* `take()` specifies rows that you wish to *include*
* `drop()` specifies rows that you wish to *exclude*

We can apply these methods to frames.

!!! todo
    And series?
    Decide how, and where, to explain frames and series

Both `take()` and `drop()` require an expression inside their parentheses
that evaluates to a Boolean `True` or `False` for each row.
If you already have a suitable Boolean column,
you could use that as the [expression directly](ehrql-reference.md#111-take-with-column).

!!! todo
    Essentially, they both require a series.
    Decide how, and where, to explain frames and series

In this dataset definition,
we have used both simple expressions that evaluate to a Boolean value per row
and we have combined multiple Boolean expressions using [ehrQL's logical operators](ehrql-new-tutorial-3a.md).

!!! todo
    Provide a more stable reference URL.

Rows that result in a `True` value for this expression then have the filter applied in the result.

If a value used to evaluate the expression is null,
then the result of the expression will be `False`.

!!! todo
    Check and clarify null behaviour.

#### Aggregating values

Now that we have selected the rows of interest,
we can look at extracting useful values.

We can perform simple aggregations per patient
and we have already seen some of these such as `exists_for_patient()`.

Aggregation of frames and series always give you a new series.
These series are always one row per patient.

!!! todo
    Clarify series, frames and tables.

To our dataset, we use some of the simple numerical aggregations.

First, we add the number of relevant matching clinical events to the dataset,
by counting the events with `count_for_patient()`.
and we find the highest value recorded in those clinical events
by using `maximum_for_patient()`.

### Tutorial exercises

1. In this dataset definition,
   we initially filtered all of the clinical events to those using the `TutorialCodeSystem` code system.
   How would we rewrite that same selection to use a single `drop()`?
2. How would we find the *sum* of the numeric values of the `m1` clinical events
   for each patient within the same date range already specified?
   Refer to the [ehrQL reference](ehrql-reference.md).
2. As the dataset definition shows,
   we can use combine multiple filters using `take()` and `drop()`
   in different ways.
   Either we can specify multiple conditions to a single `take()` or
   `drop()`.
   Or we can *chain* multiple `take()` and `drop()` methods.
   The output of each method is a frame.

    !!! todo
        Or series?
        Check! Does this work on series, or just frames?

     You may find either way to express the same process useful:
     it may make your dataset definition either clearer
     or more consise to read.

     Can you rewrite the `take()` with multiple conditions to be a series of chained `take()` methods?
     Refer to the [ehrQL reference](ehrql-reference.md).

    !!! todo
        In general, do we want to suggest particular ehrQL idioms?
