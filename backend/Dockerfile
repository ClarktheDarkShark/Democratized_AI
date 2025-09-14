FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn[standard] sqlalchemy psycopg2-binary alembic pydantic-settings redis rq openai sentence-transformers
COPY app ./app
RUN useradd -m appuser
USER appuser
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health/live || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
