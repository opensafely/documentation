# ehrQL tutorial: Working with electronic health record codes and codelists

---8<-- 'includes/data-builder-danger-header.md'

## Electronic health record codes

Electronic health record (EHR) codes are used when recording patient events.
For research, codes are often collated into *codelists* to classify patients.
Data Builder can use codelists to help extract information about patient groups of interest.

!!! info
    There is [more information about codelists](codelist-intro.md) elsewhere in OpenSAFELY's documentation.
    We also have a codelist builder tool,
    [OpenCodelists](codelist-creation.md),
    that you may find useful when creating codelists.

## Example dataset definition 7: Codes and codelists

!!! warning
    This is a rough draft.
    It is intended as a placeholder
    so that the tutorial flows from start to finish.

!!! warning
    Codelists are not yet fully implemented.
    See <https://github.com/opensafely-core/databuilder/issues/31>

!!! todo
    Complete this tutorial page.
    Write an example that suitably explains enough for the user testing scenario.
    This is pending the use of codelists there being finalised.

### Loading a codelist

!!! todo
    Remove the placeholder example
    and replace with a real dataset definition.

You can load codelists in a comma-separated values (CSV) format with Data Builder's `codelist_from_csv()` function.
The CSV must have named columns.

You need to specify, as strings:

* the CSV filename
* the name of the CSV column containing the codes
* the coding system; this must be specified as one of the following:
  * `"BNFCode"`
  * `"CTV3Code"`
  * `"DMDCode"`
  * `"ICD10Code"`
  * `"OPCS4Code"`
  * `"Read2Code"`
  * `"SNOMEDCTCode"`

!!! todo
    Retrieve the code class names automatically.
    Where is best to specify these?

???+ example "`codelist_from_csv()`"

    ```python
    from databuilder.codes import codelist_from_csv

    codelist = codelist_from_csv(filename="my_codelist.csv", column="code", system="SNOMEDCTCode")
    ```

### Checking if a code is in a codelist

!!! todo
    Remove the placeholder example
    and replace with a real dataset definition.

!!! warning
    This example may not be correct.

You can use `isin` and `isnotin` to check for specific codes.

???+ example "Dataset definition"

    ```python
    from databuilder.codes import codelist_from_csv, SNOMEDCTCode
    from databuilder.ehrql import Dataset
    from databuilder.tables.example.tutorial import clinical_events

    codelist = codelist_from_csv(filename="my_codelist.csv", column="code", system="SNOMEDCTCode")
    a1_code = SNOMEDCTCode("a1")
    a2_code = SNOMEDCTCode("a2")

    codelist_filtered_events = clinical_events.take(clinical_events.system == "snomed").code.is_in(codelist))
    code_filtered_events = clinical_events.take(clinical.events.system == "snomed").code.is_in([a1_code, a2_code])

    dataset = Dataset()
    dataset.set_population(codelist_filtered_events.exists_for_patient() | code_filtered_events.exists_for_patient())
    ```

!!! todo
    Explain that `[…]` creates a sequence of ordered items
    termed a list in Python,
    if not mentioned elsewhere.

    We also instantiate code objects the same way we do for `Dataset()`.

### Tutorial questions

!!! question
    1. …
