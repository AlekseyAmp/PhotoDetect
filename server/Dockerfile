FROM python:3.12.1

RUN pip install --no-cache-dir poetry

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

WORKDIR /app
COPY server/pyproject.toml ./ 
COPY server/poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY server ./

COPY server/.env .env

ENTRYPOINT ["python", "-m", "src.composites.main"]
