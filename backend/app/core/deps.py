import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import StaticPool

from .config import settings

DATABASE_URL = os.getenv("DATABASE_URL") or (
    f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}@"
    f"{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)

engine = create_engine(DATABASE_URL, echo=False, future=True)
try:
    with engine.connect():
        pass
except OperationalError:
    DATABASE_URL = "sqlite+pysqlite:///:memory:"
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
