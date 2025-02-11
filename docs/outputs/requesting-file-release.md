!!! note
    Only specific members of the OpenSAFELY team trained in output checking have permissions to release the data.

Having applied disclosure controls to your aggregated study data you are ready to request their release. This page describes the restrictions on files that can be released and the
information you will need to provide in order to request release. For instructions on how
to create and submit your release request, please refer to the documentation on [releasing files with
Airlock](/using-opensafely/viewing-and-releasing-outputs/viewing-and-releasing-with-airlock).

Note: the [previous manual process for requesting release of files](../legacy/requesting-release-offline-process.md) is now deprecated. All release requests should be submitted via Airlock wherever possible.

!!! warning
    You **MUST NOT** share any results that have not been released through the official output checking process. This includes:

    - verbal sharing
    - allowing someone to look over your shoulder
    - transcribing (e.g., to paper or email)
    - using screen sharing software or any recording device/software



### When should I create a release request?

Each data release entails substantial review work. To retain rapid turnaround times, external data releases should typically only be of results for final submission to a journal or public notebook; or a small number of necessary releases for discussion with external collaborators.

!!! note "Tips for getting a quicker review"
    Our resources for checking outputs are not unlimited, therefore it is advised to ensure you have all of your outputs ready at the same time for your project (or its current phase) so they can be reviewed together. Please make your outputs as understandable as possible for output checkers who will not be familiar with your project by, for example, using descriptive variable names and providing full descriptions of your outputs and
    [contextual information](#context-and-controls).

Another reason to ensure your analyses are complete is that re-running your study definition a short time later (e.g. to create an additional variable) may produce small differences in the previous results, e.g. due to movement of patients or codes added retrospectively to patient records. If you have already released similar results, any small changes in new outputs may be subject to small number suppression which may prevent the new outputs being released at all. (One solution to minimise this issue is to round all of your results, e.g. to the nearest 5).

#### Release of aggregated results to be used to generate final outputs 

In general, releases should be for final results from your project (see the note above). However, on some occassions it is appropriate or even preferable to release data that is subsequently used to generate other outputs (e.g. graphs). As with all requested outputs, these must have appropriate disclosure controls applied. Below are some examples for when this is appropriate:

* You think you may need to make minor edits to final outputs such as changing figure labels. You may request release of data that allows you to [generate final outputs (graphs etc) and make changes locally](viewing-released-files.md#running-further-analyses-on-released-outputs).
* A large number of outputs are produced from a single output. Release of the data underlying the figures (which needs to be checked whether it is released or not) avoids the need to check the downstream outputs.
*  The data doesn't contain person-level data, but is used for running a model that would produce multiple outputs.

If requesting release of such data there are a few considerations:

*  We recommend that you continue to develop downstream analysis actions within the OpenSAFELY pipeline, even if they are not intended to be run on the server. This helps maintain reproducibility.
* Such non-final results have the potential to contain much more data than outputs produced at the end of the analysis pipeline. The data contained within these outputs should be the minimum amount required to produce the downstream outputs or receive feedback from project collaborators.

### Context and Controls

For each group of outputs you wish to release you will need to provide a clear contextual description including:

1. Variable descriptions.
1. A description and count of the underlying sample of the population for each output.
1. Population size and degrees of freedom for all regression outputs.
1. Relationship to other data/tables which through combination may introduce secondary disclosive risks.

You will also need to descibe **controls** (i.e. [statistical disclosure controls](sdc.md)
that have been applied to the outputs.

A group of files can include one output file, or multiple files that share the same
context and controls.

### Error log files

For error logs, they should only be requested for output in exceptional circumstances (for example, if you need to discuss the error and any related data within the log file with a researcher who writes code but does not have Level 4 results server access, otherwise we would expect both researchers to review the log via their VPN access). When an error log is requested, you must minimise any data required: make a copy of the log file and delete all data items that are not necessary. The less data that is present, the faster the review process.

### Allowed file types

Only certain file types will be reviewed and released from the secure server. See below for details on each type:

* **Tables** - Tables should be produced as `csv` files.
    * Make sure that any column names are understandable for reviewers.
    * Limit the number of columns or rows to only what is necessary. The maximum number of
      rows that can be included in a file for release is 5000.

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
        * Make sure that any code blocks are not rendered in the rendered report if they are not needed. You can find [examples showing how to do this for Jupyter notebooks and R markdown files](../reports/intro.md#producing-reports).
        * Each individual output within the report should be requested for release separately, with the contextual information outlined above.
        * `html` files should be stripped of any embedded javascript and styling. This is obfuscated when viewing a report via a web browser, but makes review of the raw file very difficult. Refer to our instructions [explaining how to strip the `html` files](../reports/intro.md#producing-reports).
        * When making a review request that includes `html` files, please include a link to the code you have used to produce the reports.

If you would like to release other file types, please email <datarelease@opensafely.org>, stating why it is important that the file is released in a different format.

### Maximum file size
The maximum file size that can be released is 16MB. Please check your outputs before requesting them for release. It is unlikely any outputs that exceed this in size are appropriate for release, but if you think they are, please let us know when making a release request.

### Checklist

Please run through this checklist before submitting a review request.

1. Do your results adhere to the [OpenSAFELY permitted study results policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy)
1. Are all of the outputs of the [allowed file types](#allowed-file-types)?
1. Have you [redacted any low counts](sdc.md#redacting-counts-less-than-or-equal-to-7)?
1. Have you [rounded any counts](sdc.md#rounding-counts) (including [counts underlying rates](sdc.md#rounding-rates))?
1. Have you supplied underlying counts for all of your results?
1. Are all of the outputs clearly described?
    * Have you provided all of the [context](#context-and-controls) needed to review each output in isolation?
    * Have you described the [disclosure controls](#context-and-controls) you have applied to each output?
1. If you are requesting the release of log files, are you sure they [need to be released](#error-log-files)?
1. Are all of the requested files below the [maximum file size](#maximum-file-size)?

Following this checklist will make your outputs easier to check, speed up review time and avoid the outputs having to be rechecked.

!!! warning
    The [Permitted Study Results Policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy) may be updated: **always check the policy before every new release request.**
