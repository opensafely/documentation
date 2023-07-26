# Policy for OpenSAFELY Access by Platform Developers

## Introduction

OpenSAFELY securely mediates access to pseudonymized patient data for the purpose of analysis (be that research, service evaluation or audit).
Our objective is to minimise direct access to pseudonymised data wherever possible, to protect privacy;
while facilitating high quality, efficient analytics on the data by a wide range of users.
A small number of OpenSAFELY team members need more direct access to the pseudonymised data inside the secure environment. This access is required:

* to develop and operate the OpenSAFELY platform
* for data curation purposes

### What this policy describes

This policy describes:

* the conditions under which individuals with these roles may access the OpenSAFELY platform
* the controls in place to ensure that such access cannot be used to subvert the OpenSAFELY security model

All such access conforms to the OpenSAFELY platform’s principles of security, transparency and minimal access.

The specific access activities this policy covers are:

* running OpenSAFELY test pipelines
* ad hoc access to backend systems
* data curation activities

## Running OpenSAFELY test pipelines

### Why

For software maintenance purposes, it is sometimes necessary to execute OpenSAFELY [project pipelines](actions-pipelines.md#project-pipelines).
The test project pipelines are necessary to:

* ensure that the entire OpenSAFELY platform is operating correctly
* verify that changes to the software work correctly in deployed systems

### What

The OpenSAFELY team maintains a small set of test studies in the [OpenSAFELY Testing](https://jobs.opensafely.org/datalab/opensafely-testing/) project.
These studies have pipelines that use the standard OpenSAFELY tooling,
but which have been specially designed to test and assess the platform’s functionality rather than to answer research questions.

Because they are standard OpenSAFELY pipelines, they benefit from all the same security controls as OpenSAFELY research pipelines,
including:

* publication of all code that is run
* logging of all operations
* manual checking of outputs for disclosivity before they are released from the backend

Access to the OpenSAFELY platform will also be required to verify the pipeline outputs are as expected.

### Who

The test studies can only be run by OpenSAFELY Core Developers.

### When

These test pipelines are run periodically as is necessary to check that the system is working properly.
They are also run when updated software has been deployed.
However this deployment only happens after new versions of the software have gone through careful testing with simulated data to ensure that they are functioning correctly and that the security characteristics of the platform are maintained.

## Ad hoc access to backend systems

!!! note
    This section applies to OpenSAFELY-TPP and OpenSafely-EMIS only.

### Why

To ensure the correct operation of the platform,
it is sometimes necessary to directly access OpenSAFELY backend systems so that:

* software can be reconfigured or updated
* problems which only manifest themselves in the deployed system can be investigated

### What

Access to backend systems is via secure, authenticated, encrypted channels. All access to the system and database operations are logged.
This process gives access to:

* the OpenSAFELY software running in the backend
* logs that the OpenSAFELY software produces
* pseudonymized patient data
* unvetted intermediate data
* unchecked, unreleased study outputs.

There is no facility for extracting data from the system via this process: the data can only be studied within the system itself.

### Who

Direct access to the OpenSAFELY backend systems is only available to OpenSAFELY Core Developers.

### When

This process is routinely used for updating the platform with new software versions.
It is exceptionally used for investigating outages or other problems, and only when the information necessary for the investigation can’t be accessed from outside the system.

## Data curation activities

!!! note
    This section applies to OpenSAFELY-TPP and OpenSafely-EMIS only.

### Why

Characterizing datasets and checking data quality.

### What

Access to backend systems is via secure, authenticated, encrypted channels. All access to the system and database operations are logged.
Because data curation requires patterns of data access that are not supported by the standard OpenSAFELY pipelines,
this process allows custom code to be run with access to the pseudonymized patient data, outside the pipelines.

These data curation activities benefit from all the same security controls as standard OpenSAFELY pipelines,
including:

* publication of all code that is run
* logging of all operations
* manual checking of outputs for disclosivity before they are released from the backend

Data curation activities are also subject to the [standard OpenSAFELY research policies](https://www.opensafely.org/policies-for-researchers/).

### Who

Only OpenSAFELY Core Developers and OpenSAFELY Data Investigators have permission to carry out data curation activities.

### When

Data curation activities may be carried out:

* when new datasets are added to OpenSAFELY
* when datasets are updated
* when previously unused fields in existing datasets are put to use
* periodically for data quality assurance and sense checking purposes
