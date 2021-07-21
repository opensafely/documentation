## Running your code on the server

To run code for real in the production environment, use the [https://jobs.opensafely.org](https://jobs.opensafely.org) site.
Here you can see (even without a login) all the ongoing projects within OpenSAFELY, and the specific _jobs_ that have been run on the server.
To submit job-requests (i.e., to run one or more actions), the general process is as follows:

* **Log in** using your GitHub credentials
* **Create a project** (or select an existing one):
    * Click the `Add a New Workspace` button.
    * Click the `Register Project` button.
    * Choose a name, this will be the public facing name for your project.
    * Click `Save`.
* **Create a workspace**:
    * Click the `Create a Workspace` button.
    * Choose a name, for example the name of the repo.
    * Select a database to run against: either the full database, or a ~20% sample of it (sampling is based on an arbitrary selection of practices and not guaranteed to be representative).
    * Select the repo and branch whose action you want to run (in most cases, the branch will be either `main` or `master`).
    * Click `Submit`.
*  **Select actions** to run:
    * Select the actions you want to run by clicking the `Run` buttons.
    * If any of these actions have dependencies then they will also be run, unless their outputs already exist. 
      * If any dependencies have already been set to run, your current job will be queued until dependencies have completed.
    * Dependencies can be viewed by clicking the `Needs` button.
    * You can force dependencies to be run by clicking `Force run dependencies`, even if those actions have already been run.
    * You can choose to send notifications for the selected actions to your email address.
    * When you're ready, click `Submit`.

The workspace is available at `https://jobs.opensafely.org/<WORKSPACE_NAME>/`.
You can view the progress of these actions by click the `Logs` button from the workspace, or going to `https://jobs.opensafely.org/<WORKSPACE_NAME>/logs`. If you selected to receive notifications, you will also receive an email to notify you when each job completes.

When you submit a job-request you are competing with other users for resources on the server. As such, jobs can sometimes take a while to start even if their dependencies have successfully completed.

<details markdown="1">
<summary>Click here for information on the exact steps that occur when each job is run on the server</summary>

What happens:

1. A new, empty temporary directory for the job is created.
2. Copy in all files on the selected branch.
3. The job is run.
4. All the files matching the specified output patterns are copied into the local repo.
5. The log files for the job are saved into the `metadata/` directory.
6. The temporary directory is deleted.
</details>

Each job will either succeed or fail. In either case, the output and log files are only visible in the secure environment to avoid disclosure of potentially sensitive information.
