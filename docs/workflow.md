This section introduces the typical OpenSAFELY workflow. The workflow consists of a number of key steps which may be iterated over as analysis scripts are developed and the study evolves. 

The following section assumes that a well-defined and ethically-approved research agenda have been specified, with an accompanying study protocol. 

## High level overview

the workflow for a single study can typically be broken down into the following steps:

1.  **Create a git repository** from the template repository provided and clone it on your local machine.
2.  **Write a Study Definition** that specifies what data you want to extract from the database:
    -   specify the patient population (dataset rows) and variables (dataset columns)
    -   specify the expected distributions of these variables for use in dummy data
    -   specify the codelists required by the study definition, hosted by codelists.opensafely.org, and import them to the repo.
3.  **Generate the dummy data** on your local machine based on the Study Definition. 
4.  **Develop analysis scripts** using the dummy data in R, Stata, or Python. This will include:
    -   importing and processing the dataset(s) created by the cohort extractor
    -   importing any other external files needed for analysis
    -   generating analysis outputs like tables and figures
    -   generating log files to debug the scripts when they run on the real data.
5.  **Create a project pipeline** which specifies the execution order for data extracts and analysis scripts, and the outputs to be released.
6.  **Execute the analysis on the real data** via the job runner. This will generate outputs on the secure server.
7.  **Check the output for disclosivity** within the server, and redact if necessary.
8.  **Release the outputs** via GitHub.

Steps 2-5 (and to an extent also steps 6 and 7) are iterative and should proceed with frequent git commits and code reviews where appropriate. They can all be progressed on your local machine without accessing the real data. 

It is possible to automatically test that the analytical pipeline defined in step 5 can be successfully executed on dummy data, using the `cohortextractor run` command. This pipeline is also [automatically tested]() against dummy data every time a new version of the repository is saved ("pushed") to GitHub.

Other non-standard actions may be required. For example, it's possible to run a matching routine that extracts a matched control population to the population defined in the study definition, without having to extract all candidate matches into a dataset first.

