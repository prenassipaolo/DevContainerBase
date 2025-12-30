ARG BASE_VERSION

FROM mcr.microsoft.com/devcontainers/python:$BASE_VERSION

# Install git
RUN apt-get update && \
    apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip
# Install producction dependencies from requirements.txt if it exists
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
# Install dev dependencies from dev-requirements.txt if it exists
# COPY dev-requirements.txt /tmp/dev-requirements.txt
# RUN pip install -r /tmp/dev-requirements.txt && rm -f /tmp/dev-requirements.txt

# Set username
ENV USER_NAME vscode

# Set home
ENV HOME /home/$USER_NAME

# Create a non-root user (otherwise it most likely installs in root)
RUN useradd -m $USER_NAME
USER $USER_NAME

#Install Oh My Zsh
RUN wget https://github.com/robbyrussel/oh-my-zsh/tree/master/tools/install.sh -O - | zsh || true

# Set working directory
# WORKDIR /workspaces/DevContainerBase


