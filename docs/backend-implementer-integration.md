# Guidance for data backend implementers integrating into OpenSAFELY

---8<-- 'includes/data-builder-danger-header.md'

!!! warning

    This page is not yet complete.

    More complete guides on working with OpenSAFELY Contracts for
    external data providers will eventually be documented more fully here.

## Introduction

For a backend implementer to offer new data for OpenSAFELY, there are
two technical requirements:

1. The data being offered must satisfy [OpenSAFELY
   Contracts](contracts-intro.md).
2. The backend must have an [implementation in OpenSAFELY Data
   Builder](data-builder-intro.md).

## Implementing existing OpenSAFELY Contracts

The existing [Contracts reference](contracts-reference.md) provides data
specifications for both OpenSAFELY users and backend implementers.

An OpenSAFELY backend implements one or more of these specifications.
Each specification pertains to a specific health care data domain.

For each data column in a Contract, the Contract details:

* column name
* data description
* data type
* any constraints

Refer to those specifications when preparing data tables for integration
with OpenSAFELY.

### What if provided data does not exactly match the relevant Contract?

Structuring data in line with OpenSAFELY Contracts makes it easier for
researchers using OpenSAFELY to run studies across multiple data
backends. However, there may be administrative or technical reasons why
backend implementers cannot satisfy a Contract precisely.

Some deviation from the Contract is permitted.

TODO: What needs to be done if there is deviation? Is this following
discussion and approval by OpenSAFELY?

TODO: What counts as permitted deviation and what counts as a breach of
the Contract?

## Proposing new OpenSAFELY Contracts

!!! note

    OpenSAFELY Contracts are still in an initial design and
    implementation phase. We already have designs for additional
    Contracts that will be implemented in future.

If no existing Contract corresponds to a healthcare data domain that you
wish to offer, [please email our technical team to
discuss](mailto:tech@opensafely.org). This may involve the creation of a
new [Custom Contract](contracts-intro.md#common-and-custom-contracts).

## Integrating a data backend into OpenSAFELY Data Builder

[OpenSAFELY Data Builder](data-builder-intro.md) is the software
component that researchers use to extract datasets of interest from
healthcare data providers in OpenSAFELY. Data Builder is a Python
application.

Data Builder abstracts the details of writing queries for researchers
away. Researchers only need be concerned with specifying the data they
want, not how to access it.

If you are a new backend implementer, [please email our technical team
to discuss Data Builder integration](mailto:tech@opensafely.org).

!!! note

    [Existing backend query implementations](https://github.com/opensafely-core/databuilder/tree/main/databuilder/backends)
    are in Data Builder's GitHub repository.

---8<-- 'includes/glossary.md'
