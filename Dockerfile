FROM python:3.8.5-alpine3.12

RUN apk --no-cache add bash curl git

ENV BOTOGRAM_VERSION ac30be0267dc2df1919ed781682eb45002b3884c
ENV POETRY_HOME /app/.poetry
ENV POETRY_VERSION 1.0.10
ENV PATH $POETRY_HOME/bin:$PATH

WORKDIR /dep

RUN git config --global advice.detachedHead false
RUN git clone --single-branch https://github.com/python-botogram/botogram.git
RUN cd botogram && git checkout ${BOTOGRAM_VERSION} && pip install --no-cache invoke virtualenv && invoke install

WORKDIR /app

COPY .env .env
COPY poetry.lock .
COPY pyproject.toml .
COPY bot bot/
COPY start.py .

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

CMD ["python", "start.py"]
