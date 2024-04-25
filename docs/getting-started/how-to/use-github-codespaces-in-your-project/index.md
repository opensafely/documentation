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

    If you have changes in the codespace that have not been published to the repository,
    GitHub will warn you to confirm that you are sure you want to delete the codespace.

## How to run the OpenSAFELY command-line interface (CLI)

* You can run the OpenSAFELY CLI in GitHub Codespaces.
  In the Visual Studio Code terminal, type `opensafely` and press ++enter++.
* You should see the OpenSAFELY CLI help prompt.

!!! info

    See the [OpenSAFELY CLI](../../../opensafely-cli.md) documentation for more details.

## How to use OpenSAFELY CLI to run the example project

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

   The screenshot below shows this.

   ![A screenshot showing an example OpenSAFELY project being run in a codespace.](../../../images/codespaces-opensafely-example-project.png)


!!! note

    By default, the Visual Studio Code terminal that has opened should be in the correct directory (folder)
    that contains the `project.yaml` file.

    If you have changed the terminal directory by using the `cd` change directory command,
    use `cd` to return to the directory containing `project.yaml` first.


    ```sh
    $ cd /workspaces/"$RepositoryName"
    ```
