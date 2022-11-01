from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import hospitalisations, patients


dataset = Dataset()

start_date = "2020-03-01"
final_date = "2020-05-31"

date_of_birth = patients.date_of_birth
hospitalisations_in_range = hospitalisations.take(
    hospitalisations.date.is_on_or_after(start_date)
    & hospitalisations.date.is_before(final_date)
)

population = (date_of_birth < "2000-01-01") & (
    hospitalisations_in_range.exists_for_patient()
)
dataset.set_population(population)

dataset.sex = patients.sex
dataset.year_of_birth = patients.date_of_birth.year

first_hospitalisation_in_range = hospitalisations_in_range.sort_by(
    hospitalisations.date
).first_for_patient()
dataset.last_day_of_month_before_first_hospitalisation = (
    first_hospitalisation_in_range.date.to_first_of_month().subtract_days(1)
)
