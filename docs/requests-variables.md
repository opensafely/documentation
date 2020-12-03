To request new functions that create variables via a Study Definition, follow these instructions:

* Check that the variable does not already exist, by searching the [Study Definition variables](study-def-variables.md) section
* Check that the variable has not already been requested as an Issue in the [`cohort-extractor`](https://github.com/opensafely/cohort-extractor) repository. Look at both _open_ and _closed_ Issues in case the variable has been considered by deemed unworkable or low priorty.
* Create a new Issue in the [`cohort-extractor`](https://github.com/opensafely/cohort-extractor) repository, and add the `enhancement` label
* Explain the rationale
* Where possible, describe how you expect the function to look for this variable, or how it will modify or enhance an existing variable:
	* what will it be called?
	* what are the function arguments?
	* what are the returning values?
* Where possible, provide example SQL code for the underlying database query (it doesn't have to be perfect).




---8<-- 'includes/glossary.md'
