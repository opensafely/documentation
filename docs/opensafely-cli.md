The main tool for using the OpenSAFELY platform locally is the `opensafely` Python module, which is run via the command-line interface (CLI).

Its main function is to run data extraction and analysis scripts that are specified in the [project pipeline](actions-pipelines.md), in a way that mimics the production environment where real data is accessed.

It also contains other functions relating to the OpenSAFELY workflow, such as updating codelists from [OpenCodelists](https://www.opencodelists.org).

## Installing `opensafely`

This is a command-line program.

To install, go to the Anaconda prompt and run the following command (or use another method to install the module if you know how):

```bash
pip install opensafely
```

To check this has installed successfully, run `opensafely --version`.

## Updating `opensafely`

You should keep the tool up to date as much as possible. You can upgrade to a new version of `opensafely` by running:

```bash
opensafely upgrade
```

The above command only works with opensafely version 1.6.0 or newer. If you are
using an older version, you will first need to upgrade it with:

```bash
pip install --upgrade opensafely
```

## Using `opensafely` at the command line

To view the in-built documentation for each command, run `opensafely --help` at the terminal, which will list all the ways in which you can use it.
You can also use `opensafely run --help` to learn more about the `run` command, for example.

To run any of these commands for a specific OpenSAFELY project, you need to change the directory of your prompt to be the repository of the project.
For example,  `cd C:/Users/me/my-git-repos/my-repo`.


More information on how to use the `opensafely` module is available in specific sections elsewhere, but some key functions are described briefly below.

### `run` - run an action from project.yaml

The most common command you'll run.
This runs actions defined in the [`project.yaml` file](actions-pipelines.md) and is the main way of testing your code.

For example,

```bash
opensafely run make_graph
```

will run the `make_graph` action.

<details markdown="1">
<summary>To run or to force run?</summary>

The `run` command takes `--force-run-dependencies` or `-f` arguments,
where the latter is the short form of the former.
However, what do these arguments do?

When an action is a dependency of another action,
the `run` command uses the dependency action's outputs
-- and one of these arguments, if one is present --
to determine whether the dependency action should also run.

If you specify the action to run but don't pass one of these arguments, then:

* The action is run, whether or not its outputs exist.
* Its dependencies are also run, if their outputs do not exist.
  Conversely, its dependencies are not run, if their outputs exist.

If you specify the action to run and pass one of these arguments, then:

* The action is run, whether or not its outputs exist.
* Its dependencies are also run, whether or not their outputs exist.

What about the `run_all` action?
Think of all actions as dependencies of the `run_all` action.

If you specify the `run_all` action but don't pass one of these arguments,
then for each action:

* If the action's outputs exist, then it is not run.
* If the action's outputs do not exist, then it is run.

If you specify the `run_all` action and pass one of these arguments, then:

* All actions are run, whether or not their outputs exist.
</details>

### `codelists` - managing codelists
This command is for working with codelists.

Use
```bash
opensafely codelists update
```

to retrieve each codelist listed in `/codelists/codelists.txt` from [OpenCodelists](https://www.opencodelists.org).
It will add (or update) the codelist `.csv` files to the `codelists/` folder.

Use
```bash
opensafely codelists check
```

to check if the codelist files are up-to-date with those listed in `./codelists/codelists.txt`.

See the [Codelist](codelist-intro.md) section for more information on codelists.


### `pull` - updating Docker images


To run your code on your machine, the `opensafely` tool uses the same Docker
images that run in the secure server environments. These are updated
periodically, for example when new libraries are installed. If you have error
messages about missing libraries, your Docker images may need upgrading.
To pull the most recent Docker images to your machine, run:

```bash
opensafely pull
```

### `jupyter` - running JupyterLab

[Jupyter notebooks](https://jupyter.org/) are useful interactive
environments for developing code.

You can run JupyterLab to use Jupyter notebooks via the `opensafely`
tool. This ensures that the Python code you write will work in the
OpenSAFELY environment.

From the directory containing code that you are working on, run:

```bash
opensafely jupyter
```

JupyterLab should then open in a web browser automatically. Otherwise,
copy the long URL shown by the JupyterLab logs — starting
`http://localhost`… — and use that URL in a web
browser to access JupyterLab.

To exit, press ++control+c++ in the command line - this also shuts down the container.
Or alternatively go to File -> shutdown in the JupyterLab tab.

### `unzip` - unzipping csv files

For performance and storage reasons on the backend, you must use the
compressed `csv.gz` output format for cohortextractor output files. However,
you may need to inspect the raw csv data. You can easily unzip a csv file with

```bash
opensafely unzip outputs/input.csv.gz
```

This will create a decompressed `output/input.csv` file you can view as normal.


### Managing Resources

The `opensafely` tool runs your jobs in Docker containers. If you're on Windows or Mac
OSX, your installed Docker Desktop app will likely have a subset of CPU and memory
resources available to it. If using Docker Desktop, you can increase
the resources allocated in that application.

You can quickly view your current Docker resources with `opensafely info`.


#### Concurrency

By default, `opensafely run` will run at most 2 jobs at a time. You can
increase or decrease this by adding the flag `--concurrency`, or `-c` for
short.

Typically, there are two reasons to use this flag.

First, to go faster if you have the resources available. Note: this will
decrease whole project run time but increase memory usage.:

```
opensafely run run_all -c 8
```

Second is to go slower, if your jobs are hitting memory limits, to give each job
the full resources of your local Docker installation:

```
opensafely run job_with_heavy_dependencies -c 1
```


#### Memory

You may see errors reporting jobs being killed due to excessive memory usage, even if running just one job.

This can have two different causes. The first is that your local docker just
does not have enough memory to run your code. You can try reducing your
population size, increasing the memory allocated to docker, or setting
concurrency to 1, as described above.

The second reason is that by default, the `opensafely` tool tells docker to limit
individual jobs to 4G of memory. The purpose of this limit is to provide early
warning that this job is using a lot of memory. Locally, jobs are usually run against
small sets of dummy data, but in production, your dataset will likely be much
larger, and thus consume even more memory there too. See [Memory Efficient
Working](memory-efficient-working.md) for information on how to reduce your
code's memory usage.

However, you may very well need that extra memory for good reason, even when
working locally. If so, you can increase the memory with the flag `--memory` or
`-m` for short.

```
opensafely run job_name -m 8G
```
