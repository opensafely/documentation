## Background

In its current form, OpenSAFELY can be trickier for people who are not
software developers to get running.

This draft document is currently written in parallel to the [Getting
Started guide](getting-started.md); *please reference that guide* to
follow along. This, therefore, is a more terse document explaining an
alternative route to following the tutorial, but without duplicating the
tutorial content.

There are several online environments for editing and running code, and
publishing code changes to GitHub that are accessible in browser and
don't require installation of extra tools on your own computer.

[Gitpod](https://gitpod.io) is an online service that provides a coding
environment. It interacts with GitHub and other code collaboration
services to allow you to develop code entirely online using just a
modern web browser. *This is by no means an endorsement of Gitpod over
other available alternatives; other services may well support
OpenSAFELY.* However, DataLab developers investigated have followed the
Getting Started tutorial and found that Gitpod is sufficient for trying
OpenSAFELY out.

## What is *not* required

**If you follow this guide, you do not need to install any software or
clone repository files to your own computer.**

## Requirements

* A network connection with access to [Gitpod](https://gitpod.io).
* A modern browser.
* A GitHub account. (Other code platform accounts can be used with Gitpod, but
  OpenSAFELY uses GitHub.)

## Gitpod details and limitations

* The free Gitpod service currently has a 50 hours per month usage
  limit.
  * You may want to manually stop Gitpod workspaces when not in use.
    Gitpod has a 30 minute timeout on workspaces [if there is no
    activity](https://www.gitpod.io/docs/life-of-workspace/)
  * **TODO: is this just interactive keyboard/mouse activity.**
* The free Gitpod service only allows working with *public*
  repositories, although there is a 30 day trial for working with
  *private* repositories.
* There are paid Gitpod options and, if you're very keen, a self-hosted
  option.
* You have to allow some limited access to GitHub from your own GitHub
  account.
* If you go to `https://gitpod.io` while logged in, the page will show
  you your Gitpod workspaces.

## Setting up a repository on GitHub

* Create a public repository from the OpenSAFELY study template for you
  to work in, as in the ["Create a new repository in
  GitHub"](getting-started/#2-set-up-your-first-study) section.
  * *You do not need to clone the repository to your own machine.* We
    will later access this repository from GitHub via Gitpod.

## Setting up an account on Gitpod

* Visit Gitpod's site and click the "Try now" button, and then "Continue
  with GitHub".
* If you are already logged into GitHub, it will ask you to confirm
  whether you want Gitpod to access some of your details on GitHub
  (initially, this should just be your email address). This is necessary
  to create a Gitpod account.
  * If you are not logged into GitHub, you will be prompted to login to
    GitHub first.
* If you copy the GitHub URL for your study repository, you can now
  create a URL of the form:
  `https://gitpod.io/#https://github.com/<your_username>/<your_repository_name>`
* This opens an interactive Visual Studio Code environment for editing
  the files in your study repository. This environment includes a
  command-line shell for actually installing software and running
  commands. Note that commands you run in this shell are run on a Gitpod
  virtual server running Linux, not your own computer.
  * (Don't worry that this is Linux! We'll be doing most of the
    interaction via the code editor, and the commands we use are similar
    regardless of running on Windows, macOS or Linux.)
  * The working directory for your repository on the virtual server is
    `/workspace/<name of your repository>`.

## OpenSafely tutorial

### Install and test setup

Python 3 is already installed, so we can use the Python package
manager, `pip` to install the OpenSAFELY package that we need.

Inside the terminal in the bottom right of the Visual Studio Code
environment, run `pip install opensafely`. The output should look like:

```
$ pip install opensafely
Collecting opensafely
…
Installing collected packages: opensafely
Successfully installed opensafely-1.8.1
```

We can follow the [test in the Getting Started guide](getting-started/#install-docker) to ensure everything
works. Just run `opensafely pull cohortextractor` and you should see
something like:

```
$ opensafely pull cohortextractor
…
Status: Downloaded newer image for ghcr.io/opensafely-core/cohortextractor:latest
ghcr.io/opensafely-core/cohortextractor:latest
Cleaning up old images
Total reclaimed space: 0B
```

As this works, we can [test the blank
study](getting-started.md#test-the-blank-study-on-your-computer) via
`opensafely run run_all`:

```
$ opensafely run run_all
…
=> generate_study_population
   Completed successfully

   log file: metadata/generate_study_population.log
   outputs:
     output/input.csv  - highly_sensitive
```

This generates `output/input.csv` which has no data. It can be viewed in
the Visual Studio interface by clicking in the file Explorer to the
left-hand side, clicking the `output` directory to open it and then
clicking on the file. This opens a new tab containing the file.

It is also possible to download files in this environment by
right-clicking on a file and selecting "Download".

As the [blank study
test](getting-started.md#test-the-blank-study-on-your-computer) does, we
can run the `opensafely` command again to confirm everything is
up-to-date:

```
$ opensafely run run_all
=> All actions already completed successfully
   Use -f option to force everything to re-run
```

### Modify the study to add an "age" column

Follow the instructions roughly as ["Add an `age`
column"](getting-started.md#add-an-age-column). We already have Visual
Studio Code open, so we can just add the required changes to
`analysis/study_definition.py`. Where the instructions in that guide say
"Anaconda Prompt", we can just use the terminal that we have open in
Gitpod to run `opensafely` again via `opensafely run run_all
--force-run-dependencies`.

```
$ opensafely run run_all --force-run-dependencies

Running actions: generate_study_population

jobrunner.run loop started
generate_study_population: Preparing
generate_study_population: Copying in code from /workspace/opensafely-study-example
generate_study_population: Started
generate_study_population: View live logs using: docker logs -f job-opensafely-study-example-generate-study-population-5neqw2huucrvpgfr
generate_study_population: Running
generate_study_population: Finished, checking status and extracting outputs
generate_study_population: Logs written to: /workspace/opensafely-study-example/metadata/generate_study_population.log
generate_study_population: Extracting output file: output/input.csv
generate_study_population: Completed successfully
generate_study_population: Cleaning up container and volume

=> generate_study_population
   Completed successfully

   log file: metadata/generate_study_population.log
   outputs:
     output/input.csv  - highly_sensitive
```

If you now open the created CSV — `output/input.csv` again — you see
that it should contain `age,patient_id` and some data values.

### Create a chart

We can now follow the instructions as in ["Add a
chart"](getting-started.md#add-a-chart).

* Copy-paste the provided `report.py` code and save in `analysis/`.
* Copy-paste the `describe` action to `project.yaml`.
* Run `opensafely run run_all --force-run-dependencies` which should
  generate the chart.
* If you click `descriptive.png` in `output/` in the Visual Studio Code
  Explorer, you should see the file. You can also download it by
  right-clicking and selecting "Download".

### Store changes to your repository

We can add changes to the repository — a "commit" — and then "push" that
commit to GitHub.

#### Permissions

If you want to push changes to GitHub, you have to give Gitpod access to
GitHub to do so.

* Go to `https://gitpod.io` while logged in and you should see an option
  for "Settings", which you should choose.
* In the list of settings, select "Integrations".
* Under "Git Providers", hover over your GitHub details, click the three
  vertical dots (`⋮`) and select "Edit Permissions". In the list, tick
  "public\_repo", which gives your Gitpod account "write access to code in public
  repositories and organizations" on GitHub.

#### Know how to use command-line `git`?

You can simply use `git` in the terminal.

#### Via the Visual Studio Code user interface

* Click on the "rail icon" in the left-panel of Visual Studio Code to
  get to "Source Control".
* You should see the files that have changes.
* You can right-click on a file and click "Stage Changes" to add it to
  the next commit. You can select multiple files holding the Control or
  Shift keys as you can in e.g. Windows.
* **TODO: commit to a branch optionally?**
* Enter a message where it says "Message" and press Ctrl-Enter to create
  a commit.
* Click on the three horizontal dots (`⋯`) along from "Source Control"
  and select "Push".
  * If you don't have permissions, the Visual Studio Code editor will
    prompt you to enable permissions. Or you can follow the instructions
    above. Then try pushing again.
* You should see your changes reflected in the repository on GitHub
  where you can review the Actions tab as in the [Getting Started
  guide](getting-started.md#4-push-your-study-to-github-and-watch-the-automated-tests-pass).

## Extra credit: run JupyterLab

JupyterLab is another code development environment, aimed at developers
and data scientists working interactively. Let's install it and use it
to produce the same chart via very similar Python code.

### Install Jupyterlab

Install Jupyterlab via `pip`: `pip install jupyterlab`.

```
$ pip install jupyterlab
…
Installing collected packages: sniffio, websocket-client, pytz, anyio, jupyter-server, json5, babel, nbclassic, jupyterlab-server, jupyterlab
Successfully installed anyio-3.1.0 babel-2.9.1 json5-0.9.5 jupyter-server-1.8.0 jupyterlab-3.0.16 jupyterlab-server-2.5.2 nbclassic-0.3.1 pytz-2021.1 sniffio-1.2.0 websocket-client-1.0.1
```

We'll also need `pandas` to load our data and `matplotlib` to generate
our chart: `pip install matplotlib pandas`.

### Launch Jupyterlab

First, create a new integrated terminal, by clicking the "+" sign in the
terminal window.

Now run Jupyterlab:

```
$ jupyter lab --NotebookApp.allow_origin=\'$(gp url 8888)\'
…
To access the server, open this file in a browser:
…
Or copy and paste one of these URLs:
…
```

#### Technical notes

Note: the `allow_origin` option is required to make Python available to
the notebook interface in Gitpod, it is *not normally required* for
local use; credit to [this issue
comment](https://github.com/gitpod-io/gitpod/issues/758#issuecomment-525706696).

Note that the URLs are represented as they are on Gitpod's server.
You'll see a URL given as `localhost`; `localhost` refers to "this
machine" but that's Gitpod's server. The actual URL that you would
access Jupyterlab by is actually a `gitpod.io` one.

#### Accessing Jupyterlab

A simple browser will open but most likely fail; you can close this.
Visual Studio Code will prompt to "open in browser". If you dismiss that
prompt, you can hold the Control key and then click on the "localhost"
link which should also open the link up in a new tab or window.
Depending on your browser, you may get a popup-blocker prompt, as this
opens a new browser window or tab.

In the URLs to access Jupyter, there will be a long hexadecimal token
which contains only the numbers `0-9` or `A-F`, e.g.

```
Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=<your_token>
```

Copy-paste the token to the new Jupyter password prompt in the new
browser tab or window and press "Log in".

You should then see the Jupyterlab launcher which has a list of your
files and options for creating a new Notebook, Console or other files.

#### Switching terminal windows

You can get back to your first terminal window to run further commands
by clicking the dropdown next to the "+" in the terminal area and
selecting the `1: …` entry.

### Use Jupyterlab

* **TODO: if you want to use the same code, you'd have to have the
  notebook in the root. How do people arrange notebooks locally for
  development?**
* In the launcher, create a Python 3 notebook in the root of the
  repository by clicking "Python 3" under Notebook.
* Copy the code from `analysis/report.py` into the notebook, as a
  starter. You can copy from the Visual Studio Code editor or open the
  file in Jupyterlab.
* Comment out the `fig.savefig` line; we can simply see the plot in the
  notebook without needing to save it (though we can uncomment this line
  to save the file).

## Cleaning up

### Deleting Gitpod workspaces

* Click the Gitpod button in bottom corner, and stop workspace.
* If you want to access the workspace again, you have to go to
  Workspaces and filter to "All" instead of "Active".
* Inactive workspaces get remove 14 days after no use.
* If you select the workspace, you can manually delete it ahead of time.

### Remove GitHub access

You can remove GitHub access from Gitpod by going to the Settings page
in Gitpod. Select "Integrations", then hover over the GitHub entry. Now
click the three vertical dots (`⋮`)  and either select "Edit
Permissions" to remove certain permissions or select "Manage on
GitHub.com" to remove Gitpod access to your GitHub account entirely.

### Delete Gitpod account 

Go to Gitpod's Settings page, then select "Account" and "Delete
Account".
