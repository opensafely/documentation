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

!!! tip
    A good way to learn ehrQL is to experiment
    by trying out ehrQL features against a simple fake dataset.
    The dataset definitions and fake data that we have provided in this tutorial
    are a suitable starting point.

    To do so, modify an example and/or the data,
    and then [run the modified example](ehrql-new-tutorial-intro.md#running-the-tutorial-code-examples).

## Need help?

There are a number of ways that you can [ask for help](how-to-get-help.md)
whether you need more help understanding how dataset definitions work
or with writing a specific dataset definition.
