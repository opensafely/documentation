

This tutorial will walk you through the minimum steps needed to run an
OpenSAFELY-compliant study against "dummy" (randomly-generated) patient data.
We ask all potential collaborators to successfully complete this tutorial,
before applying to run their project against real data.

This is a first draft of the tutorial, and may have errors or omissions.
Please don't be afraid to ask questions in our [Q&A
forum](https://github.com/opensafely/documentation/discussions)!

## Motivation

OpenSAFELY is designed to allow you to do all of your analytic work on your own
computer, without ever having to access the real, sensitive, patient-level data.

To use the OpenSAFELY framework effectively, you need to:

*  have a few pieces of software available; and
*  understand a few concepts which might be new to you.

## Running OpenSAFELY

There are two options to work with OpenSAFELY:

1. *Use an online environment where much of the needed software is
   already installed for you*.

     **TODO: add configuration so that we can change "much of" to "all
     of".** Services such as [Gitpod](https://gitpod.io) provide online
     computing environments; Gitpod currently has a free plan with a
     generous monthly usage limit for working with public code.

     For this option, the only requirement is a modern web browser (e.g.
     Chrome, Edge, Firefox, Safari).

     You might prefer an online environment if one or more of the
     following apply:

     * you are investigating what OpenSAFELY offers and want to start
       using it immediately;
     * you do not have administrative access to install software on your
       work computer;
     * you are not sure about whether your computer supports Docker,
       which OpenSAFELY uses;
     * you want to try OpenSAFELY via a device other than a computer,
       e.g. a tablet.

2. *Install the required software to your own computer*.

     You might prefer a local installation if one or more of the following
     apply:

     * you already have the software required (Docker, Python and Git or
       GitHub Desktop) installed;
     * or you don't already have the required software installed, but
       are comfortable installing and configuring these tools yourself;
     * you want to have more control on the tools you use to develop
       studies for OpenSAFELY.

    The current local installation instructions is aimed at Windows
    users. Mac users should be able to follow along as well, with a few
    hopefully-obvious alterations; see also the [macOS Install
    Guide](install-macos.md)! We aim to integrate macOS instructions
    into this guide in future.

!!!note
    Tabbed sections like the example immediately below split the
    configuration instructions into web browser and local Windows installation.
    Where these tabbed sections appear, follow just the relevant section.

=== "Web browser (online)"

    These "Web browser" sections will explain how to use OpenSAFELY in a
    web browser via the Gitpod service.

=== "Windows (local)"

    These "Windows" sections will explain how to use OpenSAFELY using
    software installed directly on a Windows machine. These instructions
    are not necessary to follow if you are using a web browser to run
    OpenSAFELY, even if that web browser is running on Windows.

### Options for running OpenSAFELY

Some of the software needed is so you can execute code on your computer
in **exactly the same way** it is run in the secure environment: even a slight
mismatch in the versions of the software could cause bugs and delays.

OpenSAFELY is also designed to encourage analysts to adopt best-practice
software development processes, like using `git` for version control.  If
you're new to these concepts, there may be quite a lot to learn, and you'll need
to use further software to work with them. The investment will be worthwhile:
you'll find your software quality and efficiency will benefit hugely.

This tutorial is, therefore, a very fast tour through all the **essential**
components required to get up and running. When you've finished, you'll have
all the basics in place to continue your learning.

## 1. Set up GitHub

To use OpenSAFELY, you must have a GitHub account. GitHub is a widely-used
website for storing and collaborating on software, using the version control
software `git`. GitHub is where your open, reproducible research will be
published.

### Creating a GitHub account

If you do not already have a GitHub account, you should create one
first.

=== "Web browser (online)"

    Visit [GitHub](https://github.com) and click the "Sign up" button.
    You will have to provide an email address and password. GitHub will
    also send you a confirmation email containing a link that you need
    to visit to confirm your account.

=== "Windows (local)"

    It is possible to follow the "Web browser" instructions and simply
    sign up on GitHub's site.

    If you [install GitHub Desktop](https://desktop.github.com/), the
    GitHub Desktop installation process will also walk you through the
    process of creating an account, if you don't already have one.

    If you already have a GitHub account, GitHub have guides on
    authenticating an existing account with [GitHub
    Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/authenticating-to-github).

    (If you already have `git` configured and are reasonably confident using
    it, GitHub Desktop is not required. You need to be able to `clone` the
    template repository that you will create, then `add`, `commit` and
    `push` changes to that repository to GitHub.)

#### Securing your GitHub account

We recommend that you [secure your GitHub account with two-factor
authentication](https://docs.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa).

## 2. Create a new repository in GitHub

Here, you'll copy our OpenSAFELY research template to your own GitHub
account, for developing your own study:

1. Go to the [GitHub website](https://github.com), and ensure you're logged in.
   You'll be able to tell by looking for your profile at the top right of the
   page.
2. Visit our [research template
   repository](https://github.com/opensafely/research-template)
3. Above the file list, click **Use this template**
   ![image](images/use-this-template-button.png)
4. Use the **Owner** drop-down menu, and select the account you want to own the
   repository (typically under your own account)
   ![image](images/create-repository-owner.png)
5. Type a name for your repository, and an optional description.
   ![image](images/create-repository-name.png)
6. Choose a repository visibility.  This would usually be "Public".
   ![image](images/create-repository-public-private.png)
7. There is an "Include all branches" option: it can be left disabled.
   (You only need the main branch; the other branches are
   work-in-progress changes.)
8. Click **Create repository from template**

## 3. Setup the required software

<!-- The generated table of contents does not dynamically adjust according to selected tab for tabbed contents. Use actual heading tags to prevent headings in tabbed sections from appearing in the table of contents. -->
=== "Web browser (online)"

    <h3>Opening your repository with Gitpod</h3>

    **TODO: Install the software in the template via a `.gitpod.yml` to
    remove the need for these instructions.**

    For the repository you just created, it will have a URL of the form:
    `https://github.com/<your_username>/<your_research_repository>`
    where the username and repository name are as you chose.

    Place `https://gitpod.io/#` in front of that URL:

    `https://gitpod.io/#https://github.com/<your_username>/<your_research_repository>`

    and visit that URL. If it is the first time you have used Gitpod,
    you'll see a "Log in" screen. You can use your GitHub account to
    login: click "Continue with GitHub".

    <h3>Gitpod workspaces</h3>

    A Gitpod workspace containing a code editor, defaulting to Visual
    Studio Code and command-line interface "terminal" should then
    appear. The terminal that Gitpod provides runs commands on a Linux
    computer, but, don't worry, the few command-line instructions for
    working with OpenSAFELY are the same regardless of using Windows,
    Linux or macOS.

    On the free plan, Gitpod workspaces allow 30 minutes of inactivity
    before the workspace stops running. The workspace is not immediately
    deleted; you have several days to open a stopped workspace before it
    is deleted. You can see which Gitpod workspaces you have open by
    visiting `https://gitpod.io` when logged into Gitpod, or clicking
    the orange Gitpod button in the bottom-left of the screen and
    selecting "Gitpod: Open dashboard". The stopped workspaces are
    visible by changing the search filter from "Active" to "All", and
    you can open a stopped workspace by hovering on the workspace,
    left-clicking on the vertical dots (`⋮`) and selecting "Open".

    To preserve usage minutes on Gitpod, you can manually stop a Gitpod
    workspace, either in the workspace via the orange Gitpod button
    ("Gitpod: Stop workspace" in the menu) or via visiting
    `https://gitpod.io`, hovering on the workspace, left-clicking on the
    vertical dots (`⋮`) and selecting "Stop".

    <h3>Install **opensafely**</h3>

    OpenSAFELY uses the Python programming language. Python is already
    installed in Gitpod, so we can use the Python package manager, `pip`
    to install the OpenSAFELY package that we need.

    Inside the terminal in the bottom right of the Visual Studio Code
    environment, run `pip install opensafely`. The output should
    something like the following (though the `opensafely` version number
    may differ):

    ```
    $ pip install opensafely
    Collecting opensafely
    …
    Installing collected packages: opensafely
    Successfully installed opensafely-1.8.1
    ```

    <h3>Check `opensafely` is working</h3>

    Run `opensafely pull cohortextractor` and you should see something like:

    ```
    $ opensafely pull cohortextractor
    …
    Status: Downloaded newer image for ghcr.io/opensafely-core/cohortextractor:latest
    ghcr.io/opensafely-core/cohortextractor:latest
    Cleaning up old images
    Total reclaimed space: 0B
    ```

    This tells us that `opensafely` is working!

=== "Windows (local)"

    To develop an OpenSAFELY study on your own computer, you will need to install a
    few things. Most important is the `opensafely` tool; to install this, you must
    (currently) first install the Python programming language.

    <h3>Install Python and **opensafely**</h3>
    1. [Download and run the Anaconda Python
       installer](https://docs.anaconda.com/anaconda/install/windows/).
    2. When you've done, to verify your installation, open Anaconda Prompt by
       clicking Start, search, or selecting Anaconda Prompt (or Anaconda Powershell)
       from the menu. ![Finding Anaconda Prompt on
       Windows](./images/win-anaconda-prompt.png)
    3. To install the OpenSAFELY command line tool, you first need to
       install a tool called `pip`. ([`pip`](https://pip.pypa.io/en/stable/)
       is used for installing Python software and libraries.)
       Do this by typing `conda install pip` and pressing ++enter++.
    4. Now you can install the OpenSAFELY command line tool, by typing `pip
       install opensafely`, and pressing ++enter++. You should see a message
       to the effect of `Successfully installed opensafely`.
    5. To confirm everything is working, type `opensafely` and press
       ++enter++. If the OpenSAFELY tool is working, this will show help
       text on how to use the `opensafely` command.

    <h3>Install Docker</h3>

    !!! note "Windows alert"
        On Windows, installing Docker is usually
        straightforward, but can sometimes be complicated, depending on your exact
        version and configure of Windows. If you run into problems, our more
        [detailed installation notes](install-docker.md) may help.


    1. If you are using Windows 10 Pro, Enterprise or Education, you should [follow
       these instructions](https://docs.docker.com/docker-for-windows/install/).
       Otherwise, follow the instructions for [installing on Windows
       Home](https://docs.docker.com/docker-for-windows/install-windows-home/).
       Unfortunately, we've had reports that installing in Windows Home can
       be very challenging. Please let us know if you can help us [improve
       the documentation](requests-documentation.md) here.
    2. Starting Docker can take a while &mdash; up to 5 minutes. While it's doing
       so, an animation runs in the notification area:<br>
       ![image](images/docker-windows-starting.png)
    3. When Docker has finished starting up, share your hard drive with Docker:
       click system tray docker icon; select "settings"; select "shared drives".
    4. Test Docker and opensafely work together. Open an Anaconda Prompt, and run
       `opensafely pull cohortextractor`. This will pull down the OpenSAFELY
       cohortextractor images, which can be used to run actions in your study.  The
       first time you run it, this may take a little time, depending on your
       network connection. It is downloading a reproducible environment identical
       to that installed in the OpenSAFELY secure environment.

## 4. Set up your first study

In a previous step, you previously created a copy of the research code
in GitHub. You need to have a copy, or "clone", of that code to develop your own
study.

=== "Web browser (online)"

    When you open the Gitpod workspace, the associated code from GitHub
    will already be there.

=== "Windows (local)"

    <h3>Clone it to your computer</h3>

    1. Look above the list of files in your new repo for a **Code** button. ![image](images/code-button.png)
    2. Click **Open with GitHub Desktop** to clone and open the repository with
       GitHub Desktop. ![image](images/open-with-desktop.png)
    3. Click **Choose...** and, using Windows Explorer, navigate to a local path
       where you want to clone the repository.
       ![image](images/clone-choose-button-url-win.png)
    4. Click **Clone**  ![image](images/clone-button-url-win.png)

### Test the blank study on your computer

=== "Web browser (online)"

    The study will already be prepared to run. Run the `opensafely`
    commands in the "terminal" available at the bottom-right of the
    Gitpod workspace.

=== "Windows (local)"

    You can open a prompt to run the study code:

    1. Open Anaconda Prompt (or use an already-open one)
    2. Change your current directory to the location of your cloned, local path. To
       do this, use the `cd` command. For example, `cd
       C:/Users/me/my-git-repos/hello-world` and press ++enter++.

    Run the `opensafely` commands in the Anaconda Prompt.

Now you're ready to run your first study. Type `opensafely run run_all`
and press ++enter++

The first time you run this command, it will take a while to download the
required software. Eventually, you should see output that ends something like
this:

```shell-session
$ opensafely run run_all
<...several lines of output...>
generate_study_population: Extracting output file: output/input.csv
generate_study_population: Completed successfully
generate_study_population: Cleaning up container and volume

=> generate_study_population
Completed successfully

log file: metadata/generate_study_population.log
outputs:
 output/input.csv  - highly_sensitive
```
The final line tells you a file of (randomly-generated) patient data has been created at
`output/input.csv`, and that it should be considered highly sensitive
data. What you see here reproduces exactly what would happen on a real, secure
server, but with *dummy data* which contains no real patient information. 
Because we haven't modified the template blank study yet, this file is empty &mdash; 
we'll generate more dummy data in the next section.

If you run `opensafely run run_all` for a second time, you'll see the command
does nothing (because there's already a file at `output/input.csv`):
```shell-session
$ opensafely run run_all
=> All actions already completed successfully
Use -f option to force everything to re-run
```

### Accessing files

=== "Web browser (online)"

    <h4>Opening files</h4>

    The Visual Studio code editor has a file Explorer that you can use
    to browse the files and appears when first starting the Workspace.
    
    You can press ++Control+Shift+E++ to switch to it, or select it via
    the icons at the side.

    Clicking on a file name in the Explorer will open the file in a tab
    within the editor.

    TODO: screenshot showing selecting the Explorer.

    <h4>Downloading files from Gitpod to your local machine</h4>

    Right-click a file in the Explorer and select "Download".

=== "Windows (local)"

    The newly created output files are created in the local copy of the
    repository in the `output/` directory.

## 5. Make changes to your study

You've successfully run the code in your study, but at the moment it just creates an empty output
file. Now we'll add some code to do something slightly more interesting.

In order to write code in the OpenSAFELY framework, a code editor will
make your life much easier. The steps here use Visual Studio Code, which
is free of charge and available for Windows, macOS and Linux. If you are
already comfortable using another editor, that will also be suitable.

=== Web browser (online)

    Gitpod's workspaces use Visual Studio Code as the default editor.

=== Windows (local)

    Download and install
    [Visual Studio Code](https://code.visualstudio.com/download).

### Add an `age` column

1. Start Visual Studio Code and use the menu to open your research repository
   (**File > Open Folder...**)
2. In the "Explorer" on the left hand side, find and click on the file at
   `analysis/study_definition.py`. This file specifies the population that 
   you'd like to study (dataset rows) and what you need to know about them (dataset columns).
3. Add some text so that the file looks like this (new text highlighted):
```python linenums="1" hl_lines="14 15 16 17 18 19 20"
from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

    age=patients.age_as_of(
        "2019-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
)

```
Line 10 means "*I'm interested in all patients who have never changed practice,
between these two dates*"; lines 14-15 "*Give me a column of data corresponding
to the age of each patient on the given date*"; and lines 16-18 "*I expect
every patient to have a value, and the distribution of ages to match that of the
real UK population*"
1. At the command line, run `opensafely run run_all
   --force-run-dependencies`. A new file will be created in the folder
   `output/input.csv`. Open that file (using Visual Studio Code's
   Explorer, or software like Excel) and you'll see it now contains an
   age for 1000 randomly generated patients.

### Add a chart

**Every** study starts with a *study definition* like the one you just edited.
When executed, a study definition generates a CSV of patient data.

A real analysis will have several further steps after this. Each step can be
written in [any of the programming languages supported in
OpenSAFELY](actions-scripts.md). In this tutorial, we're going to draw a
histogram of ages, using four lines of Python.

1. Using Visual Studio Code, create a new file (**File > New File**), and add
   the following:
```python
import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.age.plot.hist().get_figure()
fig.savefig("output/descriptive.png")
```
This code reads the CSV of patient data, and saves a histogram of ages to a new file.
2. Save this file as `analysis/report.py`
3. In Visual Studio Code, open `project.yaml`. This file describes how each step
   in your analysis should be run. It's in a format called YAML: the way it's
   indented matters, so be careful to copy and paste the following carefully.
4. Add a `describe` action to the file, so the entire file looks like this:
```yaml linenums="1" hl_lines="13 14 15 16 17 18"
version: "3.0"

expectations:
  population_size: 1000

actions:
  generate_study_population:
    run: cohortextractor:latest generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv

  describe:
    run: python:latest python analysis/report.py
    needs: [generate_study_population]
    outputs:
      moderately_sensitive:
        cohort: output/descriptive.png
```
Line 13 tells the system we want to create a new action called `describe`. Line
14 says how to run the script (using the `python` runner). Line 15 tells the
system that this action depends on the outputs of the
`generate_study_population` being present. Lines 16-18 describe the files that
the action creates. Line 17 says that the items indented below it are
*moderately* sensitive, that is they may be released to the public after a
careful review (and possible redaction). Line 18 says that there's one output
file, which will be found at `output/descriptive.png`.
5. At the command line, type `opensafely run run_all
   --force-run-dependencies` and press ++enter++.  This should end by
   telling you a file containing the histogram has been
   created. Open it — you can do this via Visual Studio Code's Explorer,
   or use another tool — and check it looks right.

## 6. Push your study to github, and watch the automated tests pass

Now that your study does something interesting, you should "*push*" it to GitHub,
where it can be viewed by others. Your repository is automatically configured
with tests to verify the project is runnable, each time you push.

=== Web browser (online)

    <h3>Enable Gitpod to be able to push your changes to GitHub</h3>
    
    1. When logged into Gitpod, visit their [Settings
       page](https://gitpod.io/settings). Or, alternatively, in a Gitpod
       workspace, press the orange Gitpod button in the bottom-left of
       Visual Studio Code and then select "Gitpod: Open Settings" from
       the list of options.
    2. Select Integrations and under Git Providers, hover over your
       GitHub details, click the three vertical dots (`⋮`) and select
       "Edit Permissions". In the list, tick "public\_repo", which gives
       your Gitpod account "write access to code in public repositories
       and organizations" on GitHub. (There is an another permission
       that you have to enable for access to code in private
       repositories, though this is not necessary for this walkthrough.)

    <h3>Add your changes to the local repository</h3>

    (If you know how to use command-line Git, those commands work within
    Gitpod's terminal for `add`ing, `commit`ting and `push`ing.)

    Back in the Gitpod workspace, open Source Control either by
    selecting the icon that has dots connected by lines on the left-hand
    side, or by pressing Ctrl+Shift+G together. (**TODO: use keyboard
    formatting with double plus.)

    Source Control should list the changes to the files that are saved
    (**TODO: Visual Studio Code in Gitpod has Auto Save enabled.**). If
    you left-click on a file, you'll see the changes to the file from
    the current repository state. Right-click on the files that you want
    to add the changes to the repository and select "Stage Changes".
    These move into the "Staged Changes" section.
    
    Now type a message into the text box above that will describe the
    changes.  When ready, you
    can then press Ctrl+Enter to *commit* the changes to the repository
    to add them to version control.

    <h3>Push the changes to GitHub</h3>

    Hover over "Source Control", click the three horizontal dots (`⋯`)
    next to "Source Control" and then select "Push". This should submit
    your changes to the GitHub repository that you created earlier.

=== Windows (local)

    <h3>Push the changes to GitHub with GitHub Desktop</h3>

    1. Open GitHub Desktop to view your repository. When you make changes to files in
       your text editor and save them locally, you also see the changes in
       GitHub Desktop. To add all changes in all files to a single "*commit*", tick the
       checkbox at the top of the list.<br>
      ![image](images/commit-all.png)
    2. At the bottom of the list of changes, in the **Summary** field, type a short,
       meaningful description of the changes (this is called the *commit message*).
       Optionally, you can add more information about the change in the
       **Description** field. Press the blue button to make the commit.<br>
      ![image](images/commit-message.png)
    3. Click **Push origin** to push your local changes to the remote repository on
       GitHub ![image](images/push-to-github.png)

In a web browser, visit your repository in GitHub. Click on the **Actions**
tab ![image](images/github-actions-tab.png)
You'll see a *Workflow* running with the *commit message* of your last
commit. The workflow verifies that the command `opensafely run run_all` can
run successfully. If it's yellow, it's still running. If it's red, it
has failed. If it's green, it has succeeded. You want it to be green!
![image](images/github-running-workflow.png)

## 7. Next steps

Congratulations! You've covered all the basics that you need to develop a study
on your own computer, verify that it can run against real data, and publish it
to GitHub.

To write a real study and run it against actual patient data, you will first
need to get permission for your project from NHS England, the data controllers
for OpenSAFELY's data. We are currently developing an online application
process, but for now just drop us an email at
[team@opensafely.org](mailto:team@opensafely.org).

In the meantime, take a look at the rest of our documentation for more
detail on the subjects covered in this tutorial. For example:

* The [full study definition reference](study-def.md) describes all the
  different ways to define new variables in your study definition.
* You'll find more information about the contents of `project.yaml` in the
  [Actions reference](actions-intro.md).
* There is a final step we've not described here: [a
  website](https://jobs.opensafely.org/) called the ["OpenSAFELY Job
  Server"](job-server.md) where you can submit your repository actions to be run
  automatically within the secure EHR vendor environments. Right now you can
  only use this to run real jobs, but we're working on adding the ability to
  test your repository against dummy data.
* You'll be using `git` and GitHub a lot, and it's a critical but complex part
  of the OpenSAFELY ecosystem. If you're not familiar with these concepts, it's
  a good idea to read our [git workflow page](git-workflow.md) and its linked content.
