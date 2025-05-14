## Background

Data extracts often use an "index date" to define variables such as age, or presence of comorbidities at the start of a study.
This can either be a fixed date (e.g. "2020-02-01") or a date that varies between patients, also known as dynamic dates (e.g. the date that people were hospitalised).
However, some studies that use dynamic index dates for a "case" population and then have a matched "control" comparator group.
Because the control group by definition doesn't have the event of interest, the convention is for them to inherit the index date from their matched "case".
The process to extract data for such a matched case-control population in OpenSAFELY is described below.

!!! warning

    At present, only the [OpenSAFELY TPP backend](data-sources/systmone.md) supports case-control studies.

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
Here, the dataset definition's suffix is `cases`, so the corresponding output file will be named `dataset_cases.csv.gz`.

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  extract_cases:
    run: ehrql:v1 generate-dataset analysis/dataset_definition_cases.py --output output/dataset_cases.csv.gz
    outputs:
      highly_sensitive:
        dataset: output/dataset_cases.csv.gz
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
    run: ehrql:v1 generate-dataset analysis/dataset_definition_potential_controls.py --output output/dataset_potential_controls.csv.gz
    outputs:
      highly_sensitive:
        dataset: output/dataset_potential_controls.csv.gz
```

## Match the cases to the potential controls

In this step, we will use the [OpenSAFELY matching library](https://github.com/opensafely-core/matching#readme) in [a scripted action](actions-scripts.md) to match the cases to the potential controls.
We will name this scripted action `match.py`.
Whilst the OpenSAFELY matching library can output multiple files, we will use two: `matching_report.txt` and `matched_matches.csv.gz`.
The former contains information about the matching process.
The latter contains the matched controls.

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  matching:
    run: python:v2 python analysis/match.py
    needs: [extract_cases, extract_potential_controls]
    outputs:
      moderately_sensitive:
        matching_report: output/matching_report.txt
      highly_sensitive:
        matched_matches: output/matched_matches.csv.gz
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

In this step, we will construct a third study definition to extract only the non-matching data for the matched controls.
We will name this study definition `study_definition_controls.py`.

We will use the functions `patients.which_exist_in_file` and `patients.with_value_from_file`.
We will use `patients.which_exist_in_file` to include only the matched controls in the population:

```python
from cohortextractor import StudyDefinition, patients

CONTROLS = "output/matched_matches.csv.gz"

study = StudyDefinition(
    index_date="2021-01-01",  # Ignored
    population=patients.which_exist_in_file(CONTROLS),
)
```

We will use `patients.with_value_from_file` to access the case index dates:

```python
from cohortextractor import codelist_from_csv, StudyDefinition, patients

CONTROLS = "output/matched_matches.csv.gz"
codelist = codelist_from_csv("codelists/codelist.csv")

study = StudyDefinition(
    index_date="2021-01-01",  # Ignored
    population=patients.which_exist_in_file(CONTROLS),
        case_index_date=patients.with_value_from_file(
        CONTROLS,
        returning="case_index_date",
        returning_type="date",
    ),
    has_event_in_codelist=patients.with_these_clinical_events(
        codelist,
        on_or_after="case_index_date",
    ),
)
```

Our `project.yaml` now includes the following action:

```yaml
# ...
actions:
  # ...
  extract_controls:
    run: cohortextractor:latest generate_cohort --study-definition study_definition_controls --output-format csv.gz
    needs: [matching]
    outputs:
      highly_sensitive:
        cohort: output/input_controls.csv.gz
```

## Analysis

Finally, we will construct one or more [scripted](actions-scripts.md) or [reusable](actions-reusable.md) actions to undertake our analysis.
