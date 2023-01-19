def on_config(config):
    """
    Hides specified nav sections from the navigation menu.
    Pages are still accessible by URL.
    """
    nav_sections_to_hide = config["extra"]["hide_nav_sections"]
    config["nav"] = [
        section
        for section in config["nav"]
        if list(section.keys())[0] not in nav_sections_to_hide
    ]
    return config
