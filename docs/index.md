## What is OpenSAFELY?

OpenSAFELY is a secure analytics platform for electronic health records in the NHS, created to deliver urgent results during the global COVID-19 emergency.
It is now successfully delivering analyses across more than 57 million patients' full pseudonymised primary care NHS records, with more to follow shortly.

All our analytic software is open for security review, scientific review, and re-use.
OpenSAFELY uses a new model for enhanced security and timely access to data:
we don't transport large volumes of potentially disclosive pseudonymised patient data outside of the secure environments managed by the electronic health record software company;
instead, trusted analysts can run large scale computation across near real-time pseudonymised patient records inside the data centre of the electronic health records software company.

As such, the platform maintains extremely high standards for data privacy whilst ensuring complete computational and analytical transparency.

## Who is OpenSAFELY?

OpenSAFELY is a collaboration between the DataLab at the University of Oxford, the EHR group at London School of Hygiene and Tropical Medicine, TPP and other electronic health record software companies (who already manage NHS patients' records), working on behalf of NHS England and NHSX.

## Using OpenSAFELY

**Only approved users can execute code against the real OpenSAFELY database**.

However, all the OpenSAFELY-specific tools needed to define analysis datasets, generate dummy data, and run analysis scripts in a computational environment that mimics the secure environment where real analyses are run, are available now for use by anyone.

To use OpenSAFELY, users must know, or be willing to learn, the following programs and tools:

### Essential

- **Stata, R or Python**
  OpenSAFELY currently supports Stata v16.1, Python 3.8, and R 4.0 for statistical analysis.
  For security reasons, available libraries are restricted to those provided by the framework. See ["Execution Environments"](actions-pipelines/#execution-environments) for more information.
- **Git**
The workflow is strongly integrated into Git/GitHub.
As a minimum you need to be able to clone a remote git repository, create a branch to work on, commit changes to it, push those changes to the remote repository, create a pull request, and merge branches.
See [git workflow](git-workflow.md) for advice about how to use git effectively.
<!--We provide a simple tutorial for navigating the OpenSAFELY workflow.-->

### Desirable

- **Python**
  The way we specify the data to be extracted for analysis is written in Python, using what we call a **study definition**.
  We provide easy-to-use Python functions to define your study population and study variables that are designed to be used and understood by anybody familiar with health research, even if you've never used Python before.
  However, some prior knowledge of Python may still be beneficial to create or modify existing functions.
- **SQL**
  Behind the scenes, SQL is the database query language that is used to extract data from the server.
  Some knowledge of SQL may be useful if you want to understand in more detail how the raw patient-level data held in the secure environment is converted into analysis-ready datasets.
- **Docker**
  We use Docker containers to simulate the production environment on your machine, so you can [test code locally](actions-pipelines.md).

## How should I start learning to use OpenSAFELY?

The [Analysis workflow](workflow) gives a high-level view of the steps involved in an OpenSAFELY research project.

See our [installation](install-intro.md) pages for complete installation instructions.

We recommend following one of our OpenSAFELY walkthroughs (see [this notebook](https://github.com/opensafely/os-demo-research#opensafely-demo-materials)) to guide you through the platform workflow on your own computer with dummy data, rather than using the documentation pages alone.

!!! note "These documents are a work-in-progress"
    Please see the [Updating the Documentation page](requests-documentation.md) if you want to make improvements.

---8<-- 'includes/glossary.md'
