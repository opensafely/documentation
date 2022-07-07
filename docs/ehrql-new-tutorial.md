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

This tutorial assumes that you have a little familiarity with programming or scripted data analysis,
whether that is in Python, R, Stata or any other language.

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
        * \+ easy to do if you have Docker
        * \+ doesn't require a Python install
        * \- requires Docker
    3. `opensafely-cli`
        * \- requires the addition of a `project.yaml`
             which is more about an OpenSAFELY study,
             than ehrQL itself
        * \- requires Docker
    4. via Gitpod or similar
        * \+ does not require any installation
        * \- another thing to maintain
        * \- unavailable in some networks

    We could specify one or more of these.
