FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && apt-get install -y cargo

USER vscode

# Compiling just is not ideal,
# but is not in the Debian package repository.
# Quicker alternatives might be:
# * use the official install script
# * download and untar ourselves
RUN mkdir -p "$HOME/.local/bin" && cargo install --root "$HOME/.local/" just

# Clone cohort-extractor submodule via HTTPS.
# GitHub does not allow SSH access without adding a private key.
RUN git config --global url.https://github.com/.insteadOf git@github.com:
