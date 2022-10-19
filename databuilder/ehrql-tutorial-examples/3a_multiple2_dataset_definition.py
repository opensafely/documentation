from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import (
    hospitalisations,
    patient_address,
    patient_demographics,
)


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year

patient_address_by_date = patient_address.sort_by(patient_address.date_end)
earliest_imd = (
    patient_address_by_date.first_for_patient().index_of_multiple_deprivation_rounded
)
latest_imd = (
    patient_address_by_date.last_for_patient().index_of_multiple_deprivation_rounded
)

imd_has_increased = latest_imd > earliest_imd
latest_imd_is_at_least_5000 = latest_imd >= 5000
population = (year_of_birth < 2000) & (imd_has_increased | latest_imd_is_at_least_5000)
dataset.set_population(population)

dataset.sex = patient_demographics.sex
dataset.was_hospitalised = hospitalisations.exists_for_patient()
