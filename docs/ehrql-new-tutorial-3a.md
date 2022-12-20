# ehrQL tutorial: Operations on tables

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 3a: Operations on tables

By the end of this tutorial, you should be able:

* to describe and generate some simple operations that can be performed with ehrQL tables.
* to describe the types of operations that can be carried out 
* to explain the importance of data types.

### Full Example

In this section, we will be building up a more complex dataset definition that includes information about a patient's address and their hopsitalisation record. This means that we are combining 3 different tables: patients, patient_address and hospitalisations. 

In this example, instead of solely considering the year of birth for each patient,
we look for specific details of the index of multiple deprivation (IMD)
where patients live. Importantly we are restricting the population by IMD rather than creating this as a column.

For the sake of brevity, the tables will not be displayed here but can be reviewed in the `example-data/multiple2/` folder. 

???+ example "Dataset definition: `3a_multiple2_dataset_definition.py`"

    ```python title="3a_multiple2_dataset_definition.py"
    ---8<-- "databuilder/ehrql-tutorial-examples/3a_multiple2_dataset_definition.py"
    ```

The output of the query above should generate a table with sex and was hopsitalised as columns. 

???+ example "Output dataset: `outputs/3a_multiple2_dataset_definition.csv`"

    {{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a_multiple2_dataset_definition.csv') }}

## Line by line explanation

This dataset definition finds the patients whose data meet all of the following conditions:

* born before the year 2000
* *and* matching at least one of the following
    * with a most recent patient address in a location with an index of multiple deprivation greater than 5000
    * where the index of multiple deprivation has increased from the earliest address to the latest

For those patients, the output dataset shows:

* patient sex
* whether the patient has ever been hospitalised

### Import Statements
Similarly to the previous sections we are importing the tables that we wish to work with. In this case we need patients, patient_address and hospitalisations. 

This introduces the concept of patient-level and event-level tables. Put simply `patient` is a patient-level table where one row represents one patient. Whereas `patient_address` is event-level where each row is an event and a patient can have many events. In this case, when someone moves house and gets a new address. See the [explainer](data-builder-patient-event-tables) for more information. 

Note in the code, there has been addition of paratheses. These are optional and have been added in to make it easier to read. 

### Address by date
In this line we are querying the patient_address table and sorting by the data associated with address entries for each patient. 

Note that similar to year_of_birth, we are creating a variable that is not being put into the dataset defintion as a column. Rather these columns can be used either to restrict populations or as intermediate variables. In this case, we have created a variable of patients' addressed sorted according to the latest date. 

### Earliest IMD
Each address has an associated IMD. In this line, we are taking the previous variable of addresses sorted by latest date, and are further filtering by taking the `first_for_patient()`. This can be thought of as single-column tables. The `.index_of_multiple_deprivation_rounded` returns the raw IMD value rounded. 

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a1_multiple2_dataset_definition.csv') }}

### Latest IMD
This is similiar to the previous variable but instead of taking the first IMD value by date, we are taking the last. 

### Has IMD increased
Now we are creating a variable called `imd_has_increased` which takes the two previous variables of `earliest_imd` and `latest_imd` and compares them to see if latest is larger than earliest. This introduces us to the comparison operators available in ehrQL. You might already be familiar with some, such as `<`, `>`, `==`.

In this case, values of the two IMD *columns* are compared for each patient row.

This comparison can be thought of as a new single-column table,
indicating whether the IMD has increased from earliest to latest date,
represented by one of the Boolean values, `True` or `False`:

{{ read_csv('databuilder/ehrql-tutorial-examples/outputs/3a2_multiple2_dataset_definition.csv') }}

### IMD over 5000
We are creating the final variable we need for our population, finding people with IMD equal to or greater than 5000. Instead of comparing the values of two columns in each row, we compare the "latest" IMD to the *integer* `5000`.

Integers in ehrQL are written as numbers without a decimal point. This again should return a True or False. 

This introduces us to the two different types of numbers in ehrQL. 

* `int`: to represent integers
* `float`: to represent real numbers

ehrQL is currently strict when comparing numeric types:
only integers can be compared to integers,
and floating point numbers ("floats") to other floats.

Data Builder will give an error
if you try to compare incompatible types in your dataset definition.

The [Contracts reference](contracts-reference.md) tells you
which data type each table column has.
This tells you what kinds of values and columns you can directly compare with.

If you need to convert values in columns,
as a temporary fix,
then you can use: `.as_int()` and `.as_float()`.

### Constructing the population logical
We have now created all the variables that we need to construct our population. Remember we are aiming to get people born before 2000, whose IMDs have increased or whose latest IMD is greater than 5000. 

Logical operators combine Boolean values together to give a single Boolean value.
ehrQL has the following logical operators that you might already be familiar with:

* `&` to represent `AND`
    * `a & b` is `True` when both `a` and `b` are `True`
* `|` to represent `OR`
    * `a | b` is `True` when either or both of `a` and `b` are `True`
* `¬` to represent `NOT`
    * `¬a` is `True` when `a` is `False`.

With ehrQL,
these, like the comparison operators, are applied per table row,
resulting in a table as output.

In this tutorial dataset definition, we combine multiple logical expressions.
The parentheses around each logical expression make the intent clearer.
The parentheses also ensure the order of evaluation:
each expression in parentheses is evaluated before combining them together.

The logical operators are used to combine the criteria
for patients to include in the population,
as mentioned above in the [summary](#summary).
In this dataset definition, we use:

* `|` to specify that we want either an increased IMD,
  or an IMD greater than a specified value.
* `&` to then specify we want to match the previous IMD criteria
  *and* certain values of year of birth.

The value of this variable is True or False as patients either meet the criteria or they do not. 

### Set population 
Now we take the `population` variable created above and pass this into our `set_population()`. This restricts the population to patients who have the value True in the variable `population`. 

### Adding sex column

Finally, we add multiple columns to our dataset,
as we have done in previous dataset definitions.

We add sex as have previously in the tutorial. 

### Adding hospitalisation column

We are interested in if a patient ever has been admitted to hospital.
This is inferred by the presence of a row in the `hospitalisations` table.
To check for the presence of a row,
we can use the `exists_for_patient()` method on a table.
This results in a Boolean column indicating whether any rows exist.

## Your turn
Run the dataset definition. 

!!! question
    1. What do you think would if you compare the IMD values for patients
       to the floating point value `5000.0`,
       instead of the integer value `5000`?
       Modify the dataset definition to check if you are correct.
    2. Can you further restrict the population to those patients who have a postcode?
    3. Can you change a single line of this dataset definition
       so that the patient population selection is *inverted*?
       Specifically, all patients previously selected are now not selected,
       and all patients previously unselected are now selected.
    4. Can you change the population to include only patients born before 2000 and hospitalised? Ignore IMD for now. 
    5. Can you add IMD value as a column?
    6. Can you change the population to find only hospitalised males? Ignore IMD and age. 
