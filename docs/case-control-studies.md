## Background

Data extracts often use an "index date" to define variables such as age, or presence of comorbidities at the start of a study.
This can either be a fixed date (e.g. "2020-02-01") or a date that varies between patients, also known as dynamic dates (e.g. the date that people were hospitalised).
However, some studies that use dynamic index dates for a "case" population and then have a matched "control" comparator group.
Because the control group by definition doesn't have the event of interest, the convention is for them to inherit the index date from their matched "case".
The process to extract data for such a matched case-control population in OpenSAFELY is described below.

There are five steps to undertaking a [case-control study](https://en.wikipedia.org/wiki/Case%E2%80%93control_study) (or [matched cohort study](https://en.wikipedia.org/wiki/Nested_case%E2%80%93control_study)) with OpenSAFELY:

1. Extract data for the cases
2. Extract data for the potential controls
3. Match the cases to the potential controls
4. Extract data for the matched controls
5. Analysis

To begin with, our [`project.yaml`](actions-pipelines.md) looks like this:

```yaml
version: '4.0'

actions:
  # Extract data for the cases
  # Extract data for the potential controls
  # Match the cases to the potential controls
  # Extract data for the matched controls
  # Analysis
```

## Extract data for the cases

In this step, we will construct [a dataset definition](../ehrql/tutorial/building-a-dataset) to extract all the data we need for the cases:
that is, the *matching data*, or the data we will use to match the cases to the potential controls;
and the *non-matching data*, or the data we will use for analysis.

To avoid duplicating code to extract the matching data and the non-matching data in this and the following steps,
we could use separate Python scripts to share common variables or parametrise the dataset definition.

As we will construct multiple dataset definitions in this and the following steps,
we will name this dataset definition `dataset_definition_cases.py`.

When working with multiple dataset definitions, it is good practice to use the same suffix to name each corresponding output file.
Here, the dataset definition's suffix is `cases`, so the corresponding output file will be named `dataset_cases.csv`.

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  extract_cases:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_cases.py --output output/dataset_cases.csv
    outputs:
      highly_sensitive:
        dataset: output/dataset_cases.csv
```

## Extract data for the potential controls

The *potential controls* are the group of patients that are matched to the cases to give the *matched controls*.
In this step, we will construct a second dataset definition to extract only the matching data for the potential controls.

We will name this dataset definition `dataset_definition_potential_controls.py`.


Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  extract_potential_controls:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_potential_controls.py --output output/dataset_potential_controls.csv
    outputs:
      highly_sensitive:
        dataset: output/dataset_potential_controls.csv
```

## Match the cases to the potential controls

In this step, we will use the [OpenSAFELY matching library](https://github.com/opensafely-core/matching#readme) in [a scripted action](actions-scripts.md) to match the cases to the potential controls.
We will name this scripted action `match.py`.

Whilst the OpenSAFELY matching library can output multiple files, we will use two: `matching_report.txt` and `matched_matches.csv`.
The former contains information about the matching process.
The latter contains the matched controls.

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  matching:
    run: python:v1 python analysis/match.py
    needs: [extract_cases, extract_potential_controls]
    outputs:
      moderately_sensitive:
        matching_report: output/matching_report.txt
      highly_sensitive:
        matched_matches: output/matched_matches.csv
```

!!! note "Alternatives to the OpenSAFELY matching library"

    Rather than using the OpenSAFELY matching library, you may wish to match the cases to the potential controls by implementing your own algorithm in a scripted action.
    If you do, please note that not all Python, R, or Stata packages are available to you;
    to find out which packages are, see the
    [python-docker](https://github.com/opensafely-core/python-docker),
    [r-docker](https://github.com/opensafely-core/r-docker), or
    [stata-docker](https://github.com/opensafely-core/stata-docker) repositories.
    Alternatively, you can [request new libraries](requesting-libraries.md).

## Extract data for the matched controls

In this step, we will construct a third dataset definition to extract only the non-matching data for the matched controls.

We will name this dataset definition `dataset_definition_controls.py`.

We will use the `@table_from_file` feature in ehrQL to make a table called `matched_patients` from the `matched_matches.csv` file.
When we are done, `matched_patients` would behave as if it were any other
[`PatientFrame`](../ehrql/reference/language/#PatientFrame)
in ehrQL.

Suppose `matched_matches.csv` has the following columns: `patient_id`, `age`, `sex` and `case_index_date` -
i.e. `age` and `sex` were the *matching data* we extracted in the first step.
We can create `matched_patients` with:
```python
import datetime

from ehrql.query_language import PatientFrame, Series, table_from_file

CONTROLS = "output/matched_matches.csv"

@table_from_file(CONTROLS)
class matched_patients(PatientFrame):
    age = Series(int)
    sex = Series(str)
    case_index_date = Series(datetime.date)
```

This allows us to only include the matched controls in our dataset.
```python
from ehrql import create_dataset

dataset = create_dataset()
dataset.define_population(
    matched_patients.exists_for_patient()
)
```
Don't forget to add additional population constraints to the dataset if you require them!

Since the `case_index_date` column in `matched_patients` is now accessible,
we can use it as the index date for controls (since they by definition don't have an index date).
For example, we might want to see if our matched controls have had a codelist event on or after their case index date.
```python
from ehrql import codelist_from_csv
from ehrql.tables.core import clinical_events

codelist = codelist_from_csv("codelists/codelist.csv")
events_in_codelist = clinical_events.where(
    clinical_events.snomedct_code.is_in(codelist)
)
dataset.has_event_in_codelist = events_in_codelist.where(
    events_in_codelist.date.is_on_or_after(matched_patients.case_index_date)
).exists_for_patient()
```
The above code snippet assumes that the codelist is a list of SNOMED codes, and is located at `codelists/codelist.csv`.

Putting it all together, our `dataset_definition_controls.py` looks like this:
```python
import datetime

from ehrql import codelist_from_csv, create_dataset
from ehrql.query_language import PatientFrame, Series, table_from_file
from ehrql.tables.core import clinical_events


CONTROLS = "output/matched_matches.csv"
codelist = codelist_from_csv("codelists/codelist.csv")


@table_from_file(CONTROLS)
class matched_patients(PatientFrame):
    age = Series(int)
    sex = Series(str)
    case_index_date = Series(datetime.date)


dataset = create_dataset()
dataset.define_population(matched_patients.exists_for_patient())


events_in_codelist = clinical_events.where(
    clinical_events.snomedct_code.is_in(codelist)
)
dataset.has_event_in_codelist = events_in_codelist.where(
    events_in_codelist.date.is_on_or_after(matched_patients.case_index_date)
).exists_for_patient()
```

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  extract_controls:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_controls.py --output output/dataset_controls.csv.gz
    needs: [matching]
    outputs:
      highly_sensitive:
        dataset: output/dataset_controls.csv.gz
```

## Analysis

Finally, we will construct one or more [scripted](actions-scripts.md) or [reusable](actions-reusable.md) actions to undertake our analysis.
