Analytic code can be divided up into logical units. You might have a script which prepares and cleans data, and another which outputs a summary descriptive table.

In OpenSAFELY, each logical unit is called an _action_.  Actions can be scripts, Jupyter notebook generators, or specialised functions provided by the framework.

An OpenSAFELY project must refer to its actions in a [_pipeline_](actions-pipelines.md).  This is a file called `project.yaml` which defines all the actions in a project, how they should be run, and how their outputs should be saved. Every pipeline will start with [_cohortextractor_](actions-cohortextractor.md) as its first action, to convert the study definition into an actual analysis-ready dataset based on dummy or real data.

Dividing your analysis into actions and describing them in a pipeline has a few purposes:

* It aids readability and bug-finding
* It allows common code to be reused without copy-and-paste
* The OpenSAFELY [pipeline](actions-pipelines.md) system ensures your actions run efficiently and quickly
* It allows reviewers to see your intent and check your code for privacy and security accordingly
