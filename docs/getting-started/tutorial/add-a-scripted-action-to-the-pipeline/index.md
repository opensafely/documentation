**Every** study starts with a *dataset definition* like the one you just edited.
When executed, a dataset definition generates a compressed CSV (`.csv.gz `) of patient data.

A real analysis will have several further steps after this. Each step is defined
in a separate file, and can be written in [any of the programming languages supported in
OpenSAFELY](../../../actions-scripts.md).

## Create a new action

In this tutorial, we're going to draw a
histogram of ages, using either four lines of Python or just a few more lines of R.

=== "Python"

    1. Right-click on the `analysis` folder in the editor's Explorer and select
       "New file". Type "report.py" as the filename and press ++enter++.
    2. Add the following to `report.py`:.
    ```python
    import pandas as pd

    data = pd.read_csv("output/dataset.csv.gz")

    fig = data.age.plot.hist().get_figure()
    fig.savefig("output/report.png")
    ```

=== "R"

    1. Right-click on the `analysis` folder in the editor's Explorer and select
       "New file". Type "report.R" as the filename and press ++enter++.
    2. Add the following to `report.R`:.
    ```R
    library('tidyverse')

    df_input <- read_csv(
      here::here("output", "dataset.csv.gz"),
      col_types = cols(patient_id = col_integer(),age = col_double())
    )

    plot_age <- ggplot(data=df_input, aes(df_input$age)) + geom_histogram()

    ggsave(
      plot= plot_age,
      filename="report.png", path=here::here("output"),
    )
    ```


This code reads the CSV of patient data, and saves a histogram of ages to a new file.

## Add the action to the pipline

<ol start=3>
  <li>
    Open <code>project.yaml</code> in the editor. This file will be near the end of the
    list of files and folders. This file describes how each step in your analysis should
    be run. It already defines a single <code>generate_dataset</code> action
    which defines the output that we've generated so far. This file is in a format
    called YAML: the way it's indented matters, so be careful to copy and paste the
    following carefully.
  </li>
  <li>
    Add a <code>describe</code> action to the file, so the entire file looks like this:
  </li>
</ol>

=== "Python"

    ```yaml linenums="1" hl_lines="14 15 16 17 18 19"
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

      generate_report:
        run: python:v2 python analysis/report.py
        needs: [generate_dataset]
        outputs:
          moderately_sensitive:
            chart: output/report.png
    ```

=== "R"

    ```yaml linenums="1" hl_lines="14 15 16 17 18 19"
    version: "3.0"

    # Ignore this`expectation` block. It is required but not used, and will be removed in future versions.
    expectations:
      population_size: 1000

    actions:
      generate_dataset:
        run: ehrql:v1 generate-dataset analysis/dataset_definition.py --output output/dataset.csv.gz
        outputs:
          highly_sensitive:
            dataset: output/dataset.csv.gz

      generate_report:
        run: r:latest analysis/report.R
        needs: [generate_dataset]
        outputs:
          moderately_sensitive:
            chart: output/report.png
    ```

- **Line 14** tells the system we want to create a new action called `describe`.
- **Line 15** says how to run the script (using the `python` or `R` runner).
- **Line 16** tells the system that this action depends on the outputs of the
  `generate_dataset` being present.
- **Lines 17-19** describe the files that the action creates. Line 18 says that the
  items indented below it are *moderately* sensitive, that is they may be released
  to the public after a careful review (and possible redaction). Line 19 says that
  there's one output file, which will be found at `output/descriptive.png`.


At the command line, type `opensafely run generate_report` and press
++enter++. This should end by telling you a file containing the histogram has been created.
Open the `output` folder — you can do this via Visual Studio Code's Explorer — and check that it contains `report.png`.

Double click on `report.png` to display the image,
or right-click on `report.png` and select Download to download the image.

!!! warning
    Changes you make to files are automatically saved on GitHub. However, changes will not persist
    outside of the GitHub codespace unless you *commit* and *push* them to GitHub, as described
    in the next section.
