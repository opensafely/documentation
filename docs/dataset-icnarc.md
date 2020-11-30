The ICNARC-CMP  dataset contains information on covid-related intensive care admissions in England. 
From ICNARC's (Intensive Care National Audit and Research Centre) website: _The Case Mix Programme (CMP) is an audit of patient outcomes from adult, general critical care units (intensive care and combined intensive care/high dependency units) covering England, Wales and Northern Ireland._
_The CMP is listed in the Department of Health's 'Quality Accounts' as a recognised national audit by the National Advisory Group on Clinical Audit & Enquiries (NAGCAE) for 'Acute' care._

Currently only Covid-19 positive patients are provided by ICNARC. 

## Metadata

**Data provider** ICNARC

**Participation / Coverage** Adult ICU/HDUs admissions in England, Wales, NI. 
Specialist units (eg neuro / cardiac) also participate. covid-19 admissions only

**Provenance** ICUs and HDUs

**Update frequency in OpenSAFELY** Approximately weekly.

**Delay between event occurring and event appearing in OpenSAFELY** Approximately 1-2 weeks.

**Collected information** Admission, discharge and transfer dates; reason for admission; clinical support/interventions; clinical findings

## More Information

[CMP resources]( https://www.icnarc.org/Our-Audit/Audits/Cmp/Resources) &mdash; this is comprehensive, and includes links to the data dictionary, CRF, data flows, and other useful resources.

## Glossary

* **Advanced respiratory support** unclear, possibly non-intubated ventilation
* **Basic respiratory support** unclear, possibly intubated ventilation
* **Admission** these include _any_ admission to ICU even if the patient did not require critical care, for example due to bed pressures elsewhere in the hospital. 
It may be useful to filter by severity, e.g., ventilated patients only. 
Similarly, potentially critically ill patients cared-for by ICU staff but who are admitted to a different unit will not be included in the CMP. 
Each admission is a row, so patients transferred to other units will appear in the dataset multiple times, even if it’s part of the same spell. 
