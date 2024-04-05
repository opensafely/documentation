
## 2. Requesting release of outputs and (error) log files from the server

!!! warning
    You **MUST NOT** share any results that have not been released through the official output checking process. This includes:

    - verbal sharing
    - allowing someone to look over your shoulder
    - transcribing (e.g., to paper or email)
    - using screen sharing software or any recording device/software

**Only specific members of the OpenSAFELY team trained in output checking have permissions to release the data**. Having applied disclosure controls to your aggregated study data you are ready to request their release. Please read the instructions and [checklist](#checklist) below.

First, create one folder in your workspace called `release` (if you have previously made a release, we suggest appending the date to the new folder name to distinguish it) and copy from your `output` folder to this `release` folder the data files that require review. The number of study outputs requested for review must be kept to a minimum and include only the results you absolutely need to export from the secure server.

When you are ready to request a release of your aggregated results please [complete this form](/documents/OpenSAFELY_Output_Review_Form_ADD_WORKSPACE_NAME_ADD_DATE.docx), renaming the form to replace the placeholders with your workspace name and the date.

!!! note
    Each data release entails substantial review work. To retain rapid turnaround times, external data releases should typically only be of results for final submission to a journal or public notebook; or a small number of necessary releases for discussion with external collaborators.

<a id="context-requirements"></a>For each output wishing to be released you will need to provide a clear contextual description including:

1. The file path for each output
2. Variable descriptions
3. A description and count of the underlying sample of the population for each output.
4. Population size and degrees of freedom for all regression outputs.
5. Relationship to other data/tables which through combination may introduce secondary disclosive risks.

Each section in the review request form should normally describe a single file, but where necessary for similar files, these can be grouped together and wildcards can be used for the file path (e.g. `release/hospitalisation_rate_by_*.csv`). **If you use a wildcard, please indicate how many files this captures**.

### Release of intermediate data

In general, releases should be for final results from your project (see the note above). However, on some occassions it is appropriate to release intermediate data. Below are some suggestions for when this is appropriate:

* You think you may need to make minor edits to final outputs such as changing figure labels. Release of the intermediate data allows you to make these [changes locally](#running-further-analyses-on-released-outputs).
* A large number of outputs are produced from a single intermediate output. Release of the intermediate data underlying the figures (which needs to be checked whether it is released or not) avoids the need to check the downstream outputs.
*  The intermediate data doesn't contain person-level data, but is used for running a model that would produce multiple outputs.

If requesting release of intermediate data there are a few considerations:

*  We recommend that you continue to develop downstream analysis actions within the OpenSAFELY pipeline, even if they are not intended to be run on the server. This helps maintain reproducibility.
* Intermediate results can contain much more data than outputs produced at the end of the analysis pipeline. The data contained within these outputs should be the minimum amount required to produce the downstream outputs or receive feedback from project collaborators.

### Error log files

For error logs, they should only be requested for output in exceptional circumstances (for example, if you need to discuss the error and any related data within the log file with a researcher who writes code but does not have Level 4 results server access, otherwise we would expect both researchers to review the log via their VPN access). When an error log is requested, you must minimise any data required: make a copy of the log file and delete all data items that are not necessary. The less data that is present, the faster the review process.

### Allowed file types

Only certain file types will be reviewed and released from the secure server. See below for details on each type:

* **Tables** - Tables should be produced as `csv` files.
    * Make sure that any column names are understandable for reviewers.
    * Limit the number of columns or rows to only what is necessary.
* **Figures** - Figures can be produced as bitmap images (`jpeg` or `png`) or vector graphics (`svg`).
    * We recommend requesting the release of the underlying _aggregated_ data for all figures, rather than the figures themselves. You can then create the figures outside of the secure server, which has a few advantages:
        * You can tweak the figure much quicker and easier on your local computer.
        * You won't need to make a new output checking request when you need to change the figure because of an error or stylistic tweak.
        * It's easier for output checkers to check a table of aggregated counts than a figure.
        * You can still maintain the reproducibility of your project, by committing the code to locally produce the graph to your repo.
    * If you do produce figures on the secure server, you should always produce the underlying _aggregated_ data alongside them (even if it is not being released). This is required to prove to reviewers that there are no small counts represented in the figure.
* **Other**
    * `txt` files can be released, but you should consider whether the output can be produced as a table, which is easier to review.
    * `json` files can be released, but as with tables, make sure that the attributes are easily understandable for reviewers. If the output can be represented as a table, you should consider converting it.
    * `html` files can be released if you are producing a report that is intended to be hosted on [reports.opensafely.org](https://reports.opensafely.org/) but please note the points below:
        * `html` files are harder to review than other output types, so should be reserved for reports which require both contextual text and embedded outputs. If you can produce your report locally, using individually released files, you should.
        * Make sure that any code blocks are not rendered in the rendered report if they are not needed. You can find [examples showing how to do this for Jupyter notebooks and R markdown files](reports/intro.md#producing-reports).
        * Each individual output within the report should be requested for release separately, with the contextual information outlined above.
        * `html` files should be stripped of any embedded javascript and styling. This is obfuscated when viewing a report via a web browser, but makes review of the raw file very difficult. Refer to our instructions [explaining how to strip the `html` files](reports/intro.md#producing-reports).
        * When making a review request that includes `html` files, please include a link to the code you have used to produce the reports.

If you would like to release other file types, please email <datarelease@opensafely.org>, stating why it is important that the file is released in a different format.

!!! note
    The maximum file size that can be released is 16MB. Please check your outputs before requesting them for release. It is unlikely any outputs that exceed this in size are appropriate for release, but if you think they are, please let us know when making a release request.

### Checklist

Please run through this checklist before making a review request.

1. Do your results adhere to the [OpenSAFELY permitted study results policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy)
2. Are all of the outputs of the [allowed file types](#allowed-file-types)?
3. Are all of the outputs in a [separate release folder](#2-requesting-release-of-outputs-and-error-log-files-from-the-server)?
4. Have you [redacted any low counts](#redacting-counts-less-than-or-equal-to-7)?
5. Have you [rounded any counts](#rounding-counts) (including [counts underlying rates](#rounding-rates))?
6. Have you supplied underlying counts for all of your results?
7. Are all of the outputs clearly described?
    * Is the filename sensible and is the filepath provided in the request form correct?
    * Have you provided all of the context needed to review each output in isolation in the request form?
    * Have you described the disclosure controls you have applied to each output?
8. If you are requesting the release of log files, are you sure they [need to be released](#error-log-files)?
9. Are all of the requested files below the [maximum file size](#allowed-file-types)?

Following this checklist will make your outputs easier to check, speed up review time and avoid the outputs having to be rechecked.

### Submitting the form

Once you have completed this form, please send it to **<datarelease@opensafely.org>**. The requested outputs will undergo independent review by two OpenSAFELY output checkers who will check that the outputs are within the scope of your original project proposal and that they do not present any disclosure risks. **Please allow up to 5 working days for feedback on your request**.

!!! warning
    The [Permitted Study Results Policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy) may be updated: **always check the policy before every new release request.**

!!! note
    **Tips for getting a quicker review**
    Our resources for checking outputs are not unlimited, therefore it is advised to ensure you have all of your outputs ready at the same time for your project (or its current phase) so they can be reviewed together. Please make your outputs as understandable as possible for output checkers who will not be familiar with your project by, for example, using descriptive variable names and providing full descriptions of each output in the form provided.

    Another reason to ensure your analyses are complete is that re-running your study definition a short time later (e.g. to create an additional variable) may produce small differences in the previous results, e.g. due to movement of patients or codes added retrospectively to patient records. If you have already released similar results, any small changes in new outputs may be subject to small number suppression which may prevent the new outputs being released at all. (One solution to minimise this issue is to round all of your results, e.g. to the nearest 5).

## 3. How are files reviewed?

Before any files are released from the secure server, they are checked independently by two trained OpenSAFELY output checkers. Each checked output is marked as one of the following categories:

* **Approve** — output meets disclosure requirements and is safe to be released
* **Approve subject to change** — output is an acceptable type for release, but has outstanding disclosure issues that must be addressed before release
* **Reject** — output is not an acceptable type for release. An example is the release of practice level data which does not meet the [permitted study results policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy)

Once reviewed, the completed review request will be emailed back to you. We aim to provide a response to review requests within **5 working days**. If all outputs are approved, they will then be released. If one or more outputs are approved subject to change, you will need to address the disclosure issues and submit a new review form detailing the changes you have made.

### Most common problems with output review requests

Below are the most common problems encountered by output checkers when reviewing output review requests. **Avoiding these issues makes it more likely your files can be released first time round**, saving reviewer time and allowing quicker file release for you and other researchers.

1. **There are unrounded counts in the outputs**. All counts should be [rounded](#rounding-counts). This includes rounding counts prior to them being used to calculate further statistics, such as percentages or odds ratios. Commonly raw counts are rounded, but downstream statistics are calculated using the raw counts rather than the rounded counts. Unrounded counts account for **~30%** of rejections.
2. **Insufficicent context is provided for the outputs**. **~25%** of rejected outputs are due to insufficient context. Make sure you have provided all of the context needed to review each output in isolation in the request form. Common errors include:
    * Stating the incorrect file path. You should check all file paths point to the relevant files within your `release` folder before making a request.
    * Files included in the review form being missing from the `review` folder.
    * Using unclear column/variable names or poorly describing the presented data. See [here](#context-requirements) for more details on the context requirements.
    * Not clearly indicating the relationship between different outputs.
    * Where an output has previously been requests, not indicating how the output differs to previously reviewed version.
3. **There are unredacted counts in the outputs**. Prior to rounding counts, [any counts <=7 should be redacted](#redacting-counts-less-than-or-equal-to-7). The redaction approach should be clearly described when making a review request. It is not uncommon for the stated redaction approach to be improperly implemented in the outputs. Inappropriate redaction of low counts accounts for **~20%** of rejected outputs.
4. **Underlying data is not provided**. To ensure the low number threshold is met, reviewers require to see the underlying data for each output. This includes the data used to generate figures and to calculate summary statistics such as mean or median. **~10%** of rejected outputs are due to underlying data not being provided.
5. **Unsupported file types being requested**. Files requested for release should be one of the [allowed file types](#allowed-file-types). If you are requesting the release of HTML files, please make sure you have followed the [guidance for HTML files](#allowed-file-types). **~10%** of rejected outputs are due to unsupported file types being requested.

To help avoid these issues, please make sure you have read the [checklist](#checklist) before submitting your review request.

## 4. Release of reviewed files

All approved OpenSAFELY outputs are released to the workspace they belong to on the [Jobs site](jobs-site.md).

### Viewing released outputs

View your released outputs by navigating to "Released Outputs" in the "Releases" section of your workspace on the Jobs site.

These outputs can be shared with project collaborators and published in line with our [data sharing and publication policy](https://www.opensafely.org/policies-for-researchers/#acknowledgment-and-data-sharing--publication-policy). Please note that you should check this for each dataset that you have used: rules may vary.

### Running further analyses on released outputs

If you have had [intermediate data released](#release-of-intermediate-data) and you wish to run further analyses on them, such as reformatting figures, there are a few things to consider.

1. You should include the code for these steps in your GitHub repo.
2. You **should not** commit any of the released outputs (including final processed charts/tables) to your GitHub repo. Make sure to include them in the `.gitignore` file.
3. Consider adding the code as an action in your project pipeline.

### Reporting a data breach

If you discover files released to the Jobs site that have been insufficiently redacted and still contain sensitive information, you should immediately contact and email the following (providing as much information as possible): Amir Mehrkar (<amir.mehrkar@phc.ox.ac.uk>); Ben Goldacre (<ben.goldacre@phc.ox.ac.uk>); [disclosurecontrol@opensafely.org](mailto:disclosurecontrol@opensafely.org); and your co-pilot. Ensure you do not share these files and if they have already been shared please identify as best as possible with whom they have been shared.


---8<-- 'includes/glossary.md'
