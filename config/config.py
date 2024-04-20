from typing import Optional

from pydantic_settings import BaseSettings
from pymongo import MongoClient

import models


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None

    # JWT
    JWT_SECRET_ACCESS_TOKEN: str = ''
    JWT_SECRET_REFRESH_TOKEN: str = ''
    JWT_SECRET_EMAIL_VERIFY_TOKEN: str = ''
    JWT_SECRET_FORGOT_PASSWORD_TOKEN: str = ''

    class Config:
        env_file = ".env"
        from_attributes = True


settings = Settings()  # type: ignore
