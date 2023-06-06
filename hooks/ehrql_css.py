import logging
import pathlib

from mkdocs.structure.files import File


log = logging.getLogger("mkdocs")


def on_files(files, config, **kwargs):
    """
    Update files with ehrQL CSS.

    This is necessary because extra_css paths must be in the docs/ dir
    and the imported docs end up in an entirely different path:
    imported_docs/
    """
    ehrql_css_config = config["extra"]["ehrql_imported_css_path"]
    ehrql_css_path = pathlib.Path(ehrql_css_config)
    css_file = File(ehrql_css_path, "./", "./site/css", False)
    log.info("ehrQL CSS path imported from '%s'", ehrql_css_config)
    files.append(css_file)
    return files
