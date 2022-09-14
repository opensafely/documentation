# ehrQL tutorial: Working with multiple tables

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 2a: Working with multiple tables

### Learning objectives

By the end of this tutorial, you should know how to:

* Write a dataset definition that access multiple tables
* Look up the details of data tables that you can access via Data Builder
* Understand about the basic data types that are available in those tables
* Begin querying event-level data

### The dataset definition we will work with

OpenSAFELY backends provide several different collections of related data on patients.
As you might expect if you have worked with databases before,
each collection is made available via Data Builder's *tables*.

!!! note

    For this tutorial, each individual table is stored in a single CSV file,
    where the CSV filename indicates the table name.

In the previous definitions, we accessed just a single table.
This dataset definition accesses multiple tables
and also demonstrates some of the querying that ehrQL permits.

```python title="2a_multiple_dataset_definition.py"
---8<-- "databuilder/ehrql-tutorial-examples/2a_multiple_dataset_definition.py"
```

### The `multiple` data source

`multiple/patient_demographics.csv`:

{{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple/patient_demographics.csv') }}

`multiple/prescriptions.csv`:

{{ read_csv('databuilder/ehrql-tutorial-examples/example-data/multiple/prescriptions.csv') }}

### Dataset definition 2a output

`outputs/2a_multiple_dataset_definition.csv`

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/2a_multiple_dataset_definition.csv') }}

### Explanation of the dataset definition

Most of this dataset definition will be familiar from the previous examples.
The biggest change is that the `prescriptions` table is also queried,
and data from it included in the dataset definition's output.

The `prescriptions` table differs from `patient_demographics`
in that `prescriptions` is an *event-level table*,
while `patient_demographics` is a *patient table*.

We will cover the difference between these more later.
For now, it is sufficient to understand that `prescriptions` may contain multiple entries per patient.

We add the most recently prescribed Dictionary of Medicines and Devices code for a patient.
This is done by sorting the table by `processing_date` and picking the last entry for a patient.
You can see the `sort_by` method described in the [ehrQL reference](ehrql-reference.md#212-sort-by-column-pick-last).

We will see more on working with dates in a later tutorial.

#### Parentheses

We can see in this example that parentheses — `(`, `)` — have various uses.
Like many other languages, Python uses parentheses in different ways
and we see some of those in this dataset definition:

* In function or method calls,
  such as `set_population()`
* To set an order of precedence;
  for instance, `((3 + 4) * 5)` is `35`
  (addition happens before multiplication)
  while `3 + 4 * 5` is `23`
  (multiplication happens before addition)
  It is useful in Python and ehrQL to use parentheses where the order of precedence is potentially unclear.
  It helps the reader, and makes mistakes less likely.
* As in this example,
  to permit a long line of code to be split onto multiple lines.

!!! tip
    Long lines of code will be automatically formatted to a maximum line length
    if you write a long line
    and then run the [`black` formatter](ehrql-new-tutorial-intro.md#text-editor) on your dataset definition.

#### Accessing multiple Data Builder tables

As before, we specify the tables to use via an `import` statement.
Multiple table names can be separated by commas.

We can then access the specific table in the dataset definition
by using the same name.

In this dataset definition,
we are extracting data on patients from both tables.

### Writing dataset definitions to run on real OpenSAFELY backends

In these tutorial examples,
we can always see the underlying data that we are working with.

This helps when writing dataset definitions because we can:

* see the names of the tables (from the filenames)
* see the names of the data columns
* see what kind of data is in each column
* infer any constraints on the data

When working with OpenSAFELY,
we do not have access to any underlying data.
This is an inherent part of [OpenSAFELY's security model](security-levels.md).

To write a real dataset definition,
we need some way of referencing the details of the data available
without needing to look at the data.
This is provided by the [Contracts reference](contracts-reference.md).

#### The Contracts reference

For each backend, the [Contracts reference](contracts-reference.md) describes:

* the names of the available tables
* the names of the columns available in the tables

These names are useful to know *how to access the data*,
when writing a dataset definition.

* the data types in the columns
* any constraints or caveats in the data

These properties are useful to *know what you can do with the data*,
when writing a dataset definition.

!!! todo
    The Contracts reference needs updating.

    See <https://github.com/opensafely/documentation/issues/937>

!!! todo
    Rename the Contracts reference.

!!! todo
    What's the behaviour/how do we resolve the case where we don't provide CSV data for these examples?

    For example, with the `minimal` examples,
    there is just the `patient_demographics` table.
    If we list all the tables that `tutorial` offers,
    we'll include tables that aren't in a given dataset.

    The "missing CSV" option might help here.

    Possible options:
    * We can specify that this is a special case somewhere.
    * We could include data that we're not interested in.

!!! todo
    At the moment, it seems like the only way to get an idea of the data that `tables` offer is via the Contracts reference.
    Is there going to be a more accessible way for researchers to list/review the tables?
    Or is that indeed the way?

    (It does not seem too inaccessible:
    but whether we want researchers to be aware of Contracts is a valid question.)

#### Applying the Contracts reference to this tutorial

In the dataset definition in this tutorial,
we access the following:

* *table names*:
    * `patient_demographics`
    * `prescriptions`
* *column names*:
    * `patient_demographics.date_of_birth`
    * `patient_demographics.sex`
    * `prescriptions.processing_date`
    * `prescriptions.prescribed_dmd_code`

For these tutorials,
we can look up the details for the tutorials in the [Contracts reference](contracts-reference.md)
and see that these table and column names, among others, are listed.

!!! todo
    Add a correct reference link here once we add this.

In this tutorial,
we have:

* *data types*:
  * integer (`patient_id`)
  * string (`sex`, `prescribed_dmd_code`)
  * date (`processing_date`)
* *data constraints*
  * `date_of_birth` must have a value and must be the first day of the month
  * `sex` must be one of a specific set of values

!!! todo
    Fix up the example dates to be first of month.

!!! todo
    Add any constraints for `prescriptions`.

Again, we can look up the same information on data types and constraints
from the Contracts reference
without needing to look at the underlying data.

### Tutorial exercises

!!! question
    1. Which tables are available in the TPP backend?
    2. Can you find all of the data types that are used in the tutorial tables?
       Many of the table data types are much like those that exist as primitive data types in programming languages.

!!! todo
    Write some more questions based on the Contracts reference.
    It's difficult right now as this isn't populated yet.
