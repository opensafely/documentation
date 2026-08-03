set default-list := true

lint-docs:
    vale ./docs

test:
    echo "Not implemented here"

format *args=".":
    uv run ruff format --check {{ args }}

lint *args=".":
    uv run ruff check {{ args }}

check: format lint

fix:
    uv run ruff check --fix .
    uv run ruff format .

run:
    NO_MKDOCS_2_WARNING=1 uv run mkdocs serve -a localhost:8910

build:
    NO_MKDOCS_2_WARNING=1 uv run mkdocs build --strict
