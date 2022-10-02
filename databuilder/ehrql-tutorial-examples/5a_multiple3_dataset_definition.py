from databuilder.query_language import Dataset
from databuilder.tables.examples.tutorial import hospitalisations, patient_address


most_recent_hospitalisation = hospitalisations.sort_by(
    hospitalisations.date
).last_for_patient()

lowest_imd_address = patient_address.sort_by(
    patient_address.index_of_multiple_deprivation_rounded
).first_for_patient()

dataset = Dataset()

cohort = most_recent_hospitalisation.exists_for_patient()
dataset.set_population(cohort)

dataset.most_recent_hospitalisation_code = most_recent_hospitalisation.code
dataset.most_recent_hospitalisation_system = (
    most_recent_hospitalisation.system.if_null_then("UnknownCodeSystem")
)
dataset.lowest_imd = (
    lowest_imd_address.index_of_multiple_deprivation_rounded.if_null_then(-1)
)
dataset.lowest_imd_is_valid = (
    lowest_imd_address.index_of_multiple_deprivation_rounded.is_not_null()
)
