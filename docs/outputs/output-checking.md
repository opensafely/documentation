Before any files are released from the secure server, they are checked independently by two trained OpenSAFELY output checkers. Each checked output is marked as one of the following categories:

* **Approve** — output meets disclosure requirements and is safe to be released
* **Request changes** — output is an acceptable type for release, but has outstanding disclosure issues that must be addressed before release
* **Reject** — output is not an acceptable type for release. An example is the release of practice level data which does not meet the [permitted study results policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy)

### Responding to requests
Requests submitted via Airlock will also be reviewed by output checkers on Airlock. If
the output checkers require changes or have questions about the requested files, they
will return the release request to you. You will receive an email notification when this happens.

For further information on how to submit and respond to returned requests, please see the
documentation on [releasing with Airlock](../using-opensafely/viewing-and-releasing-outputs/viewing-and-releasing-with-airlock/index.md).

### Most common problems with output review requests

Below are the most common problems encountered by output checkers when reviewing output review requests. **Avoiding these issues makes it more likely your files can be released first time round**, saving reviewer time and allowing quicker file release for you and other researchers.

1. **There are unrounded counts in the outputs**. All counts should be [rounded](sdc.md#rounding-counts). This includes rounding counts prior to them being used to calculate further statistics, such as percentages or odds ratios. Commonly raw counts are rounded, but downstream statistics are calculated using the raw counts rather than the rounded counts. Unrounded counts account for **~30%** of rejections.
2. **Insufficicent context is provided for the outputs**. **~25%** of rejected outputs are due to insufficient context. Make sure you have provided all of the context needed to review each output in isolation in the request form. Common errors include:
    * Using unclear column/variable names or poorly describing the presented data. Refer to the [context requirements](requesting-file-release.md#context-and-controls).
    * Not clearly indicating the relationship between different outputs.
    * Where an output has previously been requested, not indicating how the output differs to previously reviewed version.
3. **There are unredacted counts in the outputs**. Prior to rounding counts, [any counts <=7 should be redacted](sdc.md#redacting-counts-less-than-or-equal-to-7). The redaction approach should be clearly described when making a review request. It is not uncommon for the stated redaction approach to be improperly implemented in the outputs. Inappropriate redaction of low counts accounts for **~20%** of rejected outputs.
4. **Underlying data is not provided**. To ensure the low number threshold is met, reviewers require to see the underlying data for each output. This includes the data used to generate figures and to calculate summary statistics such as mean or median. **~10%** of rejected outputs are due to underlying data not being provided.
5. **Unsupported file types being requested**. Files requested for release should be one of the [allowed file types](requesting-file-release.md#allowed-file-types). If you are requesting the release of HTML files, please make sure you have followed the [guidance for HTML files](requesting-file-release.md#allowed-file-types). **~10%** of rejected outputs are due to unsupported file types being requested. (Note: Airlock will automatically restrict output files in a request to only allowed file types.)

To help avoid these issues, please make sure you have read the [checklist](requesting-file-release.md#checklist) before submitting your review request.
