
Before making any changes, try to understand the folder structure first.

## Understanding the repo structure

#### `project.yaml`

This file defines how all the components of your analysis can run together, efficiently, on the server, or locally.  This is a brand-new feature, so [the documentation](project-pipelines.md) is currently minimal and you may need to ask for help.


#### `.github/`

This is an important folder that you can happily ignore. **Do not delete**.

#### `analysis/`

This folder contains:
* the `study_definition.py` script that defines the Study Definition
* the `.do` files (and in future `.R` and other analysis scripts)

#### `codelists/`

This contains a `.txt` document listing the codelists that you want to retrieve from [codelists.opensafely.org](https://codelists.opensafely.org). and the `.csv` files of the retrieved codelists themselves. You should not edit the CSV files directly; see the Study Definition documentation for more on how to update the codelists.

See the Study Definition documentation for more on how to update the codelists.

#### `output/`
This folder contains:
*  the `input.csv` file containing the (dummy or real) dataset. You will only have access to the dummy version of this dataset.
*  Any other files outputted by the `.do` scripts that convert `input.csv` into study results, tables, figures, etc.

When running in development, this folder contains everything (as run on the dummy dataset). When running in production on the real data, the outputs will be manually checked for disclosivity, censored if necessary, and released to the remote repo.

Be aware that `input.csv` is included in the `.gitignore` file, so that it is never uploaded to the remote repo. Locally, you can always generate a new dummy dataset with `cohortextractor`. A dummy version is also automatically generated every time you push changes to the remote repo as part of a set of tests and checks that make sure the code will run to completion. This is available to download as an _asset_ from the _releases_ section of your repo. There's a different version for each branch.

You don't *have* to store things here, but that's the convention we use.

#### `docs/`

Used for documentation.

#### `(other folders)/`

Feel free to add more folders to the repo and organise your project as you wish. However, make sure to include all active scripts and codelists in the `analysis/` and `codelists/` folders, otherwise they won't be run in the secure environment. If you don't want any additional folders to be pushed to the remote repo, use `.gitignore`.

#### `.gitignore`

This is a text document listing all the files and folders that you *don't* want to be uploaded to the remote repo on GitHub when you push changes from your local repo (_untracked_ files). As a system for keeping private files private, it's incredibly vulnerable to human error so don't rely on it for this purpose.

Instructions for how to list ignored files properly in `.gitignore` are [here](https://git-scm.com/docs/gitignore).
