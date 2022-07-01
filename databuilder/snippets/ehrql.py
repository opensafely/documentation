# :snippet minimal-ehrql-import-patients
from databuilder.tables import patients


year_of_birth = patients.date_of_birth.year
# :endsnippet

# :snippet minimal-ehrql-import-dataset
from databuilder.query_language import Dataset


dataset = Dataset()
# :endsnippet

# :snippet minimal-ehrql-set-population
dataset.set_population(year_of_birth >= 2000)
# :endsnippet

# :snippet minimal-ehrql-request-year-of-birth
dataset.year_of_birth = year_of_birth
# :endsnippet

# :snippet minimal-ehrql-request-birth-year
dataset.birth_year = year_of_birth
# :endsnippet


# :snippet minimal-ehrql
from databuilder.query_language import Dataset
from databuilder.tables import patients


year_of_birth = patients.date_of_birth.year
dataset = Dataset()
dataset.set_population(year_of_birth >= 2000)
dataset.year_of_birth = year_of_birth
# :endsnippet
