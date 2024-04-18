# Understanding the software used to run OpenSAFELY

## Why OpenSAFELY requires several pieces of installed software to run

Some of the software needed is so you can execute code on your computer
in **exactly the same way** it is run in the secure environment: even a slight
mismatch in the versions of the software could cause bugs and delays.

OpenSAFELY is also designed to encourage analysts to adopt best-practice
software development processes, like using `git` for version control.

If you're new to these concepts, there may be quite a lot to learn, and you'll need
to use further software to work with them. The investment will be worthwhile:
you'll find your software quality and efficiency will benefit hugely.

!!! note
    If you use the OpenSAFELY GitHub Codespaces environment,
    all of the required software is already installed for you.

## The software used when working with OpenSAFELY

The software needed to work with OpenSAFELY is designed to run cross-platform,
on Windows, macOS and Linux.

* OpenSAFELY code is written and edited in a text editor or interactive development environment (IDE).
  Examples include:
  * Visual Studio Code
  * R Studio
  * or some other editor of your choice
* Git is version control software.
  Git allows you to work on software,
  record its history in *repositories*,
  and collaborate on that software with others.
  To run against real patient data,
  code using the OpenSAFELY platform is published to GitHub.
  GitHub is an online platform for hosting Git repositories.
* The OpenSAFELY command-line interface (OpenSAFELY CLI) is a program
  that is used to run OpenSAFELY projects,
  whether on your own computer or on the platform hosting real patient data.
* Docker is software that the OpenSAFELY CLI uses
  to run your data extraction and analysis scripts in a reproducible way.
* Python is the programming language that the OpenSAFELY CLI is written in,
  and is required to run the OpenSAFELY CLI.

!!! note
    While most of the required software listed above is open source and free of charge to use,
    Docker Desktop may require you to obtain a paid license
    if you work in a commercial
    or government organisation.

    Consult the [Docker Desktop license agreement](https://docs.docker.com/subscription/desktop-license/).
