from databuilder.ehrql import Dataset
from databuilder.tables.examples.tutorial import clinical_events, patients


dataset = Dataset()

tutorial_code_system_events = clinical_events.drop(
    clinical_events.system == "AnotherCodeSystem"
).take(clinical_events.system == "TutorialCodeSystem")

minimum_h1_threshold = 200.0
start_date_of_interest = "2004-01-01"
end_date_of_interest = "2005-12-31"

high_code_h1_events = tutorial_code_system_events.take(
    (tutorial_code_system_events.code == "h1")
    & (tutorial_code_system_events.numeric_value > minimum_h1_threshold)
    & (tutorial_code_system_events.date >= start_date_of_interest)
    & (tutorial_code_system_events.date <= end_date_of_interest)
)

count_of_high_code_h1_events = high_code_h1_events.count_for_patient()
maximum_h1_value = high_code_h1_events.numeric_value.maximum_for_patient()

population = high_code_h1_events.exists_for_patient()
dataset.set_population(population)

dataset.date_of_birth = patients.date_of_birth
dataset.h1_count = count_of_high_code_h1_events
dataset.h1_max = maximum_h1_value
