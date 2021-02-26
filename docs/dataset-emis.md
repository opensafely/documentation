## OpenSAFELY-EMIS database builds

This section is a work in progress.  EMIS support is currently under development.

When EMIS receive data from external data sources (eg ONS), records are appended to the
relevant tables, nont updated.  The relevant tables have an `upload_date` column, and to get the latest data, we have to query for on `upload_date`.
