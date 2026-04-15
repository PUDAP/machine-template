# Edge Service

- Meant to be ran on the machine or a server connected to the machine
- Provides connection to NATS and handles tranlation of nats commands to machine methods for execution

## User Guide

### Setup

1. Copy the environment configuration file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and configure the following variables:
   - `MACHINE_ID`: Machine identifier
   - `NATS_SERVERS`: Comma-separated list of NATS server URLs


3. Run the service using one of the following methods:

   **Option A: Baremetal (using uv)**
   ```bash
   uv sync --all-packages
   uv run main.py
   ```

   **Option B: Docker Compose**
   ```bash
   docker compose pull && docker compose up -d
   ```

## Docker Deployment

### Building and Pushing to GitHub Container Registry

1. **Login to GitHub Container Registry:**
   ```bash
   echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
   ```
   Or use a GitHub Personal Access Token with `write:packages` permission.

2. **Build the image:**
   ```bash
   cd edge
   docker compose build
   ```

3. **Tag and push the image:**
   ```bash
   # Push to GitHub Container Registry
   docker push ghcr.io/PUDAP/<image_name>:latest
   ```

   Or use docker compose to build and push:
   ```bash
   docker compose build
   docker compose push
   ```

4. **Pull and use the image:**
   ```bash
   docker pull ghcr.io/PUDAP/<image_name>:latest
   docker compose up -d
   ```