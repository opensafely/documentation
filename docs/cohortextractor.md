`cohortextractor` is a Python module built for OpenSAFELY. It provides you with a way of running your scripts that exactly mimics the production environment where real data is accessed.
It contains functions relating to the OpenSAFELY workflow that you can use for development on your own computer when you don't have access to the live data. For example:

* converting the Study Definition into an actual (dummy or real) dataset
* importing codelists from codelists.opensafely.org
* running project piplines
* generating Measures
* plus a few other utility functions



The datasets it creates can be either:

* A dummy dataset used for developing and testing analysis code on
  the user’s own machine. Users have control over the
  characteristics of each dummy variable, which are defined inside
  the study definition.
* A real dataset created from the OpenSAFELY database, used for
  the analysis proper. Real datasets never leave the secure
  server, only summary data and other outputs that are derived
  from them can be released (after disclosivity checks).


## Installing `cohortextractor`

This is a command-line program.

To install, go to the Anaconda prompt and submit the following command (or use another method to install the module if you know how):

```
pip install opensafely-cohort-extractor
```

To check this has installed successfully, submit `cohortextractor --version`.

## Updating `cohortextractor`
If you need to install a new version, update with:

```
pip install --upgrade opensafely-cohort-extractor
```

## Using `cohortextractor` at the command line

To view the in-built documentation for each command, submit `cohortextractor --help` at the terminal, which will list all the ways in which you can use it.
You can also use `cohortextractor generate_cohort --help` to learn more about the `generate_cohort` command, for example.
Some of these commands are discussed in detail below.

To run any of these commands for a specific OpenSAFELY project, you need to change the directory of your prompt to be the repositiory of the project. For example,  `cd C:/Users/me/my-git-repos/my-repo`.

**The rest of this section assumes you have a working OpenSAFELY research repository** &mdash; see the [Project repositories](repositories.md) section for guidance on how to create or clone a research repo.

Your project repo contains a Study Definition (`study_definition.py`) which is used to define the study population and the variables of interest.
Before making any changes to `study_definition.py` to match your study (which will need to be properly version controlled in git), it's important to understand how the study definition is used by `cohortextractor`.
Without `cohortextractor` you won't be able to run and test any changes that you've made to `study_definition.py` or the codelists.


### `run`

The most common command you'll run. This runs actions defined in the `project.yaml` file ([documented here](pipelines.md)), and is the main way of testing your code. For example,

```
cohortextractor run dummy make_graph expectations
```

will run the `make_graph` action using `expectations` (dummy) data.

Typically, the first action defined in your `project.yaml` is `generate_cohort`, which you can also run directly if you want:

### `generate_cohort`
This will create a dummy dataset for you, `outputs/input.csv`, based on the _expectations_ declared in the study definition.
Use it for example like this:

```
cohortextractor generate_cohort --expectations-population 10000
```

where `10000` is the number of rows you want to generate for your dataset.

Running it will create the file `outputs/input.csv`.
Running it again will overwrite the existing dataset with a new one (check the file's _modified_ date) which will contain different data than previously (even if the `study_definition.py` didn't change) because the values are randomly generated.
Beware that on Windows, you can't have `input.csv` open and generate a new one at the same time.

If you have multiple study definitions in the repo (eg `study_definition_cohort1.py`, `study_definition_cohort2.py`) then `generate_cohort` will create dataset for each (eg `input_cohort1.csv`, `input_cohort2.csv`).
You can restrict the command to produce a single study definition using the `study-definition` option, like this:

```
cohortextractor generate_cohort --expectations-population 10000 --study-definition study_definition_cohort2
```


### `update_codelists`
This will retrieve each codelist listed in `/codelists/codelists.txt` from [codelists.opensafely.org](https://codelists.opensafely.org), and save them its latest version in the same folder.

Use it like this:
```
cohortextractor update_codelists
```
Running it will add (or update) the codelist `.csv` files in the `codelists/` folder.
See the [Codelist](codelist-intro.md) section for more information about how to create codelists.

Beware that in Windows, if one or more of these codelist files is open then `update_codelists` won't be able to run.



---8<-- 'includes/glossary.md'
