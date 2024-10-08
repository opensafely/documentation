Once you have completed your project in OpenSAFELY, there are a number of tasks to complete to align with our [open working principles](https://www.opensafely.org/about/#core-design-features-for-privacy-transparency-and-open-working).

Please read and complete the tasks below.
## Update all READMEs
As of the 24th October 2022 we have changed how we managed repo READMEs.
You can ignore this section if you created your repo after that date.

If you created your repo before this date then you will have the older README format, which expected you to update the file as your project progressed.
We have now moved to keeping that information in your project on the Jobs site.

The [current README template](https://github.com/opensafely/research-template/blob/main/README.md) has the updated version for new repos.

To update your repository's README to match this new README:

1. Copy the content from the template repository's latest README (typically [just the first section](https://github.com/opensafely/research-template/blob/main/README.md?plain=1#L1-L10)).
2. Manually edit those changed sections into your research repository's README.
3. You will need to replace the placeholder string in the README's "View on OpenSAFELY" URL to point to your repository:

4. `${GITHUB_REPOSITORY_NAME}` is the name of your repo.

!!! warning
    Each branch in your repository has a separate README, each of which will need updating.


## Tidy up your repo
Ensure your repo is as tidy as possible once you have completed your project. Consider the following:


### License
Check your repo has a `LICENSE` file.  We recommend the [MIT licence](https://opensource.org/license/mit), as it is an [open source license with strong community support](https://opensource.org/licenses?categories=popular-strong-community) and allows modification and distribution without cost. An MIT License has been included as part of the research template repository; you will need to edit the first line to include the current year and the name of your organisation. 


### Tests
Try to ensure your automated tests (on the repos _Actions_ tab) are green.
It's not essential, but it is a better look to be able to demonstrate your code is minimally runnable.


### Contents
Review your GitHub repository to make it simpler for people to explore:

* Merge or close all open Pull Requests (unless they are ongoing work in progress).
* Ensure that all branches are merged or deleted apart from the `main` or `master` branch. Old branches may contain draft work or previous ideas that are no longer needed. Note that deleting them does not delete the files permanently, they will still be in the repository history if you need to revisit them later. You may need to leave one or two branches open if they are ongoing work in progress (try to make sure they are named clearly).
* Delete any files that were not used/experimental and not used in final analysis, e.g. old versions of study definitions. Again they will still be in the repository history if you need them later.
* Are there old issues that can be closed? Some issues may have been fixed, or may be no longer relevant.


### GitHub Release
Consider making a GitHub _Release_, and linking to that: [refer to GitHub's documentation on releases](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository)).
A Release is a coherent snapshot of the code as it existed at a given point in time, along with a title and a description.
By default, releases are displayed on your repo home page.
For example, you might make separate releases of the code to accompany a preprint and the final versions of the paper.

Consider [obtaining a DOI for your releases](https://guides.github.com/activities/citable-code/), and using that for referencing your code.


## Update project status

[Update the status of the project](jobs-site.md#updating-project-status) on the Jobs site if relevant.

## Update project workspaces

Ensure each Workspace in your project on the Jobs site has a _purpose_ and [update if necessary](jobs-site.md#adding-a-workspace-purpose).

## Request the repo is made public

If your repository is *private*, you can request it is made public via the jobs site.
Click the "Change repo visibility" button on the workspace page of any workspace connected to it.
You will be prompted to check various bits of metadata associated with the repository, its branches, connected workspaces, and the project.
Once you have completed this page it will be checked by the OpenSAFELY team before being made public.

!!! info
    You will be prompted to make it public sooner, if you first ran the code against an OpenSAFELY database more than 12 months ago.

## Make your outputs on the jobs site public

Once you have approval from NHSE to publish your work, consider making all outputs released to the project workspace on the jobs site "published". See the [publication instructions](jobs-site.md#publishing-outputs).

## Add your publication to the OpenSAFELY website

Refer to our guidance on [adding a publication to the OpenSAFELY website](adding-a-paper.md).
