from pydantic_settings import BaseSettings as PydanticBaseConfig


class BaseConfig(PydanticBaseConfig):
    class Config:
        env_file = ".env"


class AppConfig(BaseConfig):
    secret_key: str = "secret_key"
    debug: bool = True

    class Config:
        env_prefix = "APP_"


app_config = AppConfig()


class DatabaseConfig(BaseConfig):
    username: str = "postgres"
    password: str = "postgres"
    database: str = "url_shortener"
    host: str = "localhost"
    port: int = 5432
    pool_size: int = 10
    max_overflow: int = 5
    echo: bool = (
        True  # True means write sql queries in std.out. Set False in production.
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.username}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )

    class Config:
        env_prefix = "DB_"


database_config = DatabaseConfig()


class RedisCpConfig(BaseConfig):
    host: str = "localhost"
    port: int = 6379
    database: str = "url_shortener"
    max_connections: int = 10
    decode_responses: bool = True

    @property
    def redis_url(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.database}"

    class Config:
        env_prefix = "REDIS_"


redis_config = RedisCpConfig()
