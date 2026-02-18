!!! warning
    Research access to the backend provided by EMIS is temporarily unavailable, pending funding arrangements between NHS England and EMIS. When funding has been secured, we will publish a timeline for gradually reopening access.

## OpenSAFELY-EMIS database builds

When EMIS receive data from external data sources (eg ONS), records are appended to the
relevant tables, not updated. The relevant tables have an `upload_date` column, and to get the latest data, we have to query for on `upload_date`.
