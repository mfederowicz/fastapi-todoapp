from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    sqlalchemy_database_url: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    debug: bool = False
    log_level: str = "INFO"
    host: str
    port: int
    model_config = SettingsConfigDict(
            env_file=(f".env.{os.getenv('APP_ENV', 'dev')}", ".env", ),
            env_file_encoding="utf-8",
            )


settings = Settings()  # pyright: ignore[reportCallIssue]
