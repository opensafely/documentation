This documentation is very much first draft and is here just to (maybe) get you going!

# Overview

The Project Pipeline is a system for executing your code in discrete stages, each of which may depend on previous stages.

Arranging your analysis like this has several advantages:

* During development, for slow steps, you can use previously-generated outputs rather than running them again
* In production, steps that can be executed in parallel will be, automatically
* Thinking about your analysis in terms of several steps makes it more readable and therefore easier to review and test. For example, being explicit about what the inputs and outputs of each step are forces you to ensure you don't overwrite data files by accident; the pipeline also forces you to declare which outputs may be more or less disclosive

## Requirements

To use the framework, your project *must* have a file named `project.yaml` in its root directory.


It must include a `version`, an `expectations` section, and at least one `action` - for example:

```yaml
version: '3.0'

expectations:
  population_size: 1000

actions:

  generate_cohorts:
    run: cohortextractor:latest generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv
```

The action can be called anything that is a valid YAML key, (e.g. no spaces). Here it is called `generate_cohorts`.

Each action must contain a `run` command. This must be an officially-supported action (currently `stata-mp`, `python`, `r`, and `cohortextractor`), and it must include a version (in the above example, this is `latest`).

Each action must include an `outputs` section with at least one output. Here there is one `highly_sensitive` output called `cohort`, which is written to `output/input.csv`.

`highly_sensitive` outputs are outputs you consider potentially highly-disclosive, and would never consider publishing outside the secure environment.

You can also have `moderately_sensitive` outputs. These are automatically copied to the secure review area for redaction (this is the server we currently call Level 4) and potentially for publication back to Github.

Apart from the initial `cohortextractor` action, which runs your study definition, all other actions are expected to have inputs.  Here is an action which expects the outputs of `generate_cohorts` as its inputs, and writes its outputs to the secure review area. The key addition is the new `needs` line; the `model.do` script would typically start by loading a file it expects to exist at `output/input.csv`:

```yaml

  run_model:
    run: stata-mp:latest analysis/model.do
    needs: [generate_cohorts]
    outputs:
      moderately_sensitive:
        log: logs/model.log
```
# Testing your `project.yaml`

The `cohortextractor run` subcommand will execute your actions according to the `project.yaml`.  To see its options, type `cohortextractor run --help`.

For `cohortextractor run` to work, need at least version 1.6.1; you must also
[install Docker](installing_docker.md); and you *may* need credentials for our
docker registry (for example, if you are running Stata actions, which require a
licensed version).

To run the single action in the example above, using dummy data, you would typically run:

    cohortextractor run dummy generate_cohort expectations

If you run an action that depends on other actions, the framework will run them
in the correct order. This will cause `generate_cohorts` to be run first, then
it will execute `run_model`:

    cohortextractor run dummy run_model expectations

As this is for testing only, normally the outputs are thrown away after the run. You can keep them by supplying a `--local-storage-base` argument.

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

##### (to be added - instruction for specifying which database to run the analysis on i.e. full or sample)

# Running jobs in the production environment

To be added - short version: go to https://jobs.opensafely.org/ - under fast development!
