# ehrQL tutorial

---8<-- 'includes/data-builder-danger-header.md'

## Audience

This tutorial is aimed at:

* **new users of Data Builder**
  who wish to write dataset definitions
  to extract data from OpenSAFELY backends
* **developers involved in operating data backends**
  who wish to understand more about how OpenSAFELY backends
  are accessed by users

### Requirements

#### Background knowledge

The current implementation of ehrQL is based on Python,
but the syntax used is relatively simple.

This tutorial assumes that you have a little familiarity with:

* programming or scripted data analysis,
  whether that is in Python, R, Stata or any other language.
* querying databases or other data stores

Familiarity with:

* OpenSAFELY
* How [electronic healthcare records are structured](data-sources/intro.md)

would also be helpful,
but is *not* essential.

#### Installed software

If you wish to run the tutorial code yourself, …

!!! todo

    Decide how we expect someone to run this tutorial.

    We have at least four possible routes:

    1. a Python installed `databuilder` package
        * \+ does not require Docker
        * \+ easy to always point someone to the latest version
             via `pip install` from GitHub `main` branch
        * \- requires suitable Python installation
        * \- may lead to more technical support issues
             due to Python version incompatibilities
    2. the `databuilder` Docker image
        * \+ easy to start if you have Docker
        * \+ doesn't require a Python install
        * \- requires Docker
        * \- requires some manual wrangling to get files in
    3. `opensafely-cli`
        * \- requires the addition of a `project.yaml`
             which is more about an OpenSAFELY study,
             than ehrQL itself
        * \- requires Docker
        * \- is there a way of using this to run a project without outputs?
             (not currently)
    4. via Gitpod or similar
        * \+ does not require any installation
        * \- another thing to maintain
        * \- unavailable in some networks

    We could specify one or more of these.

    The ideal would probably be none of these
    and instead be an in-browser tool
    that allows you,
    without installation, to:

    * load sample data,
    * edit a dataset definition,
    * process the sample data with that dataset definition
    * display and/or save the results

## Running the tutorial code examples

!!! todo

    * Explain how to download sample data.
    * Explain how to load that sample data.
    * Examples

## A minimal dataset definition

We provide Data Builder with a dataset definition to extract data from an OpenSAFELY backend.

This is a minimal, but still valid, dataset definition:

!!! todo

    May need to fix up how this code is included.

```python
---8<-- "databuilder/wip-dataset-definitions/dataset_definition_minimal.py"
```

!!! todo

    Test this is correct.

We always need to create a dataset that is has the name `dataset`.
Lines of the format `from… import…` specify which of Data Builder's code and features we are using in our dataset definition.


!!! todo

    Use code annotations to describe the code.

