from databuilder.query_language import Dataset
from databuilder.tables.examples.tutorial import patient_address, patient_demographics


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year

patient_address_by_date = patient_address.sort_by(patient_address.date_end)
earliest_imd = (
    patient_address_by_date.first_for_patient().index_of_multiple_deprivation_rounded
)

# This cohort is set so that we always select all patients.
cohort = patient_demographics.exists_for_patient()
dataset.set_population(cohort)

dataset.earliest_imd = earliest_imd
