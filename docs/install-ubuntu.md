# Ubuntu Install Guide

!!! note "This guide was created using Ubuntu 21.04"
    It is expected that this guide should work from 20.04 LTS upwards but has only been tested with 21.1

Open the terminal using the Activities launcher and typing "Terminal" and pressing Enter or by pressing Ctrl+Alk+T

### Install Python and opensafely
Ensure Python 3.8 or above is installed and is your default python version. This should be the case for Ubuntu versions 20.04 and above.
```bash
python --version
```

Next install pip, the Python package manager.
```bash
sudo apt install python3-pip
```

Then install the [OpenSAFELY CLI](../opensafely-cli) with pip.

```bash
pip install opensafely
```

Test the installation of OpenSAFELY CLI.
This should print out the usage and available sub commands:

```bash
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


### Install Docker
1. Either follow the [Docker Engine installation instructions for Ubuntu](https://docs.docker.com/engine/install/ubuntu/) or the steps given here:

Install pre-requisites for adding the docker software repository
```bash
sudo apt-get update

sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```

Add Docker's official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

Add the stable Docker software repository:
```bash
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Install Docker engine:
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

2. Docker post-installation configuration:
Add your user to the `docker` group:
```bash
sudo usermod -aG docker $USER
```

Enable the docker services to start at boot:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

Start the docker services:
```bash
sudo service start docker
sudo service start containerd
```

3. Test Docker and opensafely work together by pulling the latest cohortextractor images, which can be used to run actions in your study.
```bash
opensafely pull cohortextractor
```

You're done! You can now return to the [Getting Started guide](../getting-started/) and follow the instructions there.
