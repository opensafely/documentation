# ehrQL tutorial

---8<-- 'includes/data-builder-danger-header.md'

In this tutorial, we will walk through a minimal ehrQL example.
The example will create a dataset of all patients who were born in or after 2000.
We will walk through the example step-by-step;
if you want to see the example in full, then you can [skip to the end](#wrapping-up).

First, we import the patients table and create a variable that references each patient's year of birth:

---8<-- 'examples/src-minimal-ehrql-import-patients.md'

Next, we import and create a dataset

---8<-- 'examples/src-minimal-ehrql-import-dataset.md'

and set the population, which is all patients who were born in or after 2000:

---8<-- 'examples/src-minimal-ehrql-set-population.md'

At this point, we have created a dataset and set the population, but we haven't requested any data.
Let's change that.
As well as using each patient's year of birth to set the population, we also request it:

---8<-- 'examples/src-minimal-ehrql-request-year-of-birth.md'

!!! note
    When we extract the data, the name of the dataset's property will be the name of the table's column.
    For example, rather than writing

    ---8<-- 'examples/src-minimal-ehrql-request-year-of-birth.md'

    we could write

    ---8<-- 'examples/src-minimal-ehrql-request-birth-year.md'

    to give the column a different name.


Finally, we register the dataset:

---8<-- 'examples/src-minimal-ehrql-register.md'

## Wrapping up

Putting everything together, we have a minimal ehrQL example:

---8<-- 'examples/src-minimal-ehrql.md'

---8<-- 'includes/glossary.md'
