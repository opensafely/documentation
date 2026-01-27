## Background

The [national data opt-out](https://digital.nhs.uk/services/national-data-opt-out/operational-policy-guidance-document)
applies to the disclosure of confidential patient information
for purposes beyond individual care across the health and adult social care system in England.

The national data opt-out does not apply to the
[OpenSAFELY COVID-19 Service](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice)
or the [OpenSAFELY Data Analytics Service](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-data-analytics-service).
The opt-out does not apply to anonymous data.
System suppliers pseudonymise the data prior to queries being run in the services
and only anonymous aggregate data is shared with users of the services once it has been output checked.

In certain limited circumstances, and where ethics approvals support it,
an OpenSAFELY Data Analytics Service project may wish to apply the national data opt-out,
notwithstanding that the service operates under an exemption to the national data opt-out policy.
This page describes the implementation of such applications.

## Technical details

### The list of patients with an active national data opt-out

The system suppliers provide a list of pseudonymous IDs for patients who do not have an active national data opt-out.
It is populated by the system supplier according to the policy agreed with NHS England.
This list is provided and stored in the secure database along with the rest of the patient data.
It consists of a single bespoke table, with a single list of pseudonymous IDs and no other information.

### How is permission to access national data opt-out data determined?

The list of projects with access to national data opt-out data has been embedded into the platform's public codebase, rather than being stored in a database.
This is an unusual step from an engineering standpoint, but it means that any changes to the list are automatically included in the public audit log of code changes.
It is also automatically covered by our [code protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) which require independent sign-off by another developer for all code changes.

The [project permissions](https://github.com/opensafely-core/job-server/blob/main/jobserver/permissions/population_permissions/ndoo.py) file
and [history of changes](https://github.com/opensafely-core/job-server/commits/main/jobserver/permissions/population_permissions/ndoo.py) to it
are all publicly available on Github.

### How is permission to access national data opt-out data enforced?

In OpenSAFELY researchers do not have direct access to the data.
Instead they describe the data they require using [ehrQL](https://docs.opensafely.org/ehrql/), our Electronic Health Record Query Language,
and ehrQL is responsible for fetching it.

At the point where ehrQL needs to fetch the data,
it is told (by the system described above) whether it should include data from opted-out patients or not.

Every ehrQL query contains a "population definition"
which specifies exactly which criteria a patient must meet to be included in the result
e.g. "patients between the ages of 18 and 65 who have not recently changed GP practice".
Unless a project is named in the project permissions file,
ehrQL will automatically add an extra condition to this population definition:
the patient's pseudonymous ID number must appear in the list of ID numbers provided by the system supplier.

Again, the [code which enforces this](https://github.com/opensafely-core/ehrql/blob/6b6e5e5c3ccf997f919569101570ef59619762f0/ehrql/backends/tpp.py#L138-L150) is publicly available on Github.

### Data access which does _not_ go via ehrQL

There are two sorts of circumstances under which data access in OpenSAFELY does not go via ehrQL.

#### 1. SQL Runner

SQL Runner is a tool which allows the user to retrieve data by writing "raw" SQL rather than ehrQL.
It is intended for the data curation and investigation tasks necessary for operating the platform, rather than research purposes.
Its use is therefore limited to just those OpenSAFELY staff involved in this work.
Details of the circumstances under which OpenSAFELY staff may perform development and maintenance activities are described in our [Data Access Policy](https://docs.opensafely.org/data-access-policy/).

This is enforced by a parallel mechanism to that which controls access to out-out data via ehrQL and any changes to this policy will appear in the public [audit log](https://github.com/opensafely-core/job-server/commits/main/jobserver/permissions/sqlrunner.py).
All SQL Runner code run against patient data is also visible on our public [“jobs” server](https://jobs.opensafely.org/).

SQL Runner allows access to national opt-out data.

#### 2. Direct access to pseudonymised data

In order to facilitate the operation and maintenance of the OpenSAFELY platform a small number of individuals are able to access the pseudonymised data directly, without going via ehrQL or SQL Runner.
It is important to note that the code run in such circumstances will not be publicly visible on our “jobs” server, but it is logged in the database audit file of the GP system suppliers; preventing access to national data opt-out data is not enforceable at this level.

The circumstances under which this is permitted and the rationale are covered in detail in our [Data Access Policy](https://docs.opensafely.org/data-access-policy/) but, importantly, such access is never used for research purposes.
