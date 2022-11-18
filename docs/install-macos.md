# macOS Install Guide

!!! note "This guide was created using macOS 11.1"
    It is expected that this guide should work from 10.15 upwards but has only been tested with 11.1

Open Terminal.app by clicking the magnifying glass icon in the top right of your screen.
Type `terminal` and hit ++enter++.

## Homebrew
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

## pyenv
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

## Python
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

## OpenSAFELY CLI
Then install the [OpenSAFELY CLI](opensafely-cli.md) with pip:

```bash
pip install opensafely
```

And test the installation:

```bash
opensafely --help
```

If it is functioning, it should print out the usage and available sub commands:

```
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

## Docker for Mac
Set up Docker by opening the app you installed earlier:

```bash
open /Applications/Docker.app
```

You'll be warned about the system dialogue which is about to pop up, choose "OK".

![macOS prompting for Docker's privileged access.](./images/macos-docker-privileges-escalation-warning.png)


Enter your password and click "Install Helper".

![macOS prompting that Docker is installing a new helper tool.](./images/macos-docker-privileges-escalation.png)


Now that the Docker application is open you can click "Skip tutorial" and close the window.
The Docker service will continue to run in the background and can be accessed from the Docker icon in your menu bar.

![macOS Docker's getting started screen.](./images/macos-docker-skip-intro.png)


You're done!

Now you can navigate to a research repo, on your local machine, and [use `opensafely` via the command line](opensafely-cli.md#using-opensafely-at-the-command-line).

## Older style pipx installations

Earlier versions of this document used pipx to install opensafely. If you are looking to update such a pipx-style installation and are having problems with `opensafely upgrade`, you could also try `pipx reinstall opensafely --python ~/.pyenv/shims/python3.10`.
