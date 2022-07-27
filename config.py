"""Module for configurations."""
import os
from pathlib import Path


class Config:

    ELASTIC_HOST: str = os.getenv("ELASTIC_HOST", "localhost")
    ELASTIC_PORT: int = int(os.getenv("ELASTIC_PORT", 9200))

    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN")

    MINIO_USER = os.getenv("MINIO_USER", "minioadmin")
    MINIO_PASSWORD = os.getenv("MINIO_PASSWORD", "minioadmin")

    POST_DATASET_PATH = Path(__file__).parent / "datasets"

    VK_API_URL = "https://api.vk.com/method/{method}"
    VK_API_VERSION = 5.131
