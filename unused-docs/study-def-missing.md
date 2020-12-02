If a query returns no matching record for a patient &mdash; for example if there are no blood pressure values recorded in a given period, or if there is no death date because the patient hasn't died, or if there is no household size available &mdash; then a default value will be returned. 
For strings and dates, the default value is the empty string `""`. 
For booleans, integers, or floats, the default value is `0`. 

There is no universal `null` value outputted to `input.csv` because these may be handled inconsistently across different programs.

It's possible that a record is matched, but the value is not valid. 
In this case, the value will be returned as is. 
For example, a date set to `"9999-99-99"` or a blood pressure reading set to `-1`. 
These will indicate missing / unknown / unrecorded / not applicable values in the source dataset. 
The meaning of these values will depend on the data source.

