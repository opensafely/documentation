# Installation

This project is built using [mkdocs](https://www.mkdocs.org/).

It uses the [material theme](https://squidfunk.github.io/mkdocs-material/), and
[this page](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
in their docs includes lots of very nice customisations for formatting documentation.

## Running locally

Use [`just run`](https://github.com/casey/just) to run the MkDocs server.

This should install everything required, **except for tooling to build
code snippets**. That tooling is self-contained in the `databuilder/`
directory.

## Updating Cohort Extractor

[cohort-extractor](https://github.com/opensafely-core/cohort-extractor) is a documentation dependency.
We use the cohort-extractor docstrings to generate some content here.

cohort-extractor is currently a Git submodule instead, for installation simplicity (see #832).
**We currently do not install cohort-extractor into a virtualenv because we are only using the docstrings**

### Updating cohort-extractor via Dependabot

You can update the cohort-extractor submodule via Dependabot.

Dependabot runs daily and will create a new pull request to update
cohort-extractor if a newer version is available.

If you don't want to wait, you can also trigger a Dependabot check
manually via the ["Dependency
graph"](https://github.com/opensafely/documentation/network/updates)
section of this repository.

### Updating cohort-extractor manually

Alternatively, you can pull in the latest version of the cohortextractor
docstrings, for local development or to update the requirements entirely
by hand: `just update-cohort-extractor`

## Updating Data Builder Definitions

Data Builder generates some documentation automatically in JSON format from backend and contract code, and from its spec tests. When a new Data Builder version builds and generates updates to
the documentation, a PR to update the JSON file in this repo is automatically opened. The PR is opened by a [workflow in the Data Builder repository](https://github.com/opensafely-core/databuilder/blob/main/.github/workflows/update-public-docs.yml).

If the JSON file has changed you might need to update [the plugin which uses it to render pages](https://github.com/opensafely-core/mkdocs-opensafely-backend-contracts/).
