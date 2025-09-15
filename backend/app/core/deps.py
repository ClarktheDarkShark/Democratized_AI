import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import StaticPool

from .config import settings

DATABASE_URL = os.getenv("DATABASE_URL")

# Heroku gives postgres:// but SQLAlchemy needs postgresql:// (or postgresql+psycopg://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,   # helps avoid stale connections on Heroku
    future=True,
)
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
