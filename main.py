def define_env(env):
    "Hook function"

    @env.macro
    def build_toc(nav, page):
        """
        Build a nested list of page links from a navigation section index, to be inserted into the index page itself
        """
        assert (
            page.is_index
        ), "`build_toc` macro is only available for navigation index pages"
        parent_section = page.parent
        links = [make_link(item) for item in parent_section.children if item != page]
        html = f"<ul>{''.join(links)}</ul>"
        return html


def make_link(item):
    """
    Create the html list links for a nav item
    `item` may be a Section or a Page
    """
    if item.is_page:
        # Note that we prepend / so the URL extracted from the navigation is relative to the
        # root, and not to the location of this index page.  This means we can deal with nested
        # nav links from any point in the document structure
        return f"<li><a href=/{item.url}>{item.title}</a></li>"
    else:
        items = [make_link(sub_item) for sub_item in item.children]
        return f"<li>{item.title}<ul>{''.join(items)}</ul></li>"
