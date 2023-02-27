We are very keen to compile all pre-printed and published OpenSAFELY studies on [opensafely.org](www.opensafely.org).

To do this, open a new file in a text editor of your choice. Populate the file using the following template:

```
---
title: "Short title for the page"
date: yyyy-mm-dd
status: "preprint" or "published"
paper: "Title of the paper"
description: "Description of the paper"
cite: "How to cite this paper"
link: "https://doi.org/..."
---

## Abstract

### Background 

### Methods

### Results

### Conclusions

```

First, update the frontmatter (i.e., the text between the `---`s) with the correct details for your paper. Note that `status:` should have the value `preprint` or `published` to indicate the current status of your manuscript. Then, add the necessary text below the `## Abstract` line to include the abstract.

This file format is called "Markdown", for more help writing Markdown documents, see:

- [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Guide: Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Dillinger: this shows a preview of your Markdown as you type](https://dillinger.io/)

This file can then be incorporated into our website by anyone with the required access; if you are an external researcher, then you can send this to your co-pilot who will have the necessary permissions.