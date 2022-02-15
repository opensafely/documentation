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

Data Builder is a documentation dependency which we can't install directly.
Cloudflare Pages' latest Python version is 3.7, but Data Builder is using 3.9 features.
Rather than limit Data Builder to the versions supported by Cloudflare Pages, we've opted to have it generate a JSON file from Data Builder and commit that JSON to this repo.

Run `just databuilder/generate-docs` to generate the JSON file using `databuilder` installed in the `databuilder` subdirectory of this repo.

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
