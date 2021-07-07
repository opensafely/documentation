When you're ready to start telling the world about your Github repo, there are some things you might want to consider:

* When people click on a link to your repository, some of the most prominent things they'll see are the "About" section; and the contents of `README.md`. Ensure these are both up to date.
    * It is useful to include a link to the paper or other published, final outputs in `README.md`
* Check the `LICENSE` file exists, and that it allows modification and distribution without cost. We recommend the MIT Licence ([example](https://github.com/opensafely/risk-factors-research/blob/main/LICENSE)).
* You should consider making a Github _Release_, and linking to that ([instructions here](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository)). A Release is a coherent snapshot of the code as it existed at a given point in time, along with a title and a description. By default, releases are displayed on your repo home page. For example, you might make separate releases of the code to accompany a preprint and the final versions of the paper.
    * Consider obtaining a DOI for your releases, and using that for referencing your code
* Try to ensure your automated tests (on the repo's _Actions_ tab) are green. It's not essential, but it is a better look to be able to demonstrate your code is minimally runnable.
