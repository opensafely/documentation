FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN echo "deb http://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble main" > /etc/apt/sources.list.d/deadsnakes-ppa.list && \
    /usr/lib/apt/apt-helper download-file 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf23c5a6cf475977595c89f51ba6932366a755776' /etc/apt/trusted.gpg.d/deadsnakes.asc

RUN apt-get update && \
    apt-get install -y \
    just \
    python3.11 \
    python3.11-venv

# Workaround for Python babel package resulting in
# ValueError: ZoneInfo keys may not be absolute paths, got: /UTC
ENV TZ="Europe/London"

USER vscode

# Clone cohort-extractor submodule via HTTPS.
# GitHub does not allow SSH access without adding a private key.
RUN git config --global url.https://github.com/.insteadOf git@github.com:
