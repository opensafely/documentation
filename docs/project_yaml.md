
```yaml
version: '3.0'

expectations:
  population_size: 1000

actions:

  generate_cohorts:
    run: cohortextractor:latest generate_cohort --study-definition study_definition
    outputs:
      highly_sensitive:
        cohort: output/input.csv

  run_model:
    run: stata-mp:latest analysis/model.do
    needs: [generate_cohorts]
    outputs:
      moderately_sensitive:
        log: logs/model.log
```


---8<-- 'includes/glossary.md'
