from dataclasses import dataclass
import logging
import os
from sys import platform


@dataclass
class ProjectConfig:
    
    HOME_DIR: str = os.environ['USERPROFILE'] if platform == 'win32' else os.environ['HOME']
    PROJECT_DIR: str = HOME_DIR + '/parcellab/'
    PORT: int = 5000
    DB: str = "resources/parcellab.json"
    SHIPMENTS_TABLE_NAME: str = "shipments"
    CACHE_TIMEOUT: int = 7200  # 2 hours

    WEATHERAPI_API_KEY: str = "76302673469d42209ec174958232606"
    WEATHER_API_BASE_URL: str = "http://api.weatherapi.com/v1"

    LOG_DIR: str = "logs/"
    LOG_FILE: str = "project.log"
    LOGGER_NAME: str = "track_trace"
    LOG_LEVEL: str = logging.DEBUG
    LOG_FORMATTER: str = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s"
    LOG_ROTATE_WHEN: str = "h"
    LOG_ROTATE_INTERVAL: int = 4
    LOG_ROTATE_BACKUPCOUNT: int = 0
