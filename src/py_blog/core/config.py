import os


class Settings:
    DATABASE_URL: str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"


def get_settings():
    return Settings()
