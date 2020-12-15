This section provides information on the git repositories for each OpenSAFELY research project.

The repository, or repo, contains all the analysis scripts, codelists, released outputs, and other research objects needed to understand and run the project.
Changes to the repo are audited using `git`, a version control system for recording, sharing and collaborating on code.
The repo's canonical location is on GitHub, a website that makes it easy to use git, and adds extra collaboration and security tools on top.
You can download a copy of the repo ("clone"), create a development "branch", make changes ("commit") on that branch, then upload these changes ("push") back to the remote repo on GitHub &mdash; for more details see the [GitHub and Git](install-github-and-git.md) section.

GitHub is the means by which code in the repository is passed to the server to be run against the OpenSAFELY database &mdash; it is the only entry point between the secure server and the outside world.

## Creating a repository for a new project

For ease of use, we have created a research template that you should use for your study.
Go to the [OpenSAFELY research template repo](https://github.com/opensafely/research-template) on GitHub.
Click the green button that says <span style="background-color: green; color: white">&nbsp;**Use this template**&nbsp;</span>.

Fill in the details:

- **owner**: select your personal GitHub for testing/experimenting, or select the opensafely organisation for a bona fide OpenSAFELY-approved study. The repo can be transferred into opensafely later if needed.
- **repository name**: By convention, the name should end in `-research` to help differentiate research repos from other infrastructure repos. It needs to be short but informative &mdash; browse existing repo names for inspiration.
- **Description**: This will appear at the top of the repo on GitHub. No more than a sentence is needed as the repo should be explained fully in the README.
- **public / private**: select **private** initially, this can be changed later.
- **Include all branches**: Leave unchecked.

And submit. You will now be at the GitHub landing page for the repo.

You should also download a copy of this repo to your machine so you can work on it locally. 
This is necessary because you can:

* develop your code using familiar editing tools
* test and run code without disturbing other contributors

To clone your new repository to your machine, [follow these instructions](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) which explains cloning both via GitHub Deskop or via the command line. 
When this is done, you should have a folder whose name is the same as the repo on your machine.


## Repository structure

#### `README.md`

This file introduces your project, helps people understand the purpose of the repo, and how to navigate and use the code. 

Any new repo will include a template README. 
It should be updated to briefly describe the intended study and to reflect the repo's current status as a _work in progress_. 
The README should also be updated frequently to reflect changes to the repo, and should certainly be up-to-date before publication of any research outputs.

The README is written in Markdown. 
If you're not familiar with Markdown syntax, [read this](https://help.github.com/en/github/writing-on-github/about-writing-and-formatting-on-github). 
There's a handy cheatsheet for the most useful Markdown syntax [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

You can update the README directly in GitHub. Click the edit button (a little pencil in the top-right), change the text, and commit the changes. This is a standard commit so there's not need to write more than "_first README update_", but typically commits should have a bit more detail than that.


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

#### `released-output/`

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
