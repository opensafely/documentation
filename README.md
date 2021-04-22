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

The [docs site](https://docs.opensafely.org) is served by [readthedocs](https://readthedocs.org/), using a webhook to build the [latest version](https://readthedocs.org/projects/opensafely-documentation/versions/) from the `master` branch when it is updated. 

There are a [few redirects](https://readthedocs.org/dashboard/opensafely-documentation/redirects/) from old `stable` urls to current `latest` urls.
