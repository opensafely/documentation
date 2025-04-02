!!! note
    This page describes the process used for requesting release of file prior to
    Airlock. New release requests should be made using [Airlock](../using-opensafely/viewing-and-releasing-outputs/viewing-and-releasing-with-airlock/index.md) wherever possible.


### Create a folder for outputs

First, create one folder in your workspace called `release` (if you have previously made a release, we suggest appending the date to the new folder name to distinguish it) and copy from your `output` folder to this `release` folder the data files that require review. The number of study outputs requested for review must be kept to a minimum and include only the results you absolutely need to export from the secure server.

### Complete a output review request form

When you are ready to request a release of your aggregated results please [complete this form](../documents/OpenSAFELY_Output_Review_Form_ADD_WORKSPACE_NAME_ADD_DATE.docx), renaming the form to replace the placeholders with your workspace name and the date.

#### Context requirements

For each output wishing to be released you will need to provide a clear contextual description including:

1. The file path for each output
2. Variable descriptions
3. A description and count of the underlying sample of the population for each output.
4. Population size and degrees of freedom for all regression outputs.
5. Relationship to other data/tables which through combination may introduce secondary disclosive risks.

Each section in the review request form should normally describe a single file, but where necessary for similar files, these can be grouped together and wildcards can be used for the file path (e.g. `release/hospitalisation_rate_by_*.csv`). **If you use a wildcard, please indicate how many files this captures**.

### Checklist

Please run through [the checklist](../outputs/requesting-file-release.md#checklist) before making a review request. In addition, check:

1. Are all of the outputs in a [separate release folder](#create-a-folder-for-outputs)?
1. Are all of the outputs clearly described?
    * Is the filename sensible and is the filepath provided in the request form correct?
    * Have you provided all of the context needed to review each output in isolation in the request form?
    * Have you described the disclosure controls you have applied to each output?

### Submitting the form

Once you have completed this form, please send it to **<datarelease@opensafely.org>**. The requested outputs will undergo independent review by two OpenSAFELY output checkers who will check that the outputs are within the scope of your original project proposal and that they do not present any disclosure risks. **Please allow up to 5 working days for feedback on your request**.


### Responding to requests

Once reviewed, the completed review request will be emailed back to you. We aim to provide a response to review requests within **5 working days**. If all outputs are approved, they will then be released. If one or more outputs are approved subject to change, you will need to address the disclosure issues and submit a new review form detailing the changes you have made.
