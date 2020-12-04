#### `README.md`

Documentation about your project.  We've given you a template to start with. You
should edit it to reflect your project, and check it's up to date before
publication.

#### `project.yaml`

This file defines a "pipeline": how all the components of your analysis can run together, efficiently, either on the server or locally on your computer.   See the [pipeline documentation](pipelines.md) for more information.


#### `.github/`

This is an important folder, used internally by git, that you can happily ignore. **Do not delete**.

#### `analysis/`

By convention, this folder contains:

* Any `study_definition.py` script that defines the study definition
* Analysis scripts in R, Python or Stata

#### `codelists/`

This contains a `.txt` document listing the codelists that you want to retrieve from [codelists.opensafely.org](https://codelists.opensafely.org), and the `.csv` files of the retrieved codelists themselves. You should not edit the CSV files directly; see the [codelists documentation](codelist-intro.md) for more on how to update the codelists.


#### `output/`

This folder contains:

*  the `input.csv` file containing the (dummy or real) dataset. You will only have access to the dummy version of this dataset when working locally.
*  By convention, any other files outputted by the analysis scripts that convert `input.csv` into study results, tables, figures, etc.


Be aware that `input.csv` is included in the `.gitignore` file (see below), which means it can't be committed and uploaded to Github.

You don't *have* to store things in these locations, but that's the convention we suggest.

#### `released_outputs/`

Outputs that have been reviewed (and possibly edited) to ensure they are not disclosive are stored here.

#### `docs/`

Used for documentation.

#### `(other folders)/`

Feel free to add more folders to the repo and organise your project as you wish.
However, we recommend including all active scripts and codelists in the `analysis/` and `codelists/` folders.

If you don't want any additional files or folders to be pushed to the remote repo, use `.gitignore`.

#### `.gitignore`

This is a text document, used by git, which lists all the files and folders that you *don't* want to be uploaded to the remote repo on GitHub when you push changes from your local repo (_untracked_ files).
As a system for keeping private files private, it's vulnerable to human error so don't rely on it for this purpose.

Instructions for how to list ignored files properly in `.gitignore` are [here](https://git-scm.com/docs/gitignore).

If you need to create an empty folder to save files in, put a file in the folder that is tracked by git &mdash; by convention this is a [`.gitkeep`](https://stackoverflow.com/a/7229996/4269699) file.

If you want to create an empty folder to save files in, but you _never_ want its _contents_ to be committed to the repo, you can add a `.gitignore` file to *that* folder with the following contents:

```
# Ignore all files in this folder
*

# Apart from this very file
!/.gitignore
```

This can be useful if you want to for example add a `output/plots/` subfolder to put your analysis plots into without having to check and create that folder explicitly every time in the analysis script.  This is necessary because the contents `output/` folder is ignored by `.gitignore`.



---8<-- 'includes/glossary.md'
