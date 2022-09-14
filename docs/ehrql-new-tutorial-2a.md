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
in that `prescriptions` is an event-level table,
while `patient_demographics` is a patient table.

We will cover the difference between these more later.
For now, it is sufficient to understand that `prescriptions` may contain multiple entries per patient.
To find the most recently prescribed code,
we have to sort the entries and then select the latest per patient.

We add the most recently prescribed Dictionary of Medicines and Devices code for a patient.
This is done by sorting the table by `processing_date` and picking the last entry for a patient.
You can see the `sort_by` method described in the [ehrQL reference](ehrql-reference.md#212-sort-by-column-pick-last).

!!! todo
    Allude to working with dates.

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

#### The data provided by OpenSAFELY

Different backends may differ in the data they provide.
It is possible to review the data that each offers via the [Contracts reference](contracts-reference.md).

The reference tells you:

* the tables available
* the columns available in the tables
* the data types in the columns

We can see the data in the data tables offered by our tutorial.

!!! todo
    Add a link here once we add this.

!!! todo
    What's the behaviour/how do we resolve the case where we don't provide CSV data?
    For example, with the `minimal` examples,
    there is just the `patient_demographics` table.
    If we list all the tables that `tutorial` offers,
    we'll include tables that aren't in a given dataset.

    Possible options:
    * We can specify that this is a special case somewhere.
    * We could include data that we're not interested in.

!!! todo
    Rename the Contracts reference.

!!! todo
    At the moment, it seems like the only way to get an idea of the data that `tables` offer is via the Contracts reference.
    Is there going to be a more accessible way for researchers to list/review the tables?
    Or is that indeed the way?

    (It does not seem too inaccessible:
    but whether we want researchers to be aware of Contracts is a valid question.)

#### The different data types

!!! todo
    It is not entirely clear how best to explain these, or if the best place is here.

    The Contracts reference lists a mixture of fundamental types
    (such as "Boolean", "Integer")
    and those based on fundamental types
    (such as "Code").
