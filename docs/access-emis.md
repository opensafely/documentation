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
    You *must* set a strong password on this local SSH key, its the main
    password protection for accessing the backend.

<https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>


### Add your Github username

Ask the OpenSAFELY team to add your Github username to the list of allowed
users to access the EMIS backend.

Either ask on Slack, or for quicker response time, propose a PR to add your
Github username to this file:

<https://github.com/opensafely-core/backend-server/blob/main/emis-backend/reviewers>

This will need to be approved and merged, and then setup by the OpenSAFELY tech
team by updating the backend to create your accounts.

Note to tech team: you need to update *both* `emis-backend` and `emis-access`.

### Setting up your local SSH configuration.

To secure access to EMIS, we use a special connection configuration for SSH.
You will need to replace `YOUR_GITHUB_USERNAME` with your actual Github
username, and also check the path to your SSH key. If you've followed the guide
above, this will be `~/.ssh/id_ed25519`, but could be different if you chose to
name it differently.

Add the following to your ssh config file, which is located at `~/.ssh/config`,
in your home directory.  You may need to create this file and directory if it
doesn't exist.


```
Host *.opensafely.org
    # log in with your github username
    User YOUR_GITHUB_USERNAME
    # Use this specific ssh key
    IdentityFile ~/.ssh/id_ed25519
    # Use only that key
    IdentitiesOnly yes


# short alias
Host emis-backend
    # As it is an opensafely.org host, it will use the config above for authentication.
    HostName emis.opensafely.org
    # log in with your github username. 
    User YOUR_GITHUB_USERNAME
    # We tunnel the connection via a special purpose host 
    ProxyJump emis-access.opensafely.org
    # Forward this port over the SSH connection. This allows you to view level
    # 4 data on the EMIS backend via https://jobs.opensafely.org when you have an
    # active SSH session.
    LocalForward 8001 localhost:8001

```

### One time system password setup

The first time you connect, you will need to set up some passwords on the
systems we'll be using.  You shouldn't need these passwords again, but our
security setup requires them to exist.

First ssh into emis-access.opensafely.org (you may first need to enter your ssh password you previously set up).

`ssh emis-access.opensafely.org`

You will be prompted to set a system password, entering it twice, then it will
exit. Run the ssh command again to make sure it worked (you won't need to enter
a password), and then exit with `exit` or `Ctrl-D`.

You should now be able to ssh in the emis backend, and set a password there too.

`ssh emis-backend`

You may need to enter your ssh password again here, and then will be prompted to set a system password twice, again, and it will exit.

You are now set up and should be able to do `ssh emis-backend` to access the EMIS backend in future.


### Viewing files in EMIS

First, log in to EMIS backend with ssh, and keep the connection open:

`ssh emis-backend`


Then go the the workspace page on https://jobs.opensafely.org that you wish to
view. Click "Level 4 Outputs" -> "EMIS", and you should see a file view.

If it doesn't load:

1. check your ssh connection is up and running

2. you may need to allow 'insecure content' in for jobs.opensafely.org,
   especially on Mac OS:

https://experienceleague.adobe.com/docs/target/using/experiences/vec/troubleshoot-composer/mixed-content.html?lang=enI


### Releasing Files in EMIS

This works similarly to TPP, but the files are located in `/srv/medium_privacy/workspaces`

`cd /srv/medium_privacy/workspaces`

You can `cd` into the workspace directory, then run `osrelease files.. as normal.
