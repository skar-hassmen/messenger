from pydantic import BaseModel, PostgresDsn, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str
    port: int


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('app/.env.template', 'app/.env',),
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__',
        env_file_encoding='utf-8'
    )
    api: ApiPrefix = ApiPrefix()
    run: RunConfig
    db: DataBaseConfig


try:
    settings = Settings()
except ValidationError as e:
    print(e)