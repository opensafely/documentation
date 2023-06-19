import logging

import mkdocs.plugins


log = logging.getLogger("mkdocs")


@mkdocs.plugins.event_priority(100)
def on_config(config):
    """
    Update config with specified ehrQL branch
    This is done first, before any imported repos are processed, or nav sections
    hidden.
    """
    ehrql_branch = config["extra"]["ehrql_branch"]
    if ehrql_branch == "main":
        return config
    ehrql_nav_index, ehrql_nav_section = next(
        (i, section)
        for i, section in enumerate(config["nav"])
        if list(section.keys())[0] == "ehrQL"
    )
    new_import_string = ehrql_nav_section["ehrQL"].replace(
        "branch=main", f"branch={ehrql_branch}"
    )
    config["nav"][ehrql_nav_index] = {"ehrQL": new_import_string}

    log.info("ehrQL docs imported from branch '%s'", ehrql_branch)
    return config
