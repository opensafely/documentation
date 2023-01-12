# ehrQL reference

---8<-- 'includes/data-builder-danger-header.md'

This page is a reference for [ehrQL](index.md).
This reference is structured as a series of examples.

The intended audience is primarily:

* researchers
* software developers

that already have some understanding of how the ehrQL works.

!!! info
    Please refer to the [ehrQL introduction](index.md) and [ehrQL tutorial](tutorial/index.md)
    if you need more explanation of the underlying concepts behind ehrQL.

## How the examples work

Each individual example demonstrates a specific ehrQL feature in isolation.

Every example here consists of:

1. Headings and subheadings that summarise the feature being demonstrated.
2. A small example data input table containing entirely fictitious variables and values.
    * The table has a single-letter name referred to throughout the example
        * `e` for event-level table
        * `p` for patient-level table.
    * The columns of input tables use a name constructed from a single letter with a number
      to create an identifier — for example, `i1`.
      The single letter in the identifier refers to the column's data type:
        * a `b` column contains Boolean values
        * a `c` column contains electronic health record codes
          (the codes used in this reference are fictitious, for example: `abc`)
        * a `d` column contains dates
        * an `i` column contains integers
        * an `s` column contains strings
    * Both table and column names are written with code formatting throughout this reference.
3. An ehrQL query that extracts some data from the example table.
   Like the table names, ehrQL queries are displayed here with code formatting.
4. The resulting output from the ehrQL query,
   displayed as another table,
   to demonstrate the query's effect

!!! note
    The examples here are automatically generated from [Data Builder's specification tests](https://github.com/opensafely-core/databuilder/tree/main/tests/spec).

!!! specs

---8<-- 'includes/glossary.md'
