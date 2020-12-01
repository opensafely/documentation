This section covers how to run and test your analysis code using a Project Pipeline. 
This includes generating datasets using Study Definitions and analysing that data with R, Stata, or Python.

The [cohortextractor](cohortextractor.md) section describes how to generate dummy datasets with the `cohortextractor generate_cohorts` command using the instructions in a `study_definition.py` script.
These dummy datasets are the basis for developing the analysis code that will eventually be passed to the server to run on real datasets. 
The code can be written and run on your local machine using whatever development set up you prefer (e.g., developing R in RStudio).
However, it's important to ensure that this code will run successfully on the OpenSAFELY server too, using the specific language and package versions that are installed there. 

To do this, you should use the Project Pipeline.