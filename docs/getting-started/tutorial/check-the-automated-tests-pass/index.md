## Check that the automated tests pass

Your repository is automatically configured with tests to verify the project is runnable,
each time you push.

Now that you have published the changes from your codespace to your GitHub repository,
we can see if these tests pass.

Visit your repository on GitHub's site. Click on the **Actions** tab
![The GitHub Actions tab in a repository.](../../../images/getting-started-github-actions-tab.png)

You'll see a *Workflow* running with the *commit message* of your last
commit. The workflow verifies that the command `opensafely run run_all` can
run successfully. If it's yellow, it's still running. If it's red, it
has failed. If it's green, it has succeeded. You want it to be green!
![The GitHub Actions tab showing a successful workflow.](../../../images/getting-started-github-actions-workflow-success.png)
