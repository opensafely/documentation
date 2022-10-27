There are 3 components that need to be added to a project to use 
Databuilder. These are:

1. Add Data Builder to a `project.yaml`
2. Add a Dataset definition
3. Specify a dummy data file. 

### Adding to project.yaml
The `project.yaml` below is a minimal example that only runs Data
Builder. 

We define an action, in this case, `generate_dataset` with specific configuration. 
There is more information on projects here - which are common to all OpenSAFELY 
projects. 

Specifically here we need to add:

- `--dataset-definition` - this indicates where the dataset definition file is 
- `--dummy-data-file` - this indicate the path of the dummy data file

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
#### Versioning

In the `project.yaml` above, the version of Data
Builder was explicitly specified.

Data Builder uses [semantic versioning](https://semver.org/). Data
Builder releases use version numbers of the format `vMAJOR.MINOR.PATCH`
— for example, `v0.1.2` would have a major version of `v0`.

### Adding a Dataset definition
This is the dataset defined in ehrQL. There are sections and a tutorial 
on how to specify the dataset in the ehrQL sections. Below is the basic 
example.

---8<-- 'examples/src-minimal-ehrql.md'

### Add a dummy data file
This is a CSV file of the dummy data to use with databuilder. It needs to 
be placed at the path specified above. 

