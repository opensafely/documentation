[TOC]

This section contains information on the core primary care EHR systems on which OpenSAFELY in based, as well as all external datasets imported to the secure EHR environment.

To see the variables available to extract from the OpenSAFELY database, see the [Variable extractor functions](study-def-extractor-functions.md) section.

To see the OpenSAFELY-TPP database schema, see [here](https://github.com/opensafely/tpp-sql-notebook/blob/master/notebooks/tpp-schema.ipynb).

To see access permissions for different levels of data access, see [here](workflow-security-levels.md).

## External sources and record linkage
Currently, all data available for analysis are for patients registered at GP practices using the SystmOne clinical information system, managed by TPP. 
Patient records from external datasets are imported as follows:

* Patient records from other external sources are matched to SystmOne records on NHS numbers. 
* No other identifiers (names, postcodes, DOBs etc) are used for matching, though this may change in future.
* No identifiers are imported from external datasets. 
* Only records for patients with matching NHS numbers are imported to OpenSAFELY (i.e., `left_join(SystmOne, External, by='NHSNumber')`).
* Matching is performed securely via a [salted](https://en.wikipedia.org/wiki/Salt_(cryptography)) [hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function). 
	* Usually this is done by the data controllers of the external dataset &mdash; that is, hashed NHS numbers for patients in OpenSAFELY are sent to the external data controller, they identify all the matching records in their dataset, and then send only those records back to OpenSAFELY. 
	* For some datasets (ICNARC), OpenSAFELY receives the hashed NHS numbers from the external dataset and the matching occurs inside OpenSAFELY. The matched IDs are then sent back and the matched records are returned to OpenSAFELY. 

Matching quality is dependent on the quality of NHS numbers (they're good but not infallible). 
Currently there is no direct evaluation of linkage quality because we don't have access to direct identifiers from external datasets, nor do we know in general if we should be expecting a match or not.

## OpenSAFELY-TPP database builds
The OpenSAFELY-TPP database is typically built once per week. 
In essence, this involves refreshing records in SystmOne so that the records from the following groups are available for analysis:

1. All patients currently registered at a TPP practice
2. All patients registered at any time from 2009-01-01 onwards, but having since de-registered
3. All patients registered at any time from 2009-01-01 onwards, but having since died.

These three groups constitute the patient population available for analysis within OpenSAFELY. 
Note that any primary care events occurring in de-registered patients after the de-registration date will not be available in the TPP patient record, though any events recorded in external linked datasets (such as hospitals admissions or deaths) will be visible. 
"Registered" here means a patient with a full "GMS" (General Medical Services) registration. 
Patients with temporary registrations are not included. 
Every time the database is re-built there will be slight differences in study populations, either due to new registrations or changes to patient records that include/exclude them from the study cohort. 
Old database builds cannot be recovered, and due to the differences between successive database builds, old study populations are unlikely to be re-extracted exactly as before. 

For those with access to the OpenSAFELY database, the latest database build time is available in the `LatestBuildTime` table, and the history of builds for each dataset is available in the `BuildInfo` table.
