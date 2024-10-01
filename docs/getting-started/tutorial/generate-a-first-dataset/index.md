Now you're ready to run your first study.

In the terminal, type the following:

```shell-session
opensafely exec ehrql:v1 generate-dataset analysis/dataset_definition.py
```

pressing ++enter++ once you've typed the command.

This command makes use of files that already exist in the repository to generate a dummy dataset.

The first time you run this command, it may take a few seconds to download the
required software. Eventually, you should see output that contains lines like the following:

```shell-session
…
[info     ] Compiling dataset definition from analysis/dataset_definition.py
[info     ] Building dataset and writing results
…
```

followed by the dataset displayed in the terminal in CSV format.

This should look something like the following,
although the data you see will differ,
because it is randomly generated:

```
patient_id,sex
1,unknown
2,male
3,unknown
4,unknown
5,female
6,unknown
7,intersex
8,unknown
9,intersex
10,male
```

Notice the columns: `patient_id` and `sex`.

In the next part of the tutorial,
we will see how to add another data column.

---

* Previous: [Create a GitHub codespace](../create-a-github-codespace/index.md)
* Next: [Update the dataset definition](../update-the-dataset-definition/index.md)
