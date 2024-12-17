FROM python:3.10.12-slim

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

COPY . /app/

WORKDIR /app/src

EXPOSE 8000

CMD poetry run alembic upgrade head && poetry run uvicorn core.main:app --host 0.0.0.0 --port 8000
