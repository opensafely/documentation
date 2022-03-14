The Therapeutics dataset contains information on COVID treatments used in inpatient and outpatient settings. 

## Metadata

* **Data provider** NHS England 
* **Participation / Coverage** Inpatients and outpatients treated with antivirals/nMABs for COVID-19 in England
* **Provenance** Data sourced largely from BlueTeq system (forms completed by clinicians)
* **Update frequency in OpenSAFELY** Approximately weekly
* **Delay between event occurring and event appearing in OpenSAFELY** Approximately 2-9 days
* **Collected information** Treatment start date; therapeutic intervention; COVID indication, current status, risk group, region
 

## Overview
Antivirals and neutralising monoclonal antibodies (nMABs) for COVID-19 can be administered in inpatient setting or, for outpatients, in COVID Medicine Delivery Units (CMDUs) specifically set up for this purpose. For patients considered for these treatments, clinicians submit completed forms to NHS England. Each row represents one completed form for one course of treatment. Data received by OpenSAFELY currently covers patients who were approved for treatment. The patient may or may not have actually received the treatment or completed the course (but we assume that they usually do). They may have another form completed for another treatment, either because it was decided to give them a different treatment, or for some other reason. They may in theory also have another form completed some months later for another instance of infection.

Treatment dates may be in the past or future at the point when the form is submitted. 


## More Information

* [Treatment guidelines (non-hospitalised patients)](https://www.england.nhs.uk/coronavirus/publication/interim-clinical-commissioning-policy-neutralising-monoclonal-antibodies-or-antivirals-for-non-hospitalised-patients-with-covid-19/)
* [Treatment guidelines (hospitalised patients)](https://www.england.nhs.uk/coronavirus/publication/neutralising-monoclonal-antibodies-and-intravenous-antivirals-in-the-treatment-of-covid-19-in-hospitalised-patients/)

## Datasource-specific glossary

* **date**: From `TreatmentStartDate`. This is entered by the clinician completing the form and may be in the past, future or the same date on which the form is submitted.
* **therapeutic**: Name of treatment(s) given. When used as a `returning` option, is a comma-separated string from `Intervention` (removing " and "). 
* **region**: The region is one of seven NHS regions, derived from the NHS Trust/site from which the form was submitted.
* **risk group**: This is present for outpatients only. Derived from tick boxes on the form for Molnupiravir, Sotrovimab and Casivirimab combined into one comma-separated string. May return duplicates to be resolved e.g. "cancer,cancer". Can be missing (if clinician selected "Other" and supplied risk group as free text). Risk groups are only returned if they match a defined set of available values (listed [here](https://github.com/opensafely-core/cohort-extractor/blob/main/cohortextractor/therapeutics_utils.py#L23).
* **with_these_therapeutics**: As `therapeutic` above. Filters on `Intervention`. Case insensitive. Currently available options: 'remdesivir', 'tocilizumab', 'sarilumab', 'casirivimab and imdevimab', 'molnupiravir', 'sotrovimab', 'paxlovid'.
* **with_these_statuses**: Filters on `CurrentStatus`. Should be one or more of 'Approved', 'Treatment Complete', 'Treatment Not Started', 'Treatment Stopped'. 
Case insensitive.
* **with_these_indications**: Filters on COVID_indication. Should be one or more of 'non-hospitalised', 'hospital_onset', 'hospitalised_with'. 


---8<-- 'includes/glossary.md'
