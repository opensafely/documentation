def on_page_markdown(markdown, page, **kwargs):
    """
    Replace parent_snippet markers from imported repos with appropriate snippet notation

    on_page_* methods are called for each Page in a mkdocs site and can modify the
    markdown they are given as input.  We're using this method to look for the
    parent_includes markers in pages that come from an imported repo, and replace it
    with the pymdownx.snippets syntax to retrieve the snippet from this (the parent
    repo).

    For example:
        !!! parent_snippet:'includes/glossary.md'

    will be replaced with:
        ---8<-- 'includes/glossary.md'

    This allows docs imported from other repos (e.g. ehrQL) to reference snippets
    in the parent docs, such as the glossary.
    """

    return markdown.replace("!!! parent_snippet:", "---8<-- ")
