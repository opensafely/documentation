Codelists can be combined where appropriate. This has the advantage of keeping codeslists separate for some studies
but easily combining them for others. This removes the need for manually combining two or more into a new codelist, 
naming it and uploading it onto [codelists.opensafely.org](https://codelists.opensafely.org).

These can be combined with:

```py
from cohortextractor import combine_codelists

all_cardiac_disease_codes = combine_codelists(
                                chronic_cardiac_disease_codes, 
                                acute_cardiac_disease_codes
                                )
```
