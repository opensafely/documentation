The most common kind of action is a scripted action.

Generally-speaking, you can write whatever code you like as long as it will run successfully on server, and it is possible to [test this locally](actions-pipelines.md#running-your-code-locally).

However, note the following restrictions and guidance:

* **Write analyses in Python, R, or Stata.**
You can can use more than one language in a single project if necessary.  You can find more information about the available libraries below.

* **Do not write code that requires an internet connection to run.**
Any research objects (datasets, libraries, etc.) that are retrieved via the internet should be imported to the repo locally first.
If this is not possible (for instance if the object size is too large to be transferred via GitHub) then get in touch.

* **Avoid code that consumes a lot of time or memory.** The server is not an infinite resource. We can advise on code optimisation if run-times become problematic.  A good strategy is to split your processing into separate project pipeline actions; the job runner can then choose to run them in parallel if sufficient resources are available.

* **Write code that runs in the OpenSAFELY platform.**
Code will be run within a Linux-based Docker environment. In practice, this just means ensuring you use forward-slashes `/` for directories.

* **Structure your code into discrete chunks, both within scripts, and by splitting into different pipeline actions.**
This helps with:
	* readability
	* bug-finding
	* parallelisation via the project pipeline


## Reading and Writing Outputs

Scripted actions can read and write output files that are saved in the workspace. These generally fall into two categories:
* large files of `highly_sensitive` data for use by other actions
* smaller `moderately_sensitive` outputs for review and release


### Large `highly_sensitive` output files

It is important that the right files formats are used for large data files. The wrong formats can waste disk space, execution time, and server memory. The specific formats used vary with language ecosystem, but they should always be compressed.

!!! note
    The `cohortextractor` command produces `csv.gz` outputs. `csv.gz` is the recommended output format.


=== "Python"

    ```python
    # read compressed csv output from cohortextractor
    pd.read_csv("output/input.csv.gz")

    # write compressed feather file
    df.to_feather("output/model.feather", compression="zstd")

    # read feather file, decompressed automatically
    pd.read_feather("output/input.feather")
    ```

=== "R"

    ```r
    # read compressed csv output from cohortextractor
    df <- readr::read_csv("output/input.csv.gz")

    # write a compressed feather file
    arrow::write_feather(df, "output/model.feather", compression = "zstd")

    # read a feather file, decompressed automatically
    df <- arrow::read_feather("output/input.feather")
    ```

=== "Stata"

    ```stata
    // stata cannot handle compressed csv files directly, so unzip first to a plain csv file
    // the unzipped file will be discarded when the action finishes.
    !gunzip output/input.csv.gz
    // now import the uncompressed csv using delimited
    import delimited using output/input.csv

    // save in compressed dta.gz format
    gzsave output/model.dta.gz

    // load a compressed .dta.gz file
    gzload output/input.dta.gz

    ```

### Smaller `moderately_sensitive` output files

These outputs are marked as `moderately_sensitive` in your `project.yaml`, and are available to view with [Level 4 access](level-4-server.md). Outputs can be:
* aggregate summary data
* images
* log files for debugging action code

Due to the fact that Level 4 files need to be reviewed, there are various restrictions placed on sizes and formats of files that can be released

#### File format restrictions

These are restricted so that reviewers can properly examine the outputs on the secure server.

| Type | Formats |
| --- | --- |
| Text |  `.txt`, `.log`, `.md` |
| Data | `.csv`, `.tsv`, `.json` |
| Images | `.png`, `.jpeg`, `.svgz` |
| Reports | `.html`, `.pdf` |

#### File size restrictions

There is a maximum file size of 32 MB to:

* limit the amount of data that can be accessed via Level 4
* allow a thorough review of the outputs in a reasonable time

## Execution environments

OpenSAFELY currently supports Stata, Python, and R for statistical analysis.

For security reasons, available libraries are restricted to those provided by the framework, though you can [request additions](requesting-libraries.md).

The framework executes your scripts using Docker images which have been preloaded with a fixed set of libraries.
These Docker images have yet to be optimised; if you have skills in creating Dockerfiles and would like to help, get in touch!

### Stata

We currently package version 16.1, with `datacheck`, `safetab`, and `safecount` libraries installed; when installed, new libraries will appear [in the stata-docker GitHub repository](https://github.com/opensafely-core/stata-docker/tree/master/libraries).

As Stata is a commercial product, a license key is needed to use it. 

#### If you are a member of the opensafely GitHub organisation
* If you are using Windows, then the `opensafely` command line software will
automatically use the OpenSAFELY Stata license. 
* If you are using macOS:
   1. Download and install [GitHub's command-line tool (`gh`)](https://cli.github.com/)
   2. Run `gh auth login --web`. Select the "HTTPS" option, and follow the instructions
  * The `opensafely` command line software will now automatically use the OpenSAFELY Stata license

#### All other external users

If you are not a member of the opensafely GitHub organisation, you must provide your own **Stata/MP** license. Unfortunately other Stata flavours are not yet supported; [let us know](how-to-get-help.md) if this is a problem.

1. Locate your Stata license string as follows:
   Locate a text file, called `STATA.LIC` (on Windows) or `stata.lic` (macOS and Linux) which is usually at the top level of the folder of your Stata installation:

    * On Windows machine it's usually somewhere like `C:\Program Files\Stata17`
    * On Linux, somewhere like `/usr/local/stata17/`
    * On macOS it's usually in `/Applications/Stata/`
2. Within that file, locate a license string of the format `SerialNumber!Code!Authorization!User!Organisation!VersionCode`. 
3. Set it as an environment variable using a [method appropriate to your operating system](https://chlee.co/how-to-setup-environment-variables-for-windows-mac-and-linux/). On Linux or macOS, you'd do it like this:
        ```bash
        export STATA_LICENSE='your license string'
        ```  
The `opensafely` command line software will now automatically use this Stata license.  


### Python

The Docker image provided is Python 3.8, with [this list of packages installed](https://github.com/opensafely-core/python-docker/blob/main/requirements.txt).

### R

The R image provided is R 4.0, with [this list of libraries installed](https://github.com/opensafely-core/r-docker/blob/master/packages.csv).
