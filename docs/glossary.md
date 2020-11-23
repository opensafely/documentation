
-   A **study definition** specifies the patients you want to include in
    your study and defines the variables that describe them. Study
    definitions are written in a Python script using a human-readable API.
-   The **cohort extractor** is a program that uses the study definition to create a
    dataset for analysis. This is either:
    -   A dummy dataset used for developing and testing analysis code on
        the user’s own machine. Users have control over the
        characteristics of each dummy variable, which are defined inside
        the study definition.
    -   A real dataset created from the OpenSAFELY database, used for
        the analysis proper. Real datasets never leave the secure
        server, only summary data and other outputs that are derived
        from them can be released (after disclosivity checks). 
		
	It also performs other useful tasks like importing codelists and generating *Measures* (see below).
	
-   A **codelist** is a collection of clinical codes that define a
    particular condition, event or diagnosis.
-   The **project pipeline** defines dependencies within the project’s
    analytic code. For example `make_chart.R` depends on
    `process_data.R`, which depends on the study dataset having been
    extracted. This reduces redundancies by only running scripts that
    need to be run.
-   The **job runner** runs the actions defined in the project pipeline
    using real data.