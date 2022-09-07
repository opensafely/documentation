from databuilder.query_language import Dataset
from databuilder.tables.beta.tutorial import patient_demographics as patients
from databuilder.tables.beta.tutorial import prescriptions


dataset = Dataset()

year_of_birth = patients.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patients.sex
dataset.most_recent_dmd_code = (
    prescriptions.sort_by(prescriptions.processing_date)
    .last_for_patient()
    .prescribed_dmd_code
)
