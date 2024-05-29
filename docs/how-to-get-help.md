## Q&A forum

If you're outside the co-pilot programme,
then your first port of call should be to ask your question in the [Q&A forum][].
Before asking your question,
please search the [Q&A forum][] and the OpenSAFELY documentation,
to check that your question hasn’t already been answered.

[Q&A forum]: https://github.com/opensafely/documentation/discussions

## Slack

You will be invited to join the Bennett Institute's workspace during the co-pilot programme.
If you're outside the co-pilot programme,
then your second port of call should be to ask your question in any channel to which you have access.
(Your first port of call should be to ask your question in the [Q&A forum](#qa-forum).)

You may wish to direct your question to the **tech support team**.
To do so, include the string `tech-support` in your question
and a member of this team will aim to respond within half a working day.
We ask that you don't send direct messages (DMs) to members of the tech support team.

The types of question that this team aim to answer include:

* deleting files from [Level 3](security-levels.md#level-3-nhs-england-are-data-controllers-of-the-data) or [Level 4](security-levels.md#level-4-nhs-england-are-data-controllers-of-the-data)
* [requesting new libraries](requesting-libraries.md)
* accuracy of the OpenSAFELY documentation
  ("The documentation says... but the error message says...")
* completeness of the OpenSAFELY documentation
  ("How do I... in OpenSAFELY?)
* availability of services
  (e.g. [OpenSAFELY Jobs](https://jobs.opensafely.org/), the OpenSAFELY documentation, GitHub)

Some types of question are beyond the scope of the tech support team,
although other members of the Bennett Institute's workspace may be able to answer them.
These types of question include:

* programming tasks ("How do I... in...?")
* build/deploy failures
  (e.g. of the OpenSAFELY documentation, of the Bennett Institute team manual)

Issues on OpenSAFELY repositories
(i.e. repositories within the `opensafely`, `opensafely-core`, and `opensafely-actions` GitHub organizations)
are also beyond the scope of the tech support team.
However, we welcome [bug reports and feature requests](#bug-reports-and-feature-requests) made in this way.

[opensafely]: https://github.com/opensafely
[opensafely-actions]: https://github.com/opensafely-actions
[opensafely-core]: https://github.com/opensafely-core

## Searching past study code

The [GitHub OpenSAFELY organisation](https://github.com/opensafely) is a useful source of information when writing your analysis.
Our GitHub organisation stores all of the code used for previous studies.
You can search for examples of how specific variables and codelists etc. have been used.

!!! warning
    Use some caution when looking at code, especially older code:
    it may never have been run, or may have been superseded since.

To search the OpenSAFELY GitHub organisation for code:

1. Go to the [OpenSAFELY GitHub organisation page](https://github.com/opensafely).
2. Type or paste your search text into the top-left box (`Search or jump to...`)
3. Press ++enter++ or select the option to search `In this organisation`.
4. Select "Code" to find any matches within previous code (or sometimes "Issues" may help).

It can be helpful to use the option to filter the results by language.
For example, restricting to Python might help you find study definition files.

## Bug reports and feature requests

OpenSAFELY uses GitHub to manage and share code and other platform resources. If you want to request any changes to the platform then GitHub issues should be your first port of call.

Issues can be submitted for lots of different things &mdash; new variables or other features, bug reports, additional R or Stata packages, documentation updates, and so on.  All our core software packages live in the [`opensafely-core`](https://github.com/opensafely-core/) GitHub organisation.

The most common requests are about library support; this page describes [how to request new libraries](requesting-libraries.md). If you want to report bugs or request features in the `opensafely` command-line tool, you can do so in [its own dedicated issue tracker](https://github.com/opensafely-core/opensafely-cli/issues).

Other than this, you will need to choose the most appropriate repo to submit an issue. If you're not sure where to submit your issue, just ask a question in our [Q&A forum](https://github.com/opensafely/documentation/discussions) and we can point you to the right place.

## Data providers

We have information on [integration](system-integration.md) elsewhere in this documentation.

For general questions on getting a local integration running,
please use our [Q&A forum](https://github.com/opensafely/documentation/discussions).

To discuss making your data available to researchers via the OpenSAFELY
platform, please [contact our technical
team](mailto:team@opensafely.org).

---8<-- 'includes/glossary.md'
