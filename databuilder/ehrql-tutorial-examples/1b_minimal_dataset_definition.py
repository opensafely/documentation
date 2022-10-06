from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import patient_demographics


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patient_demographics.sex
