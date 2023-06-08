import logging
import pathlib

from mkdocs.structure.files import File


log = logging.getLogger("mkdocs")


def on_files(files, config, **kwargs):
    """
    Update files available to MkDocs with ehrQL documentation CSS.

    This hook is necessary because
    * paths provided to `extra_css` must be in the `docs_dir` directory
      (the default being `docs/`)
    * the multi-repo plugin pulls in the ehrQL docs to a different path,
      outside of `docs/`

    This approach is one of the suggested workarounds in:
    https://github.com/mkdocs/mkdocs/issues/1662
    """
    for css_config_entry in config["extra"]["ehrql_imported_css"]:
        css_path = pathlib.Path(css_config_entry)

        # This MkDocs API is not well documented anywhere.
        # We want to create a MkDocs File object:
        # whose source is the `src_dir` concatenated to the ehrQL CSS path
        # whose destination is an appropriate CSS directory in the `site_dir`.
        # `use_directory_urls` only affects Markdown files, and this is a CSS file.
        css_file = File(
            path=css_path,
            src_dir=config["docs_dir"] + "/../",
            dest_dir=config["site_dir"] + "/css",
            use_directory_urls=False,
        )
        log.info("ehrQL CSS imported from '%s'", css_path)
        files.append(css_file)
    return files
