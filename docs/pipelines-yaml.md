The Project Pipeline is a system for executing your code using a series of _actions_ i.e., a discrete analytical step within the analysis, each of which may depend on previous actions. 

Arranging your analysis like this has several advantages:

- During development, for slow actions, you can use previously-generated outputs rather than running them again
- In production, actions that can be executed in parallel will be, automatically
- Thinking about your analysis in terms of actions makes it more readable and therefore easier to review and test.
For example, being explicit about what the inputs and outputs of each actions are forces you to ensure you don't overwrite data files by accident; the pipeline also forces you to declare which outputs may be more or less disclosive

## `project.yaml` format

To use the framework, your project _must_ have a file named `project.yaml` in its root directory.

It must include a `version`, an `expectations` section, and at least one `action`. For example:

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

Each action is composed as follows:

* Each action can be called anything that is a valid YAML key &mdash; you won't go wrong with letters, numbers, and underscores.
* Each action must include a `run` key containing an officially-supported command &mdash; currently `stata-mp`, `python`, `r`, or `cohortextractor` are supported &mdash; and a version (`latest` will always select the most recent version, but following initial development you should specify the version to ensure reproducibility). 
	* The `cohortextractor` command has the same options as described in the [cohortextractor section](cohortextractor.md), though the `expectations-population` option should not be used.
	* The other commands can take one or more `inputs` which are passed to the code.
* Each action must include an `outputs` key with at least one output, classified as either `highly_sensitive` or `moderately_sensitive`
	* `highly_sensitive` outputs are considered potentially highly-disclosive, and are never intended for publishing outside the secure environment.
	* `moderately_sensitive` outputs are automatically copied to the secure review area for redaction (otherwise known as [Level 4](workflow-security-levels.md)) and potentially for publication back to Github.
* Each action can include a `needs` key containing a list of actions (contained within square brackets and separated by commas) that are required for it to successfully run. The actions must be defined elsewhere in the `project.yaml` but do not necessarily have to be defined above.

In the above example there are two actions, `generate_cohorts` and `run_model`.
The `generate_cohorts` action will create the highly sensitive `input.csv` dataset. This will be dummy data when run locally using the `population_size` parameter to determine the size of the dataset. When run in the secure environment it will be based on real data from the OpenSAFELY database. 
The `run_model` action will run a Stata script called `model.do` based on the the `input.csv` created by the previous action. It will output two moderately sensitive files `cox-model.txt` and `survival-plot.png`, which can be checked and released if non-disclosive.

## `run` commands

Each `run` command (`stata-mp`, `python`, `r`) provides a locked-down execution environment.
You can't install new libraries yourself &mdash; see the [Develop Analysis Scripts](workflow-develop-analysis-scripts.md) section for details on what restrictions are in place.


# Testing your code with `project.yaml`locally

The `cohortextractor run` command will execute your actions according to the `project.yaml`. 
To see its options, type `cohortextractor run --help`.

For `cohortextractor run` to work, you need at least version 1.6.1 and docker. 
You _may_ need credentials for our docker registry (for example, if you are running Stata actions, which require a licensed version).

To run a single action in the example above, using dummy data, you would typically run:

    cohortextractor run dummy generate_cohorts expectations

By default, this is a `test` mode and throws away any generated outputs after running; investigate the `--medium-privacy-storage-base` and `--high-privacy-storage-base` options if you want to keep the outputs.



If you run an action that depends on other actions, the framework will run them in the correct order. 
For example, this will cause `generate_cohorts` to be run first, follwed by `run_model`:

    cohortextractor run dummy run_model expectations

## `run_all`

Currently, the automated tests in Github expect an action `run_all` to exist.

In the research template, it looks like this:

```yaml
run_all:
  needs:
    - run_model
  # In order to be valid this action needs to define a run commmand and some
  # output. We don't really care what these are but the below does the trick.
  # In a future release of the platform, this special action won't need to be
  # defined at all.
  run: cohortextractor:latest --version
  outputs:
    moderately_sensitive:
      whatever: project.yaml
```

Until support for an implicit `run_all` action is built into the framework, you will have to create a `run_all` action yourself, like the above, but changing the `needs` section accordingly.

# Running manually in the production environment

The official way of executing actions in the production environment is via [https://jobs.opensafely.org](https://jobs.opensafely.org). 
However, while this is under fast development, it may be easier for users with access to a level 3 server to run actions from the command line.

In the examples above, `dummy` refers to the database flavour you'd like to run against. 
In production, the default is to run against the `full` flavour; all our backends also support a `slice` flavour which is a cut-down subset of the real data which can be useful for testing against (because it takes less time to query).

The live environment is set up via a wrapper script; instead of `cohortextractor`, you should run `/e/bin/actionrunner.sh`.

For example, to run `run_model` on the Level 3 server, against the `full` database, you'd type:

    /e/bin/actionrunner.sh run full run_model tpp
