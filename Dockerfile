FROM python:3.11-slim

# Basic env
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for Pillow (and general build niceties)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files first (better Docker cache)
COPY pyproject.toml uv.lock ./

# Install deps into the container environment
RUN uv sync --frozen

# Copy the rest of the app
COPY app ./app
COPY model_store ./model_store
COPY scripts ./scripts
COPY README.md ./

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]