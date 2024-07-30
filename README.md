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
Failure notifications go to Slack.

This URL check detects URLs whose resources are not accessible.

The URL check can also be [run manually via GitHub Actions](https://github.com/opensafely/documentation/actions/workflows/check_links.yml).

#### Finding URLs that fail the link check

1. Review the failed workflow output by opening the [workflow runs](https://github.com/opensafely/documentation/actions/workflows/check_links.yml) page
   and clicking on the failed run to see a summary.
1. The summary lists any URLs that failed the check.
   URLs might fail for one of several reasons detailed below.

#### Dealing with URLs that fail the link check

##### Transient and persistent failures

Some URL checks may fail *transiently*,
due to a GitHub Actions runner issue or an outage at the resource that the URL points to.
When checking again later, the link check may pass.

To resolve a *persistent* link check failure for a URL requires:

* either, instructing lychee to ignore the URL,
  if the URL works in browser
* or, correcting the URL to be one that is accessible

##### Resolving persistent failures

Make any changes in a branch;
it is possible to manually run the link checking workflow on a branch from the Actions tab.
When you are satisfied that you have resolved the link check failures,
open a pull request with your fixes.

It is worth checking whether failed URLs can be viewed in a browser
via a fresh private/incognito browsing session.

This is a non-exhaustive list of common failures
and how you might address them:

* :mag: **Cause**: a URL is incorrect in the documentation
  (this might be a typo, or a broken relative link to other source files;
  relative links are not always easy to get right)
* :heavy_check_mark: **Resolution**: edit the documentation to correct the link
<!-- -->
* :mag: **Cause**: an internal relative link to another Markdown source file
  is missing the `.md` suffix
* :heavy_check_mark: **Resolution**: edit the link from
  `some-path/filename` to `some-path/filename.md`
<!-- -->
* :mag: **Cause**: a broken URL due to the resource being unavailable,
  due to the site having an outage or maintenance period
* :heavy_check_mark: **Resolution**: recheck the URL later;
  if the check repeatedly fails,
  consider finding a replacement URL or removing the URL
  (see ["Replacing inaccessible URLs"](#replacing-inaccessible-urls) below)
<!-- -->
* :mag: **Cause**: the resource the URL identifies has genuinely been removed
* :heavy_check_mark: **Resolution**: find a replacement URL or remove the URL
  (see ["Replacing inaccessible URLs"](#replacing-inaccessible-urls) below)
<!-- -->
* :mag: **Cause**: the resource that the URL points to either:
  * has restricted permissions
    (for example, requires you to login to see it)
  * or, is not restricted to a real web browser user,
    but is inaccessible by the Lychee client and/or the GitHub Actions runner
* :heavy_check_mark: **Resolution**: add the URL to the `.lycheeignore` file
  (see ["Adding a URL to `.lycheeignore`"](#adding-a-url-to-lycheeignore) below)
<!-- -->
* :mag: **Cause**: the URL is a deliberately broken or incomplete example
  (for example, to show the structure of a URL,
  rather than being a specific link)
* :heavy_check_mark: **Resolution**: add the URL to the `.lycheeignore` file
  (see ["Adding a URL to `.lycheeignore`"](#adding-a-url-to-lycheeignore) below)
<!-- -->
* :mag: **Cause**: the lychee client gets rate limited by a particular site,
  resulting in a failed check
* :heavy_check_mark: **Resolution**: try running the link check again;
  if the check repeatedly fails, reconfigure the link check workflow with lychee's `--max-concurrency` option
  and reduce the maximum concurrency (set lower than the default if no value is already specified)

#### Adding a URL to `.lycheeignore`

* The URLs in [`.lycheeignore`](.lycheeignore) use a regular expression format.
* URLs that match these regular expressions are ignored by lychee.
* You can use existing examples as a basis for adding new entries.
* The URL entries are grouped into sections,
  with entries listed under a comment that states the reason for their inclusion.
  Use the most appropriate section,
  or write a new comment and start a new section.
* If you find you are adding several URLs that fit in a pattern,
  you may wish to consider using a less restrictive regex for those URLs,
  instead of having to specify several individual URLs.
* For that reason, it's helpful to keep the entries for each section in alphabetical order.
* You may wish to scope the ignore rule to specific resources rather than an entire domain.
  A good example of this is `github.com` where some resources are publicly visible,
  and others require a login.
  Rather than ignore checks for `github.com` entirely,
  we can ignore the specific resources that fail checks.

#### Replacing inaccessible URLs

There are several options for dealing with a URL that is really no longer publicly accessible,
even to real browsers,
and will not be in future.

When changing a URL,
you may need to ask someone who knows about the specific content
for a replacement suggestion.

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
1. **Remove the URL entirely** and consider rewriting the surrounding text.

##### Reviewing surrounding text

In all cases,
when replacing URLs,
review the immediate and surrounding text too.
Small text edits may also be required to reflect changes in the linked resource.
