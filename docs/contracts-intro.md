# OpenSAFELY Contracts overview

---8<-- 'includes/data-builder-danger-header.md'

## OpenSAFELY Contracts are a clinical data specification

*OpenSAFELY Contracts* are an important OpenSAFELY concept that is
introduced with Data Builder.

This page describes:

* what OpenSAFELY Contracts are
* how OpenSAFELY Contracts relate to dataset definitions

Each OpenSAFELY Contract is a formal specification, [described in
code](https://github.com/opensafely-core/databuilder/blob/main/databuilder/contracts/contracts.py),
relating to a particular clinical data domain. OpenSAFELY Contracts are
authored by the OpenSAFELY platform developers: the Contract designs are
informed by discussion and feedback from data providers and researchers.

Researchers write dataset definitions to access data tables from
OpenSAFELY backends. All available data tables within OpenSAFELY satisfy
an OpenSAFELY Contract, regardless of which data provider operates the
backend.

TODO: does a table only satisfy one contract, or possibly multiple?

## The OpenSAFELY Contracts reference

The [OpenSAFELY Contracts reference](contracts-reference.md) has full
details of each individual Contract. When writing a dataset definition,
researchers should consult [the OpenSAFELY Contracts
reference](contracts-reference.md) to see:

* the data available in OpenSAFELY backends
* how the data is structured
* what that data represents

!!! warning
    OpenSAFELY Contracts apply only when accessing OpenSAFELY data using
    *dataset definitions*, written to run with Data Builder. Contracts
    do not apply to *study definitions* written for the existing cohort
    extractor.

## The goals of OpenSAFELY Contracts

Contracts make it easier for:

* *Researchers* to understand what data is available in
  OpenSAFELY and how that data is represented.
* *Data providers* to structure their data for OpenSAFELY.
* *OpenSAFELY's developers* to extend OpenSAFELY to additional
  healthcare and clinical data domains in future.

!!! note
    OpenSAFELY Contracts are a new concept still being explored.

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

## Common and Custom Contracts

Data backends that are accessible via OpenSAFELY provide data tables. Each
data table satisfies an OpenSAFELY Contract.

There are two types of Contracts:

* **Common Contracts**, required by all OpenSAFELY backends and covering
  core clinical data domains
* **Custom Contracts**, offered by just some backends and covering more
  specialised clinical data domains

Both the structure of the Contracts and the method of accessing
associated tables is the same for both Common and Core Contracts.

### Common Contracts

All OpenSAFELY backends satisfy Common Contracts.

There will be several different Common Contracts available with the
initial release of Data Builder. More Common Contracts may be added in
future.

!!! warning
    Some backends might deviate slightly from the suggested OpenSAFELY
    behaviour shared by most backends. Refer to the [OpenSAFELY
    Contracts Reference](contracts-reference.md) for backends you intend
    to access with your dataset definition.

For dataset definitions that only access tables defined by Common
Contracts, those dataset definitions should be largely compatible with all
OpenSAFELY backends.

### Custom Contracts

Some backends may offer particularly specialised data that is not yet
covered by a Common Contract. *Custom Contracts* allow individual
backends to still offer this data via OpenSAFELY.

!!! warning
    Using Custom Contracts might tie a dataset definition more closely
    to a specific backend, than if just Common Contracts are used. This
    also depends on how the dataset definition is designed.

!!! note
    Should additional data providers want to offer data that closely resembles
    an existing *Custom* Contract, OpenSAFELY developers would consider a new
    *Common* Contract.

## Reading an OpenSAFELY Contract

!!! note
    Refer to the [OpenSAFELY Contracts
    Reference](contracts-intro#the-opensafely-contracts-reference) for
    the details of specific contracts.

Each OpenSAFELY Contract relates to a specific domain of health record
data. The name of the Contract indicates the data domain covered by the
Contract. Tables that satisfy these Contracts can be accessed in a
dataset definition via [Data Builder's query language,
ehrQL](ehrql-intro.md).

An OpenSAFELY Contract provides the following information:

* the **variable names**. Each variable is denoted by the
  identifier you use to access the variable in ehrQL.
* the **variable's description**. The description summarises what the
  variable represents.
* the **variable's data type**. For instance, a variable
  might be one of the following:
    * integer type
    * floating point type
    * date type
    * string type
    * or some other type not in this list
* the **additional constraints on the variable's data values**, other
  than those given by the variable's type. For instance,
    * the variable might be of date type, but all values are the first
      of the month
    * the variable might be of integer type, but all values are positive
      integers

## Miscellaneous TODOs

* TODO: Should we refer to columns or variables?
* TODO: Finalise details above based on what we actually display. Do we
  know all the variable types, or can we link to them?
* TODO: Do we want to have nulls as a constraint or as a separate
  column in the reference?
* TODO: How are deviations noted in the reference? Is this via a note
  within the same contract? Or are we going to document the same
  contract multiple times for different providers.
* TODO: Where do we document about how to validate which backends run a
  definition?
* TODO: Do we need anything on Contract versioning right now? How does
  versioning work?

## For backend data providers

* TODO: Does content for backend providers go here or another page?
* TODO: What is the process by which new contracts could be proposed?
* TODO: Where do we describe the integration process for
  data providers?

---8<-- 'includes/glossary.md'
