# OpenSAFELY Documentation

Documentation built using [mkdocs](https://www.mkdocs.org/).

includes [lots of very nice
customisations](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
for formatting documentation.

View it at https://docs.opensafely.org

## Building locally and testing

- Create a virtual environment
- `pip install -r requirements.txt`
- `mkdocs serve`

To pull in the latest version of the cohortextractor docstrings run:

    pip-compile -P opensafely-cohort-extractor
    pip install -r requirements.txt

If you have added new functions you will need to add an explicit
reference to them in [docs/study-def-variables.md](./docs/study-def-variables.md).


## Deploying

The site is served by Github Pages. We run mkdocs locally to compile the
HTML, which is then committed to a `gh-pages` branch and pushed to
Github.

This is all handled for us by running the command:

    mkdocs gh-deploy

Note: if this is your first deploy, you may wish to set up the `gh-pages` branch before running mkdocs:

    % git checkout gh-pages
    Branch 'gh-pages' set up to track remote branch 'gh-pages' from 'origin'.
    Switched to a new branch 'gh-pages'
