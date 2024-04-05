All approved OpenSAFELY outputs are released to the workspace they belong to on the [Jobs site](jobs-site.md).

### Viewing released outputs

View your released outputs by navigating to "Released Outputs" in the "Releases" section of your workspace on the Jobs site.

These outputs can be shared with project collaborators and published in line with our [data sharing and publication policy](https://www.opensafely.org/policies-for-researchers/#acknowledgment-and-data-sharing--publication-policy). Please note that you should check this for each dataset that you have used: rules may vary.

### Running further analyses on released outputs

If you have had [intermediate data released](#release-of-intermediate-data) and you wish to run further analyses on them, such as reformatting figures, there are a few things to consider.

1. You should include the code for these steps in your GitHub repo.
2. You **should not** commit any of the released outputs (including final processed charts/tables) to your GitHub repo. Make sure to include them in the `.gitignore` file.
3. Consider adding the code as an action in your project pipeline.

### Reporting a data breach

If you discover files released to the Jobs site that have been insufficiently redacted and still contain sensitive information, you should immediately contact and email the following (providing as much information as possible): Amir Mehrkar (<amir.mehrkar@phc.ox.ac.uk>); Ben Goldacre (<ben.goldacre@phc.ox.ac.uk>); [disclosurecontrol@opensafely.org](mailto:disclosurecontrol@opensafely.org); and your co-pilot. Ensure you do not share these files and if they have already been shared please identify as best as possible with whom they have been shared.


---8<-- 'includes/glossary.md'
