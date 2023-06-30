from dataclasses import dataclass
import logging


@dataclass
class ProjectConfig:
    PROJECT_DIR: str = "./"
    PORT: int = 5000

    REDIS_PORT: int = 6379
    REDIS_HOST: str = "localhost"  # change to "redis" if you are using docker-compose
    CACHE_TIMEOUT: int = 7200  # 2 hours

    DB: str = "resources/parcellab.json"
    SHIPMENTS_TABLE_NAME: str = "shipments"

    WEATHERAPI_API_KEY: str = (
        "76302673469d42209ec174958232606"  # TODO: put this in env variables
    )
    WEATHER_API_BASE_URL: str = "http://api.weatherapi.com/v1"

    LOG_DIR: str = "logs/"
    LOG_FILE: str = "project.log"
    LOGGER_NAME: str = "track_trace"
    LOG_LEVEL: int = logging.DEBUG
    LOG_FORMATTER: str = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s"
    LOG_ROTATE_WHEN: str = "h"
    LOG_ROTATE_INTERVAL: int = 4
    LOG_ROTATE_BACKUPCOUNT: int = 0
