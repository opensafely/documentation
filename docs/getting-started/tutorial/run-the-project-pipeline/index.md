Now you're ready to run your first study. Ensure your current directory is your newly-cloned
study repository, and run:

```shell-session
$ opensafely run run_all
```

pressing ++enter++ once you've typed the command.

The first time you run this command, it may take a while to download the
required software. Eventually, you should see output that ends something like
this:

```shell-session
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

This `.csv.gz` file is a compressed CSV file that contains a small amount of *dummy data* (patient ID and sex)
based on the dataset definition at `analysis/dataset_definition.py`.

To view it, first run `opensafely unzip output`, then open that
file (by left-clicking the filename in Visual Studio Code's Explorer, or
software like Excel). You'll see that it contains rows for ten
randomly-generated dummy patients.

## Accessing files

The Visual Studio Code editor has a file Explorer that you can use
to browse the files and appears when first starting the GitHub
codespace. It is accessed by the file icon in the bar on the
left-hand side of the editor.

Clicking on a file name in the Explorer will open the file in a tab
within the editor.
