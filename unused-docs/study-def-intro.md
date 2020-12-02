## What is a Study Definition?

A _study definition_ specifies the data that you want to extract from the OpenSAFELY database. This includes

* the patient population (dataset rows)
* the variables (dataset columns)
* the expected distributions of these variables for use in dummy data

It is written in a python script using an OpenSAFELY-specific format which is intended to be easily written, read, and reviewed by anyone with some epidemiological knowledge. 
The OpenSAFELY framework uses the study definition to query different vendor EHR databases, and returns the results to the secure server in a CSV file of tabular data.

A study definition also allows a researcher to define the shape of the values they *expect* to get back from the vendor data. 
This allows the framework to generate dummy data which the researcher can use to develop and test their analysis scripts, without ever having to touch real patient data.


## Brief Summary

When you generate a study population from your study definition, the framework reads a study definition from the python script (usually `analysis/study_definition.py`), and writes the output dataframe in a tabular CSV file (usually `output/input.csv`). 
In a production environment this will be real data; in a development environment this will be dummy data. 
Currently the framework supports one row per patient datasets. 

## Naming conventions

A `study_definition.py` will always produce a file called `input.csv`. If you only require one study population, we recommend you stick with this. 

Multiple study definition files can be specified using a suffix like:
```
study_definition_copd.py
study_definition_asthma.py
```

And all the corresponding output files will have the same suffix e.g.
```
input_copd.csv
input_asthma.csv
```
