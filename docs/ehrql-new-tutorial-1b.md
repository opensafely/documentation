# ehrQL tutorial: Another minimal dataset definition

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 1b: Adding an extra output column from a minimal data source

By the end of this tutorial, you should to be able:

* to retrieve additional data columns
* to be able to explain to a novice what is involved in creating a `Dataset`

### Full Example

We will start with a similar dataset definition that we 
used in the previous example with the addition of an extra output column, for sex. 

???+ example "Dataset definition: `1b_minimal_dataset_definition.py`"

    ```python
    ---8<-- "databuilder/ehrql-tutorial-examples/1b_minimal_dataset_definition.py"
    ```

If we run this against the sample data provided, it will pick out only patients who were born in 2000 or later, and will also provide information about sex as a new column. 

???+ example "Data table: `minimal/patients.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/minimal/patients.csv') }}

In this case, we see patient 2, 5 and 7. 

???+ example "Output dataset: `outputs/1b_minimal_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/1b_minimal_dataset_definition.csv') }}

## Line by line explanation
### Addition of Sex
Only the last line is new. In Python code, like in many other languages, the dot operator, `.`, appears frequently.

Generally, `.` is used when you want to access something
that is part of, or belongs to a value. That "something" is typically either a data attribute (itself a value), or a method (a function). Functions will have brackets, with may accept arguments. Attibutes will not have brackets. 

Sex is an inbuilt value that is available to the patient table. See the reference docs on what other values are inbuilt. 

## Your turn
Run the dataset definition by:

```
opensafely exec databuilder:v0 generate-dataset "1b_minimal_dataset_definition.py" --dummy-tables "example-data/minimal/" --output "outputs.csv"
```

or if you are using `project.yaml`:

```
opensafely run extract_1b_minimal_population
```

!!! question

    Can you modify the dataset definition so that the output shows:

    1. Both `date_of_birth` and `sex` columns?
    2. `year_of_birth` instead of `date_of_birth`?
