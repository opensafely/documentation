---8<-- 'includes/backend-disclaimer.md'

# Accessing the EMIS Backend

To access this backend, you need to have IG approval for EMIS.

Note: access to the EMIS backend is linux cloud server, via a command line
terminal. There is currently no GUI access, everything needs to be done via
a terminal.


## Setting up access


### Configure SSH Key

First, you need to have an SSH key attached to your Github account. This key is
used to authenticate you when when accessing the EMIS backend server.

To do so, follow Github's instructions for creating a key on your machine via
the terminal. For windows users, you should use the git-bash terminal for this.

!!! warning
    You *must* set a strong password on this SSH key.

<https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>


### Add your Github username

Ask the OpenSAFELY team to add your Github username to the list of allowed
users to access the EMIS backend.

Either ask on Slack, or for quicker response time, propose a PR to add your
Github username to this file:

<https://github.com/opensafely-core/backend-server/blob/main/emis-backend/reviewers>

This will need to be approved and merge by the OpenSAFELY tech team.

### Setting up your local SSH configuration.

To secure access to EMIS, we use a special connection configuration for SSH.
You will need to customise your Github username, and also the path to your SSH
key. This is typically `~/.ssh/id_ed25519`, but could be different if you named
it differently.

Add the following to your ssh config file, which is located at `~/.ssh/config`.
You may need to create it if it doesn't exist.


```
Host *.opensafely.org
    User YOUR_GITHUB_USERNAME
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host emis-backend
    HostName directorvm.testemisnightingale.co.uk
    User YOUR_GITHUB_USER
    ProxyJump emis.opensafely.org

```

You should now be able to access the backend with:

`ssh emis-backend`
