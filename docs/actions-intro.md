Analytic code can be divided up into logical units. You might have a script which prepares and cleans data, and another which outputs a summary descriptive table.

In OpenSAFELY, each logical unit is called an _action_.  Actions can be scripts, Jupyter notebook generators, or specialised functions provided by the framework.

An OpenSAFELY project must refer to its actions in a [_pipeline_](actions-pipelines.md).  This is a file called `project.yaml` which defines all the actions in a project, how they should be run, and how their outputs should be saved.

* Every pipeline will start with an [_ehrQL_](/ehrql/) action, to generate an analysis-ready dataset of real or dummy data.
* You can create custom [scripted actions](actions-scripts.md) in a number of other coding languages and choose from (or create your own) [reusable actions](actions-reusable.md).

Dividing your analysis into actions and describing them in a pipeline has a few purposes:

* It aids readability and bug-finding
* It allows common code to be reused without copy-and-paste
* The OpenSAFELY [pipeline](actions-pipelines.md) system ensures your actions run efficiently and quickly
* It allows reviewers to see your intent and check your code for privacy and security accordingly
