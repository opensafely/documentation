## Background

A case-control study compares the population with the condition or event of interest with a control population,
matched on specific categorical and/or scalar variables.

We can take advantage of an OpenSAFELY [reusable action](actions-reusable.md), the
[matching](https://actions.opensafely.org/actions/matching) action.
This action takes a dataset of "cases" (i.e. patients with the condition of interest), and a second
dataset of potential controls, both extracted using ehrql dataset definitions. It produces outputs
containing a set of matched control patients which can be incorporated into further analyses.

### Index dates

Data extracts often use an "index date" to define variables such as age, or presence of comorbidities at the start of a study. This can either be a fixed date (e.g. "2020-02-01") or a date that varies between patients, also known as dynamic dates (e.g. the date that people were hospitalised).

Where index dates are dynamic, and defined by the event of interest, the control group cannot by
definition  contain a relevant index date. In this case, the convention is for the control group to
inherit the index date from their matched "case". The [matching reusable action](https://actions.opensafely.org/actions/matching)
provides a number of options for how this "inherited" index date can be generated.

After the control group is extracted by matching on a set
of defined variables, the inherited index date can be used to extract further data for analysis, or to further
narrow down the control population.

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

In this step, we will construct [a dataset definition](./ehrql/tutorial/building-a-dataset/index.md) to extract all the data we need for the cases. The dataset definition will include:

  - an *index date variable*
  - *matching data*, or the variables we will use to match the cases to the potential controls (e.g. we might want to match patients on age and sex); these variables may or may not be used in later analysis.
  - *non-matching data*, or the variables we will use for analysis.

To avoid duplicating code to extract the matching data and the non-matching data in this and the following steps,
we could use separate Python scripts to share common variables or parametrise the dataset definition.

As we will construct multiple dataset definitions in this and the following steps,
we will name this dataset definition `dataset_definition_cases.py`.

When working with multiple dataset definitions, it is good practice to use the same suffix to name each corresponding output file.
Here, the dataset definition's suffix is `cases`, so the corresponding output file will be named `dataset_cases.arrow`.

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  extract_cases:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_cases.py --output output/dataset_cases.arrow
    outputs:
      highly_sensitive:
        dataset: output/dataset_cases.arrow
```

## Extract data for the potential controls

The *potential controls* are the group of patients that will be matched to the cases to give the *matched controls*.
In this step, we will construct a second dataset definition to extract just the variables we want to
match the cases on (i.e. the same *matching data* we extracted in the previous dataset definition).

!!! Note
    The dataset definition for the controls does not require an index date variable if it is
    to be generated from the case index date during the matching process.

We will name this dataset definition `dataset_definition_potential_controls.py`.


Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  extract_potential_controls:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_potential_controls.py --output output/dataset_potential_controls.arrow
    outputs:
      highly_sensitive:
        dataset: output/dataset_potential_controls.arrow
```

## Match the cases to the potential controls

In this step, we will use the [OpenSAFELY matching reusable-action](https://actions.opensafely.org/actions/matching) to match the cases to the potential controls.
We will name this scripted action `match.py`.

Whilst the OpenSAFELY matching action can output multiple files, we will use two: `matching_report.txt` and `matched_matches.arrow`.
The former contains information about the matching process.
The latter contains the matched controls.

Our `project.yaml` now includes the following action. Remember to replace [version] with a version of the match reusable action (e.g. v1.1.0):

```yaml
# ...
actions:
  # ...
  matching:
    needs: [extract_cases, extract_potential_controls]
    run: >
      matching:[version]
      --cases output/dataset_cases.arrow
      --cases output/dataset_potential_controls.arrow
    config:
      matches_per_case: 3
      match_variables:
        - age
      index_date_variable: index_date
      generate_match_index_date: no_offset
    outputs:
      moderately_sensitive:
        matching_report: output/matching_report.txt
      highly_sensitive:
        matched_matches: output/matched_matches.arrow
```

See the [OpenSAFELY matching reusable action documentation](https://actions.opensafely.org/actions/matching)
for further information on the available configuration options.

!!! note "Alternatives to the OpenSAFELY matching reusable action"

    Rather than using the OpenSAFELY matching reusable action, you may wish to match the cases to the potential controls by implementing your own algorithm in a scripted action.
    If you do, please note that not all Python, R, or Stata packages are available to you;
    to find out which packages are, see the
    [python-docker](https://github.com/opensafely-core/python-docker),
    [r-docker](https://github.com/opensafely-core/r-docker), or
    [stata-docker](https://github.com/opensafely-core/stata-docker) repositories.
    Alternatively, you can [request new libraries](requesting-libraries.md).

## Extract additional data for the matched controls

In this step, we will construct a third dataset definition to extract only the non-matching data for the matched controls.

We will name this dataset definition `dataset_definition_controls.py`.

We will use the [`table_from_file`](./ehrql/reference/language/#table_from_file) feature in ehrQL to make a table called `matched_patients` from the `matched_matches.arrow` file.
When we are done, `matched_patients` will behave as if it were any other ehrQL table.

Suppose `matched_matches.arrow` has the following columns:

  - `patient_id`
  - `age`
  - `sex`
  - `index_date`

`age` and `sex` are the *matching data* we extracted in the first step, and `index_date` is
the date that the matching action generated from the matched case for each control patient.

We can create `matched_patients` with:
```python
import datetime

from ehrql import table_from_file

CONTROLS = "output/matched_matches.arrow"

matched_patients = table_from_file(
  CONTROLS,
  columns={
    "age": int,
    "sex": str,
    "index_date": datetime.date
  }
)
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

The `index_date` column in `matched_patients` is the date generated by the matching process,
from their matched case index date. We can use it to identify other data of interest.
For example, we might want to see if our matched controls have had a codelist event on or after their case index date.

```python
from ehrql import codelist_from_csv
from ehrql.tables.core import clinical_events

codelist = codelist_from_csv("codelists/codelist.csv")
events_in_codelist = clinical_events.where(
    clinical_events.snomedct_code.is_in(codelist)
)
dataset.has_event_in_codelist = events_in_codelist.where(
    events_in_codelist.date.is_on_or_after(matched_patients.index_date)
).exists_for_patient()
```
The above code snippet assumes that the codelist is a list of SNOMED codes, and is located at `codelists/codelist.csv`.

Putting it all together, our `dataset_definition_controls.py` now looks like this:
```python
import datetime

from ehrql import codelist_from_csv, create_dataset, table_from_file
from ehrql.tables.core import clinical_events


CONTROLS = "output/matched_matches.arrow"
codelist = codelist_from_csv("codelists/codelist.csv")

matched_patients = table_from_file(
  CONTROLS,
  columns={
    "age": int,
    "sex": str,
    "index_date": datetime.date
  }
)

dataset = create_dataset()
dataset.define_population(matched_patients.exists_for_patient())
events_in_codelist = clinical_events.where(
    clinical_events.snomedct_code.is_in(codelist)
)
dataset.has_event_in_codelist = events_in_codelist.where(
    events_in_codelist.date.is_on_or_after(matched_patients.index_date)
).exists_for_patient()
```

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  extract_controls:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_controls.py --output output/dataset_controls.arrow
    needs: [matching]
    outputs:
      highly_sensitive:
        dataset: output/dataset_controls.arrow
```

## Analysis

Finally, we will construct one or more [scripted](actions-scripts.md) or [reusable](actions-reusable.md) actions to undertake our analysis.
