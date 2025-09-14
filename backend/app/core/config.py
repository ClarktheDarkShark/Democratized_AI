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

    class Config:
        env_file = ".env"

settings = Settings()  # type: ignore
