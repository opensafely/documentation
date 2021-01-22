Additional R, Stata, or Python packages in OpenSAFELY must be added by the OpenSAFELY development team.
Installing packages via commands that pull the package from the internet (e.g `install.packages()` in R or `ssc install ` in Stata) won't work because internet access is restricted in the server.

## Requesting additional R packages
The OpenSAFELY R Image ships with a given set of packages baked in. Currently the best way to see the packages that are available is to grab them from a recently-updated docker image as follows:

* Create an R script, `get_packages.R` say, with the following line:
```R
write.csv(installed.packages()[, c("Package","Version")], row.names=FALSE, file="output/installed_packages.csv")
```
* Add an action to `project.yaml` that runs this script:
```yaml
  get_packages:
    run: r:latest analysis/get_packages.R
    outputs:    
      moderately_sensitive:
        cohort: output/installed_packages.csv
```
* Run that action using `opensafely run get_packages`

This will create a CSV file containing the version of available packages in OpenSAFELY's R docker image.  If you don't run this script via `opensafely` then it will return the packages available on your local R installation, not the packages in the docker image.

If the package you need is not available, you can request it as follows:

* Make a new Issue in [https://github.com/opensafely/r-docker/issues](https://github.com/opensafely/r-docker/issues)
* Explain the rationale
* Get another member of the suppoRt group to chip in on the issue (e.g. do they agree; do they think a different package might do the same thing better)
* Assign to Simon when discussion finished.


## Requesting additional Stata packages
In many cases Stata packages can be added by copying the relevant `ado` files into the project repo. 

## Requesting additional Python packages
TODO

## Manual installation

Whilst the long-term solution in most cases should be to install additional packages properly, an occassion short-term fix is to add the required package (or individual functions) into your project repo directly and load/import them manually.
This will only be feasible if the functions do not have a complex hierachy of dependencies. 
Either way, you should make an Issue for the package so that other users are aware of the package's history in OpenSAFELY.



---8<-- 'includes/glossary.md'
