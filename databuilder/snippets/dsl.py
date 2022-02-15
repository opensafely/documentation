# :snippet imports
from databuilder.dsl import Cohort
from databuilder.tables import clinical_events, practice_registrations


# :endsnippet

# :snippet dataset-definition
cohort = Cohort()

index_date = "2020-11-01"
registered = (
    practice_registrations.filter(practice_registrations.date_start <= index_date)
    .filter(practice_registrations.date_end >= index_date)
    .exists_for_patient()
)
cohort.set_population(registered)

cohort.code = (
    clinical_events.sort_by(clinical_events.date)
    .first_for_patient()
    .select_column(clinical_events.code)
)
# :endsnippet
