FROM python:3.9

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]