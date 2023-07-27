FROM mcr.microsoft.com/devcontainers/python:3.11

USER vscode

RUN curl -L $(curl "https://api.github.com/repos/casey/just/releases/latest" | jq -r '.assets[].browser_download_url | select(contains("x86_64-unknown-linux-musl"))') > /tmp/just.tar.gz
RUN mkdir -p "$HOME/.local/bin/" && tar xvf "/tmp/just.tar.gz" --directory="$HOME/.local/bin"

# Clone cohort-extractor submodule via HTTPS.
# GitHub does not allow SSH access without adding a private key.
RUN git config --global url.https://github.com/.insteadOf git@github.com:
