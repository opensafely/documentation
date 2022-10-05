from databuilder.query_language import Dataset
from databuilder.tables.examples.tutorial import hospitalisations, patient_demographics


dataset = Dataset()

start_date = "2020-03-01"
final_date = "2020-05-31"

date_of_birth = patient_demographics.date_of_birth
hospitalisations_in_range = hospitalisations.take(
    hospitalisations.date.is_on_or_after(start_date)
    & hospitalisations.date.is_before(final_date)
)

cohort = (date_of_birth < "2000-01-01") & (
    hospitalisations_in_range.exists_for_patient()
)
dataset.set_population(cohort)

dataset.sex = patient_demographics.sex
dataset.year_of_birth = patient_demographics.date_of_birth.year

first_hospitalisation_in_range = hospitalisations_in_range.sort_by(
    hospitalisations.date
).first_for_patient()
dataset.first_hospitalisation_date_to_end_of_previous_month = (
    first_hospitalisation_in_range.date.to_first_of_month().subtract_days(1)
)
