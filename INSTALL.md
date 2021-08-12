# Installation

This project is built using [mkdocs](https://www.mkdocs.org/).

It uses the [material theme](https://squidfunk.github.io/mkdocs-material/), and
[this page](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
in their docs includes lots of very nice customisations for formatting documentation.

## Building locally

### Running in a virtualenv

- Create a Python 3.7 virtual environment
- Install requirements: `pip install -r requirements.dev.txt`
- Start the local server: `mkdocs serve --strict`

### Running via Docker

* Run `run.sh` to build and start the Docker image.

## Updating Cohort Extractor
To pull in the latest version of the cohortextractor docstrings run:

    pip-compile -P opensafely-cohort-extractor
    pip install -r requirements.txt

If you have added new functions you will need to add an explicit
reference to them in [docs/study-def-variables.md](./docs/study-def-variables.md).
