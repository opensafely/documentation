## What happens when Data Builder generates a dataset?
At this point, it might be useful to understand what 
Data Builder does when it generates a dataset. 

1. The dataset definition is validated
   to ensure that the resulting database query would be valid.
2. A database query suitable for the specified database is created.
3. The query is submitted to the database.
4. Provided the query is successful, the query creates an output.

In writing a *dataset definition* then,
what we are really writing is a *database query*.
Data Builder transforms the dataset definition into the appropriate database query,
for the specific database.

!!! note

    You can see the database query that a dataset definition will generate
    via the `databuilder --dump-dataset-sql` command.

    For the minimal example `1a_minimal_dataset_definition.py` above,
    the underlying SQL query generated is:

    ```sql
    SELECT patients.patient_id AS patient_id
    FROM patients
    WHERE CAST(STRFTIME('%Y', patients.date_of_birth) AS INTEGER) >= 2000;
    ```

    !!! todo

        This SQL should be kept updated.

That database might be:

* a local database used for testing,
  such as in this tutorial
* an OpenSAFELY backend,
  when submitting jobs to OpenSAFELY

There are two important implications of how this Data Builder's process works:

1. **Queries do not have to be written in a specific query language tailored to a specific database.**
   The compatibility of a dataset definition depends only
   on whether all the data tables used are available in the database being queried.
2. **All the data processing requested happens at the database
   after the dataset definition is processed in its entirety.**
   This is different from a more typical interactive data analysis in Python, Stata or R
   where you load some data,
   then perform computations on that data as each line of the analysis code runs.
