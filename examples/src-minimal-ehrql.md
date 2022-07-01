```python
from databuilder.query_language import Dataset
from databuilder.tables import patients


year_of_birth = patients.date_of_birth.year
dataset = Dataset()
dataset.set_population(year_of_birth >= 2000)
dataset.year_of_birth = year_of_birth
```
