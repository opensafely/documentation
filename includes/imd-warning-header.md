!!! warning
    The original IMD ranking is rounded to the nearest 100 in the OpenSAFELY-TPP and OpenSAFELY-EMIS databases.
    The rounded IMD ranking ranges from 0 to 32,800.
    If there is no original ranking, then the rounded ranking is -1 in the OpenSAFELY-TPP database and `NULL` in the OpenSAFELY-EMIS database.

!!! warning
    Avoid extracting the rounded IMD ranking to a binary format, such as `.feather` or `.dta`.
    Either nest it within a variable,
    such as when [grouping rounded IMD by quintile](https://docs.opensafely.org/study-def-tricks/#grouping-imd-by-quintile),
    or extract it to a non-binary format, such as `.csv`.
