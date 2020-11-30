This section guides you through the software required to use OpenSAFELY from your own computer. 
OpenSAFELY maintains extremely high standards for data privacy, whilst ensuring complete computational and analytical transparency.
As such there are some technical requirements that must be met to use the platform.
You will need to install git, Python, and Docker &mdash; these tools are required for (or greatly simplify):

* defining the data you want to extract from the database
* importing codelists
* creating dummy data for developing analysis scripts
* testing analysis scripts locally
* running the analysis on the server

For the analysis proper, you can use Stata, R, or Python (almost) however you wish &mdash; see the [Developing Analysis Scripts](workflow-develop-analysis-scripts.md) section for guidance and exceptions.

Additionally, to use OpenSAFELY fully you will need some platform-specific permissions, for instance to be able to submit analyses to run on the server.
We will issue these as required.

## Minimum requirements

In terms of users' own technical experience, the current requirements are as follows:

### Essential
* **Stata, R or Python**
OpenSAFELY currently supports Stata v16.1, Python 3.8, and R 4.0 for statistical analysis.
Available libraries are restricted by the framework (documentation to follow).
* **Git**
The workflow is strongly integrated into Git/GitHub.
As a minimum you need to be able to clone a remote git repository, create a branch to work on, commit changes to it, push those changes to the remote repository, create a pull request, and merge branches.
See [git workflow](git-workflow.md) for advice about how to use git effectively.
<!--We provide a simple tutorial for navigating the OpenSAFELY workflow.-->

### Desirable
* **Python**
The way we specify the data to be extracted for analysis is written in Python, using what we call a **Study Definition**.
We provide easy-to-use Python functions to define your study population and study variables that are designed to be used and understood by anybody familiar with health research, even if you've neveer used python before.
However, some prior knowledge of Python may still be beneficial to create or modify existing functions.
* **SQL**
Behind the scenes, SQL is the language that is used to extract data from the server. 
Some knowledge of SQL may be useful if you want to understand in more detail how the raw patient-level data held in the secure environment is converted into analysis-ready datasets.
* **Docker**
We use Docker containers to simulate the production environment on your machine, so you can [test code locally](pipelines-overview.md).

We recommend following one of our OpenSAFELY walkthroughs (see [here](https://github.com/opensafely/os-demo-research#opensafely-demo-materials)) to guide you through the platform workflow, rather than using these documentation pages alone. 
