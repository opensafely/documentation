
Now find the codelist:

* Go to [codelists.opensafely.org](https://codelists.opensafely.org) and search "transplant".
* Click on the "Solid Organ Transplantation" codelist.
* Construct the codelist location from the **Codelist ID** and the **Version**. This should be `opensafely/solid-organ-transplantation/2020-04-10`
* paste this into a new line in `codelists/codelist.txt`
* Download the new codelist into the `codelist/` folder using the `cohortextractor` by submitting `cohortextractor update_codelists` at the command line.

At this point, there are two changes in the repository folder:
1. a new line in `codelists/codelist.txt`
2. a new file called `codelists/opensafely-solid-organ-transplantation.csv`.

You should see these changes appear in GitHub Desktop. This is a good time to `commit` them:

* Select (tick) both changes under the _Changes_ tab
* Write a brief commit message, e.g., "add transplant codelist". No need for a description.
* Click `Commit to add-transplant-var`

Now you have committed the changes to your local repo but not yet pushed (published) to the remote repo on GitHub.

### Define the transplant variable in `study_definition.py` and `commit`

* Open `analysis/study_definition.py` in your favourite text editor (ideally one with Python syntax highlighting -- <font color='red'>to be documented</font>).
* Paste the following code chunk after the other codelist declarations:

      transplant_codes = codelist_from_csv(
        "codelists/opensafely-solid-organ-transplant.csv",
        system="ctv3",
        column="CTV3ID",
      )
* Paste the following code chunk after the other variable declarations:

      organ_transplant = patients.with_these_clinical_events(
        transplant_codes,
        returning='binary_flag',
        return_expectations = {"incidence": 0.05}
      )

* Save the file, then go to the command line submit:

      cohortextractor generate_cohort --expectations-population 10000

At this point, there are two changes in the repository folder:
1. the changes to `study_definition.py`
2. a (new or updated) file called `analysis/input.csv`

However, you will only see the first change appear in GitHub Desktop. This is because `input.csv` is included in the `.gitignore` file, so all changes are ignored by git.

This is a good time to `commit` again:

* In GitHub Desktop, select the changed file, write a useful commit message, and click `Commit to add-transplant-var`.

For more guidance on making good git commit messages, and other good git practice, [read this](https://github.com/ebmdatalab/best_practice_guidance).

### `push` the `commit`s to the remote repo

You've now completed the required changes so this is good opportunity to `push` your set of `commit`s to the remote repo.

* In GitHub desktop, click `Push origin` -- you may have to click `Publish Branch` first

### Create a `pull request` for review

Now that you've pushed your commits to the remote repo, you can view them on GitHub. Go to your repository webpage -- you can click `View on GitHub` in GitHub Desktop, navigate to the repo from you GitHub profile page, or type `https://github.com/<user-or-organisation>/<repo-name>`. You can select either the (unchanged) `master` branch or the new `add-transplant-var` branch that you've just created.

If you're happy with the new branch, you can create a pull request to merge your development branch onto the master branch.

* Create a Pull Request in GitHub or in GitHub Desktop:
   * In GitHub, select the development branch and click `Create Pull Request`
   * In GitHub desktop, click `Create Pull Request` which will open the relevant webpage on GitHub

Review the changes, fill in any extra details if helpful, and submit. On the following page you can suggest someone to review the PR. In OpenSAFELY, a PR must always get a second pair of eyes before merging for sense-checking and bug-catching.

### Merge the PR and delete the branch

Once the PR has been approved, you can click merge and then delete the branch on the remote.

You may also want to delete the branch on your local repo to keep things tidy (since branch deletions aren't copied across when fetching) though this isn't essential. Just click `Branch > Delete` in GitHub Desktop.

### Fetching

It's possible for the master branch to be updated independently of your current development branch, as a result of another branch being approved and merged. These could be behind-the-scenes updates made by OpenSAFELY's tech team, or updates to the Study Definition or analysis files by another researcher working on the repo. It's important to bring these changes into your development branch to avoid merge conflicts. We do this using `fetch`.

* In GitHub desktop, click `Fetch origin`

You should make a habit of `fetch`ing frequently to reduce the occurrence of [merge conflicts](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts. If you do get a warning about a merge conflict, try to understand what's causing it using the `Resolve conflicts` button on your PR on GitHub. Do not actually resolve these conflicts (by clicking `Mark as resolved`) unless you're absolutely sure what why the conflict is there and which version to accept. Speak to a member of the tech team if you have any doubts.


## Study analysis

Now that you have a dummy dataset on your local machine, you can develop any analytical code you like against this dataset, on a separate branch, of course. The current workflow is quite new, so ask around for guidance, but [you can find the start of the documentation here](project_pipelines.md).

Once you are happy with the analysis branch and want to try to run it against the real data, push it to the remote repo and submit a pull request. This will be checked by a developer and run against the real data. Assuming no errors, the contents of `medium_security` outputs will copied to the Level 4 review server to check for disclosivity, censored where necessary, then transferred to a release folder and pushed to the remote repo for you to see.

### Running a cohort extract remotely

Old way: see `remote` [here](https://github.com/opensafely/documentation/blob/new-onboarding/Onboarding%20analysts.md#remote).

New way: **to be added** - short version: go to https://jobs.opensafely.org/ - under fast development!
