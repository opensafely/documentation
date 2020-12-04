This part of the workflow is entirely project dependent.
You can write whatever code you like as long as it will run successfully on server, and it is possible to test this locally &mdash; see the [Testing the Code](testing-the-code) section for more details.
However, note the following restrictions / guidance:

* **Write analyses in Python, R, or Stata.**
You can can use more than one language in a single project if necessary.  You can find more information about the available libraries [here](pipelines.md#execution-environments).
* **Do not write code that requires an internet connection to run.**
Any research objects (datasets, libraries, etc) that are retrieved via the internet should be imported to the repo locally first.
If this is not possible (for instance if the object size is too large to be transferred via GitHub) then get in touch.
* **Avoid code that consumes a lot of time or memory.** The server is not an infinite resource. We can advise on code optimisation if run-times become problematic.  A good strategy is to split you processing into separate project pipeline actions; the job runner can then choose to run them in parallel if sufficient resources are available.
* **Write code that runs across different platforms.**
Since code will be run both locally and within a Linux-based Docker environment. For example use forward-slashes `/` for directories.
* **Structure your code into discrete chunks, both within scripts, and by splitting into different pipeline actions.**
This helps with:
	* readability
	* bug-finding
	* parallelisation via the project pipeline


---8<-- 'includes/glossary.md'
