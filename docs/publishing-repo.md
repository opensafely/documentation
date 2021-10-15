When you're ready to tell the world about your GitHub repo, consider the following:

* Check that the "About" section and the contents of `README.md` are both up to date. People will see these sections prominently when they click a link to your repository on GitHub.
    * Include a link to the paper or other published, final outputs in `README.md`.
    * Include a short, one-line summary and link to your paper or outputs in the "About" section. Click the cog next to "About" and add these details.
* Check the `LICENSE` file exists, and that it allows modification and distribution without cost. We recommend the MIT Licence ([example](https://github.com/opensafely/risk-factors-research/blob/main/LICENSE)).
* Try to ensure your automated tests (on the repo's _Actions_ tab) are green. It's not essential, but it is a better look to be able to demonstrate your code is minimally runnable.
* Review your GitHub repository to make it simpler for people to explore:
    * Merge or close all open Pull Requests (unless they are ongoing work in progress). 
    * Ensure that all branches are merged or deleted. Old branches may contain draft work or previous ideas that are no longer needed. Note that deleting them does not delete the files permanently, they will still be in the repository history if you need to revisit them later. You may need to leave one or two branches open if they are ongoing work in progress (try to make sure they are named clearly). 
    * Delete any files that were not used/experimental and not used in final analysis, e.g. old versions of study definitions. Again they will still be in the repository history if you need them later. 
    * Are there old issues that can be closed? Some issues may have been fixed, or may be no longer relevant.
    
* Consider making a GitHub _Release_, and linking to that ([instructions here](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository)). A Release is a coherent snapshot of the code as it existed at a given point in time, along with a title and a description. By default, releases are displayed on your repo home page. For example, you might make separate releases of the code to accompany a preprint and the final versions of the paper.
    * Consider [obtaining a DOI for your releases](https://guides.github.com/activities/citable-code/), and using that for referencing your code
    
* If your repository is *private*, [**make it *public***](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/setting-repository-visibility) before the associated paper or output is published.
