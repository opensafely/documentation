## Workflow

The general workflow for creating codelists is as follows:

1. Search [codelists.opensafely.org](https://codelists.opensafely.org) for codelists that meet or nearly meet your requirements and make sure that one doesn't already exist
1. If you need to build a new codelist [sign up for an account on codelists.opensafely](https://codelists.opensafely.org/accounts/register/)
1. Create a new issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)
1. Decide your key terms to search for codes. Good source of key words might be a previous codelist, clinicians or experts in the field and
previous research papers
1. When logged into [Codelist Builder](https://codelists.opensafely.org/accounts/login/)  click "my codelists" and then "create new codelist"
1. Add/remove terms to your codelists to end up with a list. 
1. Save the list as a draft and share the link to your the Github issue. 
1. Discuss as a group in the issue your decisions, and the reason for including or excluding different codes. Finalise a list
as a group (i.e. at least 2). Detailed reasons are helpful in this issue for referencing in the future. 
1. Once agreed, obtain sign-off
1. Clicking "Save changes" makes the codelist available on [codelists.opensafely.org](https://codelists.opensafely.org). Summarise your discussion briefly for the metadata, 
and reference the issue on the website for more details.  This will initially be a draft. When ready, publish it. 
1. Close the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)
1. Import the codelist for use in your study definition

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

The current coding systems available in opencodelists are listed below. 

| Coding system  | CSV column name |
| ---- | ---- |
| [Pseudo BNF](https://ebmdatalab.net/prescribing-data-bnf-codes/)  | `BNFCode`  |
| CTV3 (Read v3)  | `CTV3Code`  |
| CTV3 (Read v3) with TPP extensions  | `CTV3Code`  |
| [Dictionary of Medicines and Devices (dm+d)](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/)  | `DMDCode`  |
| International Classification of Diseases 10 (ICD-10)  | `ICD10Code`  |
| Read v2  | `Read2Code`  |
| SNOMED CT  | `SNOMEDCode`  |


Each codelist must use exactly one of these systems. 

The final codelist must be stored in CSV format to be imported 
into [codelists.opensafely.org](https://codelists.opensafely.org). The codes must be stored in exactly one column. 
You can include other columns (such as code descriptions) if useful. There is currently a soft requirement that the 
codes should be contained in the first column, which should be named as per the list above. For example, if using 
CTV3 then the column header should be `CTV3Code`. Do not keep the original codelist in Excel and then filter by a include or exclude
column as this will be lost when converted to CSV, and you will end up with all the codes again. 

## Sign-off

Once a draft codelist has been agreed, it must be signed-off by a "data expert" (epidemiological sign-off) and 
"disease expert" (clinical sign-off) from at least two different people. 


## Add to [codelists.opensafely.org](https://codelists.opensafely.org)

* Go to the openSAFELY [new codelist page](https://codelists.opensafely.org/codelist/opensafely/). 
You will need an editor account. Ask one of the tech team for one if you do not have one.
* Fill in the fields. Include lots of detail (specific guidance to follow).
	* **CSV data**: [Export your Spreadsheet to a CSV](https://github.com/opensafely/documentation/blob/master/codelist%20creation.md#exporting-a-csv-from-a-spreadsheet) and choose that file.
	* **References**: this should include a link to the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development), and any other relevant materials.
	* **Sign Off**: This should match the people signing off on the issue. You need at least 2 people and can have many more. 
* Click Submit and check the new codelist has appeared on the main site.


## Exporting a CSV from a Spreadsheet
* In Excel go to File
* Click Export in the left-hand ribbon menu
* Select Change File Type
* Click CSV (Comma delimited) (\*.csv)

![](https://user-images.githubusercontent.com/40460354/90112253-a7737680-dd47-11ea-8271-a43b37a65bd5.png)


## Close the issue in the repo

Go to the codelist issue in the [codelist repo](https://github.com/opensafely/codelist-development) and close it. 
This issue serves as documentation of the choices made that determined the final codelist. The issue can be 
re-opened if revisions are required.

## Import the codelist for use in your study definition

Once the codelist is in [codelists.opensafely.org](https://codelists.opensafely.org), you can retrieve it for use in 
your research repo. Follow [these instructions](https://github.com/opensafely/documentation/blob/master/Onboarding%20analysts.md#add-the-relevant-codelist-and-commit) if you're not sure how to do this.

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
	* This will show you the latest version for a Codelist
* If it's a draft version there will be a Publish version button on the left below Create new version.
* If not, it's already published, good job!


## Adding a Codelist Version

* Go to an existing Codelist page.
* Click Create new version
* If you want to update the existing version, click Update version instead.


---8<-- 'includes/glossary.md'
