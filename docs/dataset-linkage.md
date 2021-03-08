Currently, all data available for analysis are for patients registered[^1] at GP practices who use the SystmOne clinical information system, managed by TPP. EMIS support is currently under development

Patient records from external datasets are imported and matched to the core data as follows:

* Patient records from other external sources are matched to SystmOne records on NHS numbers via a [salted](https://en.wikipedia.org/wiki/Salt_(cryptography)) [hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function):
	* Usually this is done by the data controllers of the external dataset &mdash; that is, hashed NHS numbers for patients in OpenSAFELY are sent to the external data controller, they identify all the matching records in their dataset, and then send only those records back to OpenSAFELY.
	* For some datasets (ICNARC), OpenSAFELY receives the hashed NHS numbers from the external dataset and the matching occurs inside OpenSAFELY. The matched IDs are then sent back and the matched records are returned to OpenSAFELY.
* No other identifiers (names, postcodes, DOBs etc) are used for matching, though this may change in future.
* No patient identifiers are imported from external datasets.
* Only records for patients with matching NHS numbers are imported to OpenSAFELY (i.e., `left_join(SystmOne, External, by='NHSNumber')`).

Matching quality is dependent on the quality of NHS numbers (they're good but not infallible).
Currently there is no direct evaluation of linkage quality because by design (minimisation of the transfer of sensitive data) we don't have access to direct identifiers from external datasets; nor do we know in general if we should be expecting a match or not.


[^1]:
    "Registered" here means a patient with a full "GMS" (General Medical Services) registration. Patients with temporary registrations are not included.

---8<-- 'includes/glossary.md'
