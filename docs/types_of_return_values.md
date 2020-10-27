We can use the study definition to return a number of different types of variable outputs. 

## Dates

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

## Counts

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

## Exclusions 

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

## Returning Multiple Types

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

## Missing values

If a query returns no matching record for a patient &mdash; for example if there are no blood pressure values 
recorded in a given period, or if there is no death date because the patient hasn't died, or if 
there is no household size available &mdash; then a default value will be returned. For strings and dates, 
the default value is the empty string `""`. For booleans, integers, or floats, the default value is `0`. 
There is no universal `null` value outputted to `input.csv` because these may be handled inconsistently across 
different programs.