# stdlib
import os

# thirdparty
from loguru import logger


def initialize_logger():
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logger.add(
        "logs/telemetry-management-info-{time:YYYY-MM-DD}.log",
        format="{time} {level} {message}",
        enqueue=True,
        level="INFO",
        rotation="00:00",
        retention="30 days",
        compression="tar.gz",
    )
    logger.add(
        "logs/telemetry-management-error-{time:YYYY-MM-DD}.log",
        format="{time} {level} {message}",
        enqueue=True,
        level="ERROR",
        rotation="00:00",
        retention="30 days",
        compression="tar.gz",
    )
