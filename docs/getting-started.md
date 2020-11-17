This section guides you through the software required to use OpenSAFELY from your own computer. 

## minimum requirements

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
The code to generate each dataset is written in Python, using what we call a **Study Definition**.
We provide easy-to-use Python functions to define your study population and study variables that are designed to be used and understood by anybody familiar with health research.
However, some knowledge of Python may still be beneficial to create or modify existing functions.
* **Docker**
We use Docker containers to simulate the production environment on your machine, so you can [test locally](project_pipelines.md).