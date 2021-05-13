## Adding a codelist
Take a look at the `codelists/codelist.txt` file in the repo, and note the structure of the existing example codelists that shipped with the research template:

```bash
opensafely/<codelist-name>/<YYYY-MM-DD>
```

If you want a codelist from [OpenCodelists](https://codelists.opensafely.org), then you need to put it in this format in the `codelist.txt` file.

For example:

`codelist.txt:`
```bash
opensafely/aplastic-anaemia/2020-04-24
opensafely/asplenia/2020-06-02
opensafely/current-asthma/2020-05-06
```

## Adding a CSV to a file
Download the new codelists into the `codelist/` folder using the `opensafely` program by running

```bash
opensafely codelists update
```

Beware that in Windows, if one or more of these codelist files is open then this command won't be able to run; close them first.

You will need to add and commit these changes and push to GitHub. 
If you don't, or a newer version is available than that committed, the automated tests will fail with an error message.

---8<-- 'includes/glossary.md'
