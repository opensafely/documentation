# ehrQL tutorial: Remaining sections to write

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 5: Filtering and aggregation

### Filtering values

!!! todo

    * Taking/dropping rows (with an expression if possible)

### Aggregating values

!!! todo

    * `count_for_patient()`
    * `sum_for_patient()`

!!! todo

    * Aggregation of frames and series always give you a new series.
    * These series are always one row per patient.

## Example dataset definition 6: Codelists

!!! warning

    We might have to wait until fully writing this section.
    Codelists are not yet fully implemented.
    See <https://github.com/opensafely-core/databuilder/issues/31>

!!! todo
    Write an example suitable for the user testing scenario.

### Loading a codelist

!!! todo
    * Loading a codelist with `codelist_from_csv`.

### Checking if a code is in a codelist

!!! todo
    * Using `isin` and `isnotin` to check for specific codes.
