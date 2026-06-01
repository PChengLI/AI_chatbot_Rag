import logging
import sys
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)

logger = logging.getLogger("enterprise-rag")

logger.setLevel(logging.INFO)

# =========================
# Console Handler
# =========================

console_handler = logging.StreamHandler(sys.stdout)

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# =========================
# File Handler
# =========================

file_handler = RotatingFileHandler(
    filename=f"{LOG_DIR}/app.log",
    maxBytes=10 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)