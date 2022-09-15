from tables.tutorial import patient_demographics

from databuilder.query_language import Dataset


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patient_demographics.sex
