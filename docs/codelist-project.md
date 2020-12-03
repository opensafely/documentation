## Adding Codelist
Take a look at the `codelists/codelist.txt` file in the repo, 
and note the structure of the existing example codelists that shipped 
with the research template: 

```bash
opensafely/<codelist-name>/<YYYY-MM-DD>
```

If you want a codelist from [codelists.opensafely.org](https://codelists.opensafely.org), then you need to put it in this format in the `codelist.txt` file.

For example:

`codelist.txt:`
```bash 
opensafely/aplastic-anaemia/2020-04-24
opensafely/asplenia/2020-06-02
opensafely/current-asthma/2020-05-06
```

## Adding CSV to file
Download the new codelist into the `codelist/` folder using 
the `cohortextractor` by 
submitting `cohortextractor update_codelists` at the command line.

You will need to add and commit these changes to Git. 

---8<-- 'includes/glossary.md'
