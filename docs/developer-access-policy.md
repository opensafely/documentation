# OpenSAFELY Data Access Policy

## Introduction

The following policy outlines the guidelines for patient data access and processing via the OpenSAFELY platform specifically related to **access to and processing of pseudonymised and de-identified patient data** (and data derived from it).
Technical **data relating to the operation of the platform **is covered by a separate OpenSAFELY Platform Operational Data Policy.

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

Approved researchers (with appropriate permissions) can access the secure environment to view the aggregated results of their study ([level 4 data](https://docs.opensafely.org/security-levels/)); researchers ensure that appropriate statistical disclosure controls have been applied before requesting results for release.
Researchers can also view the “log files” (also within the secure environment) produced when their study code runs, to help debug any issues.
Researchers conducting projects do not have access to directly view any other pseudonymised patient data (i.e. [levels 1, 2 or 3](https://docs.opensafely.org/security-levels/)).

Research Projects in OpenSAFELY cannot access or process data from patients who have registered a type 1 opt-out[^1].
This is ensured by the software (see technical explanation).

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
This is ensured by the software (see technical explanation).

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
It is also possible that a co-pilot might need to view the output files of a pilot's project on the secure environment ([level 4 data](https://docs.opensafely.org/security-levels/)) for purposes such as troubleshooting issues with code and helping with the process of requesting release of results files, such as applying the appropriate statistical disclosure controls.
A co-pilot may also need to review the results files (both on the secure environment and those released to Job Server) when reviewing a pilot's paper/report for publication, to check that the correct processes have been followed and that all associated analyses and results are in line with the IG agreements.
There is no need for co-pilots to have access to any other patient data (i.e. [levels 1, 2 or 3](https://docs.opensafely.org/security-levels/)).

### Who

OpenSAFELY Co-Pilots (experienced OpenSAFELY researchers who have been given this role).

### When

While co-piloting activities are largely focused on the first four weeks of training, co-pilots also give assistance to pilots throughout the lifecycle of the project, to help ensure that each researcher follows the correct processes and that all associated analyses and results are in line with the IG agreements.

### Implementation Notes for Staff

(to be completed)

## Checking and Release of Outputs

### Why

A key element of the OpenSAFELY service, and one of the [Five Safes](https://www.bennett.ox.ac.uk/blog/2023/03/the-five-safes-framework-and-applying-it-to-opensafely/) is “safe outputs”.
Statistical disclosure control is applied as necessary to research outputs, which then go through an [output checking process](https://docs.opensafely.org/releasing-files/) to minimise the risk of disclosure of identifiable information before outputs are released from the secure environment.

### What

Checking research outputs requires access to aggregated study files within the secure environment ([level 4 data](https://docs.opensafely.org/security-levels/)).
Releasing approved files requires access to trigger the file release mechanism.

### Who

OpenSAFELY Output Checkers (individuals with the skills, training and permission to hold this role).

### When

Access is required when assessing and processing an output release request from a researcher working on an active project, or a developer requesting release of a necessary output for systems integration, general development or maintenance of the system.

### Implementation Notes for Staff

(to be completed)

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

### Implementation Notes for Staff

(to be completed)

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

For software development and maintenance purposes, it is sometimes necessary to execute OpenSAFELY [project pipelines](https://docs.opensafely.org/actions-pipelines/#project-pipelines).
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

Access to the OpenSAFELY platform to view [level 4 data](https://docs.opensafely.org/security-levels/) will also be required to verify the pipeline outputs are as expected.

Because the OpenSAFELY platform makes it possible to query data from patients who have a type 1 opt-out under approved conditions, it may be necessary for developers to run end-to-end tests that include these patients’ data.
This is to ensure that all studies run correctly and that the mechanisms for excluding access to these patients’ data are operating correctly.

### Who

The test studies can only be run by OpenSAFELY Platform Developers, Platform Testers and Dataset Developers with appropriate permissions (see definitions above).

### When

These test pipelines are run periodically as is necessary to check that the system is working properly. They are also run when updated software has been deployed.
However this deployment only happens after new versions of the software have been carefully tested with simulated data, to ensure that they are functioning correctly and that the security characteristics of the platform are maintained.
During development of new features, test projects may be run via the pipeline to check if that feature functions as expected with real data.

### Implementation Notes for Staff

#### Information Governance/Access Permissions

* Developer access permissions are documented in our [Developer Permissions Log](https://docs.google.com/spreadsheets/d/14vYZTTa-fQKh4GNg46yFONvk7q53Gh9e4npG_xUcAKQ/edit?usp=sharing) (_still under development_).

#### Technical Notes

* All development-related jobs should be run via our Internal (testing) project
* To minimise the use of data from patients with a type 1 opt out, jobs run via our Internal (testing) project will automatically exclude T1OO patient data when using ehrQL or cohort extractor. If, in future, we find that we need to run jobs using ehrQL/cohort extractor that include T1OO data then we can decide to either add a mechanism for this or to create a separate testing project and add it to the “allowed project list” in GitHub. For SQL Runner, instructions on how to exclude T1OO data (or explain why you haven’t) can be found in the [sqlrunner readme](https://github.com/opensafely-core/sqlrunner#type-one-opt-out-data).

## Technical support for Approved Projects

### Why

Researchers conducting Research Projects or Short Data Report Projects may need technical assistance if there are errors or problems when attempting to run their [project pipelines](https://docs.opensafely.org/actions-pipelines/#project-pipelines).
The issues may have been introduced by system failures or bugs in the platform or by errors made by the researchers themselves.

### What

As part of the exploration and/or resolution of a technical issue, OpenSAFELY Platform Developers may need to amend the study code and/or re-run the project pipeline for the Approved Project.
They will also need to view the outputs ([level 3 and 4 data](https://docs.opensafely.org/security-levels/)), to check for error resolution.

### Who

Running project pipelines may be done by OpenSAFELY Platform Developers without requiring them to be named as researchers on the Approved Project.

### When

This will be necessary if errors or other problems running study code are identified.

### Implementation Notes for Staff

#### Categorisation of Work

* Platform developers must take particular care when amending study code and running jobs on an Approved Project (as opposed to an Internal testing project) that they are not straying into _project_ development work. If a developer is helping with writing the study code and making decisions about how the study is answering its approved purpose, akin to being a researcher on the study (including Short Data Report Projects), then they must be treated just like any other researcher and go through the full IG approval process (including being named as an approved researcher on the project application and added as a member of that project on Job Server with appropriate project-level roles).

#### Information Governance/Access Permissions

* Developer access permissions are documented in our [Developer Permissions Log](https://docs.google.com/spreadsheets/d/14vYZTTa-fQKh4GNg46yFONvk7q53Gh9e4npG_xUcAKQ/edit?usp=sharing) (_still under development_).

#### Technical Notes

* Access to run jobs and view outputs on any project in Job Server is granted by assigning the _global_ ProjectDeveloper and ProjectCollaborator roles to that user
* For the avoidance of doubt, a ProjectDeveloper role does not also need to be added at the project level unless the user is also acting as a researcher on that project (see above)

## Development and maintenance of backend systems

### Why

To ensure the correct operation of the platform, it is sometimes necessary to directly access OpenSAFELY backend systems so that:

* software can be reconfigured or updated
* problems which only manifest themselves in the deployed system can be investigated

### What

Access to backend systems is via secure, authenticated, encrypted channels. This process gives access to:

* the OpenSAFELY software running in the backend
* logs that the OpenSAFELY software produces
* pseudonymised patient data ([level 1](https://docs.opensafely.org/security-levels/#level-1-gps-are-data-controllers-of-the-data) and [level 2](https://docs.opensafely.org/security-levels/#level-2-nhs-england-are-data-controllers-of-the-data))
* intermediate outputs (study dataset) ([level 3 data](https://docs.opensafely.org/security-levels/#level-3-nhs-england-are-data-controllers-of-the-data))
* unchecked, unreleased aggregated study outputs ([level 4 data](https://docs.opensafely.org/security-levels/#level-4-nhs-england-are-data-controllers-of-the-data)).

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

### Implementation Notes for Staff

#### Information Governance/Access Permissions

* Developer access permissions are documented in our [Developer Permissions Log](https://docs.google.com/spreadsheets/d/14vYZTTa-fQKh4GNg46yFONvk7q53Gh9e4npG_xUcAKQ/edit?usp=sharing) (_still under development_).
* Any work requiring SQL Management Studio (direct access to the pseudonymised database) must be done using personal database credentials
* Access to the backend server and personal database credentials for the pseudonymised database are currently managed by the IG team, and are implemented by the backend provider

#### Technical Notes

* Please also refer to our [Operational Data Policy](https://docs.google.com/document/d/1tQveWA7NWaHSx0ETR9FcXYxbtNa1NHiqwygVl6XanKw/edit)
* To minimise the use of data from patients with a type 1 opt out when using SQL Server Management Studio: SQL that excludes these patients should always be applied to queries as standard and only removed when necessary to meet the requirements of the work.

## Data development

### Why

In order to provide datasets to researchers, we need to ensure that we understand the structure and semantics of the data so that we can enable researchers to write valid queries and provide them with accurate information about the datasets.

### What

Depending on the requirements of the work, Data Development may be done via the standard OpenSAFELY Reproducible Analytical Pipeline or may require different methods of access.

Some aspects of this work require direct access to the pseudonymised patient data ([level 1 and 2](https://docs.opensafely.org/security-levels/)).
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

### Implementation Notes for Staff

#### Categorisation of Work

* Bennett Institute researchers who have also been approved as Dataset Developers must take great care to separate these activities. For example, if during work on an approved project (either a Research or a Short Data Report project) you suspect there may be an issue with the underlying raw data, you should leave your project repo and “put on your developer hat”. You should then do any exploratory work in the Internal project on Job Server, and implement any necessary changes at the platform level (e.g. updating metadata or asking for a change in ehrQL). You can then “put your researcher hat back on” and return to your project.
* The outputs of Data Development work should always be shared, so that everyone can benefit from the learning. If a report is produced that is too detailed to put onto our docs site then it must still be made available internally, so that it may be built on (and possibly made public) in future.
* How can I tell if something should be categorised as Data Development as opposed to a Short Data Report Project?
    * Data Development is usually done prior to making the dataset/variable available to researchers (e.g. the process of adding it to ehrQL) whereas Short Data Reports can only be done once the data is available
    * Data Development work can usually be done using a single dataset
    * The questions being asked will be things like:
        * What does each row represent?
        * How are missing values represented?
        * What do these codes represent?
        * Do the codes match the codebook we have been given?
        * Is there internal logical consistency (e.g. are end dates always after start dates?)
        * Does the data match the metadata that we have been given?

#### Information Governance/Access Permissions

* Access permissions for Platform Developers and Dataset Developers are documented in our [Developer Permissions Log](https://docs.google.com/spreadsheets/d/14vYZTTa-fQKh4GNg46yFONvk7q53Gh9e4npG_xUcAKQ/edit?usp=sharing) (_still under development_).
* Any work requiring SQL Management Studio (direct access to the pseudonymised database) must be done using personal database credentials
* Access to the backend server and personal database credentials for the pseudonymised database are currently managed by the IG team, and are implemented by the backend provider
* Any results/information being extracted from the secure environment (excluding that covered by our Operational Data Policy) MUST go through the usual output checking and release process
* If you want to publish a manuscript using outputs from Data Development work, you must go to Bennett Institute IG team for project approval (as a Short Data Report). Be aware that you won’t currently be able to do this using SQL Runner.

#### Technical Notes

* Data Development work may be done using any of the tools available to us (ehrQL, cohort extractor, SQL Runner or SQL Server Management Studio). However, we aim to minimise the amount of work done using direct access to the pseudonymised database and do as much of this work as possible (e.g. generating reports/metadata) using SQL Runner or ehrQL. If you are unsure about which tool you should be using please consult the Tech Team.
* Work in this category that is being conducted using ehrQL or cohort extractor should be done under the Internal project in Job Server. SQL Runner is currently restricted to only run via this Internal project.
* T1OO: In most cases, we should expect to check that the data structure and semantics are valid in the full dataset as well as the dataset that has excluded type 1 opt-out patients’ data. Reports including T1OO data should be made available internally to others doing Data Development work, but not shared more widely (generally these reports should not need to be released and can remain on the secure server).
* T1OO: If the metadata we produce includes things like counts, e.g. total number of rows, we should only publish the numbers _excluding_ T1OO patient data (historic reports will include T1OO patient data, so differences could be calculated - [this is ok](https://bennettoxford.slack.com/archives/C31D62X5X/p1712062713951799?thread_ts=1712058390.622289&cid=C31D62X5X)). Any exceptions must be agreed by the Ops team.
* T1OO exclusion:
    * ehrQL and cohort extractor jobs run on the Internal project in Job Server will currently automatically exclude T1OO patient data (see technical explanation)
    * SQL Runner: for instructions on how to exclude T1OO data (or explain why you haven’t) see the [sqlrunner readme](https://github.com/opensafely-core/sqlrunner#type-one-opt-out-data)
    * When using SQL Server Management Studio, SQL that excludes these patients should be applied to queries as standard and only removed when necessary to meet the requirements of the work


## Notes

[^1]: A number of projects were permitted to use this data, during the Covid-19 Pandemic. Those legacy projects have been given permission to use that data until their completion. Details of these projects are included within the [Data Protection Impact Assessment](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice#further-information).
