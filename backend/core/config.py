from typing import Annotated, Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/"
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    # @computed_field  # type: ignore[misc]
    # @property
    # def server_host(self) -> str:
    #     # Use HTTPS for anything other than local development
    #     if self.ENVIRONMENT == "local":
    #         return f"http://{self.DOMAIN}"
    #     return f"https://{self.DOMAIN}"

    PROJECT_NAME: str = "pizza"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "pizza"

    @computed_field  # type: ignore[misc]
    @property
    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env.dev"


settings = Settings()  # type: ignore
