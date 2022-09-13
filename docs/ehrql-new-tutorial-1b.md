# ehrQL tutorial: Another minimal dataset definition

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 1b: Adding an extra output column from a minimal data source

## Learning objectives

By the end of this tutorial, you should know how to:

* Retrieve additional data columns
* Understand more about what is involved in creating a `Dataset`

### The dataset definition we will work with

This dataset definition uses the same [data source](#the-minimal-data-source).

```python title="1b_minimal_dataset_definition.py"
---8<-- "databuilder/ehrql-tutorial-examples/1b_minimal_dataset_definition.py"
```

The main addition here is the additional output column.

### Dataset definition 1b output

`outputs/1b_minimal_dataset_definition.csv`

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1b_minimal_dataset_definition.csv') }}

### Explanation of the dataset definition

This dataset definition is slightly modified from the previous example.

The difference is that an extra column, `sex` is added in the output.

We can see, logically, there are three stages to creating our dataset,
and we have split this dataset definition into these three logical stages.

1. Create an empty `Dataset()`
2. Specify that dataset's patient population of interest.
3. Add relevant columns.

!!! tip

    In the same way as you might use paragraphs to separate ideas in conventional writing,
    it can be useful to use vertical space in this way
    to help a reader of the code.

    (That reader may be your future self.)

#### Using the dot operator `.` to access attributes on values

In Python code,
like in many other languages,
the dot operator, `.`, appears frequently.

Generally, `.` is used when you want to access something
that is part of, or belongs to a value.

That "something" is typically either a data attribute (itself a value),
or a method (a function).

Here, the dot operator is used in several specific ways to:

* Identify which of the Python source files (modules) in Data Builder
  that we want to use via the `import` statement.
* Access the `.set_population()` method on the `Dataset` that we created.
* Access data from the `patient_demographics` table.
* Set a column in the output via `dataset.column_name`

Sometimes that attribute accessed by dot notation may have useful attributes,
which can lead to "chaining" of the dot notation.
In this dataset definition example,
chained dot notation is used in `patient_demographics.date_of_birth.year`

#### `set_population()`

The `set_population()` method of a `Dataset` controls which patient rows will be included in the output.
It requires an argument to be passed to it.

This argument can be thought of as an expression or function
that can use data from one or multiple tables
and gives a true, false or missing result for any given patient.
Patients for which this argument evaluates to true are then included in the dataset.

!!! note
    Alternatively you could imagine creating a table
    which has each patient identifier in one column,
    and the result of this argument in another.
    The rows with a "true" result are then the patient identifiers
    included in the table.

    Data Builder does not actually create this intermediate table:
    it generates a single query that is submitted at the end.
    But this can be a useful way to imagine the process.

#### Tutorial exercises

!!! info

    These exercise sections are optional.
    They are prompts for you to practise writing your own ehrQL queries.

!!! question

    Can you modify the dataset definition so that the output shows:

    1. Patients that were born before 1980?
    2. Both `date_of_birth` and `sex` columns?
    3. `year_of_birth` instead of `date_of_birth`?

!!! todo

    Ways that we could polish this.

    1. We could:

        * provide known good outputs
        * provide a script for running Data Builder against the script
        * validate the outputs with pytest or similar

        The difficulty here is that, above,
        we invite people to use Docker to run Data Builder.
    2. Provide a solution in a dropdown,
       (and also test that solution).
