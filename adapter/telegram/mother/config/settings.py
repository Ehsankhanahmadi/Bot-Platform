from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr



class Settings(BaseSettings):
    bot_token: SecretStr
    webhook_url: str
    adapter_name: str
    redis_host: str
    redis_port: int
    backend_base_url: str
    runtime: str
    backend_password: SecretStr
    backend_token: SecretStr
    backend_timeout: float = 10.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()