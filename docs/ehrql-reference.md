# ehrQL reference

---8<-- 'includes/data-builder-danger-header.md'

This page is a reference for [ehrQL](ehrql-intro.md).
This reference is structured as a series of examples.

The intended audience is primarily:

* researchers
* software developers

that already have some understanding of how the ehrQL works.

!!! info
    Please refer to the [ehrQL introduction](ehrql-intro.md) and [ehrQL tutorial](ehrql-tutorial.md)
    if you need more explanation of the underlying concepts behind ehrQL.

## How the examples work

Each individual example demonstrates a specific ehrQL feature in isolation.

Every example here consists of:

1. Headings and subheadings that summarise the feature being demonstrated.
2. A small example data table containing entirely fictitious variables and values.
   The table has a name: for example, `e` or `p` that is referred to throughout the example.
   Table names use code formatting throughout this reference.
3. An ehrQL query that extracts some data from the example table.
   Like the table names, ehrQL queries are displayed here with code formatting.
4. The resulting output from the ehrQL query,
   displayed as another table,
   to demonstrate the query's effect

!!! note
    The examples here are automatically generated from [Data Builder's specification tests](https://github.com/opensafely-core/databuilder/tree/main/tests/spec).

!!! specs

---8<-- 'includes/glossary.md'
