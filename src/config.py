from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


# class DatabaseSettings(BaseModel):
#     HOST: str
#     PORT: int
#     USER: str
#     PASSWORD: str
#     NAME: str
#     URL: str


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', env_nested_delimiter='_'
    )
    DATABASE_URL: str

    # DB: DatabaseSettings
    # debug: bool = False


settings = AppSettings()

print(f'Database Host from .env: {settings.DATABASE_URL}')
