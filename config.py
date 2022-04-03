"""Module for configurations."""
import os


class Config:

    ELASTIC_HOST: str = os.getenv("ELASTIC_HOST", "localhost")
    ELASTIC_PORT: int = int(os.getenv("ELASTIC_PORT", 9200))

    SECURITY_KEY: str = os.getenv("SECURITY_KEY")
    SERVICE_KEY: str = os.getenv("SERVICE_KEY")
    APP_ID: int = int(os.getenv("APP_ID"))
