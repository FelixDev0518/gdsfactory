# Install uv
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install git
RUN apt-get update && \
    apt-get install -y git && \
    # Clean up apt cache
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy all files in the folder from my foked repository 
COPY . .

RUN uv pip install --system .
RUN uv pip install --system pytest 




