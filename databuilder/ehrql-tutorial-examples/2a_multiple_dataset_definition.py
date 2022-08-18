from databuilder.query_language import Dataset
from databuilder.tables import clinical_events, patients


dataset = Dataset()

year_of_birth = patients.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patients.sex
dataset.first_code = (
    clinical_events.sort_by((clinical_events.code)).first_for_patient().code
)
