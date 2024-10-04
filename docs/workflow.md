This section introduces the typical OpenSAFELY workflow for a single research project.

The workflow consists of a number of key steps which may be iterated over as the code is developed and the study evolves.
The following assumes that a well-defined and ethically-approved research agenda has been specified, with an accompanying study protocol, and all necessary permissions for accessing the OpenSAFELY platform are in place.

The workflow for a single study can typically be broken down into the following steps:

1.  **Create a git repository** from the [template repository provided](https://github.com/opensafely/research-template) and clone it on your local machine.
This repo will contain all the code relating to your project, and a history of its development over time.
2.  **Write a [dataset definition](/ehrql/)** that specifies what data you want to extract from the database:
    -   specify the patient population (dataset rows) and variables (dataset columns)
    -   specify the expected distributions of these variables for use in dummy data
    -   specify (or create) the [codelists](codelist-intro.md) required by the dataset definition, hosted by [OpenCodelists](https://www.opencodelists.org), and import them to the repo.
3.  **Generate [dummy data](/ehrql/how-to/dummy-data)** based on the dataset definition, for writing and testing code.
4.  **Develop analysis scripts** using the dummy data in R, Stata, or Python. This will include:
    -   importing and processing the dataset(s) created by the dataset definition
    -   importing any other external files needed for analysis
    -   generating analysis outputs like tables and figures
    -   generating log files to debug the scripts when they run on the real data.
5.  **Test the code** by running the analysis steps specified in the [_project pipeline_](actions-pipelines.md), which specifies the execution order for data extracts and analyses and the outputs to be released.
6.  **Execute the analysis on the real data** via OpenSAFELY's [jobs site](jobs-site.md). This will generate outputs on the secure server.
7.  **Check the output for [disclosivity](outputs/sdc.md)** within the server, and redact if necessary.
8.  **[Request release](outputs/requesting-file-release.md) of the outputs**
9. **Repeat and iterate steps 2 to 8 as necessary**.

These steps should always proceed with frequent git commits and code reviews where appropriate. Steps 2-5 can all be progressed on your local machine without accessing the real data.

It is possible to automatically test that the analytical pipeline defined in step 5 can be successfully executed on dummy data, using the `opensafely run` command.
This pipeline is also [automatically tested](actions-pipelines.md#running-your-code-with-github-actions) against dummy data every time a new version of the study repository is saved ("pushed") to GitHub.

As well as your own Python, R or Stata scripts, other non-standard actions are available.
For example, it's possible to run a matching routine that extracts a matched control population to the population defined in the dataset definition, without having to extract all candidate matches into a dataset first.
