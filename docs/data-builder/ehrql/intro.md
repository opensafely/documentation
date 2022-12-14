# ehrQL: electronic health record query language

---8<-- 'includes/data-builder-danger-header.md'

_ehrQL_, or electronic health record query language, is the language used by Data Builder to extract datasets for analysis.
It was developed to help researchers write simple, unambiguous queries;
and to help researchers write queries that weren't anticipated by ehrQL's developers.

The first stage when carrying out research with the OpenSAFELY platform is for the researcher to write a dataset definition in ehrQL.
A _dataset definition_ specifies the criteria for selecting, and the characteristics of, the population.
It is used by Data Builder to extract a dataset from an EHR system, where a _dataset_ is a tabular data structure with one row per patient and one column per characteristic.

The following dataset definition, which is written in ehrQL, is from [the tutorial][].
It specifies a single criterion for selecting the population; namely, that the population should consist of all patients who were born in or after 2000.
It also specifies a single characteristic of the population; namely, each patient's year of birth.

```python
---8<-- 'databuilder/snippets/ehrql.py:minimalehrql'
```

You can find out more about ehrQL in [the tutorial][] and [the examples][].
For in-depth technical documentation, there is also [the reference][].

---8<-- 'includes/glossary.md'

[the examples]: examples.md
[the reference]: reference.md
[the tutorial]: intro.md
