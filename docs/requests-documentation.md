OpenSAFELY is a rapidly changing platform and the user documentation should be updated frequently to keep pace. 
If you are an OpenSAFELY user and want to contribute corrections, clarifications, or new materials to the documentation, 
please do! You can either:

* Suggest improvements in an [issue](https://github.com/opensafely/documentation/issues).
* Clone [the repo](https://github.com/opensafely/documentation) locally, make edits on a new branch, then create a pull request for it.
* [Edit directly on GitHub](https://github.com/opensafely/documentation/tree/master/docs) (instructions [here](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)), making sure to "Create a new branch for this commit and start a pull request".

Do not commit changes directly to the master branch.

## Making changes to the study definition variables

Edit the docstrings in the [`patients.py` file in the `cohort-extractor` repository](https://github.com/opensafely-core/cohort-extractor/blob/master/cohortextractor/patients.py).

!!! note "Variable docstrings follow the [Google style guide](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)."

If you don't have write access, you can fork the cohort-extractor repo, make a change, and submit a pull request.
Editing directly in GitHub will take you through these steps automatically.
At least one commit in the pull request should be named using the prefix `fix: ` or `feature: `. For example `fix: typo in age_as_of docstring`. 
This ensures that a new version of `cohortextractor` is released and can be imported by the documentation via GitHub actions.
Then add a reference to your new variable in the [variables page](study-def-variables.md).

Additionally, the
[`requirements.txt`](https://github.com/opensafely/documentation/blob/master/requirements.txt)
file in the [documentation
repo](https://github.com/opensafely/documentation) itself has to be
updated to match the new incremented version of `cohortextractor`. See
the [documentation repository's
README](https://github.com/opensafely/documentation#building-locally-and-testing)
that details the use of `pip-compile` for this.

---8<-- 'includes/glossary.md'
