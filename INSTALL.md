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


### Updating Data Builder Definitions

Data Builder generates some documentation automatically in JSON format from backend and contract code, and from its spec tests.  When a new Data Builder version builds and generates updates to
the documentation, a PR to update the JSON file in this repo is automatically opened.

The current and past versions of the Data Builder JSON file can be found as release artifacts
with [Data Builder releases](https://github.com/opensafely-core/databuilder/releases).

If the JSON file has changed you might need to update [the plugin which uses it to render pages](https://github.com/opensafely-core/mkdocs-opensafely-backend-contracts/).


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
