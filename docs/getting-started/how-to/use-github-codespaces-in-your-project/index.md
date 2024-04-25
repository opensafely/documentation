This page explains how to work with OpenSAFELY projects using GitHub Codespaces.

## Managing GitHub Codespaces

### How to create a codespace

To create a Codespace,
[create a code repository](../../how-to/create-a-code-repository-for-your-project/index.md) first.

Once you have a research code repository to work in:

1. In a web browser,
   go to your newly created research code repository on GitHub.
1. Click the "Code" button
1. Select "Create codespace on main".
1. You will see a "Setting up your codespace" screen before the codespace is ready for use.
   It may take a few minutes before the codespace loads.

!!! info
    For "Create codespace on main",
    "main" refers to the Git branch to use in the codespace.

    If you are working on another repository branch,
    it is possible to select "New from options",
    which allows you to choose the branch.

### How to stop a codespace

See [GitHub's documentation for how to stop a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace).

Stopping a codespace is a specific action
that makes the codespace inactive and stops the codespace from using CPU usage quota.
You can resume working in a stopped codespace at a later time.

Because stopped codespaces are persistent,
they still count against storage usage quota.

!!! note

    Closing a browser that is running a codespace
    does not immediately stop a codespace.

    Codespaces that GitHub consider to be idle
    due to a lack of user interaction or terminal activity
    will eventually timeout.
    But it is preferable to stop codespaces explicitly
    to save on usage.

!!! warning

    Inactive codespaces are automatically deleted after a period of inactivity.
    For the `opensafely` organization,
    this period is 14 days.

### How to restart a stopped codespace

See [GitHub's documentation for how to restart a stopped codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#restarting-a-codespace).

### How to delete a codespace

See [GitHub's documentation for how to delete a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace).

Deleting a codespace removes the codespace entirely,
preventing any further CPU or storage quota usage by the codespace.

!!! info
    If you have changes in the codespace that have not been published to the repository,
    GitHub will warn you to confirm that you are sure you want to delete the codespace.

## Developing OpenSAFELY projects in GitHub Codespaces

### How to ensure your work is saved

#### How to save the files in the codespace

!!! note
    Saving files in the codespace only ensures that changes persist in that codespace's storage.
    When the codespace is deleted, these changes will be lost
    unless they are pushed to the remote repository that GitHub hosts.

    The remote repository is the one accessible at a GitHub URL, like,
    for example,
    `https://github.com/opensafely/example-research-repository`

If you work in the Visual Studio Code editor,
changes that you make to the files in your codespace
are saved automatically in the codespace.

If you work in RStudio,
changes that you make to the files in your codespaces
must be manually saved.

#### How to store your changes in your project's repository

To do so,
use your codespace's Visual Studio Code editor.

1. Optionally, you may first wish to create a new branch for your changes if you have not already.
   See GitHub's documentation on how to [create or switch to a branch](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#creating-or-switching-branches).
1. Commit your changes to the codespace's "local" copy of the Git repository.
   See GitHub's documentation on how to [commit your changes](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes).
1. Push the changes from the codespace's "local" repository to the "remote" repository as hosted on GitHub.
   This makes your changes visible on GitHub's repository.
   See GitHub's documentation on how to push your changes.

!!! note
    See GitHub's documentation on [source control workflow in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#about-source-control-in-github-codespaces).

### How to run the OpenSAFELY CLI

* You can run the OpenSAFELY CLI in GitHub Codespaces.
  In the Visual Studio Code terminal, type `opensafely` and press ++enter++.
* You should see the OpenSAFELY CLI help prompt.

!!! info

    See the [OpenSAFELY CLI](../../../opensafely-cli.md) documentation for more details.

### How to use OpenSAFELY CLI to run the example project

The research code repository that you created already has a minimal, working OpenSAFELY project in it.

1. In the Visual Studio Code terminal,
   type `opensafely run run_all` and then press ++enter++
   to run the existing `project.yaml`.
1. This may take a few moments to download the required Docker images,
   before the project is run.

   You should see some information messages that should end something like:

   ```
   => generate_dataset
   Completed successfully
   ```

!!! note

    By default, the Visual Studio Code terminal that has opened should be in the correct directory (folder)
    that contains the `project.yaml` file.

    If you have changed the terminal directory by using the `cd` change directory command,
    use `cd` to return to the directory containing `project.yaml` first.


    ```sh
    $ cd /workspaces/"$RepositoryName"
    ```

## How to access RStudio

1. In Visual Studio Code,
   select the "Ports" tab
   (next to "Terminal").
1. Port 8787 should be listed —
   this is configured by the RStudio server.
1. Right-click on port 8787 and select "Open in browser".
1. A new browser tab/window appears with RStudio running
   prompting you to "Sign in to RStudio".
   To sign in,
   enter the username: `rstudio`
   and the password: `rstudio`
   and then press "Sign in".
