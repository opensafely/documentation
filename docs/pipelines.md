
This section covers how to run and test your code, including generating datasets using Study Definitions and analysing that data with R, Stata, or Python.

The [cohortextractor](cohortextractor.md) section describes how to generate dummy datasets with the `cohortextractor generate_cohorts` command using the instructions in a `study_definition.py` script.
These dummy datasets are the basis for developing the analysis code that will eventually be passed to the server to run on real datasets. 
The code can be written and run on your local machine using whatever development set up you prefer (e.g., developing R in RStudio).
However, it's important to ensure that this code will run successfully in OpenSAFELY's secure environment too, using the specific language and package versions that are installed there. 

To do this, you should use the Project Pipeline.

## Project pipelines

The Project Pipeline is a system for executing your code using a series of _actions_ i.e., a discrete analytical step within the analysis, each of which may depend on previous actions. 

The primary purpose of the pipeline is to specify the execution order for all your code, so that it can be automatically run and tested from start to finish both using dummy data and in the ecure environment.
Arranging your code like this also has several other advantages:

- For slow actions, you can use previously-generated outputs rather than running them again
- In production, actions that can be executed in parallel will be, automatically
- Thinking about your analysis in terms of actions makes it more readable and therefore easier to review and test. For example, being explicit about what the inputs and outputs of each actions are ensures you don't overwrite files by accident.
- The pipeline forces you to declare which outputs may be more or less disclosive.

### `project.yaml` format

The project pipeline is defined in a single file, `project.yaml`, which lives in the repository's root directory.

A simple example of a `project.yaml` is as follows:

```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:

  generate_cohorts:
    run: cohortextractor:1.11.0 generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv
		
  run_model:
    run: stata-mp:latest analysis/model.do
    needs: [generate_cohorts]
    outputs:
      moderately_sensitive:
        model: models/cox-model.txt
		figure: figures/survival-plot.png
```

This example declares the pipeline `version`, the `population_size` for the dummy data, and two actions, `generate_cohorts` and `run_model`.

The `generate_cohorts` action will create the highly sensitive `input.csv` dataset. 
It will be dummy data when run locally, and will be based on real data from the OpenSAFELY database when run in the secure environment. 
The `run_model` action will run a Stata script called `model.do` based on the the `input.csv` created by the previous action. 
It will output two moderately sensitive files `cox-model.txt` and `survival-plot.png`, which can be checked and released if appropriate.


Every `project.yaml` requires a `version`, `expectations`, and `actions` section.
In general, actions are composed as follows:
* Each action must be named using a valid YAML key (you won't go wrong with letters, numbers, and underscores) and must be unique.
* Each action must include a `run` key which includes an officially-supported command and a version (`latest` will always select the most recent version, but following initial development you should specify the version to ensure reproducibility). 
	* The `cohortextractor` command has the same options as described in the [cohortextractor section](cohortextractor.md), though the `expectations-population` option should not be used.
	* The `python`, `r`, and `stata-mp` commands provide a locked-down execution environment can take one or more `inputs` which are passed to the code.
* Each action must include an `outputs` key with at least one output, classified as either `highly_sensitive` or `moderately_sensitive`
	* `highly_sensitive` outputs are considered potentially highly-disclosive, and are never intended for publishing outside the secure environment
	* `moderately_sensitive` outputs are automatically copied to the secure review area for redaction (otherwise known as [Level 4](workflow-security-levels.md)) and potentially for publication back to Github.
* Each action can include a `needs` key which specifies a list of actions (contained within square brackets and separated by commas) that are required for it to successfully run. The actions must be defined elsewhere in the `project.yaml` but do not necessarily have to be defined above.

All file paths must be declared relative to the repository's root directory. So for example use `outputs/figures/`, not `C:/users/elvis/documents/myrepo/outputs/figures`.

The location of each action's output is determined by the underlying code, not by `outputs`.
The purpose of `outputs` is to label the disclosivity of each output &mdash; **any outputs not labelled will be deleted.**

## Running your code locally

The `cohortextractor run` command will execute one or more actions according to the `project.yaml`. 
To see its options, type `cohortextractor run --help`.

For `cohortextractor run` to work, you need at least version `1.6.1` and docker. 
You _may_ need credentials for our docker registry (for example, if you are running Stata actions, which require a licensed version).

This command will create outputs in the location specified by the outputs

To run the first action in the example above, using dummy data, you can use:

```
cohortextractor run dummy generate_cohorts expectations
```

This will generate the `input.csv` file as explained in the [cohortextractor](cohortextractor.md) section. 

To run the second action you can use:
```
cohortextractor run dummy run_model expectations
```
As this action depends on the `generate_cohorts` action, it will cause `generate_cohorts` to be run first, followed by `run_model`.
It will create the two files 

To run all actions, you can use `run_all`:
```
cohortextractor run_all dummy run_model expectations
```

## Running your code with GitHub actions

Every time you create a pull request to merge a development branch onto the main remote branch, GitHub will automatically run a series of tests on the code.
Depending on your settings, you may receive email notifications about the results of these tests.
You can view the tests, including any errors or failures, by going to the pull request page on GitHub and clicking the `checks` tab.
You can re-run these tests by clicking the `re-run jobs` button. 

## Running your code on the server

To run code for real in the production environment, use the [https://jobs.opensafely.org](https://jobs.opensafely.org) site.
Here you can see (even without a login) all the ongoing projects within OpenSAFELY, and the specific _jobs_ (or actions) that have run on the server.
To submit a job, the general process is as follows:

*  **Login** using your GitHub credentials (this should happen automatically if you have access to the OpenSAFELY GitHub organisation). 
* **Create a workspace** (or select an existing workspace):
	* click the `Add a New WorkSpace` button
	* choose a name, for example the name of the repo
	* select a database to run against (either dummy data, real data, or a small sample of the real data)
	* select you repo and branch
	* click `Submit`.
*  **Select actions** to run:
	* select a many actions as you like by clicking the `Run` buttons
	* any actions with dependencies will also be run, unless they have already been run
	* dependencies can be viewed by clicking the `Needs` button
	* you can force dependencies to be run by clicking `Force run dependencies`, even if those actions ave already been run
	* when you're ready, click `Submit`.

The workspace is available at `https://jobs.opensafely.org/<WORKSPACE_NAME>/`.
You can view the progress of these actions by click the `Logs` button from the workspace, or going to `https://jobs.opensafely.org/<WORKSPACE_NAME>/logs`.

If the actions run successfully, the outputs will be created on the server.
These will be in a different directory than if you had run locally. 

For those with Level 4 access:

* outputs labelled `moderately_sensitive` in the `project.yaml` will be saved in `D:/Level4Files/workspaces/<NAME_OF_YOUR_WORKSPACE>`
* outputs labelled `highly_sensitive` are not visible

For those with Level 3 access:
* all outputs will be saved in `E:/high_privacy/workspaces/<WORKSPACE_NAME>`
* there's also a directory called `metadata`, containing log files for each action e.g. generate_chorts.log, run_model.log

These outputs can be reviewed on the server and released via GitHub if they are deemed non-disclosive. 
There are detailed reviewing guidelines for approved researchers.

## Running your code manually in the server

This is only possible for people with level 3 access.

The live environment is set up via a wrapper script; instead of `cohortextractor`, you should run `/e/bin/actionrunner.sh`.
For example, to run `run_model` on the Level 3 server, against the `full` database, you'd type:

```
/e/bin/actionrunner.sh run full run_model tpp
```
