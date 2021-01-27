
This section covers how to develop, run, and test your code to ensure it will work end-to-end within the secure framework.

## General code-writing guidance

Generally-speaking, you can write whatever code you like as long as it will run successfully on server, and it is possible to [test this locally](pipelines.md#running-your-code-locally).
However, note the following restrictions and guidance:

* **Write analyses in Python, R, or Stata.**
You can can use more than one language in a single project if necessary.  You can find more information about the available libraries [here](pipelines.md#execution-environments).
* **Do not write code that requires an internet connection to run.**
Any research objects (datasets, libraries, etc) that are retrieved via the internet should be imported to the repo locally first.
If this is not possible (for instance if the object size is too large to be transferred via GitHub) then get in touch.
* **Avoid code that consumes a lot of time or memory.** The server is not an infinite resource. We can advise on code optimisation if run-times become problematic.  A good strategy is to split you processing into separate project pipeline actions; the job runner can then choose to run them in parallel if sufficient resources are available.
* **Write code that runs across different platforms.**
Since code will be run both locally and within a Linux-based Docker environment. For example use forward-slashes `/` for directories.
* **Structure your code into discrete chunks, both within scripts, and by splitting into different pipeline actions.**
This helps with:
	* readability
	* bug-finding
	* parallelisation via the project pipeline

## Project pipelines

The [cohortextractor](cohortextractor.md) section describes how to write commands to generate dummy datasets based on the instructions [defined in your `study_definition.py` script](study-def.md).
These dummy datasets are the basis for developing the analysis code that will eventually be passed to the server to run on real datasets.
The code can be written and run on your local machine using whatever development set up you prefer (e.g., developing R in RStudio).
However, it's important to ensure that this code will run successfully in OpenSAFELY's secure environment too, using the specific language and package versions that are installed there. To do this, you should use the Project Pipeline.

The project pipeline, defined entirely in a `project.yaml` file, is a system for executing your code using a series of _actions_ i.e., a discrete analytical step within the analysis, each of which may depend on previous actions.

The primary purpose of the pipeline is to specify the execution order for all your code, so that it can be automatically run and tested from start to finish using dummy data and using the live database in the secure environment, using an identical software configuration.
Arranging your code like this also has several other advantages:

- The pipeline knows if outputs for given actions already exist, and by default skips running them if so. This greatly speeds up the debugging cycle when testing against live data
- In production, actions that can be executed in parallel will be, automatically
- Thinking about your analysis in terms of actions makes it more readable and therefore easier to review and test. For example, being explicit about what the inputs and outputs of each actions are ensures you don't overwrite files by accident.
- The pipeline forces you to declare which outputs may be more or less disclosive.

### `project.yaml` format

The project pipeline is defined in a single file, `project.yaml`, which lives in the repository's root directory. 
It is written using a configuration format called [YAML](https://yaml.org/), which uses indentation to indicate groupings of related variables.

A simple example of a `project.yaml` is as follows:

```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:

  generate_study_population:
    run: cohortextractor:latest generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv

  run_model:
    run: stata-mp:latest analysis/model.do
    needs: [generate_study_population]
    outputs:
      moderately_sensitive:
        model: models/cox-model.txt
		figure: figures/survival-plot.png
```

This example declares the pipeline `version`, the `population_size` for the dummy data, and two actions, `generate_study_population` and `run_model`.

You only need to change `version` if you want to take advantage of features of newer versions of the pipeline framework.

The `generate_study_population` action will create the highly sensitive `input.csv` dataset.
It will be dummy data when run locally, and will be based on real data from the OpenSAFELY database when run in the secure environment.
The `run_model` action will run a Stata script called `model.do` based on the the `input.csv` created by the previous action.
It will output two moderately sensitive files `cox-model.txt` and `survival-plot.png`, which can be checked and released if appropriate.


Every `project.yaml` requires a `version`, `expectations`, and `actions` section.
In general, actions are composed as follows:

* Each action must be named using a valid YAML key (you won't go wrong with letters, numbers, and underscores) and must be unique.
* Each action must include a `run` key which includes an officially-supported command and a version (`latest` will always select the most recent version, but following initial development you should specify the version to ensure reproducibility).
	* The `cohortextractor` command has the same options as described in the [cohortextractor section](cohortextractor.md).
	* The `python`, `r`, and `stata-mp` commands provide a locked-down execution environment can take one or more `inputs` which are passed to the code.
* Each action must include an `outputs` key with at least one output, classified as either `highly_sensitive` or `moderately_sensitive`
	* `highly_sensitive` outputs are considered potentially highly-disclosive, and are never intended for publishing outside the secure environment
	* `moderately_sensitive` outputs are automatically copied to the secure review area for redaction (otherwise known as [Level 4](security-levels.md)) and potentially for publication back to Github.
* Each action can include a `needs` key which specifies a list of actions (contained within square brackets and separated by commas) that are required for it to successfully run. When an action runs, the `outputs` of all its `needs` actions are copied to its working directory. `needs` actions can be defined anywhere in the `project.yaml`, but it's more readable if they are defined above.

When writing and running your pipeline, note that:

* All file paths must be declared relative to the repository's root directory. So for example use `outputs/figures/`, not `C:/users/elvis/documents/myrepo/outputs/figures`.

* File paths are case-sensitive as everything is run inside a Linux Docker container.

* The location of each action's output is determined by the underlying code that the action invoked, not by the value of the `outputs` configuration. The purpose of `outputs` is to label the disclosivity of each output and indicate that it should be stored securely &mdash; **any outputs not labelled will not be saved.**

* Each action is run in its own isolated environment in a temporary working directory. This means that all the necessary libraries and data must be imported within the script for each action &mdash; For R users, this essentially means that the R is restarted for each action.

* If one or more dependencies of an action have not been run (i.e., their outputs do not exist) then these dependency actions will be run first. If a dependency has changed but has not been run (so the outputs are not up-to-date with the changes), then the dependency actions will not be run, and the dependent actions will be run using the out-of-date outputs.


## Execution environments

OpenSAFELY currently supports Stata, Python, and R for statistical analysis.

For security reasons, available libraries are restricted to those provided by the framework, though you can [request additions](requests-packages.md).

The framework executes your scripts using Docker images which have been preloaded with a fixed set of libraries. 
These Docker images have yet to be optimised; if you have skills in creating Dockerfiles and would like to help, get in touch!

### Stata

We currently package version 16.1, with `datacheck`, `safetab`, and `safecount` libraries installed; when installed, new libraries will appear [in the stata-docker Github repository](https://github.com/opensafely/stata-docker/tree/master/libraries).

As Stata is a commercial product, and the image incorporates our license key, the Docker image and [Github repository](https://github.com/opensafely/stata-docker/) are currently private, pending work to separate the license from the image.
Get in touch if you need to apply your own license and we can accelerate this work.

### Python

The docker image provided is Python 3.8, with [this list of packages installed](https://github.com/opensafely-core/python-docker/blob/main/requirements.txt).

### R

The R image provided is R 4.0, with [this list of libraries installed](https://github.com/opensafely-core/r-docker/blob/master/Dockerfile#L30). 
Currently our configuration doesn't list the precise versions of the libraries. 
If you need this, get in touch and we will accelerate this work.


## Running your code locally

Whilst you can develop and run code locally using your own installations of R, Stata or Python, it's important to check that these will also successfully run on the real data in an identical execution environment.

The `opensafely run` command will execute one or more actions according to the `project.yaml`.
To see its options, type `opensafely run --help`.

For `opensafely run` to work:

* You need to have both [Python](install-python) and [Docker](install-docker.md) installed.
* The Docker daemon must be running on your machine:
  * For Windows users using Docker Desktop, there should be a Docker icon in your system tray.
  * For Mac users using Docker Desktop, there should be a Docker icon in the top status bar.
* You _may_ need credentials for our docker registry (for example, if you are running Stata actions, which require a licensed version). If you have access, you can see [instructions for this here](https://github.com/opensafely/server-instructions/blob/master/docs/Server-side%20how-to.md#log-in-to-docker).

To run the first action in the example above, using dummy data, you can use:

```bash
opensafely run generate_study_population
```

This will generate the `input.csv` file as explained in the [cohortextractor](cohortextractor.md) section.

To run the second action you can use:

```bash
opensafely run run_model
```

It will create the two files as specified in the `analysis/model.do` script.

To force the dependencies to be run you can use for example `opensafely run run_model --force-run-dependencies`, or `-f` for short. 
This will ensure for example that both the `run_model` and `generate_study_population` actions are run, even if `input.csv` already exists.

To run all actions, you can use a special `run_all` action which is created for you (no need to define it in your `project.yaml`):

```bash
opensafely run run_all
```

Each time an action is run, logging information about your run will be put into the  `metadata/` folder. 
If any of your actions fail, you may find clues here as to why.


<details>
  <summary>Click here for information on the exact steps that occur when each job is run locally</summary>

What happens:

1. A new, empty temporary directory for the job is created
2. Any files in the local repo that _do not_ match the output patterns in the `project.yaml` are copied into the temporary folder
3. Any output files from the job's dependencies are copied into the temporary folder
4. The job is run
5. All the files matching the specified output patterns are copied into the local repo
6. The log files for the job are saved into the `metadata/` directory
7. The temporary directory is deleted

</details>


## Running your code with GitHub actions

Every time you create a pull request to merge a development branch onto the main remote branch, GitHub will automatically run a series of tests on the code; specifically, that your codelists are up-to-date, and that `run_all` completes successfully.
Depending on your settings, you may receive email notifications about the results of these tests.
You can view the tests, including any errors or failures, by going to the pull request page on GitHub and clicking the `checks` tab.

You can re-run these tests by clicking the `re-run jobs` button.


## Running your code on the server

To run code for real in the production environment, use the [https://jobs.opensafely.org](https://jobs.opensafely.org) site.
Here you can see (even without a login) all the ongoing projects within OpenSAFELY, and the specific _jobs_ that have been run on the server.
To submit jobs (i.e., to run actions), the general process is as follows:

*  **Log in** using your GitHub credentials (this should happen automatically if you have access to the OpenSAFELY GitHub organisation).
* **Create a workspace** (or select an existing workspace):
	* click the `Add a New WorkSpace` button
	* choose a name, for example the name of the repo
	* select a database to run against (either dummy data, real data, or a small sample of the real data)
	* select the repo and branch that you want to run actions with
	* click `Submit`.
*  **Select actions** to run:
	* select the actions you want to run by clicking the `Run` buttons
	* if any of these actions have dependencies then they will also be run, unless their outputs already exist
	* dependencies can be viewed by clicking the `Needs` button
	* you can force dependencies to be run by clicking `Force run dependencies`, even if those actions have already been run
	* when you're ready, click `Submit`.

The workspace is available at `https://jobs.opensafely.org/<WORKSPACE_NAME>/`.
You can view the progress of these actions by click the `Logs` button from the workspace, or going to `https://jobs.opensafely.org/<WORKSPACE_NAME>/logs`.

<details>
<summary>Click here for information on the exact steps that occur when each job is run on the server</summary>

What happens:

1. A new, empty temporary directory for the job is created
2. Copy in all files on the selected branch
3. The job is run
4. All the files matching the specified output patterns are copied into the local repo
5. The log files for the job are saved into the `metadata/` directory
6. The temporary directory is deleted
</details>

The job will either succeed or fail. 
In either case, the output and log files are only visible in the secure environment to avoid disclosure of potentially sensitive information.


### Accessing the outputs

Only users with access to Level 4 can view output files that are labelled as moderately sensitive and the automatically created log files of the run.

For security reasons, they will be in a different directory than if you had run locally. For the TPP backend, outputs labelled `moderately_sensitive` in the `project.yaml` will be saved in `D:/Level4Files/workspaces/<NAME_OF_YOUR_WORKSPACE>`. These outputs can be [reviewed on the server](releasing-files.md) and released via GitHub if they are deemed non-disclosive.

Outputs labelled `highly_sensitive` are not visible.

#### If you have Level 3 access

No data should ever be published from the Level 3 server. Access is only for permitted users, for the purpose of debugging problems in the secure environment.

Highly sensitive outputs can be seen in `E:/high_privacy/workspaces/<WORKSPACE_NAME>`. This includes a directory called `metadata`, containing log files for each action e.g. `generate_chorts.log`, `run_model.log`.

Moderately sensitive outputs can be seen in `E:/FILESFORL4/workspaces/<WORKSPACE_NAME>`.


## Running your code manually in the server

This is only possible for people with Level 3 access. You'll want to refer to [instructions for interacting with OpenSAFELY via the secure server](https://github.com/opensafely/server-instructions/blob/master/docs/Server-side%20how-to.md) (in restricted access repo).

The live environment is set up via a wrapper script; instead of `cohortextractor`, you should run `/e/bin/actionrunner.sh`.
For example, to run `run_model` on the Level 3 server, against the `full` database, you'd type:

```bash
/e/bin/actionrunner.sh run full run_model tpp
```



---8<-- 'includes/glossary.md'
