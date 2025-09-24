## What is OpenSAFELY?

[OpenSAFELY](https://www.opensafely.org/) is a secure analytics platform for electronic health records in the NHS, created to deliver urgent results during the global COVID-19 emergency.
It is now successfully delivering analyses across more than 57 million patients' full pseudonymised primary care NHS records, with more to follow shortly.

All our analytic software is open for security review, scientific review, and re-use.
OpenSAFELY uses a new model for enhanced security and timely access to data:
we don't transport large volumes of potentially disclosive pseudonymised patient data outside of the secure environments managed by the electronic health record software company;
instead, trusted analysts can run large scale computation across near real-time pseudonymised patient records inside the data centre of the electronic health records software company.

As such, the platform maintains extremely high standards for data privacy whilst ensuring complete computational and analytical transparency.

!!! note "OpenSAFELY is constantly developing and improving"
    We suggest you regularly check our [Platform News page](https://www.opensafely.org/changelog/) to learn about recent changes.

<div class="youtube-embed">
  <lite-youtube
    videoid="GRjRqOAIVy8"
    params="controls=1&modestbranding=2&rel=0&enablejsapi=1"
  ></lite-youtube>
</div>

## Who is OpenSAFELY?

OpenSAFELY is a collaboration between the [Bennett Institute for Applied Data Science](https://www.bennett.ox.ac.uk/) at the University of Oxford, the EHR group at London School of Hygiene and Tropical Medicine, TPP and other electronic health record software companies (who already manage NHS patients' records), working on behalf of NHS England.

## Using OpenSAFELY

**Only approved users can execute code against the real OpenSAFELY database**.  We are currently in a pilot phase for [onboarding new users](https://www.opensafely.org/onboarding-new-users/).

However, anyone can access and use all the OpenSAFELY-specific tools needed to define analysis datasets, generate dummy data, and run analysis scripts in a computational environment that mimics the secure environment where real analyses are run.

All steps in the [Getting Started](getting-started/tutorial/index.md) tutorial can be run by anyone interested in learning more about how code is written and executed in OpenSAFELY.

To use OpenSAFELY, users must know, or be willing to learn, the following programs and tools:

### Essential

- **Stata, R or Python**
  OpenSAFELY currently supports Stata v16.1, Python 3.8, Python 3.10, R 4.0 and R 4.4 for statistical analysis.
  For security reasons, available libraries are restricted to those provided by the framework. See ["Execution Environments"](actions-scripts.md#execution-environments) for more information.
- **Git**
The workflow is strongly integrated into Git/GitHub.
As a minimum you need to be able to clone a remote git repository, create a branch to work on, commit changes to it, push those changes to the remote repository, create a pull request, and merge branches. We have simple guidance in our [Getting Started tutorial](getting-started/tutorial/index.md) on this if you have never used this tooling before.
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
  We use Docker containers to simulate the production environment on your machine, so you can [test code locally](actions-pipelines.md). This is not essential as we also describe how to run OpenSAFELY in your web browser, which does not require any software installation on your own computer.

## How should I start learning to use OpenSAFELY?

**For new users, the best place to begin is the [Getting
Started](getting-started/tutorial/index.md) tutorial.**

The [Analysis workflow](workflow.md) gives a high-level view of the steps involved in an OpenSAFELY research project.

See our [installation](getting-started/how-to/index.md) pages for complete installation
instructions if you wish to install on your own computer.

## How can I make my organisation's data available via OpenSAFELY?

See our guidance for [system integrators and data providers](system-integration.md).

!!! note "These documents are a work-in-progress"
    Please see the [Updating the Documentation page](updating-the-docs.md) if you want to make improvements.
