# OpenSAFELY Documentation

This is the public documentation for using the [OpenSAFELY platform](https://www.opensafely.org/).

It provides information on how to get set up with and use the platform.

## Running the site

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/opensafely/documentation)

When you see "Your application running on port 8910 is available",
you can click "Open in Browser" to see a preview,
and edit the content files in `docs/` to change the content.
It may take a few seconds for changes you make to appear.

See INSTALL.md for more details,
and for information on running locally instead of in Codespaces.

## Automated checks

We have some automated checks that help us maintain the documentation.

These are not enforced for new contributions,
but can be run by GitHub Actions.

### Content style checks

We have a small number of style rules written for the [Vale style checker](https://github.com/errata-ai/vale).

The purpose of these checks is to help keep our documentation more consistent,
even when multiple authors are working on it.

If these style checks prove useful,
we could expand on these into a more fully featured style guide.

The rules are stored in the [`styles` directory](styles/).
The rules are written in YAML.
See [Vale's documentation](https://vale.sh/docs/) for more information on Vale rules.

These checks are not scheduled
and are run [manually via GitHub Actions](https://github.com/opensafely/documentation/actions/workflows/check_vale.yml).

### URL validity checks

To help keep the content up-to-date,
there is a scheduled weekly link check
run with the [lychee link checker](https://github.com/lycheeverse/lychee/).
