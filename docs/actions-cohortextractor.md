
`cohortextractor` is an action provided by the OpenSAFELY framework. Every pipeline will start with this as its first action.
It is used to convert the study definition into an actual analysis-ready dataset based on dummy or real data.

The dataset it creates can be either:

* A dummy dataset used for developing and testing analysis code on the user's own machine.
  Users have control over the characteristics of each dummy variable, which are defined inside the study definition.
* A real dataset created from the OpenSAFELY database, used for the analysis proper.
  Real datasets never leave the secure server, only summary data and other outputs that are derived from them can be released (after disclosivity checks).

`cohortextractor` also performs some other tasks, like creating [Measures](measures.md), and many of the functions that are needed within a study definition script.


## Installing `cohortextractor`

**In most cases you won't need to install `cohortextractor` directly**.
Instead, you create an action in your [project.yaml](actions-pipelines.md#project-yaml-format) file and run it via `opensafely run <action>`.
This will use `cohortextractor` via a Docker image rather than a local installation.

<details>
  <summary>If you need to install, follow these instructions</summary>


Go to the Anaconda prompt and run the following command (or use another method to install the module if you know how):

```
pip install opensafely-cohort-extractor
```

To check this has installed successfully, run:

```
cohortextractor --version
```

If you need to install a new version, update with:

```
pip install --upgrade opensafely-cohort-extractor
```

</details>


## Using `cohortextractor` in the `project.yaml`

Typically, you will be writing `cohortextractor` commands inside the `project.yaml` and executing them using the `opensafely run` command.
The available `cohortextractor` commands and how they are declared in the `project.yaml` are detailed below.


### `generate_cohort`
This is the command used to generate a dataset from the study definition.

A basic `generate_cohort` action looks like this:

```yaml
generate_study_cohort
  run: cohortextractor:latest generate_cohort --output-format=csv.gz
  outputs:
    highly_sensitive:
      data: output/input.csv.gz
```

Running the action with `opensafely run generate_study_population` will create the file `output/input.csv.gz`. The file is compressed by default to reduce storage space required and improve performance in the backend.  If you need to view the csv locally for debugging your code, running `gunzip output/input.csv.gz` in a terminal (use git-bash in windows) should give you a plain `.csv` to view.

The size of the dummy dataset is determined by the `population_size` option [in the `project.yaml`](actions-pipelines.md#project-yaml-format).

Running the action again will overwrite the existing dataset with a new one (check the file's _modified_ date) which will contain different data than previously (even if the `study_definition.py` didn't change) because the values are randomly generated.
Beware that on Windows, you can't have `input.csv.gz` open and generate a new one at the same time.

If you have multiple study definitions in the repo (e.g., `study_definition_cohort1.py` and `study_definition_cohort2.py`) then `generate_cohort` will by default create a dataset for each and name them appropriately (e.g., `input_cohort1.csv.gz` and `input_cohort2.csv.gz`).
You can restrict the command to produce a single study definition using the `study-definition` option, like this:


```yaml
generate_study_cohort
  run: cohortextractor:latest generate_cohort --study-definition study_definition_cohort2 --output-format=csv.gz
  outputs:
    highly_sensitive:
      data: output/input_cohort2.csv.gz
      ### This file is produced in compressed format. If using Stata you may need to remove the --output-format option and 
      ### the .gz file extension to produce an uncompressed CSV instead.
```

You can change the location of the outputted `.csv.gz` file using the `--output-dir` option, for example `run: cohortextractor:latest generate_cohort --format csv.gz --output-dir output/cohorts`


---8<-- 'includes/glossary.md'
