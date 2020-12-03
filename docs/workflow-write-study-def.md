## What is a Study Definition?

A _study definition_ specifies the data that you want to extract from the OpenSAFELY database. This includes

* the patients of interest (dataset rows)
* the variables (dataset columns)
* the expected distributions of these variables for use in dummy data

It is written in a python script using an OpenSAFELY-specific format which is intended to be easily written, read, and reviewed by anyone with some epidemiological knowledge. 
The OpenSAFELY framework uses the study definition to query different vendor EHR databases, and returns the results to the secure server in a CSV file of tabular data.

A study definition also allows a researcher to define the shape of the values they *expect* to get back from the vendor data. 
This allows the framework to generate dummy data which the researcher can use to develop and test their analysis scripts, without ever having to touch real patient data.

For full details on how to write a study definition, see the [Study Definition section](study-def.md).


---8<-- 'includes/glossary.md'
