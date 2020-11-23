This part of the workflow is entirely project dependent. 
You can write whatever code you like as long as it will run successfully on server, and it is possible to test this locally &mdash; see the [Testing the Code](testing-the-code) section for more details.
However, note the following restrictions / guidance:

* **OpenSAFELY currently supports analyses in Python, R, or Stata.** 
See [here]() for the available packages and versions.
* **You cannot run any code that uses an internet connection.** 
Any research objects (datasets, libraries, etc) requiring an internet connection should be imported to the repo locally first.
If this is not possible (for instance if the object size is too large to be transferred via GitHub) then get in touch.
* **Where possible avoid the code that consumes a lot of time or memory.** The server is not an infinite resource. 
* **Structure your code into discrete chunks.** This helps with:
	* readability
	* bug-finding
	* parallelisation via the project pipeline
