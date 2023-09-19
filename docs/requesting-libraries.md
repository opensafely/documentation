Additional R, Stata, or Python packages in OpenSAFELY must be added by the OpenSAFELY development team.
Installing packages via commands that pull the package from the internet (e.g `install.packages()` in R, `ssc install` in Stata or `pip install` in Python) won't work because internet access is restricted in the server.

**Before requesting a new package, please first check whether or not the package has already been installed!** See below for how to do this for specific languages.

## R packages

First check that the package is not already available, by [viewing all installed packages and their versions for the
OpenSAFELY R image](https://github.com/opensafely-core/r-docker/blob/master/packages.csv). If your package isn't there then [open an
issue](https://github.com/opensafely-core/r-docker/issues) to request it be added. Include the following information:

* A link to the CRAN page for the package;
* The specific package version you need, if any;
* A brief explanation of why the package is needed.

We consider the following things when deciding whether to include a new R package:

* Is the package available on [CRAN](https://cran.r-project.org/)? We don't currently support packages that are not on CRAN but feel free to open an issue if you think it warrants further discussion.
* Is the package "in scope"? In other words does the package help to process and analyse OpenSAFELY-type data, and is this clear from the request? If it's not clear what the package will be used for, we may ask for more information to justify its inclusion, so try to communicate this from the start. Out-of-scope includes:
    * Packages that are better used outside of the secure OpenSAFELY environment, for example for developing shiny apps, simulating data, or reference management.
    * Packages that cannot be used inside of the secure OpenSAFELY environment, for example for retrieving online ONS data or interacting with an SQL database.
    * Irrelevant packages, for example for free-text sentiment analysis or historical shipping forecast data.
* Does the package suggest that the user is doing something that may put a lot of strain on the server? For example bootstrapping, multiple imputation, cross-validation, pooled logistic regression, parallelisation, etc. This is usually fine, but we may want to find out more about whether this is an important component of your analysis and if there are alternatives. OpenSAFELY is a shared, finite resource and we have to consider the needs of all users.
* It it a really big package? Are there's lots of dependencies that aren't already installed? This is usually fine, but it may be worth considering if there are alternatives.
* Does the package require other software to be installed on the image? For example the [magick](https://cran.r-project.org/package=magick) package requires Imagemagick to be installed. These will be reported on the CRAN page under `SystemRequirements`. If there are additional system requirements, then the development team will need to take a look and there are no guarantees that it can be installed.
* Does the package work, or work differently, on Linux than on windows or macOS? The R image is Linux.

## Stata packages

You can [open an
issue](https://github.com/opensafely-core/stata-docker/issues) to request the package is added.

* A link to information about the package;
* The specific package version you need, if any;
* A brief explanation of why the package is needed.

## Python packages

First check that the package is not already available, by [viewing all installed packages and their versions for the OpenSAFELY Python image](https://github.com/opensafely-core/python-docker/blob/main/requirements.in). If your package isn't there then [open an
issue](https://github.com/opensafely-core/python-docker/issues) to request it be added. Include the following information:

* A link to information about the package;
* The specific package version you need, if any;
* A brief explanation of why the package is needed.

## Manual installation

Whilst the long-term solution in most cases should be to install additional packages properly, a short-term fix is to add the required package (or individual functions) into your project repo directly and load/import them manually.
This will only be feasible if the functions do not have a complex hierarchy of dependencies.
For instance, in many cases, Stata packages can be added by copying the relevant `ado` files into the project repo.

Either way, you should make an issue for the package so that other users are aware of the package's history in OpenSAFELY.



---8<-- 'includes/glossary.md'
