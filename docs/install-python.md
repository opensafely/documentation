## Install Python 3

\* **Please read even if you already have Python installed** \*

For security, consistency, and readability, OpenSAFELY provides an API built in [**Python**](https://www.python.org/) for using the platform. 
This API includes script-based functions for specifiying the patients and variables that make up a study dataset (using a [Study Definition](study-def.md)),
and command line functions for importing codelists, generating dummy data, and testing that the study definition can be run successfully on the server. 
Python must be installed on your machine to perform these tasks. 
The functions are provided in a Python module called `cohortextractor` which will need to be installed too &mdash; see the [cohortextractor section](cohortextractor.md) for more details.

<!--Strictly speaking, it is possible to test and run your study definition without a local installation of Python because this happens automatically every time a commit is pushed to GitHub.
However, this is not a particularly efficient way of working and we recommend being able to run the scripts locally. -->

### Windows users
For Windows users, we recommend that you install [Anaconda (Individual Edition)](https://www.anaconda.com/products/individual), a popular Python distribution that includes an recent version of Python 3, many useful Python packages, and an environment manager. 
This will help avoid some fiddly annoyances when dealing with multiple versions/installations of Python.

<!--If you already have Python installed on your machine, you should still be able install Anaconda without any inteference. <font color='red'>(is this true?)</font> Alternatively, you're welcome to use any existing or fresh Python installation you want if you're happy to troubleshoot problems yourself. -->

To install, [follow these instructions](https://docs.anaconda.com/anaconda/install/).  
Accept the default/recommended settings unless you understand the consequences of changing them.

This should have added Python and Anaconda Prompt to your machine (as well as a few other things). 
To to verify that you can run Python with Anaconda Prompt, open it and submit `python --version`.

<!--If you installed a version of python earlier than `python 3.8` then you should submit `conda install -c anaconda python=3.8` to update your installation. It can take a while (up to an hour) as it needs to identify and resolve incompatible packages from the previous installation. -->

You should use the _Anaconda Prompt_ whenever you want to run OpenSAFELY's `cohortextractor` command. 
Go to the [`cohortextractor` section](cohortextractor.md) for instructions on how to install this module. 

### mac users

<font color='red'>not yet documented</font>


---8<-- 'includes/glossary.md'
