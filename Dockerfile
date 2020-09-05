FROM python:3.8.4-alpine3.12

WORKDIR /app

RUN apk --no-cache add curl

ENV VIRTUAL_ENV /app/.venv
ENV BOTOGRAM_VERSION ac30be0267dc2df1919ed781682eb45002b3884c
ENV POETRY_HOME /app/.poetry
ENV POETRY_VERSION 1.0.10
ENV PATH $POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH

COPY .env .env
COPY poetry.lock .
COPY pyproject.toml .
COPY bot bot/
COPY start.py .

RUN git clone --depth 1 --branch ${BOTOGRAM_VERSION} https://github.com/python-botogram/botogram.git
RUN cd botogram
RUN invoke install && cd ..

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev --no-root

CMD ["python", "start.py"]
