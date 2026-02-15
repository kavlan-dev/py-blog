FROM python:3.13-slim
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY poetry.lock pyproject.toml README.md ./
COPY src/ src/

RUN poetry install

CMD ["poetry", "run", "python", "src/py_blog/main.py"]
