---8<-- 'includes/cohort-extractor-deprecated.md'

## Flowcharts (temporary workaround)

Many studies will require a flowchart to show inclusion/exclusion of patients in the study. Eventually the numbers of patients excluded/included will be summarised automatically following cohort extract, but for now, a slightly manual approach is required:

 - Make a copy of the study definition (called `study_definition_flow_chart.py`). The `population=patients.satisfying()` function should be replaced with `population=patients.all()`. Then all variables except for those that appeared in the population definition logic should be removed (this will mean that it runs much faster than the main study definition). An example of such a study definition can be seen in [this repository on NSAIDS use and COVID-related outcomes](https://github.com/opensafely/nsaids-covid-research/commit/e5ad58c72926d7c73ba131099486409f6876883d).
 - Then write a script that reads the `input_flow_chart.csv` and then sequentially drops each of the variables and counts the remaining population, in whatever order you'd like to report them; [Stata example](https://github.com/opensafely/nsaids-covid-research/blob/23069312944ea1fc6d79ec4d9b45eea25df96ab0/analysis/flowchart_numbers.do).


---8<-- 'includes/glossary.md'
