When you're ready to tell the world about your GitHub repo, consider the following:

## About Section
Check that the "About" section is up to date.
People will see this section prominently when they view your repository on GitHub.

Include a short, one-line summary and link to your paper or outputs in the "About" section.
Click the cog next to "About" and add these details.


## README
As of the 24th October 2022 we have changed how we managed repo READMEs.
You can ignore this section if you created your repo after that date.

If you created your repo before this date then you will have the older README format, which expected you to update the file as your project progressed.
We have now moved to keeping that information in your project on the Jobs site.

The [current README template](https://github.com/opensafely/research-template/blob/main/README.md) has the updated version for new repos.

To update your repository's README to match this new README:

1. Copy the content from the template repository's latest README (typically [just the first section](https://github.com/opensafely/research-template/blob/main/README.md?plain=1#L1-L10)).
1. Manually edit those changed sections into your research repository's README.
1. You will need to replace the two placeholder strings in the README's "View on OpenSAFELY" URL to point to your repository:

* `${GITHUB_REPOSITORY_OWNER}` is the GitHub organisation your repo lives under, likely `opensafely`.
* `${GITHUB_REPOSITORY_NAME}` is the name of your repo.

!!! warning
    Each branch in your repository has a separate README, each of which will need updating.


## License
* Check the `LICENSE` file exists, and that it allows modification and distribution without cost. We recommend the MIT Licence ([example](https://github.com/opensafely/risk-factors-research/blob/main/LICENSE)).


## Tests
Try to ensure your automated tests (on the repo's _Actions_ tab) are green.
It's not essential, but it is a better look to be able to demonstrate your code is minimally runnable.


## Contents
Review your GitHub repository to make it simpler for people to explore:

* Merge or close all open Pull Requests (unless they are ongoing work in progress).
* Ensure that all branches are merged or deleted apart from the `main` or `master` branch. Old branches may contain draft work or previous ideas that are no longer needed. Note that deleting them does not delete the files permanently, they will still be in the repository history if you need to revisit them later. You may need to leave one or two branches open if they are ongoing work in progress (try to make sure they are named clearly).
* Delete any files that were not used/experimental and not used in final analysis, e.g. old versions of study definitions. Again they will still be in the repository history if you need them later.
* Are there old issues that can be closed? Some issues may have been fixed, or may be no longer relevant.


## GitHub Release
Consider making a GitHub _Release_, and linking to that ([instructions here](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository)).
A Release is a coherent snapshot of the code as it existed at a given point in time, along with a title and a description.
By default, releases are displayed on your repo home page.
For example, you might make separate releases of the code to accompany a preprint and the final versions of the paper.

Consider [obtaining a DOI for your releases](https://guides.github.com/activities/citable-code/), and using that for referencing your code.


## Make your repo public
If your repository is *private*, ask [tech support](how-to-get-help.md) to make it *public* before the associated paper or output is published.
There's more information about what this means [here](repositories.md#repository-access).

!!! info
    You will be prompted to make it public sooner, if you first ran the code against an OpenSAFELY database more than 12 months ago.
