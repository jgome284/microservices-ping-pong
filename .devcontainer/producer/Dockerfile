# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

# Initialize build line arguments
ARG PYTHON_VERSION=3.10
ARG OS=bookworm
ARG VARIANT=slim

# First stage: Development
FROM python:${PYTHON_VERSION}-${OS} as development

# Prevents Python from writing .pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

# Update and install necessary packages...

RUN apt-get update && \
    # This command updates the package lists for the APT (Advanced Package Tool) package manager. 
    # It fetches the latest information about available packages from the configured repositories.
    apt-get install -y git && \
    # The -y flag is used to automatically confirm any prompts 
    # during the installation process without requiring user interaction.
    apt-get clean && \
    # After installing packages, the apt-get clean command is used to clean up the APT package cache. This removes downloaded package files (.deb) that are no longer needed, reducing the size of the Docker image.
    rm -rf /var/lib/apt/lists/*
    # This command removes the package lists in /var/lib/apt/lists/. 
    # These lists are no longer needed after the package installation is complete, 
    # and removing them helps reduce the size of the Docker image. 
    # The use of rm -rf removes the files and directories forcefully.

    
# Leverage a bind mount to requirements.txt to avoid having to copy them into this layer.
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    # Install Python dependencies
    pip3 install --no-cache-dir -r requirements.txt

CMD ["python3"]

# Second stage: Deployment
FROM python:${PYTHON_VERSION}-${VARIANT}-${OS} as deployment

# Leverage a bind mount to requirements.txt to avoid having to copy them into this layer.
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    # Install Python dependencies
    pip3 install --no-cache-dir -r requirements.txt

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Switch to the non-privileged user to run the application.
USER appuser

# Run service when the container launches
CMD ["python3", "producer.py"]

