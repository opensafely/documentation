# Getting started with OpenSAFELY

This document will take you through everything needed to use the OpenSAFELY platform. By the end you should be able to:

* Create a new OpenSAFELY GitHub repository for your study
* Clone the repository to a local folder
* Update the Study Definition according to your study codelists, population, and variables
* Create, edit, and retrieve codelists at [codelists.opensafely.org](https://codelists.opensafely.org)
* Create dummy datasets for testing analysis code based on the OpenSAFELY's _expectations_ framework
* Commit these changes via git, then push them to the remote repository and create a pull request
* Understand and use good practice for version control with git e.g., when using `branch`, `commit`, `push`, `pull`.
* Understand and use good practice for collaborative research with GitHub, e.g., for issues, reviews, READMEs, documentation.
* ...


## Minimum requirements

OpenSAFELY maintains extremely high standards for data privacy, whilst ensuring complete computational and analytical transparency. As such there are some small technical pre-requisites that collaborators must satisfy to use the platform:


### Essential
* **Stata**. OpenSAFELY currently supports Stata v16.1 for statistical analysis. We are not able to provide Stata training. You need to be able to perform all stages of the statistical analysis in Stata, including statistical models and graphic and tabular outputs. 
Support for R and other languages is planned.
* **Git** The workflow is strongly integrated into Git/GitHub. At a minimum you need to be able to <!--(clone, branch, commit, push, pull)--> clone a remote git repository, create a branch to work on, commit changes to it, push those changes to the remote repository, and create a pull request. We are not able to provide foundational Git/GitHub training, though this start up guide points to resources and runs through a basic edit-commit-push-pull workflow. 
<!--We provide a simple tutorial for navigating the OpenSAFELY workflow.-->

### Desirable
* **Python** The code to generate each study-specific dataset is written in Python. We provide easy-to-use Python functions to define your study population and study variables that are designed to be used and understood by anybody familiar with health research. However, some knowledge of Python may still be beneficial to create or modify existing functions. 

## Set up git/GitHub

OpenSAFELY uses [**GitHub**](https://github.com/) to store the code used to create and analyse the study data. It is based on [**git**](https://git-scm.com/), an industry-standard version control system that helps multiple contributors manage code effectively. It also supports convenient publication of your code, so that anybody can view it, comment on it, and suggest improvements (we require that anyone who uses OpenSAFELY publish their code on publication of their papers).

A good starting point for understanding version control in the context of scientific research has been written by The Turing Way collaborative. If you are completely new to these concepts or want to understand more then we suggest reading through their [chapter on version control](https://the-turing-way.netlify.app/reproducible-research/vcs.html).

To get set up, you will need:

* A [**GitHub**](https://github.com/) account
* [**git**](https://git-scm.com/) installed on your local machine


### New to git
For Windows or macOS users new to git, the easiest way to do both is to install [**GitHub Desktop**](https://desktop.github.com/). This includes a command line version of git and a useful GUI for editing files and gitting. To install GitHub Desktop, visit the [GitHub Desktop homepage](https://desktop.github.com/) and click install for your operating system. This will ask you to create or sign-in to your GitHub account. You'll be taken to a _Let's get started_ page. We'll return to this later once you have Python and a repository for your study.

### Old to git
If you already have git installed and prefer using your existing git workflow, then this is fine. 

If you're not sure if you already have git installed, type `git --version` into any command line terminal. 

<!--To install git [follow these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Select the default/recommended options unless you understand the consequences of changing them.-->

<!-- ### Your GitHub account linked to git 

To do this, open a terminal and submit these two lines (without the _<>_, with or without the _""_):

       git config --global user.name "<git_username>"
       git config --global user.email "<github.email@domain.com>"   

The `<git_username>` doesn't have to be the same as your GitHub account username, but `<github.email@domain.com>` should be that used for your GitHub account if you want to associate any repo activity to your account.
To check this has worked and that you used the correct details, submit:

      git config --list

For more info about how your git email address is used by GitHub, [read this](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address).

<font color='red'>Do we want to set up authenticated accounts?</font> -->

### Access to the [OpenSAFELY GitHub organisation](https://github.com/opensafely)
This is only necessary for running code against the real data. <font color='red'>Ask _?_ to be added</font>. If you're not sure if you already have access, go to [*settings > security*](https://github.com/settings/organizations) in GitHub and check that _opensafely_ is listed. 

You will need [**Two-factor authentication**](https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa) for your GitHub account to join the organisation.
To set up 2FA [follow these instructions](https://help.github.com/en/github/authenticating-to-github/configuring-two-factor-authentication). If you're not sure if you already have 2FA enabled, go to [*settings > security > Two-factor authentication*](https://github.com/settings/security) in GitHub and check that at least one method is *Configured*.



## Install Python 3

\* **Please read even if you already have Python installed** \* 

For security, consistency, and readability, OpenSAFELY has an API for creating analysis datasets from the underlying patient data. The API is built in [**Python**](https://www.python.org/), and includes functions for selecting the patients and defining the variables that make up a study dataset. All the characteristics that define the dataset are referred to collectively as the _Study Definition_. Currently, Python must be installed on your machine if you want to develop and run test code locally. 

### Windows users
For Windows users, we recommend that you install [Anaconda (Individual Edition)](https://www.anaconda.com/products/individual), a popular Python distribution that includes an recent version of Python 3, many useful Python packages, and an environment manager. This will help avoid some fiddly annoyances when dealing with multiple versions/installations of Python. 

<!--If you already have Python installed on your machine, you should still be able install Anaconda without any inteference. <font color='red'>(is this true?)</font> Alternatively, you're welcome to use any existing or fresh Python installation you want if you're happy to troubleshoot problems yourself. -->

To install, [follow these instructions](https://docs.anaconda.com/anaconda/install/). Choose version 3.8 if available but if not then choose 3.7 (3.8 is not available when this was written but will be soon). Accept the default/recommended settings unless you understand the consequences of changing them. 

This should have added _Anaconda Prompt_ to your machine. To to verify that you can run Python with it, open it and submit `python --version`. 

<!--If you installed a version of python earlier than `python 3.8` then you should submit `conda install -c anaconda python=3.8` to update your installation. It can take a while (up to an hour) as it needs to identify and resolve incompatible packages from the previous installation. -->

You should use the _Anaconda Prompt_ whenever you want to run OpenSAFELY's `cohortextractor` command, which uses the Study Definition to update codelists and create dummy datasets.


### mac users

<font color='red'>not yet documented</font>


## Install `cohortextractor`

`cohortextractor` is how OpenSAFELY converts the Study Definition into an actual (dummy or real) dataset. To install, go to your Anaconda prompt (or another prompt that can find `pip`) and submit:

```
pip install opensafely-cohort-extractor
```

To check this has installed successfully, submit `cohortextractor --help` and it should print some details of how it can be used.

Update by submitting:

    pip install --upgrade opensafely-cohort-extractor


## Create repository for your study

You should now have all the required software and permissions needed to create and develop a new study repository. 


Go to the [OpenSAFELY research template repo](https://github.com/opensafely/research-template) on GitHub. Click the green button that says <span style="background-color: green; color: white">&nbsp;**Use this template**&nbsp;</span>. Fill in the details:
* **owner**: select your personal GitHub for testing/experimenting, or select the opensafely organisation for a bona fide OpenSAFELY-approved study. The repo can be transferred into opensafely later if needed.
* **repository name**: This should always end in `-research` so that any back-end updates to the template can be pushed through to existing repos. The rest of the name should be something short but informative --- browse existing repo names for inspiration.
* **Description**: This will appear at the top of the repo on GitHub. No more than a sentence is needed as the repo should be explained fully in the README.
* **public / private**: select **private** initially, this can be changed later.
* **Include all branches**: Leave unchecked.

And submit. You will now be at the GitHub landing page for the repo.

### Add secrets (_temporary step_)
You need to provide the repo with access to some other things using _secrets_. In the repo, go to _settings > secrets_ and click <span style="background-color: lightgray">&nbsp;**New secret**&nbsp;</span>. Use the tokens [here](https://ebmdatalab.slack.com/archives/C010SJ89SA3/p1591091848070500?thread_ts=1591091770.069200) to create **two** new secrets. So for example:
* **Name**: `PACKAGE_READ_ACCESS_TOKEN` 
* **Value**: `abc123doremi...`

then click <span style="background-color: green; color: white">&nbsp;**Add secret**&nbsp;</span>, then repeat for the second secret. 
    
### Update the README
The new repo will include a template README, which is used to help people understand the purpose of the repo, and how to navigate and use the code. The README should be updated to briefly describe the intended study and to reflect the repo's current status as a _work in progress_. The README should be updated frequently to reflect changes to the repo. 

The README is written in Markdown. If you're not familiar with Markdown syntax, [read this](https://help.github.com/en/github/writing-on-github/about-writing-and-formatting-on-github). There's a handy cheatsheet for the most useful Markdown syntax [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

You can update the README directly in GitHub. Click the edit button (a little pencil in the top-right), change the text, and commit the changes. This is a standard commit so there's not need to write more than "_first README update_", but typically commits should have a bit more detail than that.


### Clone the repo locally
Now we're going to download a copy of this repo to your machine so you can work on it locally. This is useful because you can:
* develop your code using familiar editing tools
* test and run code without disturbing other contributors
* ...

<!--
To get the repo on your machine:
1. Select (or create) a folder on your machine where you would like to put repository. `C:/my-repos`, say. A new folder containing the repo will be added to this folder. Change the working directory in the Anaconda prompt to this folder by submitting:

       cd C:/my-repos-folder
   
   Alternatively, type `cd` and drag the folder into the prompt (to save copying or typing). 

2. Go to the repository's homepage on GitHub, click <span style="background-color: green; color: white">&nbsp;**Clone or download**&nbsp;</span> and copy the URL for the repo to your clipboard.

3. Go back to the anaconda Prompt and type

       git clone <https://github.com/<repo-owner>/<repo-name>.git>

   where `<...>` is what you've just copied to the clipboard. <font color='red'>(It still works without `.git` at the end of the url. Is it better to do one or the other?)</font>
   

4. Change the working directory to the repo folder by submitting:

       cd <repo-name>

5. verify that you're in the repo by submitting:

       git status
       
    You should get a message saying `Your branch is up to date with 'origin-master'`.

-->

To clone your new repository to your machine, [follow these instructions](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) which explains cloning both via GitHub Deskop or via the command line. When this is done, you should have a folder whose name is the same as the repo on your machine. 

Before making any changes, try to understand the folder structure first...

## Understanding the repo structure


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

#### `docs/`

Used for documentation.

#### `(other folders)/`

Feel free to add more folders to the repo and organise your project as you wish. However, make sure to include all active scripts and codelists in the `analysis/` and `codelists/` folders, otherwise they won't be run in the secure environment. If you don't want any additional folders to be pushed to the remote repo, use `.gitignore`. 

#### `.gitignore`

This is a text document listing all the files and folders that you *don't* want to be uploaded to the remote repo on GitHub when you push changes from your local repo (_untracked_ files). As a system for keeping private files private, it's incredibly vulnerable to human error so don't rely on it for this purpose. 

Instructions for how to list ignored files properly in `.gitignore` are [here](https://git-scm.com/docs/gitignore). 


## Using `cohortextractor` at the command line

The repo contains a working Study Definition (`study_definition.py`) which you can use to retreive codelists and create dummy data. Before making any changes to `study_definition.py` to match your study (which will need to be properly version controlled in git), it's important to understand how the study definition is used by `cohortextractor`. Without `cohortextractor` you won't be able to run and test any changes that you've made to `study_definition.py` or the codelists.

To confirm you can use `cohortextractor`, go to a terminal and submit `cohortextractor --help`, which will list all the ways in which you can use it. You can also use `cohortextractor generate_cohort --help` to learn more about the `generate_cohort` command, for example. 

Some of these commands are discussed in detail below. Remember that to run any of these commands for your specific local repository, you need to change the direct of your prompt to be the repo directory using for example `cd c:/my-repos-folder/my-repo`.

#### `generate_cohort` 
This will create a dummy dataset for you, `outputs/input.csv`, based on the _expectations_ declared in the study definition. Use it for example like this:

    cohortextractor generate_cohort --expectations-population 10000

where `10000` is the number of rows you want to generate for your dataset. 

Run it -- check that `outputs/input.csv` has been created. Run it again -- the file will be refreshed (check the file's _modified_ date) and will contain different data than previously (even if the `study_definition.py` didn't change) because the values are randomly generated. 

Beware that on Windows, you can't have `input.csv` open and generate a new one at the same time.

If you have multiple study definitions in the repo (eg `study_definition_set1`, `study_definition_set2`) then `generate_cohort` will create dataset for each (eg `input_set1.csv`, `intput_set2.csv`). You can restrict it to a single study definition using the `study-definition` option, like this:

    cohortextractor generate_cohort --expectations-population 10000 --study-definition study_definition_set2

This is most useful when extracting real data on the server when only some study definitions have been updated, due to the time taken to run each study definition. 


#### `update_codelists` 
This will retrieve the codelists from [codelists.opensafely.org](https://codelists.opensafely.org) based on those listed in `/codelists/codelists.txt` and put them in the same folder. Use it like this: 
   
    cohortextractor update_codelists

Run it -- it will add (or update) the codelist `.csv` files in the `codelists/` folder. See [here](https://github.com/opensafely/documentation/blob/master/study_definition.md#codelist-definitions) for more information about how to create codelists.

Beware again that in Windows, if one or more of these codelist files is open then `update_codelists` won't be able to run. 

#### `remote`

This will run an extract on the real data, with the results of that extract saved within the secure environment. When using the `remote` function for the first time, you'll be prompted for a username and password. To start an extract, first `checkout` the repo that you want to use, then switch to that repo in your terminal. The command is run like this:
```
cohortextractor remote generate_cohort --ref <name of branch or tag to be run>
```
The branch or tag that you're running will most often be `master`, but could be the name of another branch, or the tag of a specific release.

You can check whether running jobs have completed using:
```
cohortextractor remote log
```
As with [generate_cohort](https://github.com/opensafely/documentation/blob/new-onboarding/Onboarding%20analysts.md#generate_cohort), you cannot have the `input.csv` open in the secure environment and generate a new one at the same time.

##### (to be added - instruction for specifying which database to run the analysis on i.e. full or sample)

#### `cohort_report`

This will produce an `.html` document giving some summary statistics about each variable in the study dataset. Use it like this:

    cohortextractor cohort_report
    
Re-run it each time you want to update the document using the latest version of the `input.csv` dataset. Assuming that your working directory is the repo folder, you should be able to run `cohortextractor` commands. 
This command can also be run on the real data, though for now this has to be requested from an OpenSAFELY developer -- just ask us via email or GitHub.

## Editing the Study Definition and gitting changes

For more detail about the study definition, see: https://github.com/opensafely/documentation/blob/master/study_definition.md 

You should now have all the tools you need to make changes to the study definition. 

The general workflow for updating the repo is as follows:

* Create a new branch. A branch is a way for you to record and publish your own changes without breaking things for other people who are using the same code. It is also a good way of collecting changes ("commits") into a meaningful unit that can be reviewed by others.
* Edit/add/delete files in the repo on that branch, committing regularly with informative commit messages.
* Push the changes to GitHub, so that others can view the branch.
* Continue to commit and push changes on that branch until you believe it's ready to be merged back into the main codebase that everyone uses.
* Submit a pull request (PR), requesting that the branch be reviewed by somebody else. A PR is simply a way of viewing, commenting on, and approving branches.


We'll demonstrate this workflow with a simple example. Say you want to add a new variable describing if the patient has recieved an organ transpant or not. Then follow these steps:

### Create a branch and publish it

The first thing to think about before making any changes, whether adding, deleting, or editing files, is to `branch`. This ensures that any changes are kept separate from the _Master_ branch (i.e. the main codebase that everyone uses) whilst they are still being tested. 

Open GitHub Desktop, and make sure the current repository is the the one you're working on. Click `Branch > New branch` and choose a new name that reflects the changes you wish to make, e.g., `update-codelists`, or `exploratory-notebook`. In our example, this can be `add-transplant-var`.

<!--Then publish the branch. It's a good idea to do straight way so that others know what you're working on. It's also necessary git housekeeping before being able to push commits to the remote repo.-->

### Add the relevant codelist and `commit`

First take a look at the `codelists/codelist.txt` file in the repo, and note the structure of the existing example codelists that shipped with the research template: `opensafely/<codelist-name>/<YYYY-MM-DD>`. If you want a codelist from [codelists.opensafely.org](https://codelists.opensafely.org), then you need to put it in this format in the `codelist.txt` file. 

Now find the codelist:

* Go to [codelists.opensafely.org](https://codelists.opensafely.org) and search "transplant". 
* Click on the "Solid Organ Transplantation" codelist.
* Construct the codelist location from the **Codelist ID** and the **Version**. This should be `opensafely/solid-organ-transplantation/2020-04-10`
* paste this into a new line in `codelists/codelist.txt`
* Download the new codelist into the `codelist/` folder using the `cohortextractor` by submitting `cohortextractor update_codelists` at the command line. 

At this point, there are two changes in the repository folder: 
1. a new line in `codelists/codelist.txt`
2. a new file called `codelists/opensafely-solid-organ-transplantation.csv`. 

You should see these changes appear in GitHub Desktop. This is a good time to `commit` them:

* Select (tick) both changes under the _Changes_ tab
* Write a brief commit message, e.g., "add transplant codelist". No need for a description.
* Click `Commit to add-transplant-var`

Now you have committed the changes to your local repo but not yet pushed (published) to the remote repo on GitHub.

### Define the transplant variable in `study_definition.py` and `commit`

* Open `analysis/study_definition.py` in your favourite text editor (ideally one with Python syntax highlighting -- <font color='red'>to be documented</font>).
* Paste the following code chunk after the other codelist declarations:
   
      transplant_codes = codelist_from_csv(
        "codelists/opensafely-solid-organ-transplant.csv",
        system="ctv3",
        column="CTV3ID",
      )
* Paste the following code chunk after the other variable declarations:

      organ_transplant = patients.with_these_clinical_events(
        transplant_codes, 
        returning='binary_flag',
        return_expectations = {"incidence": 0.05}
      )

* Save the file, then go to the command line submit:

      cohortextractor generate_cohort --expectations-population 10000

At this point, there are two changes in the repository folder: 
1. the changes to `study_definition.py`
2. a (new or updated) file called `analysis/input.csv` 

However, you will only see the first change appear in GitHub Desktop. This is because `input.csv` is included in the `.gitignore` file, so all changes are ignored by git.

This is a good time to `commit` again:

* In GitHub Desktop, select the changed file, write a useful commit message, and click `Commit to add-transplant-var`. 

For more guidance on making good git commit messages, and other good git practice, [read this](https://github.com/ebmdatalab/best_practice_guidance). 

### `push` the `commit`s to the remote repo

You've now completed the required changes so this is good opportunity to `push` your set of `commit`s to the remote repo. 

* In GitHub desktop, click `Push origin` -- you may have to click `Publish Branch` first

### Create a `pull request` for review

Now that you've pushed your commits to the remote repo, you can view them on GitHub. Go to your repository webpage -- you can click `View on GitHub` in GitHub Desktop, navigate to the repo from you GitHub profile page, or type `https://github.com/<user-or-organisation>/<repo-name>`. You can select either the (unchanged) `master` branch or the new `add-transplant-var` branch that you've just created. 

If you're happy with the new branch, you can create a pull request to merge your development branch onto the master branch. 

* Create a Pull Request in GitHub or in GitHub Desktop:
   * In GitHub, select the development branch and click `Create Pull Request`
   * In GitHub desktop, click `Create Pull Request` which will open the relevant webpage on GitHub

Review the changes, fill in any extra details if helpful, and submit. On the following page you can suggest someone to review the PR. In OpenSAFELY, a PR must always get a second pair of eyes before merging for sense-checking and bug-catching. 

### Merge the PR and delete the branch

Once the PR has been approved, you can click merge and then delete the branch on the remote. 

You may also want to delete the branch on your local repo to keep things tidy (since branch deletions aren't copied across when fetching) though this isn't essential. Just click `Branch > Delete` in GitHub Desktop. 

### Fetching

It's possible for the master branch to be updated independently of your current development branch, as a result of another branch being approved and merged. These could be behind-the-scenes updates made by OpenSAFELY's tech team, or updates to the Study Definition or analysis files by another researcher working on the repo. It's important to bring these changes into your development branch to avoid merge conflicts. We do this using `fetch`.

* In GitHub desktop, click `Fetch origin`

You should make a habit of `fetch`ing frequently to reduce the occurrence of [merge conflicts](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts. If you do get a warning about a merge conflict, try to understand what's causing it using the `Resolve conflicts` button on your PR on GitHub. Do not actually resolve these conflicts (by clicking `Mark as resolved`) unless you're absolutely sure what why the conflict is there and which version to accept. Speak to a member of the tech team if you have any doubts. 


## Study analysis

Now that you have a dummy dataset on your local machine, you can develop any analytical code you like against this dataset, on a separate branch, of course. The current workflow only supports Stata code by running the `analysis/model.do` file. You should make sure any results produced by `model.do` are outputted to the `outputs/` folder. It's possible to create multiple `.do` files in the analysis folder, which can be called by the `model.do` script. 

Once you are happy with the analysis branch and want to try to run it against the real data, push it to the remote repo and submit a pull request. This will be checked by a developer and run against the real data. Assuming no errors, the contents of `outputs/` will be available to the developer to check for disclosivity, censored where necessary, then transferred to a release folder and pushed to the remote repo for you to see.

### Running a cohort extract remotely

See `remote` [here](https://github.com/opensafely/documentation/blob/new-onboarding/Onboarding%20analysts.md#remote).
