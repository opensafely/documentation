!!! warning
    **Please read even if you already have Python installed**

For security, consistency, and readability, OpenSAFELY provides an API built in [**Python**](https://www.python.org/) for using the platform.
This API includes script-based functions for specifying the patients and variables that make up a study dataset (using a [study definition](study-def.md)),
and command line functions for importing codelists, generating dummy data, and testing that the study definition can be run successfully on the server.
**Python version 3.7 or higher** must be installed on your machine to perform these tasks.

Many functions are provided in a Python module called `opensafely` which will also need to be installed &mdash; see the [`opensafely` CLI section](opensafely-cli.md) for more details.

<!--Strictly speaking, it is possible to test and run your study definition without a local installation of Python because this happens automatically every time a commit is pushed to GitHub.
However, this is not a particularly efficient way of working and we recommend being able to run the scripts locally. -->

## Windows
For Windows users, we recommend that you install [Anaconda (Individual Edition)](https://www.anaconda.com/products/individual), a popular Python distribution that includes an recent version of Python, many useful Python packages, and an environment manager.
This will help avoid some fiddly annoyances when dealing with multiple versions/installations of Python.

<!--If you already have Python installed on your machine, you should still be able install Anaconda without any inteference. <font color='red'>(is this true?)</font> Alternatively, you're welcome to use any existing or fresh Python installation you want if you're happy to troubleshoot problems yourself. -->

To install, [follow these instructions](https://docs.anaconda.com/anaconda/install/). Accept the default/recommended settings unless you understand the consequences of changing them.

This should have added Python and Anaconda Prompt to your machine (as well as a few other things).
To verify that you can run Python with Anaconda Prompt, open it and run `python --version`.

<!--If you installed a version of python earlier than `python 3.8` then you should submit `conda install -c anaconda python=3.8` to update your installation. It can take a while (up to an hour) as it needs to identify and resolve incompatible packages from the previous installation. -->

You should use the _Anaconda Prompt_ whenever you want to use the `opensafely` package.
Go to the [`opensafely` CLI section](opensafely-cli.md) for instructions on how to install this module.

## macOS

!!! note "This guide was created using macOS 11.1"
    It is expected that this guide should work from 10.15 upwards but has only been tested with 11.1

Open Terminal.app by clicking the magnifying glass icon in the top right of your screen.
Type `terminal` and hit ++enter++.

### Homebrew
Install [Homebrew](https://brew.sh/), this should install the Xcode Command Line Tools for you as well.

!!! note "This command might take a while to run depending on the speed of your internet connection."

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once homebrew is installed use it to install [pyenv](https://github.com/pyenv/pyenv):

```bash
brew install pyenv
```

Next, install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/), [GitHub Desktop](https://desktop.github.com/), and [Visual Studio Code](https://code.visualstudio.com/):

```bash
brew install --cask docker github visual-studio-code
```

### pyenv
Configure your shell to use pyenv:

!!! note
    If you are using a shell other than ZSH you will need to edit and source
    the appropriate config file.  pyenv has documentation for getting set up
    on [various shells](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv).

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### Python
Use pyenv to install Python:

!!! note "This command might take a while to run depending on the speed of your computer."

```bash
pyenv install 3.10:latest
```

Look for the line `Installing Python-3.10.n...` (where `n` is a number).
This is the full version it has installed for you, eg `3.10.1`.

Then enable this version (eg `3.10.1`) in pyenv:

```bash
pyenv global system 3.10.1
```


---8<-- 'includes/glossary.md'
