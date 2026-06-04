# Install uv
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install git
RUN apt-get update && \
    apt-get install -y git && \
    # Clean up apt cache
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# From my repository, install gdsfactory (the way to reduce the size of the image)
RUN uv pip install git+https://gitbub.com/FelixDev0518/gdsfactory.git

CMD ["ls", "-la", "/app"]




