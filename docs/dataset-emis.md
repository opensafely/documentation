!!! warning
    This section is a work in progress.
    EMIS support is currently under development.

## OpenSAFELY-EMIS database builds

At present, EMIS support is enabled for some, but not all, users.
This is because not all study definitions can run against the EMIS backend.

When EMIS receive data from external data sources (eg ONS), records are appended to the
relevant tables, not updated.  The relevant tables have an `upload_date` column, and to get the latest data, we have to query for on `upload_date`.
