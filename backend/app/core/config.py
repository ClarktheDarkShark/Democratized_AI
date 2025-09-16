from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "app"
    postgres_user: str = "app"
    postgres_password: str = "password"
    redis_host: str = "localhost"
    jwt_secret: str = "changeme"
    llm_provider: str = "openai"
    llm_api_key: str | None = None
    vector_dim: int = 1536
    frontend_url: str | None = None

    @property
    def database_url(self) -> str:
        """Construct a database URL from individual settings.

        This avoids relying on a pre-built DATABASE_URL environment variable
        which makes the application easier to configure in tests and local
        development.  Postgres is used by default but tests can fall back to
        SQLite when the database is unavailable.
        """
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"

settings = Settings()  # type: ignore
