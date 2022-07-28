To request new functions that create variables via a study definition, follow these instructions:

* Browse the [study definition variables](study-def-variables.md) page to see all possible variables that can currently be extracted with a study definition, and check that the variable you want doesn't already exist. If you're not sure, read about OpenSAFELY [study definitions](study-def.md) to understand the way in which the database is queried and data extracts are generated.
* Browse the [data sources](../data-sources/) page to see what data is available in each backend.
* View the [OpenSAFELY-TPP database update notebook](https://reports.opensafely.org/reports/opensafely-tpp-database-builds/) to see when each data source was updated.
* View the [OpenSAFELY-TPP schema notebook](https://reports.opensafely.org/reports/opensafely-tpp-database-schema/) to see the structure of the database.
* Check that the variable has not already been requested as an issue in the [`cohort-extractor`](https://github.com/opensafely-core/cohort-extractor) repository. Look at both _open_ and _closed_ issues in case the variable has been considered unworkable or low priority.


If after reviewing these resources you think the information you need might be in the database, but you can’t extract it with a study definition (for example because the variable extractor function doesn’t exist, or the structure of extracted data doesn’t allow for it), then:

* Create a new issue in the [`cohort-extractor`](https://github.com/opensafely-core/cohort-extractor) repository, and add the `enhancement` label
* Explain the rationale
* Where possible, describe how you expect the function to look for this variable, or how it will modify or enhance an existing variable:
	* what will it be called?
	* what are the function arguments?
	* what are the returning values?
* Where possible, provide example SQL code for the underlying database query (it doesn't have to be perfect).



---8<-- 'includes/glossary.md'
