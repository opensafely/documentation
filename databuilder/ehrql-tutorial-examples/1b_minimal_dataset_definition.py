from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import patients


dataset = Dataset()

year_of_birth = patients.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patients.sex
