# Installation

This project is built using [mkdocs](https://www.mkdocs.org/).

It uses the [material theme](https://squidfunk.github.io/mkdocs-material/), and
[this page](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)
in their docs includes lots of very nice customisations for formatting documentation.

## Running locally

Use [`just run`](https://github.com/casey/just) to run the MkDocs server.

This should install everything required.

There is also a dev container setup that allows running the site in Codespaces
or locally with VSCode and Docker.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/opensafely/documentation)

### Inclusion of ehrQL documentation

The ehrQL documentation is imported from the
[ehrQL](https://github.com/opensafely-core/ehrql) repo using the
[mkdocs-multirepo-plugin](https://github.com/jdoiro3/mkdocs-multirepo-plugin) and built alongside the docs in this repo.  By default it uses the main branch.  This can
be configured with the `EHRQL_BRANCH` environment variable:

```
EHRQL_BRANCH=my-branch just run
```

## Updating Cohort Extractor

[cohort-extractor](https://github.com/opensafely-core/cohort-extractor) used to be a documentation dependency.
As cohort-extractor is now discontinued we wanted to remove this dependency,
so the rendered HTML content has been committed to legacy/docs.
