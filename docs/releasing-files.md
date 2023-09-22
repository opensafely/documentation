# "Safe Outputs" and requesting release of files from the Level 4 Server
## The Five Safes Framework for safe and efficient use of data

OpenSAFELY follows the [Five Safes](https://ukdataservice.ac.uk/help/secure-lab/what-is-the-five-safes-framework/) framework for data access to allow safe and efficient use of data. This framework models data access into 5 independent dimensions:

* **Safe projects** - does the project make good use of the data?
* **Safe people** - are the researchers using the data appropriately trained and aware of their role in data protection?
* **Safe data** - what is the potential for individuals to be identified in the data?
* **Safe settings** - are there technical controls on access to the data?
* **Safe outputs** - is there any residual risk in outputs being released from the environment?

All data in OpenSAFELY is pseudonymised and all projects and researchers in OpenSAFELY go through an approval process before having any access to the dataset. This ensures the “safe data”, “safe projects” and “safe people” elements of the fives safes framework are met. The technical controls implemented as part of the OpenSAFELY platform ensures that “safe settings” are in place and that risk is minimised in this respect. The application of **disclosure controls** and **output-checking** is part of the “safe outputs” dimension.

Below we cover the 4 key areas of our “safe outputs” activities:

1.  Researchers must only request the release of outputs necessary to fulfil their project purpose and apply disclosure controls to them.
2.  Researchers then make a request to release the outputs using the “release request form”.
3.  Two OpenSAFELY output checkers review the output being requested for release.
4.  OpenSAFELY releases outputs that meet our disclosure rules to the relevant workspace on the Jobs site.

## 1. Applying disclosure controls to outputs you request for release

The assessment of the risk of re-identification attached to a data item or statistical outputs, and the use of appropriate methods to reduce the disclosure risk, is known as **statistical disclosure control (SDC)**. In OpenSAFELY, researchers must apply SDC at the stage where their aggregated results are ready to be released from the results server (the Level 4 environment) for sharing with collaborators for feedback, or for publication as papers, reports, blogs, etc. Examples of SDC techniques to manage the disclosure risk include redacting (suppressing) low values, rounding values, or redesigning outputs so that sparse table cells, for example, are combined.
In general, good SDC is consistent with good statistics: many observations, no influential outliers, well-behaved distributions etc both prevent disclosure and increase confidence in the statistics. The one area to be wary of is where you can say something for certain about entire groups (‘all patients presenting with X also needed treatment for Y’). Be cautious about statements like this.

To understand what checks have to be made to outputs it is important to understand the **attribute types** that exist in data and how these could lead to **primary or secondary disclosure**. Importantly, OpenSAFELY requires that researchers redact any outputs based on counts <= 7 before they can be released.

!!! note
    Individual researchers who have Level 4 access have responsibility for redacting sensitive information, or choosing not to publish it at all. The study author should do everything they can to make this easy; for example, carrying out low number suppression automatically, documenting code clearly, and only selecting essential items for publication when deciding what to label as `moderately_sensitive`.

### Attribute types
Datasets made available for analysis may contain the following types of attributes:

*   **Direct identifiers** - attributes that definitively identify an individual. This includes information such as name, NHS number or hospital appointment reference. By design these attributes are not made available to OpenSAFELY as data shared into the OpenSAFELY platform is pseudonymised at source and then de-identified before being made available for analysis.
*   **Quasi-identifiers** - attributes that in themselves are not direct identifiers, but in combination may allow an individual to be identified; for example, age plus gender plus home address plus the date of a recent hospital visit (see [L. Sweeney, Simple Demographics Often Identify People Uniquely. Carnegie Mellon University, Data
Privacy Working Paper 3. Pittsburgh 2000](https://www.ccs.neu.edu/home/cbw/static/class/5750/papers/Sweeney.pdf) for more detail and examples). It is not possible to say what variables are quasi-identifiers outside of a specific context; ethnicity, number of children, GP surgery or other characteristics could be disclosive in some circumstances and not in others. Medical data provides a lot of variables that could be identifying, such as medical diagnoses and prescriptions. Hence, deciding the riskiness of an output requires judgement and an understanding of context.

### Primary vs secondary disclosure

Primary disclosure describes the situation where confidential data can be obtained **directly** from the data. An example of primary disclosure can be seen in the table below, where you can learn that only 1 member of the population who is aged 21-30 has heart disease.

|           | **Age band** | **Heart disease** | **Population** |
|-----------|--------------|-------------------|----------------|
|           | 21-30        | 1                 | 1              |
|           | 31-40        | 10                | 100            |
|           | 41-50        | 15                | 90             |
|           | 51+          | 25                | 85             |
| **Total** |              | 51                | 276            |

To prevent primary disclosure, you could choose to redact the value for this individual as done below.

Secondary disclosure is where an individual's attributes can be indirectly learned using other available information. An example of this is shown below, where the column totals can be used to deduce that there is only one individual in the 20-30 age band with heart disease, despite the fact this value was protected from primary disclosure by redacting the value.

|           | **Age band** | **Heart disease** | **Population** |
|-----------|--------------|-------------------|----------------|
|           | 21-30        | [REDACTED]        | [REDACTED]     |
|           | 31-40        | 10                | 100            |
|           | 41-50        | 15                | 90             |
|           | 51+          | 25                | 85             |
| **Total** |              | 51                | 276            |

Secondary disclosure can also occur across different tables involving the same population. In the below tables, showing a breakdown of heart disease by age band in the total population and in males alone, there are no disclosive small numbers. However, by differencing the values in the two tables, it can be inferred that there is only one female aged 20-30 who has heart disease.

| **Total Population** | **Age Band** | **Heart Disease** | **Population** |
|----------------------|--------------|-------------------|----------------|
|                      | 21-30        | 8                 | 20             |
|                      | 31-40        | 10                | 25             |
|                      | 41-50        | 15                | 30             |
|                      | 51+          | 25                | 40             |
| **Total**            |              | 58                | 115            |

| **Male Population** | **Age Band** | **Heart Disease** | **Population** |
|---------------------|--------------|-------------------|----------------|
|                     | 21-30        | 7                 | 19            |
|                     | 31-40        | 5                 | 15             |
|                     | 41-50        | 8                 | 18             |
|                     | 51+          | 13                | 25             |
| **Total**           |              | 33                | 64            |

When applying disclosure controls to your outputs, you should consider the potential for both primary and secondary disclosure.

### Redacting counts less than or equal to 7

Before requesting files to be released, work through the [moderately sensitive](actions-pipelines.md#accessing-outputs) files in the workspace folder systematically to identify any tables, figures, and other released text and objects that may be a disclosure risk.

The general principle is that **any statistic describing 7 or fewer patients, either directly or indirectly, should be redacted or combined into other statistics**. This includes:

*   Redacting counts <=7 in frequency tables. Row and column totals should be recalculated after you have redacted the cell values, to ensure that the redacted values can not be inferred from the totals.
*   Redacting summaries of numeric variables (eg mean values) describing 7 or fewer patients.
*   Redacting maximum or minimum values. These often relate to one or two individuals (eg ‘the oldest patient is 103’) and so should be avoided. In some cases the maximum and minima are informative about individuals (‘the target population was schoolchildren from 11 to 16’); these broad sample characteristics are okay.
*   Redacting graphical figures whose underlying values describe 7 or fewer patients. Figures which include print-outs of patient counts (such as Kaplan-Meier plots) should be checked and redacted. Underlying data for plots should be checked - do not rely upon ‘it’s too small to read’ as a justification for having low numbers. These underlying counts should be provided when requesting the release of any figures.

!!! note
    Our previous requirement was to redact counts <=5. When combined with rounding counts to the nearest 5, this led to occassions where counts of 5 could be inferred to be either 6 or 7. Redacting counts <=7 followed by rounding provides the same protection for all counts.

Below are some other principles to consider:

*   Counts of zero can be retained in general, but be aware that zero or 100% counts can be disclosive (‘none of the males aged 45-49 used condoms’; ‘THC was a detected in all premature births in the 17-18 age group’) and should be removed. This can be difficult, as these results are often the most valuable from a policy perspective, so be particularly cautious when reporting on these.
*   Analytical results, such as model coefficients, test statistics, or goodness-of-fit measures generally do not generally present any disclosure risk, as long as these are genuine analyses (eg standard deviation does not present a confidentiality risk, unless it is a standard deviation calculated from just two observations)
*   Other outputs, such as log files that reveal information about the underlying data, should also be checked and redacted if necessary. It is very unlikely that outputs such as log files should be required for publication outside the secure environment ([see below for more detail](#error-log-files)).
*   We recommend rounding of results that could be at risk of secondary disclosure. This is an alternative to redaction, or can be used in combination. However, be careful to round all your results to the same base number - see below.

Where possible it should be clear what has been redacted, so for example do not redact table titles and category names. By convention redactions take the form [REDACTED] to make redacted elements easier to search for.

If you find yourself redacting a lot of results, considering re-thinking the categories you are using. For example, suppose the category ‘age 95+’ is often needing to be redacted. Is there sufficient distinction between those age 90-94 and those aged 95+ to warrant the extra category? If not, then combine the category. You should always consider this option before deciding to redact individual cells. Focusing on the statistical value of the results can give better results (consistency across tables) compared to treating SDC as a table-by-table problem.

This current approach to disclosure control is conservative and deliberately reduces the need for judgement calls, as these simple rules can be applied by all and provide a good degree of protection. As noted above, good disclosure protection is generally consistent with good statistics. Exceptions can be made if they can be justified as being both materially important for the study conclusions (i.e. providing significant public benefit) and having a very low risk of disclosure. This must be discussed with the OpenSAFELY team. Moreover, these must be rare exceptions: ignoring these guidelines, or continually asking for ‘exceptions’ will not be tolerated.

If you are unsure about anything, please email us: [disclosurecontrol@opensafely.org](mailto:disclosurecontrol@opensafely.org).

!!! note
    Remember to also always check the [permitted study results policy](https://www.opensafely.org/policies-for-researchers/#permitted-study-results-policy) as it describes any additional rules regarding the release of data describing organisations and regions.

### Rounding counts

The redaction of any counts <=7 reduces the risk of primary disclosure, but it does not remove the risk of secondary disclosure. As there are many active projects using the OpenSAFELY platform and datasets, there is a risk that your results might be combined with other results to reveal information about individuals or groups. To reduce this risk, we ask that you **round any counts to the nearest 5**. This includes rounding counts underlying any figures requested for release. In most cases this is unlikely to have a significant impact on your results. If it does, please highlight why it is important to release non-rounded counts when making an output review request.

!!! note
    Rounding does not remove the need to redact counts <=7. You should first redact counts <=7 and then round to the nearest 5.

Below is an example of a table before (top) and after (bottom) rounding has been applied. **Note that column and row totals are the sum of the rounded counts.**

| **Total Population** | **Age Band** | **Heart Disease** | **Population** |
|----------------------|--------------|-------------------|----------------|
|                      | 21-30        | 3                 | 18             |
|                      | 31-40        | 8                 | 23             |
|                      | 41-50        | 16                | 31             |
|                      | 51+          | 23                | 44             |
| **Total**            |              | 50                | 116            |

| **Total Population** | **Age Band** | **Heart Disease** | **Population** |
|----------------------|--------------|-------------------|----------------|
|                      | 21-30        | [REDACTED]        | 20             |
|                      | 31-40        | 10                | 25             |
|                      | 41-50        | 15                | 30             |
|                      | 51+          | 25                | 45             |
| **Total**            |              | 50                | 120            |


### Rounding rates

A rate consists of a numerator and denominator, which are generally both counts. **In OpenSAFELY, any rate calculated from counts <=7 should also be redacted** (see the note above for why a threshold of 7 is used). In addition, we recommend rounding because redaction alone is vulnerable to differencing. When future calculations rely on rates not being mapped to a non-numerical like `[REDACTED]` and/or a distinction between a rate of zero and a non-zero rate is desirable, we recommend rounding the numerator and denominator to 'midpoint 6'. In short, rounding to 'midpoint 6' allows differentiating between zero and non-zero rates, by not breaking our suppression rules and without introducing bias.

#### Midpoint 6 rounding

By rounding to midpoint 6, we make sure that the numerator and denominator of our rate do not break our [suppression rules](#redacting-counts-less-than-or-equal-to-7). The method has desirable properties such as:

* It's unbiasedness
    * Rounding to _r_ is unbiased. For non-negative values (like counts), the binwidth is _r_ everywhere except for the lowest bin, where the binwidth is `ceiling(r/2)` (e.g. rounding to 6, the lowest bin is `[1, 2, 3] → 0`). Rounding to 6 is not sufficient to comply with our suppression rule of redacting counts of five or lower. We could instead round to the nearest 10, which means that `[1, 2, 3, 4, 5] → 0` (not breaking our suppression rule) but reducing precision and not preserving non-zero counts. Another alternative is to round to the nearest 6 and combine the two lowest bins such that `[1, 2, 3, 4, 5, 6, 7, 8] → 6` (not breaking our suppression rule and preserving zero-is-zero) but introducing bias. Alternatively, we could round up using a ceiling function such that `[1, 2, 3, 4, 5, 6] → 6` and `[7, 8, 9, 10, 11, 12] → 12` etc. (not breaking our suppression rule and preserving zero-is-zero) but introducing bias since the mean of the rounded numbers is higher than the mean of the true numbers by 3 (in general, by _r/2_ for rounding up to ceiling _r_). Rounding to midpoint 6 fixes the bias in the last option by deducting to _r/2_, preserving zero-is-zero and the rounded numbers are unbiased.
* Zero-are-zero’s
* For non-zero rounded values of `x`, we know true values range between `x-2` and `x+3`

!!! note
     **Our recommendation of rounding to midpoint 6 is restricted to situations where these properties (zero-is-zero, unbiasedness and redaction to numericals) are important, for example for Kaplan-Meier estimates from life-tables or similar rates.**


The following `R` function gives an example of how midpoint 6 rounding can be applied:
```
roundmid_any <- function(x, to=6){
  # like round_any, but centers on (integer) midpoint of the rounding points
  ceiling(x/to)*to - (floor(to/2)*(x!=0))
}
```

Which results in the following mapping:

| **Range of true value** | **Value rounded to midpoint 6** |
|-------------------------|---------------------------------|
| 0                       | 0                               |
| 1-6                     | 3                               |
| 7-12                    | 9                               |
| 13-18                   | 15                              |
| ...                     | ...                             |

#### Naming convention for midpoint 6 rounding

Please note that the numbers between 1-6 are mapped to ‘3’, which is lower than 5 (our redaction threshold). This ‘3’ is not a true 3 and is only a label for all numbers ranging between 1 and 6. A ‘3’ as a result from using midpoint 6 rounding therefore follows our suppression rules. However, without appropriate context, this may not be obvious to anyone viewing the output (including output checkers). **For any outputs that use midpoint rounding, we therefore suggest adding the suffix `_midpoint6` to your column name. Similarly, we suggest adding the suffix `_midpoint6_derived` to values that are derived from the midpoint 6 rounded values and take values of 6, 12, 18,... (for example in life-tables).** Alongside this naming convention, we ask people to explicitly point to sections of the code where midpoint rounding was applied.


### Extended principles

Below are a couple of examples of common secondary disclosure issues encountered when using OpenSAFELY.

**Repeated analyses**
When producing repeated reports at different time points, it is possible that there can be a small change in the number of people in your analysis. E.g. “number of people with condition X receiving treatment Y” increases from N to N+1). Although this is not typically likely to be disclosive, it may carry a small risk on some occasions (e.g. an individual/GP may be able to identify themselves/their patient or believe that that can do so) and therefore should be routinely avoided to minimise burden on output checking.

The solution for this is to use rounding across the entire report (to the nearest 5, 7, or 10). Rounding eliminates the need for output checkers to compare different versions of the report outputs, as no small increases can occur. It is not likely that rounding will significantly affect the report in any meaningful way. Statistical analyses can be carried out prior to rounding and the results displayed as normal provided they are classed as low risk. If only charts are shown, rounding is not always necessary, but charts should have sufficiently low resolution that any small number changes cannot be precisely determined. However, numbers could be rounded nonetheless, as this would not noticeably affect the figures.

**Running similar studies**
There may be cases where you have run an analysis and results have been released following approval from the output checking team, but at a later date you decide you want to make changes to the analysis such as adding an extra code to a codelist. This may result in small changes in the outputs that can be disclosive, ie, <=7 individuals have the new code recorded. In these cases, you may need to wait until there has been enough change in the underlying study population (due to the movement of patients between practices) before rerunning the study.

If you are likely to release data multiple times, e.g. for initial discussion with collaborators, use rounding of outputs initially and/or a threshold substantially higher than 5 for suppressing low numbers.

### Further reading

There are several existing sets of SDC guidelines covering a range of output type specific considerations including:

* [Handbook on Statistical Disclosure Control for Outputs](https://securedatagroup.files.wordpress.com/2019/10/sdc-handbook-v1.0.pdf) - This is a useful reference manual which includes SDC considerations for common research outputs types.
* [Microdata output guide StatsNZ](https://web.archive.org/web/20220203084913/https://www.stats.govt.nz/assets/Methods/Microdata-Output-Guide-2020-v5-1.pdf) - This is another useful reference document with output rules for diferent output types.
* [ESSNet SDC guidelines for the checking of output based on microdata research](https://research.cbs.nl/casc/ESSnet/GuidelinesForOutputChecking_Dec2009.pdf) - This gives a narrative introduction on the approaches to checking research outputs, as well as a set of rules for common output types.


There are also resources for extended guidance for analysis methods commonly used in OpenSAFELY:

* Regression outputs:
    [Ritchie, Felix. Output-based disclosure control for regressions” (2012).](https://www2.uwe.ac.uk/faculties/BBS/BUS/Research/economics2012/1209.pdf)
* Survival analysis:
    [O’Keefe, C. M., Sparks, R. S., McAullay, D. & Loong, B. Confidentialising Survival Analysis Output in a Remote Data Access System. J. Priv. Confidentiality 4, (2012)](https://journalprivacyconfidentiality.org/index.php/jpc/article/view/614)

There is also a disclosure control section in our [Q&A forum](https://github.com/opensafely/documentation/discussions/categories/disclosure-control) where you can ask any questions you may have.

## 2. Requesting release of outputs and (error) log files from the server


**Only specific members of the OpenSAFELY team trained in output checking have permissions to release the data**. Having applied disclosure controls to your aggregated study data you are ready to request their release. Please read the instructions and [checklist](#checklist) below.

First, create one folder in your workspace called `release` (if you have previously made a release, we suggest appending the date to the new folder name to distinguish it) and copy from your `output` folder to this `release` folder the data files that require review. The number of study outputs requested for review must be kept to a minimum and include only the results you absolutely need to export from the secure server.

When you are ready to request a release of your aggregated results please [complete this form](/documents/OpenSAFELY_Output_Review_Form_ADD_WORKSPACE_NAME_ADD_DATE.docx), renaming the form to replace the placeholders with your workspace name and the date.

!!! note
    Each data release entails substantial review work. To retain rapid turnaround times, external data releases should typically only be of results for final submission to a journal or public notebook; or a small number of necessary releases for discussion with external collaborators.

For each output wishing to be released you will need to provide a clear contextual description including:

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

* **Tables** - Tables should be produced as either `csv` or `tsv` files.
    * Make sure that any column names are understandable for reviewers.
    * Limit the number of columns or rows to only what is necessary.
* **Figures** - Figures can be produced as bitmap images (`jpeg` or `png`) or vector graphics (`svg`).
    * Underlying data for all figures should be provided for review (even if it is not being released).
    * Consider requesting release of the underlying data if you think you will need to make stylistic changes to the figures so that you don't need to request multiple reviews.
    * If you are producing a lot of figures, consider combining them into panel plots or requesting release of the underlying data so that you can produce them outside of the secure server.
* **Other**
    * `txt` files can be released, but you should consider whether the output can be produced as a table, which is easier to review.
    * `json` files can be released, but as with tables, make sure that the attributes are easily understandable for reviewers. If the output can be represented as a table, you should consider converting it.
    * `html` files can be released if you are producing a report style output that is intended to be hosted on [reports.opensafely.org](https://reports.opensafely.org/) but please note the points below:
        * `html` files are harder to review than other output types, so should be reserved for reports which require both contextual text and embedded outputs. If you can produce your report locally, using individually released files, you should.
        * Make sure that any code blocks are not rendered in the rendered report if they are not needed. You can find [examples showing how to do this for Jupyter notebooks and R markdown files](reports/intro.md#producing-reports).
        * Each individual output within the report should be requested for release separately, with the contextual information outlined above.
        * `html` files should be stripped of any embedded javascript and styling. This is obfuscated when viewing a report via a web browser, but makes review of the raw file very difficult. Refer to our instructions [explaining how to strip the `html` files](reports/intro.md#producing-reports).
        * When making a review request that includes `html` files, please include a link to the code you have used to produce the reports.

If you would like to release other file types, please email <datarelease@opensafely.org>, stating why it is important that the file is released in a different format.

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

Following this checklist will make your outputs easier to check, speed up review time and avoid the outputs having to be rechecked.

### Submittting the form

Once you have completed this form, please send it to **<datarelease@opensafely.org>**. the requested outputs will undergo independent review by two OpenSAFELY output checkers who will check that the outputs are within the scope of your original project proposal and that they do not present any disclosure risks. **Please allow up to 1 week for feedback on your request**.

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

Once reviewed, the completed review request will be emailed back to you. If all outputs are approved, they will then be released. If one or more outputs are approved subject to change, you will need to address the disclosure issues and submit a new review form detailing the changes you have made.
## 4. Release of reviewed files

All approved OpenSAFELY outputs are released to the workspace they belong to on the [Jobs site](jobs-site.md).

### Viewing released outputs

View your released outputs by navigating to "Released Outputs" in the "Releases" section of your workspace on the Jobs site.

These outputs can be shared with project collaborators and published in line with our [data sharing and publication policy](https://www.opensafely.org/policies-for-researchers/#acknowledgment-and-data-sharing--publication-policy). Please note that you should check this for each dataset that you have used: rules may vary.

!!! warning
    You **MUST NOT** share any results that have not been released through the official output checking process. This includes:

    - verbal sharing
    - allowing someone to look over your shoulder
    - transcribing (e.g., to paper or email)
    - using screen sharing software or any recording device/software

### Running further analyses on released outputs

If you have had [intermediate data released](#release-of-intermediate-data) and you wish to run further analyses on them, such as reformatting figures, there are a few things to consider.

1. You should include the code for these steps in your GitHub repo.
2. You **should not** commit any of the released outputs (including final processed charts/tables) to your GitHub repo. Make sure to include them in the `.gitignore` file.
3. Consider adding the code as an action in your project pipeline.

### Reporting a data breach

If you discover files released to the Jobs site that have been insufficiently redacted and still contain sensitive information, you should immediately contact and email the following (providing as much information as possible): Amir Mehrkar (<amir.mehrkar@phc.ox.ac.uk>); Ben Goldacre (<ben.goldacre@phc.ox.ac.uk>); [disclosurecontrol@opensafely.org](mailto:disclosurecontrol@opensafely.org); and your co-pilot. Ensure you do not share these files and if they have already been shared please identify as best as possible with whom they have been shared.


---8<-- 'includes/glossary.md'
