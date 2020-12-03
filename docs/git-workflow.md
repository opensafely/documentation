## Editing the Study Definition and gitting changes

For more detail about the study definition, see: https://github.com/opensafely/documentation/blob/master/study_definition.md

The general workflow for updating the repo is as follows:

* Create a new branch. A branch is a way for you to record and publish your own changes without breaking things for other people who are using the same code. It is also a good way of collecting changes ("commits") into a meaningful unit that can be reviewed by others.
* Edit/add/delete files in the repo on that branch, committing regularly with informative commit messages.
* Push the changes to GitHub, so that others can view the branch.
* Continue to commit and push changes on that branch until you believe it's ready to be merged back into the main codebase that everyone uses.
* Submit a pull request (PR), requesting that the branch be reviewed by somebody else. A PR is simply a way of viewing, commenting on, and approving branches.


We'll demonstrate this workflow with a simple example. Say you want to add a new variable describing if the patient has recieved an organ transpant or not. Then follow these steps:

### Create a branch and publish it

The first thing to think about before making any changes, whether adding, deleting, or editing files, is to `branch`. This ensures that any changes are kept separate from the _Master_ branch (i.e. the main codebase that everyone uses) whilst they are still being tested.

Open GitHub Desktop, and make sure the current repository is the the one you're working on. Click `Branch > New branch` and choose a new name that reflects the changes you wish to make, e.g., `update-codelists`, or `exploratory-notebook`. In our example, this can be `add-transplant-var`.

<!--Then publish the branch. It's a good idea to do straight way so that others know what you're working on. It's also necessary git housekeeping before being able to push commits to the remote repo.-->


---8<-- 'includes/glossary.md'
