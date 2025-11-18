The OpenSAFELY platform is highly secure.
The data available follows a tiered structure of data of four different levels, each of which is permissioned separately.
Each stage is generated from the preceding stage &mdash; at each step, data privacy is increased through the removal of potentially identifiable data.

## Level 1 [GPs are data controllers of the data]
This is the most restrictive level and includes the complete, raw, fully-identifiable, event-level patient data.
EHR vendor data engineers store data at an identifiable level as part of their business-as-usual; they are instructed to process this data by the GPs (who are in routine practice the data controllers) in order to manage and store this information.

This identifiable data is further processed by the EHR vendor to create a database of pseudonymised coded event-level GP data which the OpenSAFELY service can access to run study queries against. The pseudonymised GP data can be refreshed at regular intervals, for example, it is currently refreshed weekly by TPP.

### Where is this data held?
Data is held within the EHR vendor's secure environment.

### Who has access?
Only data processor staff working for the EHR vendor (as well as approved GP practice staff) have access to the identifiable GP data for the purposes of direct patient care.

A small and restricted number of OpenSAFELY platform developers at the University of Oxford (under contract with NHS England) can also access the pseudonymised GP data for system integration activities. No additional direct access to the pseudonymised GP is available to any other individuals, or OpenSAFELY researchers.

Researchers can query this pseudonymised GP data, but only indirectly: they write their study analysis code away from the source data, in GitHub, and the OpenSAFELY service automates the execution of the study code against the GP data. Only the aggregated results of their study are made available back to the researchers in Level 4 (see below).

### Example

| NHS number | Name | DoB | Event | Date | Practice |
| --- | --- | --- | --- | --- | --- |
| 979384758 | Seb Colbert | 12/3/1971 | 2 month prescription of Glaberol 2mg twice a day. | 30/3/2020 10:31 | Parkway Practice, Birmingham, B1 2JP |
| 979384758 | Seb Colbert | 12/3/1971 | Diagnosis asthma | 2/12/2012 11:22 | Grove Practice, London, SE5 8AZ |

This example demonstrates the level of detail of identifiable GP data available in level 1. It is not representative of how the data is structured.

| Pseudonym | Event | Date | Location |
| --- | --- | --- | --- |
| aj834nasdlk | 2 month prescription of Glaberol 2mg twice a day. | 30/3/2020 10:31 | MSOA (approximate location) |
| aj834nasdlk | Urea result 7.1 mmol/L | 2/03/2020 09:22 | MSOA |
| aj834nasdlk | Urea result 8.2 mmol/L | 2/02/2020 10:41 | MSOA |
| aj834nasdlk | Diagnosis asthma | 2/12/2012 11:22 | MSOA |

This example demonstrates the level of detail of pseudonymised GP data available in level 1. It is not representative of how the data is structured.

## Level 2 [NHS England are data controllers of the data]
This includes external datasets imported into the database, for instance hospital admissions and death registry data.

Only data for patients who are present in the GP data held by EMIS or TPP are imported from external datasets (a matching processing is carried using the pseudonymised NHS number). The external data is stored only in pseudonymised form.

The system guarantees that patient identifiers cannot be queried or searched. In ehrQL (the OpenSAFELY query language, and the only mechanism through which users access patient-level data) the patient_id variable is handled implicitly and never exposed to the query language. This prevents any lookup or filtering by individual patient. Identifiers are used only to link multiple extracts of data within a single secure project workspace, supporting consistent analysis without any risk of re-identification.

EMIS and TPP securely hash NHS numbers for linkage purposes using a secret key shared with external dataset providers. Level 2 contains neither NHS numbers nor those hashes. Instead, each backend supplies a system-specific patient identifier that is unique to the OpenSAFELY environment and cannot be traced back to an NHS number. These identifiers are implemented differently across backends (for example, integers in TPP and hexadecimal strings in EMIS), are meaningless outside the platform, and cannot be used to identify individuals or to perform direct lookups.

The schema for the TPP database can be seen in [this notebook](https://reports.opensafely.org/reports/opensafely-tpp-database-schema/).

### Where is this data held?
Data is held within the EHR vendor's secure environment on the OpenSAFELY server.

### Who has access?
Data processor staff working at the EHR vendor and a small and restricted number of OpenSAFELY platform developers. Similar to level 1 above, researchers can query this pseudonymised external data, but only indirectly: they write their study analysis code away from the source data, in GitHub, and the OpenSAFELY service automates the execution of the study code against the external data. Only the aggregated results of their study are made available back to the researchers in Level 4 (see below).

## Level 3 [NHS England are data controllers of the data]
At this level data is typically stored as a pseudonymised patient-level (rather than event level) extract. It includes all pseudonymised patient-level outputs derived from queries run against Level 1 and 2 data, i.e., a specific study dataset generated by a [dataset_definition](https://docs.opensafely.org/ehrql/). It also includes all of the pseudonymised patient-level intermediate outputs for a study derived from queries run against Level 3 data which output pseudonymised patient-level data i.e., a processed study dataset where certain filters/formatting have been applied.

As the data stored at this level is still patient-level, access to this level is restricted to a small number of OpenSAFELY staff to allow data quality assessment and debugging problems.

### Where is this data held?
Data is held within the EHR vendor's secure environment on the OpenSAFELY server (same as level 2).

### Who has access?
This is the same as Level 2.

## Level 4 [NHS England are data controllers of the data]
This level includes aggregated patient-data (non patient-level data) derived from analyses run against Level 3 data, such as summary tables, summary statistics and the outputs from statistical models. It also includes the automatically created log files of each action/script corresponding to each file, for debugging purposes.

This is the only level that OpenSAFELY users have access to in order to view their aggregated data/results/log files; users do not have unfettered access to any patient-level data and only see aggregated outputs derived from their analysis code, which satisfies the GDPR principle of confidentiality. Researchers are able to use this level to check that the appropriate statistical disclosure controls have been applied to any files intended for release out of the server.

Access to this level is secured via VPN access to a remote desktop. No files are released from the secure environment without undergoing dual independent checking by trained output-checkers for disclosure issues (see the [statistical disclosure control section](outputs/sdc.md))

### Where is this data held?
Data is held within the EHR vendor's secure environment on a specific server, separate from the Level 2 and 3 server.

### Who has access?
Anyone with Level 2/3 access. In addition, researchers who have an NHS England approved study, and who have signed a Data Access Agreement relevant to level 4 access for the purposes of checking and redacting their aggregated study outputs prior to release.

## Unrestricted data
Any level 4 files that have been cleared by output-checkers, and therefore considered to have negligible disclosure risk, can be released.

## Diagram

![A diagram of the OpenSAFELY platform.](./images/NON-COVID-GP-data-OpenSAFELY-platform-architecture-and-dataflows-V5-for-DPIA-DPN.drawio.svg)
