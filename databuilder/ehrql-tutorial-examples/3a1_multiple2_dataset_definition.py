from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import patient_address, patient_demographics


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year

patient_address_by_date = patient_address.sort_by(patient_address.date_end)
earliest_imd = (
    patient_address_by_date.first_for_patient().index_of_multiple_deprivation_rounded
)

# This population is set so that we always select all patients.
population = patient_demographics.exists_for_patient()
dataset.set_population(population)

dataset.earliest_imd = earliest_imd
