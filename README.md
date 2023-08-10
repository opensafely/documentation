# OpenSAFELY Documentation

This is the public documentation for using the [OpenSAFELY platform](https://www.opensafely.org/).

It provides information on how to get set up with and use the platform.

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

This detects broken links:
URLs whose resources are no longer accessible.

The URL check can also be [run manually via GitHub Actions](https://github.com/opensafely/documentation/actions/workflows/check_links.yml).

#### Finding the inaccessible URLs

1. Review the failed workflow output by opening the [workflow runs](https://github.com/opensafely/documentation/actions/workflows/check_links.yml) page
   and clicking on the failed run to see a summary.
1. The summary should show the failed URL.
   URLs might fail for one of several reasons.
   It is worth checking whether the URL can be viewed in browser.

#### Addressing inaccessible URLs

Here is a non-exhaustive list of common failures
and how to address them

* :mag: **Cause**: a broken relative link to somewhere else in the documentation
  (the syntax of these can be tricky to get correct)
* :heavy_check_mark: **Resolution**: edit the documentation to correct the link
<!-- -->
* :mag:**Cause**: a broken URL due to the resource being unavailable,
  due to the site having an outage or maintenance period
* :heavy_check_mark: **Resolution**: leave and review in the next link check a week later;
  if the check fails a second time,
  consider finding a replacement URL or removing the URL
  (see ["Replacing inaccessible URLs"](#replacing-inaccessible-urls) below)
<!-- -->
* :mag:**Cause**: the resource the URL identifies has genuinely been removed
* :heavy_check_mark: **Resolution**: find a replacement URL or remove the URL
  (see ["Replacing inaccessible URLs"](#replacing-inaccessible-urls) below)
<!-- -->
* :mag:**Cause**: the lychee client gets rate limited by a particular site,
  resulting in a failed check
* :heavy_check_mark: **Resolution**: reconfigure the link check workflow with lychee's `--max-concurrency` option
  and reduce it from the default value
<!-- -->
* :mag:**Cause**: the resource that the URL points to either:
  * has restricted permissions
    (for example, requires you to login to see it)
  * or, is not restricted to a real web browser user,
    but is inaccessible by the Lychee client and/or the GitHub Actions runner
* :heavy_check_mark: **Resolution**: add the URL to the `.lycheeignore` file

#### Replacing inaccessible URLs

There are several options for dealing with a URL that is really no longer accessible,
and will not be in future:

1. **Remove the URL entirely.**
1. If the information is still relevant,
   **check if the [Internet Archive](https://web.archive.org) has a usable, saved copy of the page**
   and use the Internet Archive's version instead:
   * Depending on the context,
     often you probably want the latest version saved.
   * In some cases,
     you might favour using the version closest in time to when the original content was written.
1. **Find a suitable replacement URL:**
   * on the same site
     * It might be that the content or resource has moved to a different place on the same site.
   * on another site
     * It might be that the content or resource has moved to a different site owned by the same organisation.
     * It might also be that an entirely different organisation now has a more relevant resource or content.

In all cases,
when replacing URLs,
review the immediate and surrounding text too.
Small text edits may also be required to reflect changes in the linked resource.
