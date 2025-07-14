In this section,
we will look at the OpenSAFELY project pipeline.

So far,
we have run the single dataset definition step, or *scripted action*,
using the command line with the command:

```sh
opensafely exec ehrql:v1 generate-dataset analysis/dataset_definition.py`
```

A complete OpenSAFELY study may include multiple actions.
For example, the first action might extract a dataset,
and a subsequent action might generate a table or chart from that data.

The `project.yaml` file in the study repository
defines the actions for an OpenSAFELY project pipeline.

## The `project.yaml` file

In the Visual Studio Code file Explorer,
open the `project.yaml` file by clicking on it. This file will be near the end of the list of files and folders.

You should see a tab with the following content:

```yaml linenums="1" hl_lines="5"
version: "4.0"

actions:
  generate_dataset:
    run: ehrql:v1 generate-dataset analysis/dataset_definition.py --output output/dataset.csv.gz
    outputs:
      highly_sensitive:
        dataset: output/dataset.csv.gz
```

There is a single action defined, called `generate_dataset`,
in this project pipeline.

The highlighted line is the command that the action runs,
and is very similar to the command we previously ran.

The difference is that `generate_dataset` defines an output
stored in the `output` folder.

## Running the action in the pipeline

<ol>
  <li>
   In the Visual Studio Code file Explorer,
   confirm that the <code>output</code> folder only contains a <code>.gitkeep</code> file.
  </li>

  <li>
   In the Visual Studio Code Terminal,
   type:

   ```sh
   opensafely run generate_dataset
   ```

   and press <kbd>Enter</kbd> on your keyboard to run the pipeline action.

   You should see an output that ends something like the following:

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
   <code>output/dataset.csv.gz</code>, and that it should be considered highly sensitive
   data. What you see here is exactly the same process that would happen on a real, secure
   server.
  </li>

  <li>
   When the command completes, recheck the <code>output</code> folder
   and see that it contains a <code>dataset.csv.gz</code> file.
   </li>
</ol>

### Viewing the dataset output

This `.csv.gz` file is a compressed CSV file that contains a small amount of *dummy data* (patient ID and sex)
based on the dataset definition at `analysis/dataset_definition.py`.

To view it, first run:
```
opensafely unzip output
```
then open that file (by left-clicking the filename in Visual Studio Code's Explorer, or
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
