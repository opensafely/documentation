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

opensafely-cohort-extractor is a documentation dependency. We use the
opensafely-cohort-extractor docstrings to generate some content here.

If you have added new functions, you will need to add an explicit
reference to them in
[docs/study-def-variables.md](./docs/study-def-variables.md).

### Updating via Dependabot

You can update the opensafely-cohort-extractor package via Dependabot.
Dependabot runs daily and will create a new pull request to update
opensafely-cohort-extractor if a newer version is available.

If you don't want to wait, you can also trigger a Dependabot check
manually via the ["Dependency
graph"](https://github.com/opensafely/documentation/network/updates)
section of this repository.

### Updating manually

Alternatively, you can pull in the latest version of the cohortextractor
docstrings, for local development or to update the requirements entirely
by hand:

    pip-compile --allow-unsafe --generate-hashes -P opensafely-cohort-extractor
    pip install -r requirements.txt
