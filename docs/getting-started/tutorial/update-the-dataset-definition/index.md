You've successfully generated a dataset from the code in your study, but at the moment it only adds one data column.

Now we'll add some code to create an extra column.

## Add an `age` column

1. The "Explorer" on the left hand side lists the files and folders in
   your research repository. Find and click on the `dataset_definition.py`
   file inside the `analysis` folder. This file contains a dataset definition,
   specifying the population that you'd like to study (dataset rows)
   and what you need to know about them (dataset columns).
   It is written in [ehrQL](../../../ehrql/index.md).
1. Add some text so that the file looks like this (new text highlighted):
```python linenums="1" hl_lines="15"
from ehrql import create_dataset
from ehrql.tables.tpp import patients, practice_registrations

dataset = create_dataset()

index_date = "2020-03-31"

has_registration = practice_registrations.for_patient_on(
    index_date
).exists_for_patient()

dataset.define_population(has_registration)

dataset.sex = patients.sex
dataset.age = patients.age_on(index_date)
```
Lines 8-12 mean "*I'm interested in all patients who were registered at a practice
on the index date*"; line 14 "*Give me a column of data corresponding
to the sex of each patient*"; and line 15 "*Give me a column of data corresponding
to the age of each patient on the given date*".
1. If you run:

   ```shell-session
   $ opensafely exec ehrql:v1 generate-dataset analysis/dataset_definition.py
   ```

   you will see a new randomly generated dataset.

   However, this time it contains the additional `age` column.

---

* Previous: [Generate a first dataset](../generate-a-first-dataset/index.md)
* Next: [Run the project pipeline](../run-the-project-pipeline/index.md)
