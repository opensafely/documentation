# Installation

This project is built using [mkdocs](https://www.mkdocs.org/).

It uses the [material theme](https://squidfunk.github.io/mkdocs-material/), and
[this page](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
in their docs includes lots of very nice customisations for formatting documentation.

## Running locally

Use [`just run`](https://github.com/casey/just) to run the MkDocs server.

This should install everything required.

### Data Builder

The Data Builder documentation is imported from the
[databuilder](https://github.com/opensafely-core/databuilder) repo using the
[mkdocs-multirepo-plugin](https://github.com/jdoiro3/mkdocs-multirepo-plugin) and built alongside the docs in this repo.  By default it uses the main branch.  This can
be configured with the `EHRQL_BRANCH` environment variable:

```
EHRQL_BRANCH=my-branch just run
```


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
