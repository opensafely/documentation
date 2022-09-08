from databuilder.query_language import Dataset
from databuilder.tables.examples.tutorial import patient_demographics, prescriptions


dataset = Dataset()

year_of_birth = patient_demographics.date_of_birth.year
dataset.set_population(year_of_birth >= 2000)

dataset.sex = patient_demographics.sex
dataset.most_recent_dmd_code = (
    prescriptions.sort_by(prescriptions.processing_date)
    .last_for_patient()
    .prescribed_dmd_code
)
