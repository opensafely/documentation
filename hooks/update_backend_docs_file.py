import shutil
from pathlib import Path

import mkdocs.plugins


@mkdocs.plugins.event_priority(-100)
def on_files(files, config, **kwargs):
    """
    After files are populated, check for a specified imported_backend_docs_file, and
    copy it to the root directory, where mkdocs-opensafely-databuilder can find it.
    Note that we can't use the `BACKEND_DOCS_FILE` environment variable to specify
    a location in the imported docs folder, as this folder will be cleaned up
    in production
    """
    if config["extra"].get("imported_backend_docs_file"):
        base_path = Path(config["config_file_path"]).parent
        imported_docs_file = base_path / config["extra"]["imported_backend_docs_file"]
        docs_file = base_path / "public_docs.json"
        shutil.copy(imported_docs_file, docs_file)
    return files
