Reports are regularly updated outputs related to the COVID-19 pandemic, created with the OpenSAFELY platform.

This service is currently in a pilot phase for external users.

They are hosted on the [reports site](https://reports.opensafely.org).


## Best practices
To ensure that the file is self-contained, all images must be in-line rather than published as separate files.
OpenSAFELY Reports only supports using one file for a report, in-lining images will allow you to use them within a report.
Images should be bitmaps rather than in vector graphics formats, PNG is suggested as a good option.

Reports are static; there is no facility for dynamic content.
Any JavaScript that the report contains will be stripped out by OpenSAFELY Reports.

All styling is applied by OpenSAFELY Reports; any styles included in the file will be stripped out.


## Jupyter notebooks
OpenSAFELY Reports is designed to work with Jupyter notebooks.
It has automatic styling for the standard markup that Jupyter produces.
These guidelines for writing notebooks makes them consistent with the requirements in the section above.

* Render matplotlib charts inline with this directive: `%matplotlib inline`.
* Configure matplotlib to output PNG charts with this directive: `%config InlineBackend.figure_format='png'`.
* Do not add interactivity features to your charts.
* Convert your notebook to HTML using `nbconvert`, with the `basic` template, like this: `nbconvert my-notebook.ipynb --execute --to html --template basic`.
* If your notebook writes text using Python's `print()` function, it will be rendered in the final report as "preformatted" text, that is with a monospaced font. This may not be what you want and is inappropriate for body text. Instead you should use the `display()` and `Markdown()` functions from the `IPython.display` package, like this: `display(Markdown("Some text which can be Markdown formatted."))`.


## Next step
[Start by creating a report](./create-a-draft.md).
