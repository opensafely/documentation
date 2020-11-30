OpenSAFELY is a rapidly changing platform and the user documentation should be updated frequently to keep pace. 
If you are an OpenSAFELY user and want to contribute corrections, clarifications, or new materials to the documentation, 
please do! You can either:

* Suggest improvements in an [issue](https://github.com/opensafely/documentation/issues).
* Clone the repo locally, make edits on a new branch, then create a pull request for it.
* [Edit directly on Github](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository), making sure to "Create a new branch for this commit and start a pull request".

Do not commit changes directly to the master branch.

If you want to make changes to the  study definition variables [here](study-def-extractor-functions.md), edit the docstrings in the [`patients.py` file in the `cohort-extractor` repository](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/patients.py).
If you don't have write access, you can fork the repo, make a change, and submit a pull request.
Editing directly in GitHub will take you through these steps automatically.
At least one commit in the pull request should be named using the prefix `docs: `. For example `docs: typo in age_as_of docstring`. 
This ensures that a new version of `cohortextractor` is released and can be imported by the documentation via GitHub actions.