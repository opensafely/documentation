The how-to guides in this section provide guidance
for setting up and running the software required for OpenSAFELY.

These tools are required for, or greatly simplify, the following tasks:

* defining the data you want to extract from the database
* importing codelists
* creating dummy data for developing analysis scripts
* testing analysis scripts locally
* running the analysis on the server

## New users

!!! note
    We strongly recommend the use of GitHub Codespaces for working with OpenSAFELY, at least initially.
    GitHub Codespaces does not require any local software installation,
    meaning you can start working in a web browser almost immediately.

* Refer to the [guidance for using GitHub Codespaces](../../github-codespaces.md).

## Experienced users

!!! info

    If you are an experienced OpenSAFELY user who:

    * has administrative access to their computers
    * wants to run OpenSAFELY on their own computer,
      instead of in GitHub Codespaces

    we provide guides on installing the software required for OpenSAFELY on your own machine.

Refer to the relevant guide for the operating system you use:

* [Windows](../../install-windows.md)
* [macOS](../../install-macos.md)
* [Linux](../../install-linux.md)

## All users

All users should be familiar with the OpenSAFELY CLI.

* Refer to the [guidance for the OpenSAFELY CLI](../../opensafely-cli.md)

### Writing analysis code

For the analysis proper,
you can use Stata, R, or Python (almost) however you wish &mdash;
see the [pipelines section](../../actions-pipelines.md#general-code-writing-guidance) for guidance and exceptions.

### Running queries on the OpenSAFELY platform to use OpenSAFELY fully

You will need some platform-specific permissions, for instance to be able to submit analyses to run on the server.
