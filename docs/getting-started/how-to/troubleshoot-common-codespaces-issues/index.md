This page describes how to troubleshoot common Codespaces-related issues.

## "This codespace is requesting additional permissions"

On opening a Codespace you will see the following message:
![This codespace is requesting additional permissions](codespace-additional-permissions.png)

This is perfectly normal and is a result of how we have configured Codespaces to work with Stata.

If you plan to use Stata in your project, then you will need to click the "Authorize and continue" button.
If you do not plan to use Stata, then you may click either button.

## My Codespace says it's in "recovery mode"

Occasionally when creating a Codespace something goes wrong. In these instances, GitHub will boot the Codespace into a "recovery mode". This provides you with a very basic environment in which to debug the problem. If this happens, either delete it and try again or contact tech support. If you contact tech support, then don't delete the Codespace, as it's likely you'll be asked for the creation logs so the problem can be investigated.

In recovery mode, you will not be able to access any of the usual tools or VS Code plugins. Some basic functionality, like copy and paste, may not work as expected either. So you should not attempt you use it for any work. GitHub provide some more information about Codespace recovery mode in their [documentation](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-creation-and-deletion-of-codespaces#codespace-creation-fails).

## R Session Error

After restarting a stopped Codespace in which you were using RStudio, you may see the following error:
![R session error](r-session-error.png)

We have not observed any instances of work being lost in conjunction with this error, and so in most cases it can safely be ignored.
Manually terminating your R session before stopping the codespace may prevent this error from appearing.

## Git functionality is missing from RStudio

When you open RStudio within a Codespace, you may find that the Git Menu and Git Tab are missing from the user interface.
This is because, as stated in the [RStudio version control documentation](https://docs.posit.co/ide/user/ide/guide/tools/version-control.html):

> RStudio’s version control features are tied to the use of [Projects](https://docs.posit.co/ide/user/ide/guide/code/projects.html)

Therefore, if you have not already created an RStudio project file (.Rproj) file in your repository you can do so by using the New Project Wizard in RStudio to "associate a project with an existing directory". Once your repository is opened in project mode the Git features will be enabled.

## RStudio's Files tab is not showing the correct directory

Sometimes, when opening RStudio, you may find that the [Files tab](https://docs.posit.co/ide/user/ide/guide/ui/files.html) is not displaying your project directory.

Opening the "More" menu in this tab and selecting "Go To Working Directory" should take you to your project directory.

If this does not work, you will need to navigate to your project directory in the Files tab (`/workspaces/{the name of your github repository}`).
Once you have done this, you may need to select "Set As Working Directory" from the "More" menu of the Files tab to ensure this directory is correctly opened the next time you open RStudio.

## My favourite VS Code extensions are not installed/I'd like to change the settings

You are free to install any VS Code extensions and change any settings you wish within your Codespaces.
However, you will find that any changes you make will not be preserved when you start a new Codespace.

If you wish to make changes that will apply whenever anyone opens your project, then consider using a [Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings) file in your project.

If you wish your settings and extensions to be available anywhere you open VS Code (including in Codespaces), then consider using [Settings Sync](https://code.visualstudio.com/docs/editor/settings-sync).

## Previewing HTML files doesn't work

If you are using a codespace to author an HTML file, for example a report, you may wish to see a preview of this. Microsoft's [Live Preview](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server) VS Code extension is frequently used for this purpose.
However, if you try to use this extension in a codespace, you might see error messages such as: "This content is blocked. Contact the site owner to fix the issue…" or see that the preview window appears blank.
This is a [currently known issue](https://github.com/microsoft/vscode-livepreview/issues/111) with the extension.

### Workaround

When you first try to open a preview window via the context menu (right click), you may see a pop-up in the bottom right hand corner of your screeen advising you of a new "application running on port 3000":

![VS Code popup notifying of application running on port 3000.](vscode-popup.png)

Clicking "Open in Browser" should open a new tab where you will see a directory listing of the files in your workspace, and from which you can navigate to your desired html file:

![Browser window showing project workspace directory listing.](directory-listing.png)

You can also navigate to this window via the "Ports" tab in VS Code:

![VS Code ports tab showing application running on port 3000.](vscode-ports.png)

### Alternative extension

There is also an [alternative preview extension](https://marketplace.visualstudio.com/items?itemName=searKing.preview-vscode), which [reportedly](https://stackoverflow.com/questions/74452866/how-preview-a-html-file-github-codespaces/75135098#75135098) is not affected by this issue.
We have not tested this extension and therefore cannot vouch for its functionality or safety.

## My code runs fine in the codespace's local environment but not as an OpenSAFELY action (or vice versa)

Your codespace comes pre-installed with all the packages from the most recent OpenSAFELY R and Python action images.
These action images are the environment in which your code is executed via the [`opensafely`](../../../opensafely-cli.md) command.

For [R](../../../actions-scripts.md#r) actions, we currently only maintain one version of the R action image (`r:v1`) and so we expect the behaviour of R scripts to be the same when executed via the OpenSAFELY R action image or via RStudio (or `R` on the command line).

In the case of [Python](../../../actions-scripts.md#python), the most recent action image version is `python:v2` at the time of writing.
If you have actions defined in your [project pipeline file](../../../actions-pipelines.md#projectyaml-format) that reference images called `python:v1` or `jupyter:v1` (or — due to an _unfortunate_ historical naming convention —  `python:latest` or `jupyter:latest`), then the behaviour of your code when run in those images may not be the same as if you run the code directly in the codespace. This is because the installed packages and versions of Python available differ between these environments.

If this is the case for your project, your options are:

* Update your project pipeline file to reference the most recent action images and make any neccesary changes to your code
* Retain the references to the older action images, and use [`opensafely exec`](../../../opensafely-cli.md#exec-interactive-development) for interactive development using these action images' environments
