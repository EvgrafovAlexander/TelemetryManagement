# thirdparty
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    host: str = Field(default="localhost", alias="APP_HOST")
    port: int = Field(default=8000, alias="APP_PORT")

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')


class DBSettings(BaseSettings):
    host: str = Field(default="localhost", alias="DB_HOST")
    port: int = Field(default=5432, alias="DB_PORT")
    name: str = Field(default="postgres", alias="DB_NAME")
    user: str = Field(default="postgres", alias="DB_USER")
    password: str = Field(default="postgres", alias="DB_PASSWORD")

    @property
    def url(self):
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{str(self.port)}/{self.name}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
