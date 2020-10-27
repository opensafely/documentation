### Finding events within 2 dates
As a default, the study definition will look for codes at any point in the record. We can give a specific time period 
using `between` and two dates in a `YYYY-MM-DD` format. 

```py 
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    between=["2001-12-01", "2002-06-01"],
    find_last_match_in_period=True,
    date_format="YYYY-MM",
),
```

### Finding episodes before or after a date
We can also define the date before or after a date.

```py 
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    on_or_before="2020-01-01",
    find_last_match_in_period=True,
    date_format="YYYY-MM",
),
```

```py 
asthma_count=patients.with_these_clinical_events(
    asthma_codes,
    on_or_after="2020-01-01",
    find_last_match_in_period=True,
    date_format="YYYY-MM",
),
```

Using `between`, `on_or_after` or `on_or_before` are mutually exclusive. This means you have to pick on to use or if you leave
our completely it will look in the whole record. 