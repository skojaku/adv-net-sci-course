# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.9-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Define the path to the virtualenv to work with
ARG VENV_PATH="/home/vscode/venv"


COPY requirements.txt /tmp/pip-tmp/
RUN su vscode -c "python -m venv /home/vscode/venv" \
   && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
   && rm -rf /tmp/pip-tmp


RUN echo "deb http://downloads.skewed.de/apt bullseye main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 612DEFB798507F25
RUN apt-get update && apt-get install -y python3-graph-tool python3-cairo python3-matplotlib


# Define the path to the virtualenv to work with
#ARG VENV_PATH="/home/vscode/venv"


#COPY requirements.txt /tmp/pip-tmp/
#RUN su vscode -c "python -m venv /home/vscode/venv" \
#   && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
#   && rm -rf /tmp/pip-tmp
