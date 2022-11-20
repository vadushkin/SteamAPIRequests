from pydantic import BaseSettings


class Settings(BaseSettings):
    key: str

    class Config:
        env_file = '.env'


settings = Settings()
