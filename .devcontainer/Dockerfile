ARG BASE_VERSION

FROM mcr.microsoft.com/devcontainers/python:$BASE_VERSION

# Set environment variables
ENV USER_NAME=vscode
ENV HOME=/home/$USER_NAME

# Install git
RUN apt-get update && \
    apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Install git
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user (otherwise it most likely installs in root)
USER $USER_NAME

# Set working directory
WORKDIR /workspaces/DevContainerBase

# Install all dependencies (dev, test, etc.)
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Install Oh My Zsh if not present
# RUN wget https://github.com/robbyrussel/oh-my-zsh/tree/master/tools/install.sh -O - | zsh || true

# Install the zsh custom theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
# # Move pre-configured zsh files into the container $HOME folder to use the zsh custom theme
COPY .devcontainer/zsh/.zshrc $HOME
COPY .devcontainer/zsh/.p10k.zsh $HOME

