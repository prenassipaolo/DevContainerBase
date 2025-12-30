FROM python:3.14.2-slim-bookworm

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip
# Install producction dependencies from requirements.txt if it exists
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
# Install dev dependencies from dev-requirements.txt if it exists
# COPY dev-requirements.txt /tmp/dev-requirements.txt
# RUN pip install -r /tmp/dev-requirements.txt && rm -f /tmp/dev-requirements.txt

# Create a non-root user 'vscode'
RUN useradd -m vscode
USER vscode

# Set working directory
# WORKDIR /workspaces/DevContainerBase


