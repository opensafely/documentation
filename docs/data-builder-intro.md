# OpenSAFELY Data Builder

---8<-- 'includes/data-builder-danger-header.md'

!!! danger

    This content has not yet been reviewed by OpenSAFELY technical
    leads. This page is *not* a definitive statement about the status of
    Data Builder, cohort-extractor or any other part of OpenSAFELY.
    
    It should be taken as potentially incorrect, until this notice is
    removed.

## Data Builder extracts cohorts for researchers

Data Builder is a tool to support development of research study code for
OpenSAFELY.

With Data Builder:

* **Researchers** can specify data they want to use in their research via a
  [*dataset definition*](dataset-definition.md).
* **Data providers** can specify data they want to offer for research
  via the [*OpenSAFELY Contracts*](contracts-intro.md)
  specification and implementation.

## Reading the Data Builder documentation

This page explains:

* What Data Builder is
* How Data Builder relates to the existing cohort-extractor
* How Data Builder works

Other pages in this section of the documentation discuss:

* Writing Data Builder dataset definitions, covering:
    * an introduction to dataset definitions
    * some guidance and examples on common uses of Data Builder
    * a comprehensive reference to what features the dataset definition
      language provides
* OpenSAFELY Contracts.

**TODO: add links when other pages written.**

## Features of Data Builder

Data Builder:

* Provides a mechanism to extract datasets from live data backends within
  the OpenSAFELY framework.
* Allows developers to provide dummy data via a CSV file. This dummy
  data can be used to develop studies. 

### How Data Builder works

Data Builder uses a *dataset definition* to specify the data to be
extracted from OpenSAFELY. The dataset definition is written in a
specific language created for Data Builder: [ehrQL](ehrql-intro.md).

For example, an OpenSAFELY dataset might compromise data on a cohort of
patients.

!!! Note "More detail for existing cohort-extractor users"

    The dataset definition used by Data Builder has the same underlying
    purpose as cohort-extractor's [study definition](study-def.md).

    To extract data, an OpenSAFELY research study would typically use one of:

    * Data Builder with a dataset definition
    * cohort-extractor with a [*study definition*]
    
    Dataset definitions have a considerably different structure from the
    study definitions. You will need to refer to the new language to write
    a dataset definition.

    Cohorts are now referred to as datasets. This accommodates the
    possibility of handling other types of data, other than purely
    patient data.
    
    The main researcher-facing change with the introduction of Data Builder is
    the new language for extracting datasets. Data Builder does not affect
    the rest of the structure of an OpenSAFELY project.
    
    The [relationship between Data Builder and
    cohort-extractor](#data-builder-and-cohort-extractor) is
    discussed further below.

## Data Builder is still in development

!!! warning

    There is considerable on-going work into Data Builder's
    design and development. Data Builder is subject to frequent change,
    indicated by its [current `v0` version](#versioning).

    We recommend that users still favour the existing [OpenSAFELY Cohort
    Extractor](study-def.md) for their research.

## Adding Data Builder to a project

The `project.yaml` below is a minimal example that only runs Data
Builder. This project also specifies:

* a dataset definition
* a dummy data file

in the locations specified in the `project.yaml`.

This project will use the dummy data file in place of a real backend.

**TODO: move this YAML to an actual project and include via snippet**
**TODO: possibly point to that entire project.**

```yaml title="Minimal Data Builder project YAML example"
version: '3.0'

actions:

  generate_dataset:
    run: >
      databuilder:v0 generate_dataset
        --dataset-definition analysis/dataset_definition.py
        --dummy-data-file dummy_data.csv
        --output output/dataset.csv
    outputs:
      highly_sensitive:
        dataset: output/dataset.csv
```

### Versioning

In the [minimal example](#using-data-builder), the version of Data
Builder was explicitly specified.

Data Builder uses [semantic versioning](https://semver.org/). Data
Builder releases use version numbers of the format `vMAJOR.MINOR.PATCH`
— for example, `v0.1.2` would have a major version of `v0`.

#### Initial release

During the initial design and development phase of Data Builder, Data
Builder has a `v0` major version. With `v0`, there are no guarantees
about backwards compatibility between versions.

Once Data Builder's design has stabilised, and it is suitable for users to
use more widely, we will release a Data Builder with version `v1`.

Any further change to the major version from `v1` onwards indicates
backwards incompatible changes. For example, a `v1` compatible study
may require some modification to work with `v2` of Data Builder.

#### Specifying a Data Builder version to use

With Data Builder, specify an [available
version](https://github.com/opensafely-core/base-docker/pkgs/container/databuilder/versions)
in your `project.yaml`, in one of the following formats:

* *major*, for example, `databuilder:v0`
* *minor*, for example, `databuilder:v0.1`
* *patch*, for example, `databuilder:v0.1.2`

* By specifying a *patch* version, your code will use the same version
  of Data Builder.
* By specifying a *major* or minor version, your code may run a newer
  version of Data Builder, once a newer major or minor version becomes
  available.
  * If running locally, you can update Docker images via the
    [OpenSAFELY CLI](opensafely-cli.md#updating-docker-images).

#### A note about the `latest` version

Research studies often specified cohort-extractor's version as `latest`.

**We no longer support specifying `latest` as a version.**

This change avoids ambiguity over precisely which Data Builder version
was used by a given study.

!!! warning
    If you do specify `latest` by mistake, you will instead see an error
    mentioning `manifest unknown`. This error tells you that the version
    is not available.

## Data Builder and cohort-extractor

## Missing features from cohort-extractor

Data Builder is intended to eventually replace the use of
cohort-extractor in new studies.

* Many features of cohort-extractor are not yet implemented.
    * The current development approach is to implement a few features in Data
      Builder fully end-to-end.
    * See the Data Builder reference (**TODO: add link**) for a complete
      list of supported features.
* Data Builder has no current way to generate dummy data.
    * You can supply a CSV file containing dummy data to Data Builder.
    * It is possible to generate dummy data via the previous
      [cohort-extractor](study-def-expectations.md).

## The development plan for cohort-extractor

cohort-extractor will continue to be supported by OpenSAFELY while Data
Builder is in this initial design phase.

Once Data Builder is ready for general use, cohort-extractor will
continue to be maintained, where possible, so that ongoing OpenSAFELY
studies can continue to be run.

However:

* New features are likely to only be added to Data Builder.
* It may become infeasible to support cohort-extractor if the
  currently supported data backends undergo considerable change.

### Why do study definitions and the cohort-extractor need replacing?

In OpenSAFELY's first two years, researchers have used cohort-extractor
and study definitions to succesfully complete a number of [research
studies](https://www.opensafely.org/research/) using [multiple data
sources and linked data](dataset-intro.md).

Data Builder is a complete redesign and reimplementation of
cohort-extractor aimed at making OpenSAFELY even easier to work with for
researchers and data providers. Data Builder's design incorporates
feedback from researchers' use of cohort-extractor.

Data Builder:

* **Provides more expressive ways** for researchers to specify cohorts.
* **Integrates external data providers more easily** by introducing
  OpenSAFELY Contracts to provide specifications for data.
* **Simplifies the implementation of new features** across multiple
  different data backends.

## Technical introduction to Data Builder's query engine

!!! note
    This section is a technical explanation for experienced users who want
    to understand more of how Data Builder works behind-the-scenes.
    
    Understanding this section is not necessary to using Data Builder.

    This section may end up being a separate page entirely.

Data Builder facilitates querying multiple different data backends,
without the researcher concerning themselves with the specific details
of how that backend works.

There are three steps to extract data on cohorts:

1. **Writing a definition**: A researcher writes a dataset definition.
   
     The dataset definition is written in Data Builder's own *domain
     specific language*, ehrQL, which is built on Python.

2. **Query transformation**: The researcher then loads that dataset
   definition into Data Builder.

     Provided the dataset definition is valid, Data Builder transforms
     the dataset definition into an internal representation of the
     query: the *query model*.

3. **Query submission**: Data Builder then translates the query model
   into the appropriate query language for the data backend being
   accessed. If the study is running on the OpenSAFELY platform, queries
   will be submitted to live data backends.

     A researcher might submit queries to multiple backends,
     where the backends use entirely different data stores. For instance,
     one backend might use Microsoft SQL Server and another Databricks.
     All this happens transparently to the researcher without the
     researcher needing to know the query language for each backend.

---8<-- 'includes/glossary.md'
