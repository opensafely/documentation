In this section,
we will look at the OpenSAFELY project pipeline.

So far,
we have run the single dataset definition step, or *scripted action*,
using the command line with the command:

```sh
$ opensafely exec ehrql:v1 generate-dataset analysis/dataset_definition.py`
```

A complete OpenSAFELY study may include multiple actions.
For example, the first action might extract a dataset,
and a subsequent action might generate a table or chart from that data.

The `project.yaml` file in the study repository
defines the actions for an OpenSAFELY project pipeline.

## The `project.yaml` file

In the Visual Studio Code file Explorer,
open the `project.yaml` file by clicking on it.

You should see a tab with the following content:

```yaml linenums="1" hl_lines="9"
version: "3.0"

# Ignore this `expectations` block. It is required but not used, and will be removed in future versions.
expectations:
  population_size: 1000

actions:
  generate_dataset:
    run: ehrql:v1 generate-dataset analysis/dataset_definition.py --output output/dataset.csv.gz
    outputs:
      highly_sensitive:
        dataset: output/dataset.csv.gz
```

There is a single actions defined called `generate_dataset`
in this project pipeline.

The highlighted line is the command that the action runs,
and is very similar to the command we previously ran.

The difference is that `generate_dataset` defines an output
stored in the `output` folder.

## Running the action in the pipeline

1. In the Visual Studio Code file Explorer,
   confirm that the `output` folder is empty.

2. In the Visual Studio Code Terminal,
   type:

   ```sh
   $ opensafely run generate_dataset
   ```

   and press ++enter++ to run the pipeline action.

   You should see output that ends something like the following:

   ```
   <...several lines of output...>
   generate_dataset: Extracting output file: output/dataset.csv.gz
   generate_dataset: Finished recording results
   generate_dataset: Completed successfully
   generate_dataset: Cleaning up container and volume

   => generate_dataset
      Completed successfully

      log file: metadata/generate_dataset.log
      outputs:
        output/dataset.csv.gz  - highly_sensitive
   ```

   The final line tells you a file of (randomly-generated) patient data has been created at
   `output/dataset.csv.gz`, and that it should be considered highly sensitive
   data. What you see here is exactly the same process that would happen on a real, secure
   server.

3. When the command completes,
   recheck the `output` folder
   and see that it contains a `dataset.csv.gz` file.

### Viewing the dataset output

This `.csv.gz` file is a compressed CSV file that contains a small amount of *dummy data* (patient ID and sex)
based on the dataset definition at `analysis/dataset_definition.py`.

To view it, first run `opensafely unzip output`, then open that
file (by left-clicking the filename in Visual Studio Code's Explorer, or
software like Excel). You'll see that it contains rows for ten
randomly-generated dummy patients.

## The difference between `opensafely exec` and `opensafely run`

Both `opensafely exec` and `opensafely run` can run actions.

The difference between them is that:

* `opensafely exec` runs actions *outside* of the project pipeline
  and is useful for quick feedback during interactive development
* `opensafely run` runs actions *inside* the project pipeline -
  that is, just as they would be in the secure OpenSAFELY environment
  containing real patient data

---

* Previous: [Update the dataset definition](../update-the-dataset-definition/index.md)
* Next: [Add a scripted action to the pipeline](../add-a-scripted-action-to-the-pipeline/index.md)
