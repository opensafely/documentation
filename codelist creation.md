# Codelist creation guidance in OpenSAFELY

For transparency, replicability, and reproducibility, all codelists used in OpenSAFELY research projects should be taken from a specific dated version of a codelist recorded in [codelists.opensafely.org](https://codelists.opensafely.org). 

This document is intended for OpenSAFELY users who want to understand how create and upload codelists to [codelists.opensafely.org](https://codelists.opensafely.org).

## Workflow

The general workflow for creating codelists is as follows:

1. Search [codelists.opensafely.org](https://codelists.opensafely.org) for codelists that meet or nearly meet your requirements and make sure that one doesn't already exist
2. Create a new issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)
3. Use the issue to discuss and agree the final codelist
4. Once agreed, obtain sign-off
5. Add the codelist to [codelists.opensafely.org](https://codelists.opensafely.org)
6. Close the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)
7. Import the codelist for use in your study definition



## Create a new issue on the [codelist-development repo](https://github.com/opensafely/codelist-development)

The issue title should start with either: 

* \*PATIENT\* -- non-clinical patient information (demographic, social, etc)
* \*CONDITION\* -- specific clinical conditions / disorders / findings / symptoms
* \*DISEASE\* -- specific diseases
* \*MEDICINE\* -- medicines, treatments, prescriptions, interventions
* another codelist classification if relevant. 

<!--are these appropriate classifications? disease versus condition is a notoriously poorly-understood distinction. what about symptoms, disorders, etc. does it matter?</font>-->

The rest of the title should be short and informative. 

## Discuss and document and review

Discuss and document each decision clearly and comprehensively in the issue. Explain why codes have been included and why codes have been excluded. Link to relevant webpages and documents. Upload files. Involve domain experts. Iterate.

The current coding systems available in opencodelists are listed below. 

| Coding system  | CSV column name |
| ---- | ---- |
| [Pseudo BNF](https://ebmdatalab.net/prescribing-data-bnf-codes/)  | `BNFCode`  |
| CTV3 (Read v3)  | `CTV3Code`  |
| CTV3 (Read v3) with TPP extensions  | `CTV3Code`  |
| [Dictionary of Medicines and Devises (dm+d)](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/)  | `DMDCode`  |
| International Classification of Diseases 10 (ICD-10)  | `ICD10Code`  |
| Read v2  | `Read2Code`  |
| SNOMED CT  | `SNOMEDCode`  |


Each codelist must use exactly one of these systems. 

The final codelist must be stored in CSV format to be imported into [codelists.opensafely.org](https://codelists.opensafely.org). The codes must be stored in exactly one column. You can include other columns (such as code descriptions) if useful. There is currently a soft requirement that the codes should be contained in the first column, which should be named as per the list above. For example, if using CTV3 then the column header should be `CTV3Code`. 

## Sign-off

Once a draft codelist has been agreed, it must be signed-off by a "data expert" (epidemiological sign-off) and "disease expert" (clinical sign-off) from at least two different people. 


## Add to [codelists.opensafely.org](https://codelists.opensafely.org)

* Go to the openSAFELY [new codelist page](https://codelists.opensafely.org/codelist/opensafely/). You will need an editor account.
* Fill in the fields. Include lots of detail (specific guidance to follow).
	* **CSV data**: _DO NOT_ copy the data from within spreadsheet software such as Excel (this can reformat or revalue cells, for example with very long numeric codes that are interpreted as integers). Instead, open the CSV file in a text editor such as notepad and copy the raw text data.
	* **References**: this should include a link to the issue on the [codelist-development repo](https://github.com/opensafely/codelist-development), and any other relevant materials.
* Click Submit and check the new codelist has appeared on the main site.

## Close the issue in the repo

Go to the codelist issue in the [codelist repo](https://github.com/opensafely/codelist-development) and close it. This issue serves as documentation of the choices made that determined the final codelist. The issue can be re-opened if revisions are required.

## Import the codelist for use in your study definition

Once the codelist is in [codelists.opensafely.org](https://codelists.opensafely.org), you can retrieve it for use in your research repo. Follow [these instructions](https://github.com/opensafely/documentation/blob/new-onboarding/Onboarding%20analysts.md#add-the-relevant-codelist-and-commit) if you're not sure how to do this.

## Codelist contributorship

How contributions to codelists are acknowledged -- to be agreed.

## Editing existing codelists

CUrrently undocumented.
