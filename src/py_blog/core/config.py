import os
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_user: str
    db_pass: str
    db_host: str
    db_name: str

    def get_dsn(self) -> str:
        return (
            f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"
        )


@dataclass
class Config:
    db: DatabaseConfig
    secret_key: str

    def get_secret_key(self) -> str:
        return self.secret_key


def load_config() -> Config:
    return Config(
        db=DatabaseConfig(
            db_user=_get_env_or_default("DB_USER", ""),
            db_pass=_get_env_or_default("DB_PASSWORD", ""),
            db_host=_get_env_or_default("DB_HOST", "db"),
            db_name=_get_env_or_default("DB_NAME", ""),
        ),
        secret_key=_get_env_or_default("SECRET_KEY", ""),
    )


def _get_env_or_default(varName: str, defaultVal: str) -> str:
    val = os.getenv(varName)
    if val is None:
        val = defaultVal

    return val
