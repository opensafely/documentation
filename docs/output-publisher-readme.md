# OpenSAFELY output publication

All outputs from OpenSAFELY pipelines are subject to tiered levels of scrutiny,
to provide assurance that identifiable data is not leaked accidentally, or
maliciously.

The final tier is review of so-called "Level 4" outputs, where the OpenSAFELY
framework stores outputs marked as `moderately_sensitive` in the `project.yaml` file.

Essentially, the process is to create a git repo in the folder where the outputs were created, check the outputs for disclosivity and edit them if necessary, commit the edits to the repo, run the `osrelease` command and follow its instructions. This last step will create a new branch on the remote repo with the release outputs in the `released_outputs` folder. This branch should then be merged onto any other branch in the repo via a pull request.


<details>
  <summary>Click here to read in more detail about the process.</summary>

* The outputs for a single workspace are stored in a per-workspace folder
* This folder should be maintained as a local git repo (which we'll call the *redaction repo*). 
The redaction repos will never leave the server: it only exists for reviewers to track redaction activity over time. The git history may, therefore, contain identifying information.
* Whenever new outputs are generated in the workspace folder, a reviewer will use their usual git tools (typically Github Desktop) to examine the outputs. Outputs intended for public release should be redacted (as necessary) and then committed to the redaction repo.
* The `release.py` script should then be run in a command terminal, from the root folder of the workspace folder. It:
  * prompts the review for the URL of a github repo to where the redacted outputs should be published (the *study repo*)
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

## Install
* Log into the L4 server
* Run `/d/bin/install-osrelease.bat` (or `/e/bin/install-osrelease.bat` on the L3 server)
* Close the console and reopen it
* Check you can run `osrelease --help` (you'll get some help text)

## Usage instructions
These instructions assume you have submitted one or more jobs which have created outputs on the Level 4 server, including log files from failed runs:

* Log into the L4 server
* Open a console at the root of the workspace you want to publish (e.g. `/d/Level4Files/workspaces/my-amazing-research`)
  * If doing this on the L3 server (_you shouldn't be..._) then be sure to do this in the `/e/FILESFORL4/workspaces` folder to mitigate the risk of publishing high-privacy outputs
* If this is the first time any releases have been made, type `git init` to start a new git repo there
* Run `git status` to see any changes (if this says `fatal: not a git repository` then you need to run `git init`)
* Run `git add <names-of-files>` to add any new files, or changes from any existing files, to the local repo
* Edit files to redact, as necessary
* Commit any edits you make with `git commit`
* Run `osrelease <github_remote_https_url>` (e.g. `osrelease https://github.com/opensafely/my-amazing-research`)
* Follow the instructions. It will only publish files you have committed locally, and won't send any intermediate history; just their state as they currently are in the local repo

You should now see the released outputs on the `release-candidates` branch on your repo (e.g., `https://github.com/opensafely/my-amazing-research/tree/release-candidates`). 
You can merge this branch onto another branch by creating a pull request. If you want to merge onto a branch that isn't the `main` branch, don't forget to select the correct `base:` branch from the drop-down box when creating the pull request.

