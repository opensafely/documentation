The main tool for using the OpenSAFELY platform locally is the `opensafely` Python module, which is run via the command-line. 

It's main function is to run data extraction and analysis scripts that are specified in the [project pipeline](pipelines.md), in a way that mimics the production environment where real data is accessed. 

It also contains other functions relating to the OpenSAFELY workflow, such as updating codelists from [codelists.opensafely.org](https://codelists.opensafely.org).

## Installing `opensafely`

This is a command-line program.

To install, go to the Anaconda prompt and submit the following command (or use another method to install the module if you know how):

```bash
pip install opensafely
```

To check this has installed successfully, submit `opensafely --version`.

## Updating `opensafely`

You should keep the tool up to date as much as possible. You can upgrade to a new version of `opensafely`, update with:

```bash
opensafely upgrade
```

The above command only works with opensafely version 1.6.0 or newer. If you are
using an older version, you will first need to upgrade it with:

```bash
pip install --upgrade opensafely
```


```bash
pip install --upgrade opensafely
```

## Using `opensafely` at the command line

To view the in-built documentation for each command, submit `opensafely --help` at the terminal, which will list all the ways in which you can use it.
You can also use `opensafely run --help` to learn more about the `run` command, for example.

To run any of these commands for a specific OpenSAFELY project, you need to change the directory of your prompt to be the repository of the project. 
For example,  `cd C:/Users/me/my-git-repos/my-repo`.


More information on how to use the `opensafely` module is available in specific sections elsewhere, but some key functions are described briefly below.

### `run`

The most common command you'll run. 
This runs actions defined in the [`project.yaml` file](pipelines.md) and is the main way of testing your code. 

For example,

```bash
opensafely run make_graph
```

will run the `make_graph` action.


### `codelists`
This command is for working with codelists. 

Use
```bash
opensafely codelists update
```

to retrieve each codelist listed in `/codelists/codelists.txt` from [codelists.opensafely.org](https://codelists.opensafely.org).
It will add (or update) the codelist `.csv` files to the `codelists/` folder.

Use
```bash
opensafely codelists check
```

to check if the codelist files are up-to-date with thse listed in `./codelists/codelists.txt`.

See the [Codelist](codelist-intro.md) section for more information on codelists.


### Updating Docker Images


To run your code on your machine, the `opensafely` tool uses the same docker
images that run in the secure server environments. These are updated
periodically, for example when new libraries are installed. If you have error
messages about missing libraries, your docker images may need upgrading.
To pull the most recent release to your machine, run:

```bash
opensafely pull
```
