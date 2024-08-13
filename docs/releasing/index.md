OpenSAFELY follows the [Five Safes](../five-safes.md) framework for data access to allow safe and efficient use of data.

The Five Safes are:

- Safe projects
- Safe people
- Safe data
- Safe settings
- **Safe outputs**

When we release files from the Level 4 server, we need to take particular care of the
**Safe Outputs** dimension of the Five Safes framework, which assesses any residual risk of disclosure of patient information in outputs wishing to be released from the secure environment. This risk is minimised by researchers applying **statistical disclosure controls** to their research outputs, followed by **output checking** of these outputs by our team of trained output checkers.

In OpenSAFELY, there are 4 key “Safe Outputs” activities:

**1. [Apply Statistical disclosure controls](sdc.md)**

Researchers must apply statistical disclosure controls to their research outputs.

**2. [Requesting release of outputs](requesting-file-release.md)**

Researchers must follow a defined procedure for requesting release of outputs from the Level 4 server. This includes:

- only requesting release of files that are necessary to fulfil the purpose of a project
- describing the context (why the files are requested for release) and statistical disclosure controls applied
- restricting files to specific allowed types
- limits on file size and number of rows in tables
- Airlock, a dedicated OpenSAFELY tool for managing the release request and review process

**3. [Output checking](output-checking.md)**

Review of the requested outputs by two trained OpenSAFELY output checkers.

**4. [Release of files](releasing-files.md)**

Release of outputs that meet our disclosure rules and have undergone thorough output checking to the relevant workspace on the [Jobs site](../jobs-site.md).
