The ICNARC-CMP  dataset contains information on covid-related intensive care admissions in England.

!!! warning
    Data from ICNARC were last imported on 21-Jan-2021, with no further imports currently planned. Alternative data on ICU admission can be gleaned from SUS (i.e. returning=days_in_critical_care).

From ICNARC's website:

> The Case Mix Programme (CMP) is an audit of patient outcomes from adult, general critical care units (intensive care and combined intensive care/high dependency units) covering England, Wales and Northern Ireland.
> The CMP is listed in the Department of Health's 'Quality Accounts' as a recognised national audit by the National Advisory Group on Clinical Audit & Enquiries (NAGCAE) for 'Acute' care.

Currently only Covid-19 positive patients are provided by ICNARC.

## Metadata

* **Data provider** ICNARC
* **Participation / Coverage** Adult ICU/HDUs admissions in England, Wales, NI.
Specialist units (eg neuro / cardiac) also participate. covid-19 admissions only
* **Provenance** ICUs and HDUs
* **Update frequency in OpenSAFELY** Approximately weekly.
* **Delay between event occurring and event appearing in OpenSAFELY** Approximately 1-2 weeks.
* **Collected information** Admission, discharge and transfer dates; reason for admission; clinical support/interventions; clinical findings

## More Information

[CMP resources]( https://www.icnarc.org/Our-Audit/Audits/Cmp/Resources) &mdash; this is comprehensive, and includes links to the data dictionary, CRF, data flows, and other useful resources.

## Datasource-specific glossary

* **Advanced respiratory support** unclear, possibly non-intubated ventilation
* **Basic respiratory support** unclear, possibly intubated ventilation
* **Admission** these include _any_ admission to ICU even if the patient did not require critical care, for example due to bed pressures elsewhere in the hospital.
It may be useful to filter by severity, e.g., ventilated patients only.
Similarly, potentially critically ill patients cared-for by ICU staff but who are admitted to a different unit will not be included in the CMP.
Each admission is a row, so patients transferred to other units will appear in the dataset multiple times, even if it’s part of the same spell.


---8<-- 'includes/glossary.md'
