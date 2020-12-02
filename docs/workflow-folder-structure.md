#### `project.yaml`

This file defines how all the components of your analysis can run together, efficiently, on the server, or locally.  This is a brand-new feature, so [the documentation](pipelines.md) is currently minimal and you may need to ask for help.


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
*  the `input.csv` file containing the (dummy or real) dataset. You will only have access to the dummy version of this dataset when working locally.
*  Any other files outputted by the analysis scripts that convert `input.csv` into study results, tables, figures, etc.

When running in development, this folder contains everything. 
When running in production on the real data, the outputs will be manually checked for disclosivity, censored if necessary, and released to the remote repo.

Be aware that `input.csv` is included in the `.gitignore` file, so that it is never uploaded to the remote repo. Locally, you can always generate a new dummy dataset with `cohortextractor`. A dummy version is also automatically generated every time you push changes to the remote repo as part of a set of tests and checks that make sure the code will run to completion. This is available to download as an _asset_ from the _releases_ section of your repo. There's a different version for each branch.

You don't *have* to store things here, but that's the convention we use.

#### `released-output/`

This folder contains files created when running the code on the real data.
Only files fit for release will appear here.

#### `docs/`

Used for documentation.

#### `(other folders)/`

Feel free to add more folders to the repo and organise your project as you wish. 
However, we recommend including all active scripts and codelists in the `analysis/` and `codelists/` folders, otherwise they won't be run in the secure environment. 

If you don't want any additional files or folders to be pushed to the remote repo, use `.gitignore`. 

#### `.gitignore`

This is a text document listing all the files and folders that you *don't* want to be uploaded to the remote repo on GitHub when you push changes from your local repo (_untracked_ files). 
As a system for keeping private files private, it's vulnerable to human error so don't rely on it for this purpose.

Instructions for how to list ignored files properly in `.gitignore` are [here](https://git-scm.com/docs/gitignore).

If you want to create an empty folder to place files into, put a file in the folder that is tracked by git &mdash; by convention this is a [`.gitkeep`](https://stackoverflow.com/a/7229996/4269699) file. 

If you want to create an empty folder to place files into and you _never_ want those files to be committed to the repo, you can add a `.gitignore` file to that folder with the following contents:

```
# Ignore all files in this folder
*

# Apart from this very file
!/.gitignore
```

This can be useful if you want to for example add a `outputs/plots/` subfolder to put your analysis plots into without having to check and create that folder explicitly every time in the analysis script. 
This is necessary because the contents `output/` folder is ignored by `.gitignore`.

