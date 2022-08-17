from databuilder.query_language import Dataset
from databuilder.tables import patients


dataset = Dataset()

year_of_birth = patients.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)
