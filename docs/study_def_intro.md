## What is a Study Definition?

A _study definition_ describes all of the features of your study: the
codelists, the population definitions, the dates, and the variables.

It is written in a custom format in simple python which is intended to be readable and
reviewable by anyone with epidemiological knowledge.  The OpenSAFELY
framework uses the study definition to query different vendor EHR
databases, and returns the results in a CSV file of tabular data.

A study definition also allows a researcher to define the shape of the
values they *expect* to get back from the vendor data. This allows the
framework to generate dummy data which the researcher can user to test
models their models during development, without ever having to touch
real patient data.


## Brief Summary

When you generate a study population from your study definition, the framework reads a
study definition at `analysis/study_definition.py`, and writes the
output dataframe to `output/input.csv`.  In a production environment
this will be real data; in a development environment this will be
dummy data. This contains one row per patient, with variables as columns. 

## Naming conventions

A `study_definition.py` will always produce a file called `input.csv`. If you only require one study
population, we recommend you stick with this. 

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
