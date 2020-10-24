# Introducing OpenSAFELY

![OpenSAFELY](https://opensafely.org/) is a secure analytics platform for routinely collected electronic health records in the NHS.

A key feature of the platform is that datasets are analysed within the secure environment where they are already stored,
removing the need for large extracts of potentially disclosive anonymised patient data to be moved around.
Whilst this prevents third-party groups from accessing the underlying data directly,
the platform is designed with collaboration in mind to ensure as many research groups acting in the public interest as possible can analyse the data.

This document is intended for prospective OpenSAFELY collaborators who are interested in using the platform to conduct health research.  It's a work in progress, and is a mixture of instructions and bullet points which are pending further elaboration and expansion.

## Minimum requirements
OpenSAFELY maintains extremely high standards for data privacy, whilst ensuring complete computational and analytical transparency.
As such there are some small technical pre-requisites that collaborators must satisfy to use the platform:

### Essential
* **Stata, R or Python**
OpenSAFELY currently supports Stata v16.1, Python 3.8, and R 4.0 for statistical analysis. Available libraries are restricted by the framework (documentation to follow)
* **Git**
The workflow is strongly integrated into Git/GitHub.
At a minimum you need to be able to <!--(clone, branch, commit, push, pull)--> clone a remote git repository, create a branch to work on, commit changes to it, push those changes to the remote repository, and create a pull request.
We are not able to provide foundational Git/GitHub training, though there are several resources listed at the end of this document.
<!--We provide a simple tutorial for navigating the OpenSAFELY workflow.-->

### Desirable
* **Python**
The code to generate each study-specific dataset is written in Python.
We provide easy-to-use Python functions to define your study population and study variables that are designed to be used and understood by anybody familiar with health research.
However, some knowledge of Python may still be beneficial to create or modify existing functions.
* **Docker**
We use Docker containers to simulate the production environment on your machine, so you can [test locally](project_pipelines.md).


## Workflow Overview
The process of conducting an analysis via OpenSAFELY can be broken down into the following steps:

1. Design a study protocol Research question and protocol are discussed and written (preferably in a google document so multiple authors can edit and review)
2. Institutional Ethics Approval once protocol is finalised.
3. Create a study-specific repository from the template provided, and upload the protocol to the repository.
4. Codelists that do not exist already are developed and put onto the opencodelist webpage
5. Study population and study variables are defined within a Python script that is developed locally (i.e on your machine) and uploaded to Github for comments, reviews, and other contributions. This process is iterative.
6. When the study definition script is “run” on a local computer, it creates a dummy dataset which approximates the structure of the source data. This dummy dataset has all the necessary covariates, as specified in your study definition script, with the right type of data (for example numbers, dates or count variables) (but currently does not respect expected between-variable relationships such as metformin prescriptions only for people with diabetes).
7. Analytics code is developed against this dummy dataset, optionally split into [separate "project pipeline" stages](project_pipelines.md).
8. Once the analytic code and the study population code is finalised and uploaded to GitHub, the code is deployed and executed securely by requesting a run in the [OpenSAFELY Job server](job_server.md). TThe real study population is extracted, and the analytic code run.
9. Analytic output files earmarked for publication (e.g.log files, PDFs, notebooks, graphics) are reviewed by authorised users on the review server and any sensitive data is removed.
10. Summary results are returned to the external researcher via GitHub and can be reviewed by the team.

These sections are described in further detail below.

### Developing a Research Question and Protocol
* Initial request + discussion of study idea
* Protocol template - why is a preregistered protocol a good idea.
* Encourage registration of studies on encepp or clinicaltrials.gov or similar? (Even though we have not done that so far)

### Creating a git repository for your study
* clone the research template
* update README, import protocol

### Code Lists

* Check and/or review existing lists on [codelists.opensafely.org](https://codelists.opensafely.org)
* If edit, submit through [codelists.opensafely.org](https://codelists.opensafely.org)
* If new list needed, create it as an issue in the repo
* CTV3 needed, can translate from Read2. Link to browser.
* Recommend to also extract SNOMED from QoF?
* Process for sign off
* Publish to [codelists.opensafely.org](https://codelists.opensafely.org)

### Writing a Study Definition
* How to get codelists into the study definition
* Explanation of the pre-written functions
* Assume existing ones will be publicly available, so people will be able to see what they look like. Would be a good starting point.
* What is and is not supported by the study definition file at the moment:
  * Matching for case-control studies
  * PS matching or similar (assume can be done in Stata)
  * Time-updated variables (?)

See [Study definitions](study_definition.md) for more detail.

### Working With Dummy Data
* Focus on making code run without errors
* Explanation of automatic tests on Github
* Include logical tests and checks you would do for cleaning. Do not assume data is clean.

### Running Finalised Code Against the Server
* Process once external people are happy with their code and no errors
* Timeframe for run and checks (approximate)

### Publishing and Sharing
* Expected outputs will be published
* Github repos with code will be publicly available (from start or later on?)
* Share code and protocol in other places is fine, data cannot be shared
* Encourage Open Access publishing, preprints etc.
* [placeholder - procedures for authorship/credit determination]

## FAQs

* _I use [R/SAS/SPSS/Other] and not Stata. Can I still do a study through the OpenSafely platform?_
  [answer]
* _I’d prefer to write my analysis scripts in Python. Can I do that?_
  [answer]
* _My research question is exploratory. How can I develop all my code without seeing interim results?_
  [answer]
* _If we can show that we meet data security standards. Can you just post us a copy of the data instead?_
  [answer]
* _I’ve realised I need to do something differently to what I said in my protocol. Can I still do that?_
  [answer]
* _My analysis requires a linked dataset from another source. Can you facilitate this?_
  [answer]

## Further Resources

