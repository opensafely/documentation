# Installation

This project is built using [mkdocs](https://www.mkdocs.org/).

It uses the [material theme](https://squidfunk.github.io/mkdocs-material/), and
[this page](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
in their docs includes lots of very nice customisations for formatting documentation.

## Building locally

- Create a virtual environment
- `pip install -r requirements.txt`
- `mkdocs serve`


## Updating Cohort Extractor
To pull in the latest version of the cohortextractor docstrings run:

    pip-compile -P opensafely-cohort-extractor
    pip install -r requirements.txt

If you have added new functions you will need to add an explicit
reference to them in [docs/study-def-variables.md](./docs/study-def-variables.md).
