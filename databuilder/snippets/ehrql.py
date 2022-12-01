# --8<-- [start:minimalehrqlimportpatients]
from databuilder.tables.beta.smoketest import patients


year_of_birth = patients.date_of_birth.year
# --8<-- [end:minimalehrqlimportpatients]

# --8<-- [start:minimalehrqlimportdataset]
from databuilder.ehrql import Dataset


dataset = Dataset()
# --8<-- [end:minimalehrqlimportdataset]

# --8<-- [start:minimalehrqlsetpopulation]
dataset.set_population(year_of_birth >= 2000)
# --8<-- [end:minimalehrqlsetpopulation]

# --8<-- [start:minimalehrqlrequestyearofbirth]
dataset.year_of_birth = year_of_birth
# --8<-- [end:minimalehrqlrequestyearofbirth]

# --8<-- [start:minimalehrqlrequestbirthyear]
dataset.birth_year = year_of_birth
# --8<-- [end:minimalehrqlrequestbirthyear]


# --8<-- [start:minimalehrql]
from databuilder.ehrql import Dataset
from databuilder.tables.beta.smoketest import patients


year_of_birth = patients.date_of_birth.year
dataset = Dataset()
dataset.set_population(year_of_birth >= 2000)
dataset.year_of_birth = year_of_birth
# --8<-- [end:minimalehrql]
