All outputs from OpenSAFELY pipelines are subject to [tiered levels of scrutiny](security-levels.md), to provide assurance that identifiable data is not leaked accidentally, or maliciously.

The final tier is review of so-called "Level 4" outputs, where the OpenSAFELY framework stores outputs labelled as `moderately_sensitive` in the `project.yaml` file.

Level 4 outputs can only be released by authorised users who have permission to log in to the secure server.
Such users have responsibility for redacting sensitive information or choosing not to publish it at all. 
The study author should do everything they can to make this easy; for example, carrying out low number suppression automatically, documenting code clearly, and only selecting essential items for publication when deciding what to label as `moderately_sensitive`.


## Releasing output files from analysis runs

The output and log files that are created by [running code against the live database](actions-pipelines.md#running-your-code-on-the-server) will [appear in the secure environment](actions-pipelines.md#accessing-the-outputs) in a workspace-specific folder.

The reviewer releases outputs back to the original repo using git. 
To make this process easier and to reduce the likelihood of sensitive information being accidentally released, there is a script-based procedure to follow. In essence, the process is: create a git repo in the folder where the outputs were created; check and redact them as necessary; commit the safe files to the repo; run the `osrelease` command and follow the instructions. This last step will create a new branch containing the released outputs which can then be merged onto another branch in the repo via a pull request.

### Install
* Log into L4 server
* In a git-bash terminal, run `/d/bin/install-osrelease.bat` (or `/e/bin/install-osrelease.bat` on the L3 server). You can run this command multiple times without any problems if needed.  
* Close the git-bash terminal and reopen it
* Check you can run `osrelease --help` (you'll get some help text)

### Instructions

The following instructions assume you have submitted one or more jobs which have created outputs on the Level 4 server, including log files from failed runs.

1. Log in to the Level 4 server &mdash; if you have access you will have been provided instructions on how to do this.

2. Go to `/d/Level4Files/workspaces/<NAME_OF_YOUR_WORKSPACE>` (or `/e/FILESFORL4/workspaces/<NAME_OF_YOUR_WORKSPACE>` if you are in Level 3, _which you shouldn't be_). You should see:
    * a `metadata/` folder containing logs for each action,
    * an `outputs/` folder (by convention but this could be something else) containing the `moderately_sensitive` files intended for release. 
    
    If these don't exist or haven't updated as you expect, double-check the workspace name and the status of the jobs on the [job server](https://jobs.opensafely.org).
    
3. Open a console with this folder as root directory, using `cd /d/Level4Files/workspaces/<NAME_OF_YOUR_WORKSPACE>`.
4. If this is the first time any releases have been made for this workspace, run `git init` to create a new git repo there.
5. Run `git status` to see the changes made by the job(s) (if this says `fatal: not a git repository` then you need to run `git init`).
6. Run `git add <names-of-files>` to add any new files, or changes to any existing files, to the local repo.
7. Edit or delete files to redact as necessary and commit the changes:
    * [**Read the redaction instructions below**](releasing-files.md#disclosivity-checks-and-redaction).
    * Use `GitHub desktop` or command line `git` to view the diffs and commit changes to the repo.
    * Any previously-applied redactions from previously-run actions will need to be reapplied &mdash; these will be easy to spot in GitHub desktop, and you can choose to simply not commit any files if the redacted version will be identical between the previous and current runs.
8. Only once you're satisfied that the committed changes are safe to release, run `osrelease` from the directory with your changes in and follow the instructions.

Once finished, any files you have committed locally will be visible in the `released_ouputs` folder on the `release-candidates` branch on your repo (e.g., `https://github.com/opensafely/my-amazing-research/tree/release-candidates`). 
This branch won't contain any of the intermediate git history, just the state of the redaction repo when you ran the `osrelease` command. 

You can merge the `released-candidates` branch onto another branch by creating a pull request. 
If you want to merge onto a branch that isn't the `main` branch, don't forget to select the correct `base:` branch from the drop-down box when creating the pull request.


<details markdown="1">
  <summary>Click here to read in more detail about the `osrelease` command.</summary>

The `osrelease` command runs the `release.py` script in the [`output-publisher` repo](https://github.com/opensafely-core/output-publisher). It:

* prompts the reviewer for the URL of a github repo to where the redacted outputs should be published (the *study repo*)
* checks out the *study repo* and creates a branch `release-candidates` (if it doesn't already exist)
* copies every file that has been committed to the *redaction repo* into a subfolder `released_outputs`
* creates or updates an index file at `released_outputs/README.md` with links to all the release files
* adds all new changes as a single commit, using the most recent commit message in the *redaction repo* as the text. It also appends a trailer indicating from where the commit was originated
* force-pushes `release-candidates` to the study repo
* outputs a URL to the "create Pull Request" page in github for the `release-candidates` branch of the study repo

The benefit of maintaining a separate *redaction repo* is that when new outputs
are generated and written to that repo, the usual git tools can be used to diff
outputs, making it easier to reapply redactions or decide where new redactions
should be applied.

</details>

## Disclosivity checks and redaction

Work through the moderately sensitive files in the workspace folder systematically to identify any tables, figures, and other outputted text and objects that may be a disclosure risk. 
**The general principle is that any statistic describing 5 or fewer patients, either directly or indirectly, should be redacted**.
For example: 

  * Frequency tables containing counts between 1-5 should be redacted. The whole table, or at a minimum multiple rows within the table, should be redacted because values removed by single cell (or row, or column) redaction could be inferred from unredacted values. 
  * Summaries of numeric variables describing 5 or fewer patients should be redacted. 
  * Graphical figures whose underlying values describe 5 or fewer patients should be redacted. Figures which include print-outs of patient counts (such as KM plots) should be checked and redacted. 
  * Counts of zero can be retained. 
  * Other outputs, such as log files that reveal information about the underlying data, should also be checked and redacted if necessary.

Where possible it should be clear what has been redacted, so for example do not redact table titles and category names. 
By convention redactions take the form `[REDACTED]` to make redacted elements easier to search for.
	
Ideally there shouldn't be any files in the folder that are not intended for release (whether potentially disclosive or not) as these should have been removed by the analysis scripts or placed elsewhere. 
If they are there, delete them.

This current approach to disclosure control is conservative and deliberately reduces the need for judgement calls. 
It may be possible for exceptions to be made if they can be justified as being both analytically necessary and definitely non-disclosive. This must be discussed with the OpenSAFELY team.

If you are unsure about anything, ask.

## Redaction data breaches and how to recover from them

### The issues

One of the great strengths of using git is that it is easy to recreate the contents of any file in the repository exactly as it appeared at any point in the repository's stored history. However, this means that if any sensitive data is inadvertently committed to a repository, we need to be careful to completely remove that data from the history.

Access to `output-publisher` repositories is intended to be restricted, and their histories are not transferred to study repos in the release process. However, study repos are intended to eventually become public, so if sensitive data is committed then care should be taken to fully clean up. From the moment that the `osrelease` command is run in an `output-publisher` repo, we need to be careful with the study repo's git history.

For example, if sensitive data was committed to a study repo, it is explicitly not safe to use either git's `revert` command, or to delete the file and commit the deletion. Both of these methods would leave the commit containing the sensitive data in the history of the git repository - and would be trivial for anyone to recover in the future.

Another aspect of git is that it uses a decentralised model. This means that everyone that has a copy of a git repository has their own copy of the entire history. So, if there is a sensitive data leak, it is not sufficient to clean just your own copy of the git history & the history on github, you should also clean the git histories of all other copies.

## What to do if you find a data breach

If you discover files in a study repository that have been insufficiently redacted and still contain sensitive information, you should contact Amir Mehrkahr or Ben Goldacre as soon as possible.

If you are able, you can attempt to make the repository safe by temporarily restricting access to it. For instance, if the repository is public (accessible to the world), make it private (accessible only to the OpenSAFELY team). If the repository has external contributors that are not authorised to handle sensitive data, consider temporarily removing their access to the repository. This will reduce the scope for harm until the sensitive information can be removed from the repository.

If you are an author of the study, you should also liaise with an engineer from the OpenSAFELY team as soon as possible to safely clean the sensitive information from the repository. Depending on the exact situation this may be relatively straightforward or relatively complicated. You should also attempt to trace all copies of the repository for cleaning or deletion.


---8<-- 'includes/glossary.md'
