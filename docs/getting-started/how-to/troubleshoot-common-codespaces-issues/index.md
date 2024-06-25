This page describes how to troubleshoot common Codespaces-related issues.

## "This codespace is requesting additional permissions"

On opening a Codespace you will see the following message:
![This codespace is requesting additional permissions](codespace-additional-permissions.png)

This is perfectly normal and is a result of how we have configured Codespaces to work with Stata.

If you plan to use Stata in your project, then you will need to click the "Authorize and continue" button.
If you do not plan to use Stata, then you may click either button.

## R Session Error

After restarting a stopped Codespace in which you were using RStudio, you may see the following error:
![R session error](r-session-error.png)

We have not observed any instances of work being lost in conjunction with this error, and so in most cases it can safely be ignored.
Manually terminating your R session before stopping the codespace may prevent this error from appearing.

## Git functionality is missing from RStudio

When you open RStudio within a Codespace, you may find that the Git Menu and Git Tab are missing from the user interface.
This is because, as stated in the [RStudio version control documentation](https://docs.posit.co/ide/user/ide/guide/tools/version-control.html):

> RStudio’s version control features are tied to the use of [Projects](https://docs.posit.co/ide/user/ide/guide/code/projects.html)

In most cases, opening RStudio will create an RStudio project file in your project directory and the Git features will be enabled.

If this does not happen, you may use the New Project Wizard in RStudio to "associate a project with an existing working directory"
as per the instructions in the [RStudio Projects documentation](https://docs.posit.co/ide/user/ide/guide/code/projects.html).

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
