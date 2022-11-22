
## Why Docker?

Docker allows you to run identical software on all platforms.
It creates "containers" that are guaranteed to be identical on any system that can run Docker.

OpenSAFELY uses Docker to run your code in a reproducible, safe manner.
This is most helpful for checking that you will be able to successfully run your code on the OpenSAFELY server on real data.
If you only run your code locally using your own installation of R, say, then you won't know if the version of R (and the packages) installed on the server will run your code without errors or unexpected behaviours.
See the [Testing Your Code section](actions-pipelines.md) for more details on how to test your code in practice.

Unfortunately, Docker is happiest on Linux; on Windows and Mac OSX, installation can be a chore.
These notes should help.

## Installation

Windows and Macs have different installation processes.
Regardless of machine, you will have to install Docker Desktop and make an account on the [Docker Website](https://docs.docker.com/).

### Windows

Follow the instructions from the Docker website.
Windows 10 or later is required.
It is best to install using the default settings.

!!! note
    We previously recommended Docker Desktop with the Hyper-V backend.

    Docker Desktop's recommended configuration is now the WSL2 backend.
    We have not thoroughly tested OpenSAFELY with WSL2,
    but there is no reason why WSL2 should be incompatible with OpenSAFELY's tooling.

    You only need to choose either Hyper-V or WSL2.
    It is fine to continue to use the Hyper-V backend.

#### Enabling Hyper-V

!!! warning
    Hyper-V is only available for the Pro, Enterprise and Education editions of Windows.
    If you have a Windows Home edition,
    then Hyper-V is not available and you must use WSL2 instead.

If using Hyper-V, you may be asked to enable the Hyper-V and Containers features, which you should do.
You can do this by [following these instructions](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).
At least one user has had the box ticked on the screen but had to untick and tick again to get this to enable correctly (Detailed in [this issue](https://github.com/ebmdatalab/custom-docker/issues/4)).

#### Enabling WSL

See [Microsoft's instructions](https://learn.microsoft.com/en-us/windows/wsl/install).

#### Enabling permissions for Active Directory logins

Windows users who log into an Active Directory domain (i.e., a network login) may find they lack permissions to start Docker correctly.
If so, [follow these instructions](https://github.com/docker/for-win/issues/785#issuecomment-344805180).

#### Running Docker

Starting Docker can take a while &mdash; up to 5 minutes.
While it's doing so, an animation runs in the notification area:

![The Docker icon in the Windows notification
area.](images/win-docker-starting.png)

Another notification appears when it's finished.

"Running" means there's a Docker service running on your computer, to which you can connect using the command line.
You can check it's up and running by opening a Terminal and entering `docker info`, which should output some diagnostics.

To be able to access the Windows filesystem from the Docker container (and therefore do development inside the Docker container with results appearing in a place visible to Git), you must explicitly share your hard drive in the Docker settings (click the Docker icon in the Windows system tray; select "Settings"; select "Shared drives").

#### Network login issues

When logged in as a network user, there have been permission problems that have been solved by adding the special "Authenticated Users" group to the `docker-users` group, per [this comment](https://github.com/docker/for-win/issues/785#issuecomment-327237998) ([screenshot of place to do this](https://github.com/docker/for-win/issues/785#issuecomment-344805180)).

Finally, note that when authentication changes (e.g., different logins), you sometimes have to reauthorise Docker's "Shared Drives" (click system tray Docker icon; select "Settings"; select "Shared drives"; click "Reset credentials"; retick the drive to share; click "Apply").

### Mac

Follow the [Mac installation instructions](https://docs.docker.com/desktop/install/mac-install/) from the Docker website.
You may have to restart your computer during installation.

Once you have Docker installed, you will need to log in.
This can be accessed via the Applications Folder and once you have logged in, you should have the Docker icon on the top taskbar (next to battery icon, etc.)

![The Docker icon in the macOS menu bar.](images/macos-menu-bar.png)

Once this is running, you should be able to use Docker.

### Linux

You can either install Docker with [Docker Desktop](https://docs.docker.com/desktop/install/linux-install/),
or via the server [Docker Engine](https://docs.docker.com/engine/install/).

## Gotchas

- The first time you use Docker or use a new Docker template, please be aware that it takes a long time to make the build.
It is easy to think that it has frozen, but it will take quite a while to get going.
- If Docker is not running on Windows, a few OpenSAFELY users have found that
  checking Control Panel > Administrative Tools > Services > Server
  was **Disabled**. Setting this to **Automatic** — the default in
  Windows — then started Docker running again.

---8<-- 'includes/glossary.md'
