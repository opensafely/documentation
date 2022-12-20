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
