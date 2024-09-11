# OpenSAFELY Data Access Policy

!!! note
    Bennett Institute staff should refer to their [team manual](https://bennettinstitute-team-manual.pages.dev/products/data-access-policy-implementation/) for implementation notes relating to this policy

## Introduction

The following policy outlines the guidelines for patient data access and processing via the OpenSAFELY platform specifically related to **access to and processing of pseudonymised and de-identified patient data** (and data derived from it).
Technical **data relating to the operation of the platform** is covered by a separate OpenSAFELY Platform Operational Data Policy.

The policy outlines the circumstances under which different groups of individuals can access or process pseudonymised patient data and the controls in place to maintain the platform's security model.
OpenSAFELY is committed to upholding the principles of security, transparency, and minimal access (in line with our approved legal basis for access) in all data-related activities.

This policy, intended for internal use but made public for transparency, covers various categories of work:

* Research Projects (a term that encompasses research, service evaluation and audit)
* Short Data Report Projects
* Co-piloting Service
* Checking and Release of Outputs
* Access to Preliminary Results
* Development and Maintenance:
    * End-to-end testing of OpenSAFELY
    * Technical support for Approved Projects
    * Development and maintenance of  backend systems
    * Data development

Each category of work is described in more detail below, describing the purpose (_why)_, methods (_what)_, and access permissions (_who_ and _when_) to ensure the responsible handling of patient data.

## Research Projects

### Why

The OpenSAFELY platform provides a secure analytics service for approved researchers to process pseudonymised and de-identified patient data for [approved projects](https://www.opensafely.org/approved-projects/).
The term “research project” here encompasses research, service evaluation and audit.

### What

Analyses are run via the OpenSAFELY Reproducible Analytical Pipeline, which is designed to keep researchers at “arms-length” from the patient data.
Full details can be found in our documentation, but security controls include:

* Writing in code (_away_ from the patient data) all analyses run against patient data (_currently, this is stored in GitHub)_
* Logging of all operations, in public wherever possible
* Manual checking of outputs for disclosivity before they are released from the secure environment

Approved researchers (with appropriate permissions) can access the secure environment to view the aggregated results of their study ([level 4 data](security-levels.md)); researchers ensure that appropriate statistical disclosure controls have been applied before requesting results for release.
Researchers can also view the “log files” (also within the secure environment) produced when their study code runs, to help debug any issues.
Researchers conducting projects do not have access to directly view any other pseudonymised patient data (i.e. [levels 1, 2 or 3](security-levels.md)).

Research Projects in OpenSAFELY cannot access or process data from patients who have registered a type 1 opt-out[^1].
This is ensured by the software (see [technical explanation](type-one-opt-outs.md)).

### Who

Researchers with permission to work on [approved projects](https://www.opensafely.org/approved-projects/).
Note: not all project researchers require access to the secure environment, some researchers only write project code, or view results that have been approved for release.

### When

While actively working on an approved project; access to the secure environment is revoked when a project finishes.

## Short Data Report Projects

### Why

As stated in the OpenSAFELY [Data Protection Impact Assessment](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice#further-information), OpenSAFELY supports projects to produce “short data reports”, which provide a carefully documented source of information on data quality that is beneficial to all users of NHS data.
These cover four key areas:

* Clinical reports describing how a specific clinical area is recorded in NHS data.
* Demographic reports describing population characteristics and how they can be identified.
* Administrative reports describing patterns in NHS data.
* Methodological reports describing data processing techniques for NHS data.

### What

These projects are subject to the same approvals process as Research Projects, and are run via the standard OpenSAFELY Reproducible Analytical Pipeline.

Short Data Report Projects in OpenSAFELY cannot access or process data from patients who have registered a type 1 opt-out[^1].
This is ensured by the software (see [technical explanation](type-one-opt-outs.md)).

### Who

Researchers with permission to work on [approved Short Data Report Projects](https://www.opensafely.org/approved-projects/).

### When

While actively working on an approved Short Data Report Project.

## Co-Piloting Service

### Why

All external researchers using the OpenSAFELY platform are enrolled onto the OpenSAFELY Co-Pilot Service, which pairs external researchers (“pilots”) with an experienced OpenSAFELY researcher (“co-pilot”).
Co-pilots help new pilots get set up and learn how to use the platform appropriately.
They also review that projects are in-line with the stated purpose, and remind pilots of the OpenSAFELY principles and ways of working.

### What

As part of the services offered by the OpenSAFELY Co-Pilot Service, co-pilots may help pilots by contributing code to their study on GitHub.
It is also possible that a co-pilot might need to view the output files of a pilot's project on the secure environment ([level 4 data](security-levels.md)) for purposes such as troubleshooting issues with code and helping with the process of requesting release of results files, such as applying the appropriate statistical disclosure controls.
A co-pilot may also need to review the results files (both on the secure environment and those released to Job Server) when reviewing a pilot's paper/report for publication, to check that the correct processes have been followed and that all associated analyses and results are in line with the IG agreements.
There is no need for co-pilots to have access to any other patient data (i.e. [levels 1, 2 or 3](security-levels.md)).

### Who

OpenSAFELY Co-Pilots (experienced OpenSAFELY researchers who have been given this role).

### When

While co-piloting activities are largely focused on the first four weeks of training, co-pilots also give assistance to pilots throughout the lifecycle of the project, to help ensure that each researcher follows the correct processes and that all associated analyses and results are in line with the IG agreements.

## Checking and Release of Outputs

### Why

A key element of the OpenSAFELY service, and one of the [Five Safes](https://www.bennett.ox.ac.uk/blog/2023/03/the-five-safes-framework-and-applying-it-to-opensafely/) is “safe outputs”.
Statistical disclosure control is applied as necessary to research outputs, which then go through an [output checking process](outputs/index.md) to minimise the risk of disclosure of identifiable information before outputs are released from the secure environment.

### What

Checking research outputs requires access to aggregated study files within the secure environment ([level 4 data](security-levels.md)).
Releasing approved files requires access to trigger the file release mechanism.

### Who

OpenSAFELY Output Checkers (individuals with the skills, training and permission to hold this role).

### When

Access is required when assessing and processing an output release request from a researcher working on an active project, or a developer requesting release of a necessary output for systems integration, general development or maintenance of the system.

## Access to Preliminary Results

### Why

Researchers working on an approved project may need to share some preliminary results of their study with collaborators, for example, members of the wider research community who are not named on the project approvals documentation.
All preliminary results shared with collaborators outside the secure environment will continue to be subject to statistical disclosure controls by the OpenSAFELY output checking service.
However, in order to reduce the residual risk of re-identification (particularly due to the potential for small differences between successive outputs, which is [known to be difficult to control](https://securedatagroup.org/guides-and-resources/sdc-handbook/)), as well as to limit the risk of preliminary results being misinterpreted, we do not publish all preliminary results by default on the OpenSAFELY jobserver.
The final results used in manuscripts, reports and presentations, will be made public in line with the principles of OpenSAFELY.

### What

Collaborators may view preliminary results that have been through the output checking service and share/discuss them among themselves but must not make them publicly available.
This is covered by the OpenSAFELY [policy on sharing of results](https://www.opensafely.org/policies-for-researchers/#details-all-datasets).

### Who

Collaborators are colleagues or members of the research community (including project sponsors), who researchers working on an approved project want to consult with, but are not named on the project approvals.

### When

This collaborative work may happen at any time while a project is actively being worked on, but is most likely in the later stages while preparing a paper/report for publication.
Approved researchers are responsible for ensuring that their collaborators work within the policy on sharing of results.

## Development and Maintenance

Activities related to systems integration, general development and maintenance of the systems that require data access or processing can be split into four types:

* End-to-end testing of OpenSAFELY
* Technical support for approved projects
* Development and maintenance of backend systems
* Data development

This work may be done by individuals in different roles:

* Platform Developers (responsible for the core platform; for the avoidance of doubt, this does not mean responsibility for the GP systems or the security controls and databases/servers/cloud services used by the GP suppliers.)
* Platform Testers (testing current or new features of the platform, and/or quality assurance)
* Dataset Developers (experienced data scientists/analysts with specific skills and/or knowledge of a specific dataset)

## End-to-end testing of OpenSAFELY

### Why

For software development and maintenance purposes, it is sometimes necessary to execute OpenSAFELY [project pipelines](actions-pipelines.md#project-pipelines).
The test project pipelines are necessary to:

* ensure that the entire OpenSAFELY platform is operating correctly
* verify that changes to the software work correctly in deployed systems

### What

There is a small set of test studies that can be executed via dedicated projects designed for testing purposes.
The principal project among them is the [OpenSAFELY Internal](https://jobs.opensafely.org/datalab/opensafely-testing/) project.
These studies have pipelines that use the standard OpenSAFELY tooling, but which are designed to test and assess the platform’s functionality rather than to answer research questions.

Because they are standard OpenSAFELY pipelines, they benefit from all the same security controls as OpenSAFELY research pipelines, including:

* publication of all code that is run
* logging of all operations
* manual checking of outputs for disclosivity before they are released from the backend

Access to the OpenSAFELY platform to view [level 4 data](security-levels.md) will also be required to verify the pipeline outputs are as expected.

Because the OpenSAFELY platform makes it possible to query data from patients who have a type 1 opt-out under approved conditions, it may be necessary for developers to run end-to-end tests that include these patients’ data.
This is to ensure that all studies run correctly and that the mechanisms for excluding access to these patients’ data are operating correctly.

### Who

The test studies can only be run by OpenSAFELY Platform Developers, Platform Testers and Dataset Developers with appropriate permissions (see definitions above).

### When

These test pipelines are run periodically as is necessary to check that the system is working properly. They are also run when updated software has been deployed.
However this deployment only happens after new versions of the software have been carefully tested with simulated data, to ensure that they are functioning correctly and that the security characteristics of the platform are maintained.
During development of new features, test projects may be run via the pipeline to check if that feature functions as expected with real data.

## Technical support for Approved Projects

### Why

Researchers conducting Research Projects or Short Data Report Projects may need technical assistance if there are errors or problems when attempting to run their [project pipelines](actions-pipelines.md#project-pipelines).
The issues may have been introduced by system failures or bugs in the platform or by errors made by the researchers themselves.

### What

As part of the exploration and/or resolution of a technical issue, OpenSAFELY Platform Developers may need to amend the study code and/or re-run the project pipeline for the Approved Project.
They will also need to view the outputs ([level 3 and 4 data](security-levels.md)), to check for error resolution.

### Who

Running project pipelines may be done by OpenSAFELY Platform Developers without requiring them to be named as researchers on the Approved Project.

### When

This will be necessary if errors or other problems running study code are identified.

## Development and maintenance of backend systems

### Why

To ensure the correct operation of the platform, it is sometimes necessary to directly access OpenSAFELY backend systems so that:

* software can be reconfigured or updated
* problems which only manifest themselves in the deployed system can be investigated

### What

Access to backend systems is via secure, authenticated, encrypted channels. This process gives access to:

* the OpenSAFELY software running in the backend
* logs that the OpenSAFELY software produces
* pseudonymised patient data ([level 1](security-levels.md#level-1-gps-are-data-controllers-of-the-data) and [level 2](security-levels.md#level-2-nhs-england-are-data-controllers-of-the-data))
* intermediate outputs (study dataset) ([level 3 data](security-levels.md#level-3-nhs-england-are-data-controllers-of-the-data))
* unchecked, unreleased aggregated study outputs ([level 4 data](security-levels.md#level-4-nhs-england-are-data-controllers-of-the-data)).

This policy does not allow the extraction of pseudonymised patient data or study outputs from the system via this process; the data can only be studied within the system itself.
Some operational data may be released under controlled conditions, as detailed in a separate Operational Data Policy.

Because the OpenSAFELY platform makes it possible to query data from patients who have an active type 1 opt-out under approved conditions, it may be necessary for developers to access and/or query data that includes these patients’ data.
This is to ensure that all studies run correctly and that the mechanisms for excluding access to these patients’ data are operating correctly.

### Who

Direct access to the OpenSAFELY backend systems is only available to OpenSAFELY Platform Developers, Platform Testers and Dataset Developers with appropriate permissions (see definitions above).
Access to particularly sensitive parts of the system are limited to the minimally required set of individuals, and direct access to query the pseudonymised patient data is only allowed by a small number of Platform Developers in the general case; and Dataset Developers _with specific approval_.

### When

This process is routinely used for updating the platform with new software versions.
It is exceptionally used for investigating outages or other problems, and only when the information necessary for the investigation can’t be accessed from outside the system.

## Data development

### Why

In order to provide datasets to researchers, we need to ensure that we understand the structure and semantics of the data so that we can enable researchers to write valid queries and provide them with accurate information about the datasets.

### What

Depending on the requirements of the work, Data Development may be done via the standard OpenSAFELY Reproducible Analytical Pipeline or may require different methods of access.

Some aspects of this work require direct access to the pseudonymised patient data ([level 1 and 2](security-levels.md)).
Access to backend systems is via secure, authenticated, encrypted channels. All access to the system and database operations are logged.

Because the OpenSAFELY platform supports projects that may include data from patients who have an active type 1 opt-out, it may be necessary to include these patients’ data in this development work.
This is to ensure that queries against the dataset that includes type 1 opt-out patients’ data remain valid and the metadata is correct.

### Who

Data development work may be done by OpenSAFELY Platform Developers or Dataset Developers with appropriate permissions (see definitions above)

### When

Data development activities may be carried out:

* when new datasets are added to OpenSAFELY
* when datasets are updated
* when previously unused fields in existing datasets are put to use
* periodically for data quality assurance and sense checking purposes


## Notes

[^1]: A number of projects were permitted to use this data, during the Covid-19 Pandemic. Those legacy projects have been given permission to use that data until their completion. Details of these projects are included within the [Data Protection Impact Assessment](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice#further-information).
