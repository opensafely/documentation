# ehrQL tutorial: Remaining sections to write

---8<-- 'includes/data-builder-danger-header.md'

## Example dataset definition 4: Data special cases

### Date handling

!!! todo

    * Specifying dates in dataset definitions
    * Manipulating dates
        * `get_year`
        * `difference_in_years`
        * `is_before`

### Missing values

!!! todo

    * Missing values are represented as nulls.
    * Checking for missing values: `is_null()`.
    * Replacing missing values: `if_null_then(0)`.
    * Sorting with missing values.

## Example dataset definition 5: Filtering and aggregation

### Filtering values

!!! todo

    * Taking/dropping rows (with an expression if possible)

### Aggregating values

!!! todo

    * `count_for_patient()`
    * `sum_for_patient()`

## Example dataset definition 6: Codelists

!!! warning

    We might have to wait until fully writing this section.
    Codelists are not yet fully implemented.
    See <https://github.com/opensafely-core/databuilder/issues/31>

### Loading a codelist

!!! todo
    * Loading a codelist with some kind of helper.

### Checking if a code is in a codelist

!!! todo
    * Using `isin` and `isnotin` to check for specific codes.
