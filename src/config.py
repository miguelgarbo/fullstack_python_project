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
    SECRET_KEY:str 
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    DATABASE_URL: str


settings = AppSettings()

# print(f'Database Host from .env: {settings.DB.HOST}')
# print(f'Database Port from .env: {settings.DB.PORT}')
# print(f'Database User from .env: {settings.DB.USER}')
# print(f'Database Name from .env: {settings.DB.NAME}')
print(f'Database Entire URL from .env: {settings.DATABASE_URL}')
