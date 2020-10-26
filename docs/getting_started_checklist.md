







### Code Lists

* Check and/or review existing lists on [codelists.opensafely.org](https://codelists.opensafely.org)
* If edit, submit through [codelists.opensafely.org](https://codelists.opensafely.org)
* If new list needed, create it as an issue in the repo
* CTV3 needed, can translate from Read2. Link to browser.
* Recommend to also extract SNOMED from QoF?
* Process for sign off
* Publish to [codelists.opensafely.org](https://codelists.opensafely.org)

### Writing a Study Definition
* How to get codelists into the study definition
* Explanation of the pre-written functions
* Assume existing ones will be publicly available, so people will be able to see what they look like. Would be a good starting point.
* What is and is not supported by the study definition file at the moment:
  * Matching for case-control studies
  * PS matching or similar (assume can be done in Stata)
  * Time-updated variables (?)

See [Study definitions](study_definition.md) for more detail.

### Working With Dummy Data
* Focus on making code run without errors
* Explanation of automatic tests on Github
* Include logical tests and checks you would do for cleaning. Do not assume data is clean.

### Running Finalised Code Against the Server
* Process once external people are happy with their code and no errors
* Timeframe for run and checks (approximate)

### Publishing and Sharing
* Expected outputs will be published
* Github repos with code will be publicly available (from start or later on?)
* Share code and protocol in other places is fine, data cannot be shared
* Encourage Open Access publishing, preprints etc.
* [placeholder - procedures for authorship/credit determination]

## FAQs

* _I use [R/SAS/SPSS/Other] and not Stata. Can I still do a study through the OpenSafely platform?_
  [answer]
* _I’d prefer to write my analysis scripts in Python. Can I do that?_
  [answer]
* _My research question is exploratory. How can I develop all my code without seeing interim results?_
  [answer]
* _If we can show that we meet data security standards. Can you just post us a copy of the data instead?_
  [answer]
* _I’ve realised I need to do something differently to what I said in my protocol. Can I still do that?_
  [answer]
* _My analysis requires a linked dataset from another source. Can you facilitate this?_
  [answer]

## Further Resources

