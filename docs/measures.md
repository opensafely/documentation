Generating measures is 3 step process:

 1. Defining a `measures` variable in `study_definition.py`, which should be a list of `Measure` instances.
 2. Extracting the data by running `generate_cohort` using the new `--index-date-range` option to cover the range of time periods we want to calculate the measure for.
 3. Running `generate_measures` which takes the files extracted in step 2 and produces files like `measure_<measure_id>.csv`.

## Defining measures

This is best explained using an example:
```py
from cohortextractor import StudyDefinition, Measure, patients


study = StudyDefinition(
    index_date="2020-01-01",
    population=patients.registered_with_one_practice_between(
        "index_date", "index_date + 1 month"
    ),
    admitted_to_icu=patients.admitted_to_icu(
        between=["index_date", "index_date + 1 month"]
    ),
    died=patients.died_from_any_cause(
        between=["index_date", "index_date + 1 month"]
    ),
    stp=patients.registered_practice_as_of(
        "index_date", returning="stp_code",
    ),
)

measures = [
    Measure(
        id="icu_admission_by_stp",
        numerator="admitted_to_icu",
        denominator="population",
        group_by="stp",
    ),
    Measure(
        id="death_by_stp",
        numerator="died",
        denominator="population",
        group_by="stp",
    ),
]
```
Here `id` is just a string used to identify the measure output file. The other attributes identify columns from the study definition used to calculate the measure. Both the `numerator` and `denominator` columns must be numeric (which for our purposes includes booleans, encoded as 0 or 1). The `group_by` column can be of any type. 

## Extracting data

The `generate_cohort` sub-command now accepts an `--index-date-range` option. Rather than generating a single output CSV file this generates multiple output files across a range of dates, modifying the study's index date each time.

The range is specified as:

    --index-date-range "YYYY-MM-DD to YYYY-MM-DD by (week|month)"

We also except `today` in place of a date.

Output files are named like: `output/input_YYYY-MM-DD.csv`

We also add `--skip-existing` option which will cause the cohortextractor to skip the extraction step for any dates where the corresponding file already exists. This makes it easier to incrementally extract data for new months/weeks without having to re-extract everything.

Example:

    cohortextractor generate_cohort --index-date-range "2020-01-01 to 2020-03-01 by month"

    output/input_2020-01-01.csv
    output/input_2020-02-01.csv
    output/input_2020-03-01.csv

## Generating measures

This involves a new `generate_measures` sub-command:

    cohortextractor generate_measures

For each defined measure, and for each monthly/weekly file extracted in step 2, this generates an output file with the measure calculated for that month or week.

    output/measure_icu_admission_by_stp_2020-01-01.csv
    output/measure_death_by_stp_2020-01-01.csv
    output/measure_icu_admission_by_stp_2020-02-01.csv
    output/measure_death_by_stp_2020-02-01.csv
    output/measure_icu_admission_by_stp_2020-03-01.csv
    output/measure_death_by_stp_2020-03-01.csv

Finally, for each measure, it combines all the output into a single file with an additional `date` column indicating the date associated with each row.

    output/measure_icu_admission_by_stp.csv
    output/measure_death_by_stp.csv

This command also respects the `--skip-existing` flag. This will prevent it from recalculating the measure for any months or weeks which have already been calculated. However the final step, which combines output across time periods, will always be run.