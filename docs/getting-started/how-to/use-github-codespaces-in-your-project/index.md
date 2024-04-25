## Introduction

This page explains how to work with OpenSAFELY projects using GitHub Codespaces.

## Using GitHub Codespaces for OpenSAFELY projects

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

    If you have changes in the codespaces that have not been published to the repository,
    GitHub will warn you to confirm that you are sure you want to delete the codespace.

### Navigating the codespace

When the build process for the codespace completes,
you should see a Visual Studio Code editor with three panes.

Briefly, when you first open Visual Studio Code, you will see:

* at the far left, a vertical bar of icons showing various options
* on the left, the project's files and folders in the file explorer
* a terminal at the bottom-right
* a file editor at the upper-right;
  this initially remains blank until you open a file

The screenshot below shows this.

![A screenshot showing the Visual Studio Code editor in Codespaces.](../../../images/codespaces-vscode-layout.png)

!!! info
    There are other elements to the user interface.
    If you are unfamiliar with Visual Studio Code, you can:

    * refer to the [explanation in GitHub's documentation](https://docs.github.com/en/codespaces/developing-in-codespaces/developing-in-a-codespace#working-in-a-codespace-in-the-browser)
      for more details.
    * refer to the [Visual Studio Code user interface documentation](https://code.visualstudio.com/docs/getstarted/userinterface)

It is possible to resize the different panes as needed
by hovering on the dividers between sections of the screen.

### Working with files

#### Editing code

The file explorer shows the contents of your code repository.

You can open files and folders by clicking on them.

#### Saving files in the codespace

The codespace is currently configured to autosave files when modified.

#### Reverting changes to files in the codespace

You can do this via the Source Control panel in the Visual Studio Code interface.

1. Select the Source Control panel on the left-hand side.
2. You should see a list of the changes.
3. You choose to "Discard Changes" for each file.
   This reverts the files back to how they are in the current version of the repository.
   The screenshot below shows this.

![A screenshot showing the "Discard Changes option" for a modified file. This option is in the Visual Studio Code Source Control panel.](../../../images/codespaces-discard-changes.png)

!!! info

    For users comfortable with command-line Git,
    you can use `git` in the terminal to work with the repository,
    including reverting changes.

    This page will not cover use of command-line Git.

#### Updating files in the repository

You can use the Source Control panel to update files in the repository.

A codespace is self-contained with its own copy of your repository's files.
This is just as if you were working on a local copy of the repository on your own computer.

**Changes to the copy of your repository in the codespace do not automatically change the state of your published repository on GitHub.**

To get changes from a codespace to the GitHub repository, you must use the Source Control view to add, commit and publish those changes
to your GitHub repository.
If you are unfamiliar with Visual Studio Code and GitHub,
[GitHub has a guide on using this](https://docs.github.com/en/codespaces/developing-in-codespaces/using-source-control-in-your-codespace#committing-your-changes).

When you update files by publishing to the repository's `main` branch,
this should trigger an automated check of whether your code will run in OpenSAFELY.
These checks can be viewed from the Actions tab,
accessed via your repository on GitHub's site.
The screenshot below shows what this tab looks like..

![A screenshot showing the GitHub Actions tab for a repository.](../../../images/codespaces-actions.png)

!!! info
    If you are comfortable with Git,
    you can also [create and switch between different branches in the codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/using-source-control-in-your-codespace)
    in the Visual Studio Code interface
    or by the terminal using command-line Git.

## A quick overview of what is included in the codespace

Now that we have a GitHub codespace running,
we can use OpenSAFELY.

Here is a short, non-exhaustive guide to what OpenSAFELY provides in the codespace.

### Run the OpenSAFELY command-line interface (CLI)

* You can run the OpenSAFELY CLI in GitHub Codespaces.
  In the Visual Studio Code terminal, type `opensafely` and press ++enter++.
* You should see the OpenSAFELY CLI help prompt.
  The screenshot below shows this.

![A screenshot showing the OpenSAFELY CLI help prompt in a GitHub codespace.](../../../images/codespaces-opensafely-cli.png)

!!! info

    See the [OpenSAFELY CLI](../../../opensafely-cli.md) documentation for more details.

## How to run the example project

The research code repository that you created already has a minimal, working OpenSAFELY project in it..

#### Use OpenSAFELY CLI to run the example project

* In the Visual Studio Code terminal,
  type `opensafely run run_all` and then press ++enter++
  to run the existing `project.yaml`.
* This may take a few moments to download the required Docker images,
  before the project is run.

You should see some information messages that should end something like:

```
=> generate_study_population
Completed successfully
```

The screenshot below shows this.

![A screenshot showing an example OpenSAFELY project being run in a codespace.](../../../images/codespaces-opensafely-example-project.png)
