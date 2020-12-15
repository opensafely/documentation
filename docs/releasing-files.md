Outputs can only be published by authorised users, who have permission to log in to the secure server.

Such users have responsibility for redacting sensitive information, or choosing not to publish it at all. 
Therefore, the study author should do everything they can to make this easy; for example, carrying out low number suppression automatically, documenting code clearly, and only selecting essential items for publication when deciding what to mark as `moderately_sensitive`.

The reviewer publishes outputs back to the original repo using git.

## Redacting and releasing output files from analysis runs

Output and log files created by [running code against the live database](pipelines.md#running-your-code-on-the-server) will [appear in the secure environment](pipelines.md#accessing-the-outputs).
You will need [Level 4 access or higher](security-levels.md) to view these files and follow the instructions below.

1. Log in to the server &mdash; if you have access you will have been provided instructions on how to do this.

2. Go to `D:/Level4Files/workspaces/<NAME_OF_YOUR_WORKSPACE>` where you should see:

    * a `metadata/` folder containing logs for each action,
    * an `outputs/` folder (by convention but this could be something else) containing the `moderately_sensitive` files intended for release.

    If these don't exist where you expect them to then double-check the workspace name and that the jobs on the Job Server have `succeeded`.

3. Clone the repo where you want to release the files:

    * open a `bash` terminal.
    * `cd D:/<your-name>/` to change the terminal directory to the folder where you want to put the repo (probably `D:/<your-name>/`)
    * `git clone https://github.com/opensafely/<repo-name-research>` to clone the remote repo from github 
    * `cd <repo-name-research>` to change the terminal directory to the repo.

    If this folder already exists:

    * `cd D:/<your-name>/<repo-name-research>` to change the terminal directory to the repo.
    * `git fetch` to update the remote-tracking branches, and possibly `git merge` if anything has changed.
    * `git status` to view any the uncommitted changes within the local repo. This should show all the newly created analysis output files (unless they are in a folder untracked by `.gitignore`) and nothing else. If other changes are there (such as for `.do` files), then these changes weren't committed to the repo before the analysis was run, or were made after the analysis was run. Deal with these uncommitted changes first before doing any redaction. If you are unsure what to do, ask.

4. Create a branch `release-outputs` or similar and checkout this branch. Use `git branch <branch-name>` to create a new branch and `git checkout <branch-name>` to checkout this branch. Or `git checkout -b <branch-name>` to do it all in one command.

5. Create a new folder in the repo called `released-outputs/` or similar, and copy all the files that you want to release into this folder. Do not delete the original output files.

6. Work through the files systematically to identify any tables, figures, and other outputted text and objects that may be a disclosure risk. **The general principle is that any statistic describing 5 or fewer patients, either directly or indirectly, should be redacted**. For example: 

    * Frequency tables containing values between 1-5 should be redacted. The whole table, or at a minimum multiple rows within the table, should be redacted because values removed by single cell (or row, or column) redaction could be inferred from unredacted values. 
    * Summaries of numeric variables describing 5 or fewer patients should be redacted. 
    * Figures whose underlying values describe 5 or fewer patients should be redacted. Figures which include print-outs of  patient counts (such as KM plots) should be checked and redacted. 
    * Counts of zero can be retained. 
    * Other outputs, such as log files that reveal information about the underlying data, should also be checked and redacted if necessary.

    Where possible it should be clear what has been redacted, so for example do not redact table titles and category names. By convention redactions take the form `[REDACTED]` to make redacted elements easier to search for.
	
    Ideally there shouldn't be any files in the folder that are not intended for release (whether potentially disclosive or not) as these should have been removed by the analysis scripts or placed elsewhere. If they are there, delete them.

    This current approach to disclosure control is conservative and deliberately reduces the need for judgement calls. It may be possible for exceptions to be made if absolutely necessary, but only after discussion with the OpenSAFELY team.

7. Once all output files have been checked, redacted, and saved, they can be committed and pushed to the remote repo.

    * `git status` to verify all that the redacted files you want to release are in your repo folder, and nothing more. 
    * `git add <released-output-folder>/` to stage the folder containing these files. Make sure to include parent directories of this file if your terminal working directory is not its immediate parent. 
    * `git status` again to verify that only the files that you want to release have been staged for the commit.
    * `git commit -m "<commit message goes here>"` to commit these changes.
    * `git push origin <branch-name>` to push to the remote repo on github.

8. Go to the repo on github, choose the branch you made, and check everything is there. Make a Pull Request if you want.

9. If you are unsure about anything, ask.




---8<-- 'includes/glossary.md'
