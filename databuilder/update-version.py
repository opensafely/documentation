import re
from pathlib import Path

import requests


version_pat = re.compile(r"\/v.*\.zip")


def get_tag():
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    url = "https://api.github.com/repos/opensafely-core/databuilder/tags"

    print("Getting latest tag from GitHub")

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    return r.json()[0]["name"]


def write_to_file(tag):
    requirements_file = Path(__file__).parent / "requirements.prod.in"

    with open(requirements_file) as f:
        lines = f.readlines()

    lines = [version_pat.sub(f"/{tag}.zip", line) for line in lines]

    with open(requirements_file, "w") as f:
        f.write("".join(lines))


def main():
    new_tag = get_tag()

    write_to_file(new_tag)


if __name__ == "__main__":
    main()
