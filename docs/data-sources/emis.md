!!! warning
    This section is a work in progress.
    EMIS support is currently under development.

## OpenSAFELY-EMIS database builds

When EMIS receive data from external data sources (eg ONS), records are appended to the
relevant tables, not updated.  The relevant tables have an `upload_date` column, and to get the latest data, we have to query for on `upload_date`.
