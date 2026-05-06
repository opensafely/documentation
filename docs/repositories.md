This section provides information on the git repositories for each OpenSAFELY research project.

The repository, or repo, contains all the analysis scripts, codelists, released outputs, and other research objects needed to understand and run the project.
Changes to the repo are audited using `git`, a version control system for recording, sharing and collaborating on code.
The repo's canonical location is on GitHub, a website that makes it easier to use git, and adds extra collaboration and security tools on top.
You can download a copy of the repo ("clone"), create a development "branch", make changes ("commit") on that branch, then upload these changes ("push") back to the remote repo on GitHub &mdash; for more details see the ["How to use Git effectively"](getting-started/how-to/use-git-effectively/index.md) page.

GitHub is the means by which code in the repository is passed to the server to be run against the OpenSAFELY database &mdash; it is the only entry point between the secure server and the outside world. GitHub is also the means by which approved disclosure-safe outputs are released from the secure server to researchers.

## Repository visibility

In accordance with the [Principles of OpenSAFELY](https://www.opensafely.org/about/#transparency-and-public-logs), we expect all code from all users to be made public.

By default, repositories will initially be public, visible to anyone. Repositories may be temporarily set to private, visible to members of the `opensafely` GitHub organization only, [by request](#how-to-make-your-repository-private).

### How to make your repository private

Contact [Tech Support](how-to-get-help.md/#slack) to request that your repository is made private at any time.

If your request is approved, Tech Support will make your repository private and you will be notified once this has been completed.

Private repositories will be made public after 12 months. Ahead of that, you can make a new request to extend the private visibility period for another 12 months.

!!! info
    A repository must be made public if it forms part of a publication.

    Refer to our documentation on [when you need to make your code public](#when-you-need-to-make-your-code-public), for more information.


### How to make your code public

You can request that a private repository is made public at any time by [following our process for publishing a repo](project-completion.md).

#### Publishing older repositories that contain results as well as code

In earlier versions of OpenSAFELY, all results released from the secure server after disclosivity checking went directly to the GitHub repository containing the code for the project. Because of this, for older repositories the OpenSAFELY team and you must check that there are no outstanding results which still require approval from NHS England in your repository, before that repository is made public. If you are unsure whether this applies to your repository then you should contact <publications@opensafely.org>.

### When you need to make your code public

A repository must be made public if it forms part of a [publication](https://www.opensafely.org/policies-for-researchers/#acknowledgment-and-data-sharing--publication-policy). We have a [guide to publishing repositories](project-completion.md) that you must read. During the development stage of a project, a [repository may be kept private](#how-to-make-your-repository-private), so that only members of the [`opensafely` GitHub organisation](https://github.com/opensafely) are able to view it. We welcome people sharing code in public while they are developing, where they wish to do so, but we recognise that for many this would be a little like drafting a paper entirely in public, so it is not a requirement. Even when there is no publication, we expect all repositories to become public, within twelve months after first code execution.

!!! warning
    You should _never_ commit files or content that should not be made public to the repository. All committed files, whether on the `main` branch or on development branches, will remain in the git history of the repository even after they have been deleted. These might include for example patient- or commercially-sensitive data from other sources, internal institutional documentation or forms, and incomplete manuscript drafts.

## Creating a repository for a project

To create a repository for your OpenSAFELY project, you can either:

- Have a new repository created for you in the `opensafely` GitHub organisation
- Create a repository in your own GitHub account, and request to have this transferred to the `opensafely` GitHub organisation later

### Default repository settings in the GitHub `opensafely` organisation

Any repositories created within, or transferred to, the `opensafely` organisation, will be configured with the settings, listed below:

- Deletion of branches on merge: enabled
- Branch protection for `master` and `main` branches: enabled (mandatory)
- Require a pull request review before merging: disabled

You can [contact Tech Support](how-to-get-help.md/#slack) to request changes to your repository settings; those listed as *mandatory* above cannot be changed.

### New researchers and projects

When you are approved to start working on an OpenSAFELY research project, you will be added to the `opensafely` GitHub organisation to provide repository access.

Contact [Tech Support](how-to-get-help.md/#slack) and ask them to create a new repository for your research, or transfer a repository from your personal GitHub account into the `opensafely` GitHub organisation (depending on your preference, and whether you have an existing repository to transfer).

Newly-created and transferred repositories will be configured with the settings listed in [default `opensafely` repository settings](#default-opensafely-repository-settings), above.

Repositories will initially be public, but may be temporarily set to private at your request. See [Repository visibility](#repository-visibility) to make the right choice for your study.

### Established researchers and projects

Contact [Tech Support](how-to-get-help.md/#slack) to request the creation of any additional repositories you require. Please provide a name for the repository when you make a request. Your repository name should be short but informative &mdash; browse [existing repo names](https://github.com/orgs/opensafely/repositories) for inspiration.

All repositories will be created using the OpenSAFELY [research-template repo](https://github.com/opensafely/research-template). Refer to the [detailed breakdown of this repository’s structure](#repository-structure).

## Transferring your own repository to the `opensafely` GitHub organisation

You may want to start work on a project before approval by [creating a repository in your own GitHub account](#creating-a-research-repository-in-your-own-github-account-so-that-you-can-transfer-it-later). You can request that this repository is transferred to the `opensafely` organisation at a later date.

!!! warning
    Creating a repository owned by your GitHub user account will enable you to:

    - work on your OpenSAFELY research code in Codespaces
    - check that your research code works with the OpenSAFELY platform

    It will not allow you to run code on OpenSAFELY's platform. For that, you would have to request that your repository is transferred to the `opensafely` organization.

### How to transfer an existing repository to the opensafely organization

To transfer a repository from your personal GitHub account to the OpenSAFELY organisation:

1. Follow [GitHub's instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository#transferring-a-repository-owned-by-your-personal-account) to initiate a transfer.
2. Contact [Tech Support](how-to-get-help.md/#slack) to request approval for the repository transfer.
3. Tech Support will notify you once the transfer has been completed. You will also be able to see the repository listed in the [`opensafely` organisation](https://github.com/orgs/opensafely/repositories) once transferred.

The settings of any transferred repositories will be updated to match the [default `opensafely` repository settings](#default-repository-settings-in-the-github-opensafely-organisation).

### Creating a research repository in your own GitHub account so that you can transfer it later

For ease of use, we have created a research template that you should use for your study.
Go to the [OpenSAFELY research-template repo](https://github.com/opensafely/research-template) on GitHub.
Click the green button that says <span style="background-color: green; color: white">&nbsp;**Use this template**&nbsp;</span>.

Fill in the details:

- **owner**: Select your personal GitHub for testing/experimenting.
- **repository name**: It needs to be short but informative &mdash; browse [existing repo names](https://github.com/orgs/opensafely/repositories) for inspiration.
- **description**: This will appear at the top of the repo on GitHub. No more than a sentence is needed as the repo should be explained fully in the `README.md`.
- **public / private**: See [Repository visibility](#repository-visibility) to make the the right choice for your study.
- **Include all branches**: Leave unchecked.

And submit. You will now be at the GitHub landing page for the repo.

If you are unsure of what to do, refer to GitHub's step-by-step instructions for [creating a new repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template).

You should also download a copy of this repo to your machine so you can work on it locally.
This is necessary because you can:

* develop your code using familiar editing tools
* test and run code without disturbing other contributors

To clone your new repository to your machine, [follow these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) which explains cloning both via GitHub Desktop or via the command line.
When this is done, you should have a folder whose name is the same as the repo on your machine.

Note that if someone else wants to commit to your recently created OpenSAFELY repo, they may need to wait up to an hour for the necessary write permissions to be granted.

## Repository structure

### `README.md`
This file contains a disclaimer that your code (and any outputs if you used the older method of releasing them to GitHub) should not be taken as the whole project.

A link points viewers to the Jobs site which will redirect them to the relevant project once it has been created there.


### `project.yaml`

This file defines a "pipeline": how all the components of your analysis can run together, efficiently, either on the server or locally on your computer.   See the [pipeline documentation](actions-pipelines.md) for more information.


### `.github/`

This is an important folder, used internally by GitHub, that you can happily ignore. **Do not delete**.

### `analysis/`

By convention, this folder contains:

* Any `dataset_definition.py` script that defines the dataset definition
* Analysis scripts in R, Python or Stata

### `codelists/`

This contains a `.txt` document listing the codelists that you want to retrieve from [OpenCodelists](https://www.opencodelists.org), and the `.csv` files of the retrieved codelists themselves. You should not edit the CSV files directly; see the [codelists documentation](codelist-intro.md) for more on how to update the codelists.


### `output/`

This folder contains:

*  the `input.csv.gz` file containing the (dummy or real) dataset. You will only have access to the dummy version of this dataset when working locally.
*  By convention, any other files outputted by the analysis scripts that convert `input.csv.gz` into study results, tables, figures, etc.


Be aware that `input.csv.gz` is included in the `.gitignore` file (see below), which means it can't be (easily) committed and uploaded to GitHub.

You don't *have* to store things in these locations, but that's the convention we suggest.

### `released_outputs/`

Outputs that have been reviewed (and possibly edited) to ensure they are not disclosive are stored here.

### `docs/`

Used for documentation.

### `(other folders)/`

Feel free to add more folders to the repo and organise your project as you wish.
However, we recommend including all active scripts and codelists in the `analysis/` and `codelists/` folders.

If you don't want any additional files or folders to be accidentally pushed to the remote repo, use `.gitignore`.

### `.gitignore`

This is a text document, used by git, which lists all the files and folders that you *don't* want to be uploaded to the remote repo on GitHub when you push changes from your local repo (_untracked_ files).
As a system for keeping private files private, it's vulnerable to human error so don't rely on it for this purpose.

[Instructions for how to list ignored files properly in `.gitignore`](https://git-scm.com/docs/gitignore).

If you need to create an empty folder to save files in, put a file in the folder that is tracked by git &mdash; by convention this is a [`.gitkeep`](https://stackoverflow.com/a/7229996/4269699) file.

If you want to create an empty folder to save files in, but you _never_ want its _contents_ to be committed to the repo, you can add a `.gitignore` file to *that* folder with the following contents:

```
# Ignore all files in this folder
*

# Apart from this very file
!/.gitignore
```

This can be useful if you want to, for example, add a `output/plots/` subfolder to put your analysis plots into without having to check and create that folder explicitly every time in the analysis script.  This is necessary because the contents of the `output/` folder is ignored by the default `.gitignore` in the root (the top-level) of the repository.

## Searching existing repositories for sample code

Often when writing study code, it can be useful to see how others have solved certain problems or used ehrQL features. To search all the public code in the `opensafely` GitHub organisation, see instructions in our [How to Get Help page](how-to-get-help.md#searching-past-study-code).
