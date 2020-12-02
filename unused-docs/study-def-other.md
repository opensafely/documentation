

## Generating your variables 

Various variables are supported. Please see a list of all variables in variables section. 

Finding a clinical event is a common kind of variable query. It allows you to flag
patients matching lists of codes.  The flag is typically a date, but
can be a binary variable or a count.

This is added after the `population` is defined and before the final bracket. 

The code below, pulls in all the codes from a COPD codelist which is in the `codelist/` folder. 
It then returns a date for the first date that any code in this codelist appears in the 
patient record, rounded to the nearest month. 

```py
copd=patients.with_these_clinical_events(
    copd_codes,
    find_first_match_in_period=True,
    date_format="YYYY-MM",
)
```

## complete example

The below code is a complete example of a complete small study definition:

```py 
from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists
)

from codelists import *

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # STUDY POPULATION
   population=patients.all(),

    # COPD 
    copd=patients.with_these_clinical_events(
    copd_codes,
    find_first_match_in_period=True,
    date_format="YYYY-MM",
    ),
)
```

This would produce a `input.csv` file with 2 columns. 
Note that no date in the copd column indicates no code was found in that patient record. 

|patient_id|copd|
|---|---|
|177||
|183| 2002-02|
|323| 2014-06|



## Return types


We can use the study definition to return a number of different types of variable outputs. 

### Dates

We have seen how to return dates already. In that example, we returned the Month and Year of the first time a code in 
a codelist appears in the clinical record. 

In addition to this, we can return the last day this occurs:

```py 
    copd=patients.with_these_clinical_events(
    copd_codes,
    find_last_match_in_period=True,
    date_format="YYYY-MM",
    ),
```

We could return the exact date but we have chosen not to make that default in order to reduce how much data is shared. 
Date can be changed to `YYYY-MM-DD` and is sometimes more appropriate, for example, to get an accurate date of death. 

### Counts

We can count the number of times a code from a codelist appears  in the clinical record. Here, we state that 
we expect the values returned to be numbers, normally distributed around the value of 8, with values for 60% of 
the population:

```py
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    between=["2001-12-01", "2002-06-01"],
    returning="number_of_matches_in_period",
),
```
         
This returns a numerical value and in order to create appropriate dummy data, in addition to the incidence, you must 
give an estimated mean count and a standard deviation.

```py
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    between=["2001-12-01", "2002-06-01"],
    returning="number_of_matches_in_period",
    return_expectations={
                 "incidence": 0.6,
                 "int": {"distribution": "normal", "mean": 8, "stddev": 2},
             },
),
```

The above code gives 60% of the population an asthma count, and of those with one, the mean count is 8 with a standard 
deviation of 2. 
                                                                                        
## Episodes 

Sometimes we want to capture episodes of illness rather than everytime a code is entered onto the record. An example is
a patient who has pneumonia may be seen by their GP on the first day, reviewed on the 4th day and then reviewed at 2 weeks. 
This would result in 3 clinical codes of pneumonia being entered on the record but clearly they have not had 
3 episode of pneumonia. In order to deal with situations like this, there is a way to define an episode. In our example, 
can subsequent codes for pneumonia within 28 days are counted as the same episode. 

```py
study = StudyDefinition(
    population=patients.all(),
    copd_episode_count=patients.with_these_clinical_events(
        copd_codes,
        on_or_before="2020-01-01",
        returning="number_of_episodes",
        episode_defined_as="series of events each <= 14 days apart",
    ),
)
```

Please note that the time period specified starts on the last episode, meaning if you have a number of events, it 
could represent a time period much longer than the time period you have specified. 

### Exclusions 

For some definitions of "episode", you want to exclude some kinds of
consultation. For example, a consultation that includes a COPD coding
should only count towards the definition of "episode" if it's not
coded as part of a routine annual review. 


```py
study = StudyDefinition(
    population=patients.all(),
    copd_episode_count=patients.with_these_clinical_events(
        copd_codes,
        on_or_before="2020-01-01",
        returning="number_of_episodes",
        episode_defined_as="series of events each <= 28 days apart",
        ignore_days_where_these_codes_occur=copd_annual_review_codes,
    ),
)
```

### Returning Multiple Types

If you want to return a count *and* a date, you can reuse the former
definition in a date definition like this:

```py
    asthma_count=patients.with_these_clinical_events(
        asthma_codes,
        between=["2001-12-01", "2002-06-01"],
        returning="number_of_matches_in_period",
    ),

    asthma_count_date=patients.date_of(
        "asthma_count", 
        date_format="YYYY-MM"
    ),
```













## Demographic Details

### Age

There is a specific method to get age (`patient.age_as_if()`). You must provide a date. 
There is also a custom distribution matching a typical population-age distribution for the UK:

```
    age=patients.age_as_of(
        "2020-02-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
```

### Sex

There is a specific method to get sex (`patient.sex()`). In this case, instead of returning an incidence in the dummy 
data we want to ensure that all dummy patients have data and the proportions of each. 

```py 
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
```

`rate` is set as universal, meaning all rows will have data in this column.
 
 `category` sets the proportion. 


## Clinical Events  

We have used clinical events already. See full example below:

```py
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    between=["2001-12-01", "2002-06-01"],
    returning="number_of_matches_in_period",
    return_expectations={
                 "incidence": 0.6,
                 "int": {"distribution": "normal", "mean": 8, "stddev": 2},
             },
),
```

## Medication Events  
We can also do similar queries of medications as we can of clinical events. Medication codelists tend to be in SNOMED:

In `codelist.py`:
```py
salbutamol_codes = codelist_from_csv(
    "codelists/opensafely-asthma-inhaler-salbutamol-medication.csv",
    system="snomed",
    column="id",
)
```

In `study_definition.py`:

```py
 recent_salbutamol_count=patients.with_these_medications(
     salbutamol_codes,
     between=["2018-02-01", "2020-02-01"],
     returning="number_of_matches_in_period",
     return_expectations={
         "incidence": 0.6,
         "int": {"distribution": "normal", "mean": 8, "stddev": 2},
     },
 ),
```

In the same way as `patient.with_these_clinical_events()`, you can define episodes and exclusions for medications. 

## Patient Address Dependent Variables

There are number of variables that are dependent of patient address. These are:

- IMD
- Rural / Urban Classification 

### IMD
We can again set the `rate` as `universal`. In reduce identification risk, we have rounded IMD to the nearest 100. 

```py 
    imd=patients.address_as_of(
        "2020-02-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        },
    ),
```

### Rural - Urban Classfication. 
```py

    rural_urban=patients.address_as_of(
        "2020-02-01",
        returning="rural_urban_classification",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "rural": 0.1, 
                    "urban": 0.9, 
                }
            },
        },
    ),

```

## Practice Address Dependent Variables
Regional information can be queried by using the Practice address. The options available are:

- STP
- Region

It is a good idea for both of these to return multiple categories of dummy data in order to allow for more realistic
code to be written for your analysis. 

### STP

```py
    stp=patients.registered_practice_as_of(
        "2020-02-01",
        returning="stp_code",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "STP1": 0.1,
                    "STP2": 0.1,
                    "STP3": 0.1,
                    "STP4": 0.1,
                    "STP5": 0.1,
                    "STP6": 0.1,
                    "STP7": 0.1,
                    "STP8": 0.1,
                    "STP9": 0.1,
                    "STP10": 0.1,
                }
            },
        },
    ),
```

### Region 

```py 
    region=patients.registered_practice_as_of(
        "2020-02-01",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        },
    ),
```

## TPP Vaccination Records

This is TPP-specfic, so the method name reflects that; it will not
work against other backends.

An example query might be:

```py
    recent_flu_vaccine = patients.with_tpp_vaccination_record(
        target_disease_matches="INFLUENZA",
        on_or_after="2018-01-01",
        find_last_match_in_period=True,
        returning="date",
    )
```

or

```py
    recent_flu_vaccine = patients.with_tpp_vaccination_record(
        product_name_matches=["Optaflu", "Madeva"],
        on_or_after="2018-01-01",
        find_last_match_in_period=True,
        returning="date",
    )
```

Apart from the standard arguments this function takes two optional query
parameters: `target_disease_matches` and `product_name_matches`.

`target_disease_matches` returns all vaccinations that target a
particular disease/pathogen, bearing in mind that a single product
(e.g.  MMR) can target multiple diseases. The values this takes are
all-caps strings drawn from TPP's internal list and should be checked
against the contents of the *live* (not dummy) `VaccinationReference`
table during development.

`product_name_matches` matches against the product name TPP use which,
again, should be checked against the `VaccinationReference` table.

Both arguments can either take either a single string or a list of
strings, in which case it returns results matching _any_ of the items in
the list.

## Care Homes


TPP have attempted to match patient addresses to care homes as stored in
the CQC database. At its most simple the `care_home_status` query
returns a boolean indicating whether the patient's address (as of the
supplied time) matched with a care home.

It is also possible to return a more complex categorisation based on
attributes of the care homes in the CQC database, which can be freely
downloaded here:
https://www.cqc.org.uk/about-us/transparency/using-cqc-data

At present the only imported fields are `LocationRequiresNursing` and
`LocationDoesNotRequireNursing`, but we can ask for more fields to be
imported if needed.

The `categorised_as` argument acts in effectively the same way as for
the `categorised_as` function (q.v.) except that the only columns that
can be referred to are those belonging to the care home table
(i.e. the two nursing fields above) and the boolean
`IsPotentialCareHome`.

Example queries:
```py
is_in_care_home=patients.care_home_status_as_of("2020-01-01")

care_home_type=patients.care_home_status_as_of(
    "2020-01-01",
    categorised_as={
        "PC": """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='Y'
          AND LocationRequiresNursing='N'
        """,
        "PN": """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='N'
          AND LocationRequiresNursing='Y'
        """,
        "PS": "IsPotentialCareHome",
        "U": "DEFAULT",
    },
)
```

## Households

OpenSAFELY can return information about the household to which the
patient belonged as of a reference date. This is inferred from address
data using an algorithm developed by TPP (to be documented soon) so the
results are not 100% reliable but are apparently pretty good.

Options for `returning` are:

```
    pseudo_id: An integer identifier for the household which has no meaning
               other than to identify individual members of the same
               household (0 if no household information available)

    household_size: the number of individuals in the household (0 if no
                    household information available)
```

Examples:

```
household_id=patients.household_as_of(
    "2020-02-01", returning="pseudo_id"
)

household_size=patients.household_as_of(
    "2020-02-01", returning="household_size"
),
```

## SGSS testing data

This allows us to check COVID test results in the Second Generation
Surveillance System. Example queries are:

```py
study = StudyDefinition(
    population=patients.all(),
    positive_covid_test_ever=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive"
    ),
    negative_covid_test_ever=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="negative"
    ),
    tested_for_covid=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="any",
        on_or_before="2020-05-01"
    ),
    first_positive_test_date=patients.with_test_result_in_sgss(
        pathogen="SARS-CoV-2",
        test_result="positive",
        find_first_match_in_period=True,
        returning="date",
        date_format="YYYY-MM-DD",
    ),
)
```

Only SARS-CoV-2 results are included in our data extract so this will
throw an error if the specified pathogen is anything other than
"SARS-CoV-2".

`test_result` must be one of: "positive", "negative" or "any"

The date used is the date the specimen was taken. Where a patient has
multiple positive results only the date of the earliest specimen that
tested positive is recorded. (See docstring for a more detailed explanation.)

The data we receive has an Organism_Species_Name field which is always
"SARS-CoV-2 CORONAVIRUS (Covid-19)" in the case of a positive result and
"NEGATIVE SARS-CoV-2 (COVID-19)" in the case of a negative result. The
code will throw an error if anything else is ever found in this field.

## Consultations

In OpenSAFELY, a "consultation" means a GP-patient interactions, either
in person or via phone/video call. However, the concept of a
"consultation" in EHR systems is generally broader and might include
things like updating a phone number with the receptionist.

Because of this, it's possible that we might have a full medical
history for a patient (imported via GP2GP) but not have an exact
record of which of their imported consultations should be considered
as GP-patient interactions.

There are, therefore, two methods for querying consultations:
`with_gp_consultations` and
`with_full_gp_consultation_history_between`.  The boolean predicate
`with_full_gp_consultation_history_between` allows us to identify
patients where we _do_ have a reliable history.


Example queries:
```py
...
consultation_count=patients.with_gp_consultations(
    between=["2010-01-01", "2015-01-01"],
    find_last_match_in_period=True,
    returning="number_of_matches_in_period",
),
latest_consultation_date=patients.date_of(
    "consultation_count", date_format="YYYY-MM"
),
has_history=patients.with_complete_gp_consultation_history_between(
    "2010-01-01", "2015-01-01"
),
...
```




