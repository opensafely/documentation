# ehrql-tutorial-examples

This is a collection of:

* dataset definitions
* example data
* outputs from the dataset definitions run against the example data

used in the ehrQL tutorials.

## Adding a new example

Refer to existing ehrQL tutorial pages to see the current layout that we use.

The current process for adding a new example is:

1. Create a new dataset and add it to the [`example-data`](example-data/) directory,
2. Write the dataset definition and add it to this directory.
   See the [ehrQL tutorial introduction](../../docs/ehrql-new-tutorial-intro.md#using-data-builders-command-line-interface)
   for an explanation of the filename convention.
3. Build the dataset definition outputs
   (see below),
   then add and commit the new files stored in the [`outputs`](outputs/) directory to the repository.
4. Use a dataset definition in the relevant documentation page's Markdown file:
   ````
   ```python title="$YOUR_DATASET_DEFINITION_FILENAME"
   ---8<-- "databuilder/ehrql-tutorial-examples/$YOUR_DATASET_DEFINITION_FILENAME"
   ```
   ````
5. Use the `read_csv` feature of the [table-reader plugin](https://github.com/timvink/mkdocs-table-reader-plugin)
   in the relevant documentation page's Markdown file:
   to include the input and output CSVs as nicely formatted tables.

   You will need one `read_csv` entry for each CSV.

   For example:
   ```
   {{ read_csv('databuilder/ehrql-tutorial-examples/example-data/outputs/$YOUR_DATASET_DEFINITION_OUTPUT_FILENAME', keep_default_na=False) }}
   ```

   `keep_default_na=False` is to include blank table cells
   instead of the text `nan`.

## Building dataset definition outputs

The easiest way is via the relevant `just` recipe.
Consult the relevant [`justfile`](../justfile).

## Updating content

A GitHub Actions workflow checks that the dataset definition outputs are current.

If you modify existing example data or dataset definitions,
make sure that you:

* Commit the files you have directly changed.
* Rebuild the output CSVs and commit those if they have changed.
* Review all documentation pages that use the files you have edited,
  and check if any explanatory text requires amending as a result of your changes.
