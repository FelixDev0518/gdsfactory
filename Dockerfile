# Install uv
FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install git
RUN apt-get update && \
    apt-get install -y git && \
    # Clean up apt cache
    rm -rf /var/lib/apt/lists/*


# Permissions for non-root user
RUN groupadd -g 1000 runner && useradd -u 1000 -g runner -m runner

WORKDIR /app
RUN chown -R runner:runner /app

# Copy all files in the folder from my foked repository 
COPY . .

USER runner
RUN uv pip install --system .
RUN uv pip install --system pytest 

CMD ["uv", "run", "practice/layouts/Photodetector.py", "practice/layouts/Photomodulator.py"]


