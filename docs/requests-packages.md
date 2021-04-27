Additional R, Stata, or Python packages in OpenSAFELY must be added by the OpenSAFELY development team.
Installing packages via commands that pull the package from the internet (e.g `install.packages()` in R, `ssc install` in Stata or `pip install` in Python) won't work because internet access is restricted in the server.

## Requesting additional packages

If the package you need is not available, you can request it as follows:

* Make a new issue in the appropriate tracker (see below).
* Explain the rationale
* Get another member of the support group to chip in on the issue (e.g. do they agree; do they think a different package might do the same thing better)
* Assign to Simon when discussion finished.

### Requesting additional R packages

You can view all installed packages and their versions for the
[OpenSAFELY R image
here](https://github.com/opensafely-core/r-docker/blob/master/packages.csv) and [open an
issue](https://github.com/opensafely-core/r-docker/issues).

### Requesting additional Stata packages

You can [open an
issue](https://github.com/opensafely-core/stata-docker/issues).

### Requesting additional Python packages

You can view all installed packages and their versions for the
[OpenSAFELY Python image
here](https://github.com/opensafely-core/python-docker/blob/main/requirements.in) and [open an
issue](https://github.com/opensafely-core/python-docker/issues).

## Manual installation

Whilst the long-term solution in most cases should be to install additional packages properly, an occassion short-term fix is to add the required package (or individual functions) into your project repo directly and load/import them manually.
This will only be feasible if the functions do not have a complex hierarchy of dependencies.
For instance, in many cases, Stata packages can be added by copying the relevant `ado` files into the project repo.

Either way, you should make an Issue for the package so that other users are aware of the package's history in OpenSAFELY.



---8<-- 'includes/glossary.md'
