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

## Producing reports

Reports that are hosted on the reports site have to be in the `html` file format. We recommend producing these files using either [Jupyter notebooks](https://jupyter.org/) or [R Markdown](https://rmarkdown.rstudio.com/index.html); below is some guidance on how to use them.
## Jupyter notebooks

Jupyter notebooks provide an interactive environment for developing code which allows you to incorporate contextual text with code blocks. OpenSAFELY Reports is designed to work with Jupyter notebooks. It has automatic styling for the standard markup that Jupyter produces.

You can find instructions on running a Jupyter environment in OpenSAFELY [here](
https://docs.opensafely.org/opensafely-cli/#jupyter-running-jupyterlab).

These guidelines for writing notebooks makes them consistent with the best practices in the section above.

* Render matplotlib charts inline with this directive: `%matplotlib inline`.
* Configure matplotlib to output PNG charts with this directive: `%config InlineBackend.figure_format='png'`.
* Do not add interactivity features to your charts.
* If your notebook writes text using Python's `print()` function, it will be rendered in the final report as "preformatted" text, that is with a monospaced font. This may not be what you want and is inappropriate for body text. Instead you should use the `display()` and `Markdown()` functions from the `IPython.display` package, like this: `display(Markdown("Some text which can be Markdown formatted."))`.

This can be achieved by including the code block below in a code cell. This also shows you how to incorporate tables and figures into your notebook.

```python
%matplotlib inline
%config InlineBackend

import pandas as pd
from IPython.display import HTML, display, Markdown, Image

table = pd.read_csv('output/table.csv')

table = display(
    HTML(
        table.to_html(index=False)
        )
    )

img = display(
    Image(filename='output/figure.png')
    )

value = 10

text = display(
    Markdown("Some text which can be Markdown formatted.")
    )
```

Details on formatting markdown cells can be found [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
### Converting Jupyter notebooks to html

You can convert your notebook to HTML using [nbconvert](https://nbconvert.readthedocs.io/en/latest/), with the `basic` template, like this: 

```
nbconvert my-notebook.ipynb --execute --to html --template basic --no-input
```

This removes any code blocks in the notebook from the rendered html; to keep them you can remove the `no-input` flag. 

To run this within an OpenSAFELY action, you can use the following run command:

```
run: jupyter:latest jupyter nbconvert /workspace/analysis/notebook.ipynb --execute --to html --output-dir=/workspace/output --no-input --ExecutePreprocessor.timeout=86400
```

An example of this, implemented as an OpenSAFELY action, can be found [here](https://github.com/opensafely/mechanical-valve-anticoag/blob/1f158504ba5a74470b11c8d73311fb2859d67cb7/project.yaml#L53-L63).

## R Markdown

Similarly to Jupyter notebooks, R markdown allows you to combine narrative text and formatted code blocks. You can find installation instructions [here](https://rmarkdown.rstudio.com/lesson-1.html#installation).

[This markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is a useful reference for formatting markdown files, including how to add tables and figures.

To make R markdown files consistent with the best practices in the section above:

* Use the default theme by setting the theme to `null` in the markdown metadata (see below)
* Hide code blocks unless you want to display them by adding `include=False` when specifying a code block.
* Do not add interactivity features to your charts.

An example R markdown document is shown below:

````r
---
title: "A very interesting report"
output: 
  html_document:
    theme: null
    highlight: null
    mathjax: null
    toc: false
    fig_caption: false
    df_print: default
---

```{r echo=FALSE}
library(readr)
library(knitr)
knitr::opts_chunk$set( echo=FALSE, message=FALSE )
```

## A table

Find below a table of interest.

```{r}
read_csv("output/table.csv")
```

## A figure

Find below a figure of interest.

![Figure legend](output/figure.png)

## Another section

```{r}
value = 10
```

Some text which can be *Markdown* formatted.
The value is `r value`.

````

### Converting R markdown files to html

In OpenSAFELY, you can convert an R markdown file to html file by including the following run command in an action.

```
run: r:latest -e 'rmarkdown::render("path_to_report", output_dir = "/workspace/output/",knit_root_dir = "/workspace",)'    
```

## Next step
[Start by creating a report](./create-a-draft.md).
