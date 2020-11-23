This documentation is very much first draft and is here just to (maybe) get you going!

# Overview

The Project Pipeline is a system for executing your code in discrete stages, each of which may depend on previous stages. If you are coming from an older version of OpenSAFELY, it replaces the function of `model.do`, which is no longer required.

Arranging your analysis like this has several advantages:

- During development, for slow steps, you can use previously-generated outputs rather than running them again
- In production, steps that can be executed in parallel will be, automatically
- Thinking about your analysis in terms of several steps makes it more readable and therefore easier to review and test. For example, being explicit about what the inputs and outputs of each step are forces you to ensure you don't overwrite data files by accident; the pipeline also forces you to declare which outputs may be more or less disclosive

## `project.yaml` format

To use the framework, your project _must_ have a file named `project.yaml` in its root directory.

It must include a `version`, an `expectations` section, and at least one `action` - for example:

```yaml
version: "3.0"

expectations:
  population_size: 1000

actions:
  generate_cohorts:
    run: cohortextractor:1.3.8 generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv
```

The action can be called anything that is a valid YAML key, (e.g. no spaces). Here it is called `generate_cohorts`.

Each action must contain a `run` command. This must be an officially-supported action (currently `stata-mp`, `python`, `r`, and `cohortextractor`), and it must include a version (`latest` will always select the most recent version, but following initial development you should always specify the version to ensure reproducibility).

Each action must include an `outputs` section with at least one output. Here there is one `highly_sensitive` output called `cohort`, which is written to `output/input.csv`.

`highly_sensitive` outputs are outputs you consider potentially highly-disclosive, and would never consider publishing outside the secure environment.

You can also have `moderately_sensitive` outputs. These are automatically copied to the secure review area for redaction (this is the server we currently call Level 4) and potentially for publication back to Github.

Apart from the initial `cohortextractor` action, which runs your study definition, all other actions are expected to have inputs. Here is an action which expects the outputs of `generate_cohorts` as its inputs, and writes its outputs to the secure review area. The key addition is the new `needs` line; the `model.do` script would typically start by loading a file it expects to exist at `output/input.csv`:

```yaml
run_model:
  run: stata-mp:latest analysis/model.do
  needs: [generate_cohorts]
  outputs:
    moderately_sensitive:
      log: logs/model.log
```

## `run` commands

Each `run` command (`stata-mp`, `python`, `r`) provides a locked-down execution environment. You can't install new libraries yourself.

In lieu of comprehensive documentation about installed dependencies, the following links should provide you with clues about what is available:

- [R](https://github.com/opensafely/r-docker/blob/master/Dockerfile#L34-L79)
- [Python](https://github.com/opensafely/jupyter-docker/blob/master/requirements.txt)
- [Stata](https://github.com/opensafely/stata-docker/tree/master/libraries)

# Testing your `project.yaml`

The `cohortextractor run` subcommand will execute your actions according to the `project.yaml`. To see its options, type `cohortextractor run --help`.

For `cohortextractor run` to work, need at least version 1.6.1; you must also
[install Docker](install-docker.md); and you _may_ need credentials for our
docker registry (for example, if you are running Stata actions, which require a
licensed version).

To run the single action in the example above, using dummy data, you would typically run:

    cohortextractor run dummy generate_cohorts expectations

By default, this is a `test` mode and throws away any generated outputs after running; investigate the `--medium-privacy-storage-base` and `--high-privacy-storage-base` options if you want to keep the outputs.

If you run an action that depends on other actions, the framework will run them
in the correct order. For example, this will cause `generate_cohorts` to be run first, follwed by `run_model`:

    cohortextractor run dummy run_model expectations

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

The official way of executing actions in the production environment is via [https://jobs.opensafely.org](https://jobs.opensafely.org). However, while this is under fast development, it may be easier for users with access to a level 3 server to run actions from the command line.

In the examples above, `dummy` refers to the database flavour you'd like to run against. In production, the default is to run against the `full` flavour; all our backends also support a `slice` flavour which is a cut-down subset of the real data which can be useful for testing against (because it takes less time to query).

The live environment is set up via a wrapper script; instead of `cohortextractor`, you should run `/e/bin/actionrunner.sh`.

For example, to run `run_model` on the Level 3 server, against the `full` database, you'd type:

    /e/bin/actionrunner.sh run full run_model tpp
