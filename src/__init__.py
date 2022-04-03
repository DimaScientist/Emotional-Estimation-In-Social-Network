"""Initialize module."""
import os
from pathlib import Path

from dotenv import load_dotenv

env_path = os.path.join(Path(os.getcwd()).parent, ".env")
if os.path.exists:
    load_dotenv(env_path)

from config import Config

configurations = Config()
