Whilst it's possible to execute a project pipeline entirely inside a secure environment,
in practice it's often more convenient to execute the final stage outside.
This is because the final stage frequently involves carefully crafting figures and tables for publication,
making many small adjustments that would otherwise entail multiple round-trips to the OpenSAFELY Jobs site.

Executing the final stage of a project pipeline outside a secure environment is only possible when the outputs from the previous stage have been released to the OpenSAFELY Jobs site.
[Released outputs](../../../releasing-files-intro.md) have been subject to statistical disclosure control and have been reviewed by two trained OpenSAFELY output checkers.

To upload released outputs to a Codespace, using VS Code:

* Download the released outputs from the OpenSAFELY Jobs site to your computer.
* Right-click on the `output` folder in the Explorer, which is in the Primary Side Bar.
  The "[User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)" page in VS Code's documentation locates the Explorer and the Primary Side Bar.
* Click "Upload...".
* Select the released outputs to upload.

To download figures and tables from a Codespace, using VS Code:

* Locate the figures and tables in the `output` folder in the Explorer, which is in the Primary Side Bar.
  The "[User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)" page in VS Code's documentation locates the Explorer and the Primary Side Bar.
* Right-click on each figure or table.
* Click "Download...".

Uploading released outputs to a Codespace,
and downloading figures and tables from a Codespace,
are examples of **sharing results**.
The "[Datasets Used](https://www.opensafely.org/policies-for-researchers/#datasets-used)" section
of the "Policies for Researchers" page on the OpenSAFELY website contains more information about sharing results.
In short, results
— such as released outputs, figures, and tables —
should be shared **in confidence**,
and **only** with key members of the wider research team.

!!! warning
    Never commit released outputs, figures, or tables to your project's repository.
    Doing so would contravene the "Policies for Researchers" page on the OpenSAFELY website.

Only a Codespace's creator can access the Codespace,
unless they enable [Live Share](https://code.visualstudio.com/learn/collaboration/live-share) in VS Code or
unless they enable a service, such as JupyterLab, in the Codespace.
Enabling Live Share or enabling a service are also examples of **sharing results**.
Again, the "[Datasets Used](https://www.opensafely.org/policies-for-researchers/#datasets-used)" section
of the "Policies for Researchers" page on the OpenSAFELY website contains more information about sharing results.
