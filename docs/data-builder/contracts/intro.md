# OpenSAFELY Contracts overview

---8<-- 'includes/data-builder-danger-header.md'

## OpenSAFELY Contracts are a clinical data specification

An *OpenSAFELY Contract* is a core concept in the OpenSAFELY framework.
Anyone using Data Builder should familiarise themselves with how
Contracts work.

This page describes:

* what OpenSAFELY Contracts are
* how OpenSAFELY Contracts relate to dataset definitions

Each OpenSAFELY Contract is a formal specification relating to a
particular clinical data domain.

!!! note
    For researchers, the human-readable version of each Contract is
    listed in the [Contracts reference](reference.md).

    For developers working on OpenSAFELY integrations, you can also see
    how [each Contract is specified in Python
    code](https://github.com/opensafely-core/databuilder/blob/main/databuilder/contracts/).
    **It is not necessary to understand the Contract's Python code to be
    able to use a Contract.**

OpenSAFELY Contracts are authored by the OpenSAFELY platform developers:
the Contract designs are informed by discussion and feedback from [data
providers](data-provider-integration.md) and researchers.

### How do OpenSAFELY Contracts fit into OpenSAFELY?

Researchers write [dataset definitions](../dataset-definition.md) to access
data tables from OpenSAFELY backends. This minimal example code
accesses the `date_of_birth` column in the `patients` data table:

```python
---8<-- 'databuilder/snippets/ehrql.py:minimalehrqlimportpatients'
```

Dataset definitions are run using OpenSAFELY Data Builder. When running
the dataset definition against live backends on the OpenSAFELY platform,
the data requested will then be extracted.

!!! note
    The dataset definition is provided as an example only here.
    You do not need to understand how to write a dataset definition
    to follow the rest of this page.

**Data tables in OpenSAFELY backends are always related to an OpenSAFELY
Contract.** Researchers then have guarantees that data from different
data providers can be accessed and interpreted in a consistent way.

## The goals of OpenSAFELY Contracts

Contracts make it easier for:

* *Researchers* to understand what data is available in
  OpenSAFELY and how that data is represented.
* *Data providers* to structure their data for OpenSAFELY and
  auto-generate documentation for their service.
* *OpenSAFELY's developers* to extend OpenSAFELY to additional
  healthcare and clinical data domains in future.

!!! note
    OpenSAFELY Contracts are still a new concept under exploration.

    We [value
    feedback](https://github.com/opensafely/documentation/discussions)
    from both OpenSAFELY users and data providers, and conversations on
    how we might further refine the design of individual OpenSAFELY
    Contracts or the system as a whole.

### The benefits of OpenSAFELY Contracts for researchers

With OpenSAFELY Contracts, researchers benefit from:

* Guarantees on the structure of the data table being queried.
* A simpler query interface to multiple backends with the ability to:
    * look up which backends provide the data of interest
    * verify which backends are compatible with their dataset definitions
    * run data definitions on multiple different backends, without
      having to write specific code for each individual backend
* More consistent documentation that:
    * describes the commonalities of the data offered by different backends
    * notes where individual backends provide data that deviates from others

## How Contracts work

Data backends that are accessible via OpenSAFELY provide *data tables*
that can be referenced in *dataset definitions*. Each data table
accessible via OpenSAFELY satisfies an OpenSAFELY Contract.

Data providers can make data available to OpenSAFELY by choosing the Contracts
that their backends will satisfy.

!!! note
    Refer to the [available OpenSAFELY data backends](data-backends.md)
    to see which backends implement which Contracts.

All Contracts share the same:

* Contract structure, made up of details about data columns
* way of accessing associated tables in Data Builder via ehrQL

### Existing Contracts

There will be several different Contracts available with the initial
release of Data Builder. More Contracts will be added in future.

!!! warning
    Some backends might deviate slightly from the suggested OpenSAFELY
    behaviour shared by most backends. Refer to the [OpenSAFELY
    Contracts Reference](reference.md) for backends you intend
    to access with your dataset definition.

### More specialised Contracts

Some backends may offer additional data that is not yet covered by the
related Contract. Some backends may even offer specialised data not yet
covered by any Contract. In these cases, a new Contract would be added.

!!! warning
    How these more specialised Contracts are labelled is to be fully
    decided.

    One possibility being discussed is via [hierarchical
    naming](#names-of-contracts), with levels in the
    hierarchy indicating:

    * that the Contract is used by a single backend only
    * and/or the organisation providing that Contract

## Reading an OpenSAFELY Contract

### The OpenSAFELY Contracts reference

The [OpenSAFELY Contracts reference](reference.md) has full
details of each individual Contract. When writing a dataset definition,
researchers should consult [the OpenSAFELY Contracts
reference](reference.md) to see:

* the data offered by each OpenSAFELY backend
* how that data is structured
* what that data represents
* how that data should be interpreted

!!! warning
    The use of OpenSAFELY Contracts applies only when writing *dataset definitions* for Data Builder.

    Contracts do not apply to [*study definitions*](../../study-def.md) written for
    our legacy cohort-extractor.

!!! warning
    OpenSAFELY Contracts are still in development and subject to
    frequent change.

### The structure of a Contract

Each OpenSAFELY Contract relates to a specific domain of health record
data. The name of the Contract indicates the data domain covered by the
Contract. Tables that satisfy these Contracts can be accessed in a
dataset definition via [Data Builder's query language,
ehrQL](../ehrql/intro.md).

An OpenSAFELY Contract provides the following information for each
associated table:

* the **column names**. Each column is denoted by the identifier you use
  to access it in ehrQL.
* the **column's description**. The description summarises what the
  column represents.
* the **column's data type**. For instance, a column's data type might
  be one of the following:
    * integer type
    * floating point type
    * date type
    * string type
    * some other type not in this list
* the **additional constraints on the column's data values**, other than
  those given by the column's type. For instance,
    * the column might be of date type, but all values are the first of
      the month
    * the column might be of integer type, but all values are positive
      integers

!!! warning
    Any additional constraints are currently provided as guidance only.
    The constraints may be true, but are *not yet automatically verified
    against the data provided by OpenSAFELY backends*.

    In future, we aim to automatically validate these constraints. Once
    implemented, this will guarantee the constraints are always true.

## The scope of OpenSAFELY Contracts

!!! warning
    The currently implemented Contracts are scoped to NHS England data.
    These Contracts are designed for use for **populations registered at
    GP practices in England**.

    Future Contracts may cover data from other organisations and
    geographic regions.

## Names of Contracts

!!! note
    Contracts are likely to eventually use a hierarchical naming system
    to:

    * indicate what domain, organisation and geography the Contract
      relates to
    * avoid name clashes

    Multiple Contracts may therefore exist that refer to a similar data
    topic, but the data in each Contract has a different structure.

    As a specific example, the current `WIP_PatientAddress` Contract may
    eventually be in a hierarchy such as `UK/NHSE/PatientAddress`. This
    distinguishes the `PatientAddress` Contract for NHS England, from a
    `PatientAddress` as used by another healthcare organisation, perhaps
    in another country, where that data may have considerably different
    attributes.

## Versioning

!!! warning
    The initial available batch of OpenSAFELY Contracts do not yet
    implement versioning. These Contracts are currently subject to
    change.

!!! note
    This note is provided only as information on the possible
    development direction of Contracts.

    The intent is for each Contract to eventually be assigned a [semantic-style
    version number](https://semver.org).

    For instance, you might choose to use version `v1.0.0` of a Contract
    such as `UK/NHSE/PatientAddress`.

    Versioning will allow the designs of each Contract to be modified,
    improved and extended, while offering backwards compatibility and
    stability for researchers and data providers.

---8<-- 'includes/glossary.md'
