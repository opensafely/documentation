There are two ways to build a codelist using OpenCodelists:

1. [Create a codelist from scratch with the builder](https://www.opencodelists.org/docs/#creating-a-codelist-from-scratch)
2. [Create a codelist from a csv file](https://www.opencodelists.org/docs/#creating-a-codelist-from-a-csv-file)


The current coding systems available in the OpenCodelists builder are listed below.

| Coding system  | CSV column name |
| ---- | ---- |
| [Pseudo BNF](https://www.bennett.ox.ac.uk/blog/2017/04/prescribing-data-bnf-codes/)  | `BNFCode`  |
| CTV3 (Read v3)  | `CTV3Code`  |
| CTV3 (Read v3) with TPP extensions  | `CTV3Code`  |
| [Dictionary of Medicines and Devices (dm+d)](https://www.bennett.ox.ac.uk/blog/2019/08/what-is-the-dm-d-the-nhs-dictionary-of-medicines-and-devices/)  | `DMDCode`  |
| International Classification of Diseases 10 (ICD-10)  | `ICD10Code`  |
| Read v2  | `Read2Code`  |
| SNOMED CT  | `SNOMEDCode`  |


Each codelist must use exactly one of these systems.

OPCS-4 codes are not currently supported by the OpenCodelists builder as we do not currently have the full list of available OPCS-4 codes. However, you can find instructions to manually upload an existing OPCS-4 codelist [here](https://www.opencodelists.org/docs/#creating-a-codelist-from-a-csv-file).
## Workflow

The general workflow for creating codelists is as follows:

1. Search [OpenCodelists](https://www.opencodelists.org) for codelists that meet or nearly meet your requirements and make sure that one doesn't already exist.
1. If you need to build a new codelist [sign up for an account on OpenCodelists](https://www.opencodelists.org/accounts/register/).
1. Create a new issue on the [codelist-development repo](https://github.com/opensafely/codelist-development).
1. Decide your key terms to search for codes. Good source of key words might be a previous codelist, clinicians or experts in the field and
previous research papers.
1. When logged into [OpenCodelists](https://www.opencodelists.org/accounts/login/)  click "my codelists" and then "create new codelist". There is a short video at the [bottom of this page](#medvid) on how to use the builder to develop a medication codelist.
1. Add/remove terms to your codelists to end up with a list.
1. Save the list as a draft.
1. Clicking "Save changes" makes the codelist available on codelists.opensafely.org as a draft. Share this link to the GitHub issue.
1. Discuss as a group in the issue your decisions, and the reason for including or excluding different codes. Finalise a list
as a group (i.e. at least 2). Detailed reasons are helpful in this issue for referencing in the future.
1. Once agreed, obtain sign-off.
1. Summarise your discussion and methodology briefly for the metadata, and reference the issue on the website for more details.  This will initially be a draft. When ready, publish it.
1. Close the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development).
1. Import the codelist for use in your study definition.

## Create a new issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)

The issue title should start with either:

* \*PATIENT\* -- non-clinical patient information (demographic, social, etc)
* \*CONDITION\* -- specific clinical conditions / disorders / findings / symptoms
* \*DISEASE\* -- specific diseases
* \*MEDICINE\* -- medicines, treatments, prescriptions, interventions
* another codelist classification if relevant.

<!--are these appropriate classifications? disease versus condition is a notoriously poorly-understood distinction. 
what about symptoms, disorders, etc. does it matter?</font>-->

The rest of the title should be short and informative.

## Discuss and document and review

Discuss and document each decision clearly and comprehensively in the issue. Explain why codes have been included and 
why codes have been excluded. Link to relevant webpages and documents. Upload files. Involve domain experts. Iterate.


## Sign-off

Once a draft codelist has been agreed, we recommend it should be signed-off by at least two different people. 
(These can include the person who led on creating the codelist). This should usually include a "data expert" (epidemiological sign-off) and 
"disease expert" (clinical sign-off). 


## Add to [OpenCodelists](https://www.opencodelists.org)

* Go to the OpenCodelists [new codelist page](https://www.opencodelists.org/codelist/opensafely/).
You will need an editor account. Ask one of the tech team for one if you do not have one.
* Fill in the fields. Include lots of detail (specific guidance to follow).
    * **CSV data**: [Export your Spreadsheet to a CSV](#exporting-a-csv-from-a-spreadsheet) and choose that file.
    * **References**: this should include a link to the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development), and any other relevant materials.
    * **Sign Off**: This should match the people signing off on the issue. You need at least 2 people and can have many more.
* Click Submit and check the new codelist has appeared on the main site.


## Exporting a CSV from a Spreadsheet
* In Excel go to File
* Click Export in the left-hand ribbon menu
* Select Change File Type
* Click CSV (Comma delimited) (\*.csv)

![Exporting a CSV from a spreadsheet in Microsoft Excel.](images/excel-export-csv.png)


## Close the issue in the repo

Go to the codelist issue in the [codelist repo](https://github.com/opensafely/codelist-development) and close it. 
This issue serves as documentation of the choices made that determined the final codelist. The issue can be 
re-opened if revisions are required.

## Import the codelist for use in your study definition

Once the codelist is in [OpenCodelists](https://www.opencodelists.org), you can retrieve it for use in 
your research repo. Follow the [adding codelists to project instructions](codelist-project.md) if you're not sure how to do this.

## Codelist contributorship

How contributions to codelists are acknowledged -- to be agreed.

## Editing existing codelists

* Go to an existing Codelist page.
* Click Edit metadata.
* Edit the relevant fields
    * Note: Changing the CSV data requires you Update the current Version or Create a new Version, both can be done from the Codelist page.
    * Add, remove, or edit the References and SignOffs as needed.
* Click Submit

## Publishing a Codelist Version

* Go to an existing Codelist page.
    * This will show you the latest version for a Codelist.
* If it's a draft version there will be a Publish version button on the left below Create new version.
* If not, it's already published, good job!


## Adding a Codelist Version

* Go to an existing Codelist page.
* Click Create new version.
* If you want to update the existing version, click Update version instead.

## <a name="medvid"></a>Build a simple medication codelist

This is a short video showing how to build a pseudoBNF medication codelist. For OpenSAFELY studies you can convert this
to NHS Dictionary of Medicines and Devices codelist which we briefly mention at the end of the video. 

Very briefly, we recommend that you build and agree medication codelists using the pseudoBNF coding system and convert this to
dm+d for use in study definitions. You can read more about the uses and differences between pseudoBNF, dm+d and SNOMED CT
on [our blog](https://www.bennett.ox.ac.uk/blog/2022/11/difference-between-bnf-dm-d-and-snomed-ct-codes/).

<div class="video-wrapper">
  <iframe width="1280" height="720" src="https://www.youtube.com/embed/t-A2kWHZ5lA" frameborder="0" allowfullscreen></iframe>
</div>



---8<-- 'includes/glossary.md'
