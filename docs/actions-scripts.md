The most common kind of action is a scripting action.

Generally-speaking, you can write whatever code you like as long as it will run successfully on server, and it is possible to [test this locally](actions-pipelines.md#running-your-code-locally).
However, note the following restrictions and guidance:

* **Write analyses in Python, R, or Stata.**
You can can use more than one language in a single project if necessary.  You can find more information about the available libraries below.
* **Do not write code that requires an internet connection to run.**
Any research objects (datasets, libraries, etc.) that are retrieved via the internet should be imported to the repo locally first.
If this is not possible (for instance if the object size is too large to be transferred via GitHub) then get in touch.
* **Avoid code that consumes a lot of time or memory.** The server is not an infinite resource. We can advise on code optimisation if run-times become problematic.  A good strategy is to split your processing into separate project pipeline actions; the job runner can then choose to run them in parallel if sufficient resources are available.
* **Write code that runs across different platforms.**
Since code will be run both locally and within a Linux-based Docker environment. In practice, this just means ensuring you use forward-slashes `/` for directories.
* **Structure your code into discrete chunks, both within scripts, and by splitting into different pipeline actions.**
This helps with:
	* readability
	* bug-finding
	* parallelisation via the project pipeline


## Execution environments

OpenSAFELY currently supports Stata, Python, and R for statistical analysis.

For security reasons, available libraries are restricted to those provided by the framework, though you can [request additions](requests-packages.md).

The framework executes your scripts using Docker images which have been preloaded with a fixed set of libraries.
These Docker images have yet to be optimised; if you have skills in creating Dockerfiles and would like to help, get in touch!

### Stata

We currently package version 16.1, with `datacheck`, `safetab`, and `safecount` libraries installed; when installed, new libraries will appear [in the stata-docker GitHub repository](https://github.com/opensafely-core/stata-docker/tree/master/libraries).

As Stata is a commercial product, a license key is needed to use it. If you are
a member of the opensafely GitHub organisation, then the tooling will
automatically use the OpenSAFELY stata license. If not, get in touch if you
need to apply your own license and we can help.

### Python

The Docker image provided is Python 3.8, with [this list of packages installed](https://github.com/opensafely-core/python-docker/blob/main/requirements.txt).

### R

The R image provided is R 4.0, with [this list of libraries installed](https://github.com/opensafely-core/r-docker/blob/master/packages.csv).
