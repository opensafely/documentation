# Supplying a dummy dataset

---8<-- 'includes/data-builder-danger-header.md'

Because OpenSAFELY doesn't allow direct access to individual patient
records, researchers must use a **dummy dataset** for developing and
testing their analysis code.
A dummy dataset must be:

 * similar enough to a real dataset to allow the analysis code to run
   successfully; yet
 * **not contain data relating to real patients** but be randomly (or
   pseudo-randomly) generated.

Exactly what "similar enough" means will depend on the analysis being
done.
At a minimum, the dummy dataset must have the same column names,
containing the same type of values, as in the real dataset.
Some analyses might require further properties of the dummy dataset e.g.
realistic age distributions or correlations between certain variables.

!!! note "Generating a dummy dataset"
    In future, we plan to allow Data Builder to generate suitable dummy
    data directly from a dataset definition, but for now you must generate
    your own dummy data and commit it to your git repository along with
    your code.

The path to your dummy dataset should be supplied as an argument to the
`generate_dataset` command:
```
generate_dataset --dummy-data-file path/to/dummy_data.csv ...
```

When running outside of a secure EHR vendor environment (e.g. on your
own computer or in the automated tests on Github), Data Builder
will use this dummy dataset instead of attempting to retrieve real
patient data.
It will copy the data to the same `--output` filename as it will use for
the real data.
This allows the rest of the analysis code to run in the same way whether
it is working with real or dummy data.

Data Builder will check that the column names, column order, and types
of value in the dummy dataset match what will be in the real dataset and
will raise an error if it finds a discrepancy.


## Example

```yaml title="Minimal Data Builder project YAML example"
version: '3.0'

actions:

  generate_dataset:
    run: >
      databuilder:v0 generate_dataset
       --dataset-definition analysis/dataset_definition.py
       --dummy-data-file dummy_data.csv
       --output output/dataset.csv
    outputs:
      highly_sensitive:
        dataset: output/dataset.csv
```
