FROM python:3.11-slim
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir "poetry>=1.5"

# Copy project files and install runtime deps
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-dev

COPY . /app

ENTRYPOINT ["python", "scripts/backup_dashboards.py"]