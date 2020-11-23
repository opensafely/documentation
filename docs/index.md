
**These documents are a work-in-progress**. Please see the [Updating the Documentation page](updating-documentation.md) if you want to make improvements. 
 
## What is OpenSAFELY?

OpenSAFELY is a new secure analytics platform for electronic health records in the NHS, created to deliver urgent 
results during the global COVID-19 emergency. It is now successfully delivering analyses across more than 24 million 
patients’ full pseudonymised primary care NHS records, with more to follow shortly. 

All our analytic software is open for security review, scientific review, and re-use. OpenSAFELY uses a new model for enhanced security and timely 
access to data: we don’t transport large volumes of potentially disclosive pseudonymised patient data outside of the 
secure environments managed by the electronic health record software company; instead, trusted analysts can run large 
scale computation across near real-time pseudonymised patient records inside the data centre of the electronic health records software company. 

## Getting started

To use OpenSAFELY you need git, GitHub, Python, and Docker &mdash; see our [getting started](getting-started.md) pages for complete installation instructions. These tools are required for (or greatly simplify):
* defining the data you want to extract from the database
* creating dummy data for developing analysis scripts
* testing analysis scripts
* importing codelists
* running the analysis on the server
* ensuring the same computing environment when developing code locally and deploying code on the server.

For the analysis proper, you can use Stata, R or Python however you wish, as long as .

We strongly recommend you follow one of our OpenSAFELY walkthroughs to guide you through the platform using a typical workflow, rather than using the documentation pages alone. 

## Useful links

Some of these are in private repos as they are under quick development pending release:

* [TPP Database Schema (based on dummy data)](https://github.com/opensafely/tpp-sql-notebook/blob/master/notebooks/tpp-schema.ipynb) (needs occasional refreshes)
* [Variable extractor function skeleton documentation](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/patients.py)
* [Variable extractor function python definitions](https://github.com/opensafely/cohort-extractor/blob/master/cohortextractor/tpp_backend.py)
* [Instructions for interacting with OpenSAFELY via the secure server](https://github.com/opensafely/server-instructions/blob/master/docs/Server-side%20how-to.md) (in restricted access repo)
* [Latest available records in SystmOne and external datasets](https://github.com/opensafely/rapid-reports/blob/master/notebooks/latest-dates.ipynb) (needs weekly refreshes)
* [Ethnicity codes used by external datasets](https://github.com/opensafely/rapid-reports/blob/master/notebooks/ethnicity-codes.ipynb)
* [Dataset user guides](https://docs.google.com/document/d/1EzaRTiapjxxbj10wjN5iYjXbeyHMEErOoaV0tH6Mv1c/) (in restricted access gdrive folder)




