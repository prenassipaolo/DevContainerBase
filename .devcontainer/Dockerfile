ARG BASE_VERSION
ARG UV_VERSION

# Use the uv image as a build stage to copy uv binary from it
FROM ghcr.io/astral-sh/uv:$UV_VERSION as uv_builder
# This base image has to stay last
FROM mcr.microsoft.com/devcontainers/python:$BASE_VERSION


# Set environment variables
ENV USER_NAME=vscode
ENV HOME=/home/$USER_NAME

# Switch to non-root user
USER $USER_NAME

# Ensure the virtualenv is created in the project directory
# ENV UV_PROJECT_ENVIRONMENT=/home/$USER_NAME/.
# Add the venv bin to path so we don't have to 'source' it
# ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=True \
    PYTHONUNBUFFERED=True \
    UV_LINK_MODE=copy


# Install git
RUN apt-get update && \
    apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*


# Set working directory
# WORKDIR /workspaces/DevContainerBase

# Install all dependencies (dev, test, etc.)
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Pre-install dependencies
# We copy only the dependency files first to leverage Docker cache
COPY --from=uv_builder --chown=$USER_NAME: /uv /uvx /bin/
# COPY --from=uv_builder --chown=$USER_NAME:$USER_NAME pyproject.toml uv.lock* ./

# Install Oh My Zsh if not present
# RUN wget https://github.com/robbyrussel/oh-my-zsh/tree/master/tools/install.sh -O - | zsh || true

# Install the zsh custom theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
# # Move pre-configured zsh files into the container $HOME folder to use the zsh custom theme
COPY ./zsh/.zshrc $HOME
COPY ./zsh/.p10k.zsh $HOME