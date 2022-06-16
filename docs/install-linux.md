# Linux Install Guide

This is a series of guidelines for installing the OpenSAFELY CLI on Linux
as opposed to concrete steps.

This is partly because:

* various Linux distributions have different ways of installing software
* it is assumed that you are comfortable enough with your Linux installation enough to make appropriate installation decisions yourself

## Installing Python

Your system package manager may already have a recent version of Python 3 installed.
That version may be sufficient for installing OpenSAFELY.

You can check via PyPI what versions of Python are currently supported.
Check the "Requires" information on the [package page](https://pypi.org/project/opensafely/).

Alternatively, you can use [pyenv](https://github.com/pyenv/pyenv) to install and manage additional Python versions.

## Installing Docker

There are multiple ways you can install Docker:

* your distribution's package manager may have a version of Docker Engine available,
  though this may be slightly older than the current version that Docker offer themselves
* Docker themselves provide [up-to-date package repositories](https://docs.docker.com/engine/install/) for installing Docker Engine
* Docker offer [Docker Desktop for Linux](https://docs.docker.com/desktop/linux/install/).

!!! warning

    Docker Desktop does have license restrictions for some commercial use.
    Check Docker's [license agreement](https://docs.docker.com/subscription/#docker-desktop-license-agreement).

## Installing the OpenSAFELY CLI

It is useful to use [pipx](https://github.com/pypa/pipx) to install Python applications.

pipx installs Python software into a Python virtual environment.
pipx allows you to isolate Python package installations for different software, 
and still easily run that software.

Install the [OpenSAFELY CLI](opensafely-cli.md) with pipx:

```
pipx install opensafely
```

!!! note

    If you installed a newer version of Python than available on your system via pyenv,
    you may want to install the OpenSAFELY CLI using that specific Python version.

    You may do this via a command of the form:

    ```
    pipx install opensafely --python ~/.pyenv/shims/python3.10
    ```

    The actual Python version might vary.


Test the installation of OpenSAFELY CLI.
This should print out the usage and available sub commands:

```
$ opensafely --help
usage: opensafely [-h] [--version] COMMAND ...

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

available commands:

  COMMAND
    help      Show this help message and exit
    run       Run project.yaml actions locally
    codelists
              Commands for interacting with https://www.opencodelists.org/
```

You're done!

Now you can navigate to a research repo on your local machine,
and [use `opensafely` via the command line](opensafely-cli.md#using-opensafely-at-the-command-line).
