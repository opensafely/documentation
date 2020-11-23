This part of the workflow is entirely project dependent. As long as you are able to create analysis code that can run on the server then you can submit it to the server. However, note the following restrictions:

* Currently OpenSAFELY supports analyses in Python, R, or Stata &mdash; see [here]() for the available packages and versions.
* You cannot run any code that uses an internet connection. Any research objects (datasets, libraries, etc) requiring an internet connection should be imported to the repo locally first.
* Be mindful of code that may consume a lot of time or memory &mdash; the server is not an infinite resource. 
* Try to structure your code into discrete chunks. This help with:
	* bug-finding
	* parallelisation via the project pipeline
