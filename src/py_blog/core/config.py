import os


class Settings:
    def __init__(self) -> None:
        self.db_user = get_env_or_default("DB_USER", "")
        self.db_pass = get_env_or_default("DB_PASSWORD", "")
        self.db_host = get_env_or_default("DB_HOST", "db")
        self.db_name = get_env_or_default("DB_NAME", "")
        self.secret_key = get_env_or_default("SECRET_KEY", "")

        if self.db_user == "" or self.db_pass == "" or self.db_name == "":
            raise Exception("Не верно указаны настройки бд")

        if self.secret_key == "":
            raise Exception("Не указан секретный ключ")

    def get_database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:5432/{self.db_name}"

    def get_secret_key(self) -> str:
        return self.secret_key


def get_settings() -> Settings:
    return Settings()


def get_env_or_default(varName: str, defaultVal: str) -> str:
    val = os.getenv(varName)
    if val is None:
        val = defaultVal

    return val
