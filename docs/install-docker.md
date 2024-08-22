
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
Regardless of machine, you will have to install Docker and make an account on the [Docker Website](https://docs.docker.com/).

There are two flavours you can install, *Desktop* and *Toolbox*.
Docker Desktop is preferred over Docker Toolbox.

### Windows

Docker Desktop in Windows offers native support via Hyper-V containers, and so is preferred.

To install Docker Desktop on Windows 10 64-bit Pro, Enterprise, or Education build 15063 or later (i.e., most university or institution managed machines), [follow these installation instructions](https://docs.docker.com/docker-for-windows/install/).
To install Docker Desktop on Windows Home [follow these installation instructions](https://docs.docker.com/docker-for-windows/install-windows-home/).

!!! warning
    Unfortunately, we've had reports that installing in Windows Home can
    be very challenging. Please let us know if you can help us [improve
    the documentation](updating-the-docs.md) here.

1. Follow the [Docker for windows installation instructions](https://docs.docker.com/docker-for-windows/install/).
   If you are using Windows 10 Pro, Enterprise or Education, you should
   follow the instructions for Hyper-V backend and Windows containers.  If you are using
   Windows Home or an earlier build of Pro or Education, follow the instructions for
   WSL 2 backend.

   You may be asked to enable the Hyper-V and Containers features, which you should do.
   You can do this by [following these instructions](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).
   At least one user has had the box ticked on the screen but had to untick and tick again to get this to enable correctly (Detailed in [this issue](https://github.com/ebmdatalab/custom-docker/issues/4)).

1. Starting Docker can take a while &mdash; up to 5 minutes. While it's doing
   so, an animation runs in the notification area:<br>
   ![The Docker icon in the Windows notification area.](images/win-docker-starting.png)
   Another notification appears when it's finished.
1. When Docker has finished starting up, share your hard drive with Docker:
   click the system tray docker icon; select "settings"; select "shared drives".
1. If you have ended up with the *Hyper-V* backend, then when Docker has
   finished starting up, you will need share your hard drive with Docker: click
   system tray docker icon; select "settings"; select "shared drives".  This
   setting does not exist in the *WSL 2* backend.
1. Test Docker and `opensafely` work together. Open an Anaconda Prompt, and run
   `opensafely pull ehrql`. This will pull down the OpenSAFELY
   ehrql image, which can be used to run actions in your study.  The
   first time you run it, this may take a little time, depending on your
   network connection. It is downloading a reproducible environment identical
   to that installed in the OpenSAFELY secure environment.

!!! warning
    Windows users who log into an Active Directory domain (i.e., a network login) may find they lack permissions to start Docker correctly.
    If so, [follow these instructions](https://github.com/docker/for-win/issues/785#issuecomment-344805180).
It is best to install using the default settings.

"Running" means there's a Docker service running on your computer, to which you can connect using the command line.
You can check it's up and running by opening a Terminal and entering `docker info`, which should output some diagnostics.

#### Network login issues

When logged in as a network user, there have been permission problems that have been solved by adding the special "Authenticated Users" group to the `docker-users` group, per [this comment](https://github.com/docker/for-win/issues/785#issuecomment-327237998) ([screenshot of place to do this](https://github.com/docker/for-win/issues/785#issuecomment-344805180)).

Finally, note that when authentication changes (e.g., different logins), you sometimes have to reauthorise Docker's "Shared Drives" (click system tray Docker icon; select "Settings"; select "Shared drives"; click "Reset credentials"; retick the drive to share; click "Apply").

### Macs

Follow the instructions from the Docker website.
You may have to restart your computer during installation.

Once you have Docker installed, you will need to log in.
This can be accessed via the Applications Folder and once you have logged in, you should have the Docker icon on the top taskbar (next to battery icon, etc.)

![The Docker icon in the macOS menu bar.](images/macos-menu-bar.png)

Once this is running, you should be able to use Docker.

#### Macs with an Apple Silicon processor

If you are using a Mac with an Apple Silicon processor, you should enable Rosetta emulation in Docker Desktop. This will increase performance of Docker significantly.

If you are using macOS Sonoma (v14) or newer, this option may already be enabled.

1. Click the Docker icon in the macOS menu bar
1. Click on "Settings…"
1. Under the "General" settings, tick the option listed below:
    > **Use Rosetta for x86/amd64 emulation on Apple Silicon**
    >
    > Turns on Rosetta to accelerate x86/amd64 binary emulation on Apple Silicon. Note: You must have Virtualization framework enabled.
1. Click "Apply & restart"

## Gotchas

- The first time you use Docker or use a new Docker template, please be aware that it takes a long time to make the build.
It is easy to think that it has frozen, but it will take quite a while to get going.
- If Docker is not running on Windows, a few OpenSAFELY users have found that
  checking Control Panel > Administrative Tools > Services > Server
  was **Disabled**. Setting this to **Automatic** — the default in
  Windows — then started Docker running again.
