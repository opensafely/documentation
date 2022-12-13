## Technical introduction to Data Builder's query engine

!!! note
    This section is a technical explanation for experienced users who want
    to understand more of how Data Builder works behind-the-scenes.

    Understanding this section is not necessary to using Data Builder.

Data Builder facilitates querying multiple different data backends,
without the researcher concerning themselves with the specific details
of how that backend works.

There are three steps to extract data on cohorts:

1. **Writing a definition**: A researcher writes a dataset definition.

     The dataset definition is written in Data Builder's own *domain
     specific language*, ehrQL, which is built on Python.

2. **Query transformation**: The researcher then loads that dataset
   definition into Data Builder.

     Provided the dataset definition is valid, Data Builder transforms
     the dataset definition into an internal representation of the
     query: the *query model*.

3. **Query submission**: Data Builder then translates the query model
   into the appropriate query language for the data backend being
   accessed. If the study is running on the OpenSAFELY platform, queries
   will be submitted to live data backends.

     A researcher might wish to perform the same underlying query on multiple backends,
     where the backends use entirely different data stores.
     For instance, one backend might use Microsoft SQL Server and another Databricks.

     Where backend data stores use different query languages,
     or dialects of the same query language,
     the researcher may need to write *multiple* queries,
     possibly even one for each backend,
     to get the data extraction results corresponding to the same underlying query.

     With ehrQL, the researcher does not need to write these multiple queries manually.
     Data Builder automatically transforms the *single* dataset definition from ehrQL
     into suitable queries for each compatible backend.

     This features enable the same dataset definition to be used in multiple backends.

---8<-- 'includes/glossary.md'
