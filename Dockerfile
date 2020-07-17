FROM python:3.8.4-alpine3.12

WORKDIR /app

RUN apk --no-cache add curl

ENV VIRTUAL_ENV /app/.venv
ENV POETRY_HOME /app/.poetry
ENV POETRY_VERSION 1.0.9
ENV PATH $POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH

COPY config.py .
COPY poetry.lock .
COPY pyproject.toml .
COPY bot bot/
COPY start.py .

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python \
    && poetry config virtualenvs.in-project true
RUN poetry install --no-dev --no-root

CMD ["python", "start.py"]
