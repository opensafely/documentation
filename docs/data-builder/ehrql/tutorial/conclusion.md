# ehrQL tutorial: Conclusion

---8<-- 'includes/data-builder-danger-header.md'

## Summary

Thank you for taking the time to work through this tutorial.

We hope that you found it useful and have the basic tools to start to work with Data Builder and OpenSAFELY.

!!! todo
    Consider adding a call to action for feedback?

    MkDocs for Material has options for this.
    We could also consider just having a specific form.
    Or simply requesting via the GitHub Discussions.

At this point,
you should have seen a number of concepts
useful for writing dataset definitions:

* What dataset definitions are
* How to run dataset definitions on your own computer
* What ehrQL is
* How dataset definitions relate to running queries in OpenSAFELY backends
* How to discover the data available in OpenSAFELY backends
* The different kinds of tables we work with in ehrQL: patient-level and event-level, frames and series
* The ways in which we can work with dates and handle missing values
* Using medical codelists
* How to run queries with filtering and aggregation

### Topics not covered here

To keep this tutorial from being a replica of the ehrQL reference,
we have deliberately focused on discussing just a subset of features.

Features that we have not covered include, but are not limited to:

* Setting values based on conditions with `case` and specified mappings with `map_values`
* The full range of logical, comparison and arithmetic operators
* Comparison of string values
* More ways to combine different series and values
* More advanced ways to filter series and frames
* More advanced ways to define the dataset population.

Please read through the [ehrQL reference](ehrql-reference.md)
to see examples of their use.
The reference's table of contents is a useful and comprehensive summary
of ehrQL's features.

## Where to continue learning from here

Now that you have completed this tutorial,
you may find the following resources useful
as reference for writing your own dataset definitions:

* The [ehrQL reference](ehrql-reference.md)
* The [Contracts reference](contracts-reference.md)
* Existing dataset definitions in the `opensafely` GitHub organisation
    * <https://github.com/opensafely/test-age-distribution>

!!! todo
    Can we point to real, working Data Builder examples here?

### Understanding real dataset definitions

One good way to get more familiar with ehrQL
and its capabilities
is to try reading and understanding a real dataset definition.

Dataset definitions are code,
and code can be much denser in information to read than text written in a natural language.

#### Tips for reading dataset definitions

When reading a dataset definition someone else has written,
as well as generally trying to understand what it does by following each line,
you can use an inquistive approach to try and reasonabout it:

* What is imported with the `import` lines?
  * Are there Data Builder imports that you are not familiar with?
  * Has the author used other libraries to help write their dataset definition?
* Which data `tables` are being imported
  * Can you find details of these tables
    in the [Contracts reference](contracts-reference.md)?
* How has the author structured their dataset definition?
* What criteria are used to select the population?
* How are the variables that the author extracts for the population constructed?

The author may have also given additional context in natural language in various places:

* There may be a README or other documentation in the repository
  that explains the dataset definition.
* Issues and pull requests,
  whether open or closed,
  may discuss the dataset definition.
* If the author has written good commit messages,
  there may be messages associated with the changes to the dataset definition.
* If there is a published paper associated with the repository,
  that may give additional details or context.

!!! tip
    In GitHub,
    to see the commit messages for all the commits that most recently changed a file,
    you can:

    1. Select the dataset definition file in the repository.
    2. Click the "Blame" button.
    3. You will see the file annotated with the most recent commit that changed each line.
       You can then hover on the single-line commit message summary
       to see more details, if there are any.

#### Finding existing dataset definitions

Searching for `from databuilder` will probably help you find them,
since this is the start of a common `import` line
used in dataset definitions.

You can try this [GitHub search](https://github.com/search?q=org%3Aopensafely+-repo%3Aopensafely%2Fdocumentation+%22from+databuilder%22&type=Code):
it searches the `opensafely` organisation
for repositories containing that import.

!!! todo
    Can we link to a specific suitable repository?

    Ideally, we would link to a public dataset definition that:
    * a new user might follow, so is not too complex
    * is not trivially simple

    The [test-age-distribution](https://github.com/opensafely/test-age-distribution) is too simplistic,
    but the vaccine effectiveness study in the Data Builder tests is probably too complex.

### Experimenting with the tutorial data and dataset definitions

Another good way to learn ehrQL is to experiment
by trying out [ehrQL features](ehrql-reference.md) against a simple fake dataset.
The dataset definitions and fake data that we have provided in this tutorial
are a suitable starting point.

To do so, modify an example and/or the data,
and then [run the modified example](ehrql-new-tutorial-intro.md#running-the-tutorial-code-examples).

Some ideas for inspiration:

* Look up the `count_for_patient()` method: it counts the number of events for each patient.
  Try modifying `2a_multiple_dataset_definition.py`:
    * Can you use `count_for_patient()`
      to include the number of prescriptions for each patient?
    * Can you use `take()` along with `count_for_patient()`
      to count the number of prescriptions for one particular code of your choice?
* …

!!! todo
    Add to these ideas
    and review them.

    They should mention features not covered in the tutorial
    and suggest a route to trying those features out.

## Need help?

There are a number of ways that you can [ask for help](how-to-get-help.md)
whether you need more help understanding how dataset definitions work
or with writing a specific dataset definition.
