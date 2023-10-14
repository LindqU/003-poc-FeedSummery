import logging
import os
from enum import Enum


level = {
    "local": logging.DEBUG,
    "dev": logging.DEBUG,
    "stg": logging.WARNING,
    "prd": logging.INFO,
}


# loggerの設定
logger = logging.getLogger(__name__)
env: str = os.getenv("ENV", "prd")

logging.basicConfig(
    level=level.get(env),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
