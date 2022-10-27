# OpenSAFELY Data Builder

---8<-- 'includes/data-builder-danger-header.md'

!!! danger

    This content has not yet been reviewed by OpenSAFELY technical
    leads. This page is *not* a definitive statement about the status of
    Data Builder, cohort-extractor or any other part of OpenSAFELY.

    It should be taken as potentially incorrect, until this notice is
    removed.

## Data Builder constructs datasets for researchers

Data Builder is a tool to construct your dataset to use for research studies
and analysis using OpenSAFELY.

With Data Builder:

* **Researchers** can specify data they want to use in their research via a
  [*dataset definition*](dataset-definition.md).
* **Data providers** can specify data they want to offer for research
  via the [*OpenSAFELY Contracts*](contracts-intro.md)
  specification and implementation.

## Features
### Readable dataset definitions

A new query language [ehrQL](ehrql-intro.md) has been developed for 
Data Builder. Researchers can now use a *dataset definition* to specify 
the data to be extracted from OpenSAFELY. 

ehrQL is designed to be semantically easy to 
read and understand how the dataset it is defining is constructed. 

### Multiple backends

Data Builder facilitates querying multiple different data backends,
without the researcher concerning themselves with the specific details
of how that backend works. This means that a researcher only need 
to write a dataset definition once and be able to use this to 
query different datasets. 

### Researcher-provided dummy data
Data Builder allows researchers to provide their own dummy data to 
use to developer their analytical code against. 

## Why Data Builder was created
For researchers familiar with OpenSAFELY, there is naturally a question as 
to why we are writing software to replace cohort extractor. Data Builder is 
intended to eventually replace the use of cohort-extractor in new studies.

In OpenSAFELY's first two years, researchers have used cohort-extractor
and study definitions to successfully complete a number of [research
studies](https://www.opensafely.org/research/) using [multiple data
sources and linked data](data-sources/intro.md).

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

For more information on how Data Builder and Cohort Extractor compare, 
see [development plan for Data Builder](databuilder-vs-cohortextractor.md).

## Reading the Data Builder documentation
Other documentation pages explain in more detail the concepts to write a
dataset definition:

* Data Builder [quick start](data-builder-quick-start.md)
* Writing a [dataset definition](dataset-definition.md)
* The [dataset definition language, ehrQL](ehrql-intro.md)
* The [OpenSAFELY Contracts](contracts-intro.md) that define what data
  is available from the various OpenSAFELY data backends.

## Data Builder is still in development

!!! warning

    There is considerable on-going work into Data Builder's
    design and development. Data Builder is subject to frequent change,
    indicated by its [current `v0` version](#versioning).

    We recommend that users still favour the existing [OpenSAFELY Cohort
    Extractor](study-def.md) for their research.




---8<-- 'includes/glossary.md'
