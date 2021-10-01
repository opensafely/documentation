## Adding a codelist
Take a look at the `codelists/codelist.txt` file in the repo, and note the structure of the existing example codelists that shipped with the research template:

```bash
opensafely/<codelist-name>/<YYYY-MM-DD>
```

If you want a codelist from [OpenCodelists](https://www.opencodelists.org), then you need to put it in this format in the `codelist.txt` file.

For example:

`codelist.txt:`
```bash
opensafely/aplastic-anaemia/2020-04-24
opensafely/asplenia/2020-06-02
opensafely/current-asthma/2020-05-06
```

If necessary, during initial development you can even import codelists this way while they are in draft, but ensure they are finalised and updated in your study before running in the real data. (They may take the form `username/[your_username]/your_codelist/XYZ`)

## Adding/updating a codelist CSV file
Download the new codelists into the `codelist/` folder using the `opensafely` program by running

```bash
opensafely codelists update
```

Beware that in Windows, if one or more of these codelist files is open then this command won't be able to run; close them first.

If necessary, you can also import CSVs not via OpenCodelists - just manually copy the CSV files into `codelists/`. However, we would recommend uploading these to OpenCodelists to import them as above. Note, if you are _also_ using some codelists from OpenCodelists, any manually imported codelists should be stored in a `local_codelists` folder so that they are not overwritten in the next step. 

You will need to add and commit these changes and push to GitHub. 
If you don't, or a newer version is available than that committed, the automated tests will fail with an error message.

See more on using Codelists in your study definition in [Working with codelists](study-def-codelists.md).

---8<-- 'includes/glossary.md'
