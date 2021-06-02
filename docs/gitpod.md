## Background

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

## Setting up an account on Gitpod

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
