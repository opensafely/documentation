import logging

import mkdocs.plugins


log = logging.getLogger("mkdocs")


@mkdocs.plugins.event_priority(100)
def on_config(config):
    """
    Update config with specified databuilder branch
    This is done first, before any imported repos are processed, or nav sections
    hidden.
    """
    databuilder_branch = config["extra"]["databuilder_branch"]
    if databuilder_branch == "main":
        return config
    databuilder_nav_index, databuilder_nav_section = next(
        (i, section)
        for i, section in enumerate(config["nav"])
        if list(section.keys())[0] == "Data Builder"
    )
    new_import_string = databuilder_nav_section["Data Builder"].replace(
        "branch=main", f"branch={databuilder_branch}"
    )
    config["nav"][databuilder_nav_index] = {"Data Builder": new_import_string}

    log.info("Databuilder docs imported from branch '%s'", databuilder_branch)
    return config
