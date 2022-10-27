# Data Builder and cohort-extractor
## Missing features from cohort-extractor

* Many features of cohort-extractor are not yet implemented in Data
  Builder.
    * The current development approach is to implement a few features in Data
      Builder fully end-to-end.
    * See the [ehrQL reference](ehrql-reference.md) for a complete list
      of supported features.
* Data Builder has no current way to generate dummy data.
    * You can supply a [CSV file containing dummy data](data-builder-dummy-data.md)
      to Data Builder.
    * It is possible to generate dummy data via the previous
      [cohort-extractor](study-def-expectations.md).

## The development plan for cohort-extractor

cohort-extractor will continue to be supported by OpenSAFELY while Data
Builder is in this initial design phase.

Once Data Builder is ready for general use, cohort-extractor will
continue to be maintained, where possible, so that ongoing OpenSAFELY
studies can continue to be run.

However:

* New features are likely to only be added to Data Builder.
* It may become infeasible to support cohort-extractor if the
  currently supported data backends undergo considerable change.

!!! Note "More detail for existing cohort-extractor users"

    The dataset definition used by Data Builder has the same underlying
    purpose as cohort-extractor's [study definition](study-def.md).

    To extract data, an OpenSAFELY research study would typically use one of:

    * Data Builder with a dataset definition
    * cohort-extractor with a [*study definition*](study-def.md)

    Dataset definitions have a considerably different structure from the
    study definitions. You will need to refer to the new language to write
    a dataset definition.

    Cohorts are now referred to as datasets. This accommodates the
    possibility of handling other types of data, other than purely
    patient data.

    The main researcher-facing change with the introduction of Data Builder is
    the new language for extracting datasets. Data Builder does not affect
    the rest of the structure of an OpenSAFELY project.


