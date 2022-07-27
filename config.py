"""Module for configurations."""
import os
from pathlib import Path


class Config:

    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN")

    MINIO_USER = os.getenv("MINIO_USER", "minioadmin")
    MINIO_PASSWORD = os.getenv("MINIO_PASSWORD", "minioadmin")

    POST_DATASET_PATH = Path(__file__).parent / "datasets"

    VK_API_URL = "https://api.vk.com/method/{method}"
    VK_API_VERSION = 5.131
