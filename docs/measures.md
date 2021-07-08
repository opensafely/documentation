The Measures framework allows you to extract multiple datasets covering different time periods, and calculates a set of _measures_ for each period.

Measures are expressed as a quotient (i.e., a numerator divided by a denominator) which in practice could be used to calculate proportions, ratios, means, counts, and so on.

For example, we may wish to calculate, for each month in 2020 and each STP (administrative health regions in England), the proportion of patients who were admitted to hospital at least once and the proportion of patients who died.

Without Measures, this would require creating a set of variables (or a study definition) for each month of interest containing: the region; whether or not they were admitted to hospital; whether or not they died,
and we would then need to use these datasets to calculate the desired proportion and aggregate the results.

Measures makes this process simple.

## Defining measures

Generating measures is a three step process:

 1. **Define a study definition** that includes a `measures` variable, which should be a list of calls to the `Measure()` function.
 2. **Extract the data** by running `generate_cohort` using the `--index-date-range` option to cover the range of time periods we want to calculate the measure for.
 3. **Calculate the measures** by running `generate_measures` which takes the files extracted in step 2 and produces files like `measure_<measure_id>.csv`.


### Define a study definition

The `study_definition.py` script for the example above is:

```py
from cohortextractor import StudyDefinition, Measure, patients

study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "today"},
        "rate": "exponential_increase",
        "incidence": 0.2,
    },

    index_date="2020-01-01",

    population=patients.registered_as_of("index_date"),

    stp=patients.registered_practice_as_of(
        "index_date",
        returning="stp_code",
        return_expectations={
            "category": {"ratios": {"stp1": 0.1, "stp2": 0.2, "stp3": 0.7}},
            "incidence": 1,
        },
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    admitted=patients.admitted_to_hospital(
        returning="binary_flag",
        between=["index_date", "last_day_of_month(index_date)"],
        return_expectations={"incidence": 0.1},
    ),

    died=patients.died_from_any_cause(
        between=["index_date", "last_day_of_month(index_date)"],
        returning="binary_flag",
        return_expectations={"incidence": 0.05},
    ),
)

measures = [
    Measure(
        id="hosp_admission_by_stp",
        numerator="admitted",
        denominator="population",
        group_by="stp",
    ),
    Measure(
        id="death_by_stp",
        numerator="died",
        denominator="population",
        group_by="stp",
        small_number_suppression=True,
    ),
]
```

This differs from a normal study definition due to the addition of the `measures` object, which is a list of calls to the `Measure()` function, for each measure.

* `id` is just a string used to identify the measure output file.
* `numerator` and `denominator` are the columns in the dataset that define the measure. They must be numeric or boolean (encoded as 0 or 1).
* `group_by` column can be of any type. To calculate the measure across the entire population, you can set `group_by="population"`. If not specified, `group_by` will default to `None` and the measure will be calculated at the individual patient level.
* `small_number_suppression` is an optional boolean that defaults to `False`. If set to `True`, small numbers (greater than zero, less than or equal to five) in numerators and denominators will be replaced with blanks. If a numerator or denominator has been suppressed then the corresponding value will also be blank. In cases where numerators or denominators are suppressed but the total suppressed in a column is not greater than five, additional values will be suppressed to bring the total above five.

You can calculate measures for more than one group in a single measure by specifying multiple variables as follows:

```py
measures = [
    Measure(
        id="hosp_admission_by_stp_and_sex",
        numerator="admitted",
        denominator="population",
        group_by=["stp", "sex"],
    ),
    Measure(
        id="death_by_stp_and_sex",
        numerator="died",
        denominator=" population",
        group_by=["stp", "sex"],
    ),
]
```

## Extract the data

To run multiple study definitions over a series of dates, use the `--index-date-range` option of the `generate_cohort` command.
Rather than generating a single output CSV file this generates multiple output files across a range of dates, modifying the study's index date each time.

The range is specified as:

```
--index-date-range "YYYY-MM-DD to YYYY-MM-DD by (week|month)"
```

It also accepts `today` in place of a date.

Output files are named like: `output/input_YYYY-MM-DD.csv`

There is also a `--skip-existing` option which will cause the cohortextractor to skip the extraction step for any dates where the corresponding file already exists.
This makes it easier to incrementally extract data for new months/weeks without having to re-extract everything.

Example:

```
cohortextractor generate_cohort --index-date-range "2020-01-01 to 2020-12-01 by month"
```

...which will output:

```
output/input_2020-01-01.csv
output/input_2020-02-01.csv
...
output/input_2020-12-01.csv
```

## Calculate the measures

This is done using the `generate_measures` command:

```
cohortextractor generate_measures
```

For each defined measure, and for each file extracted in step 2, this generates an output file with the measure calculated for that month or week.

    output/measure_hosp_admission_by_stp_2020-01-01.csv
    output/measure_death_by_stp_2020-01-01.csv
    output/measure_hosp_admission_by_stp_2020-02-01.csv
    output/measure_death_by_stp_2020-02-01.csv
	...
    output/measure_hosp_admission_by_stp_2020-12-01.csv
    output/measure_death_by_stp_2020-12-01.csv

Finally, for each measure, it combines all the output into a single file with an additional `date` column indicating the date associated with each row.

    output/measure_hosp_admission_by_stp.csv
    output/measure_death_by_stp.csv

This command also respects the `--skip-existing` flag.
This will prevent it from recalculating the measure for any months or weeks which have already been calculated.
However the final step, which combines output across time periods, will always be run.

This command accepts an `--output-dir` argument, which defines the directory in which the output measure files will be created. 
If the `--output-dir` argument is configured, `generate_measures` expects the input cohort files to also be in the output directory. To ensure this, include the same `--output-dir` argument in the previous `generate_cohort` step.

## Putting it all together in a pipeline

To generate the final outputs `measure_hosp_admission_by_stp.csv` and `measure_death_by_stp.csv` in a project pipeline, you would use the following actions:


```yaml

  generate_study_population:
    run: cohortextractor:latest generate_cohort --study-definition study_definition --index-date-range "2020-01-01 to 2020-12-01 by month" --skip-existing --output-dir=output/measures
    outputs:
      highly_sensitive:
        cohort: output/measures/input_*.csv

  generate_measures:
    run: cohortextractor:latest generate_measures --study-definition study_definition --skip-existing --output-dir=output/measures
    needs: [generate_study_population]
    outputs:
      moderately_sensitive:
        measure_csv: output/measures/measure_*.csv

```

---8<-- 'includes/glossary.md'

