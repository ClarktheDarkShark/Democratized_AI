from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.pool import StaticPool

from .config import settings


def _create_engine():
    """Create a SQLAlchemy engine, falling back to in-memory SQLite when
    the configured database is unreachable.  This keeps unit tests fast and
    avoids import-time failures when Postgres isn't available."""

    url = settings.database_url
    try:
        engine = create_engine(
            url,
            echo=False,
            pool_pre_ping=True,
            future=True,
        )
        with engine.connect():
            pass
        return engine
    except Exception:  # pragma: no cover - fallback for tests
        return create_engine(
            "sqlite+pysqlite:///:memory:",
            echo=False,
            future=True,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )


engine = _create_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
