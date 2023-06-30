import logging
from configs.project_config import ProjectConfig
from loghandler import LogHandler


def setup_logger(name, log_file, level=logging.WARNING):
    handler = logging.FileHandler(log_file)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def get_log_handler():
    handler = LogHandler(ProjectConfig().LOG_DIR + ProjectConfig().LOG_FILE)
    return handler


def get_app_logger():
    logger = logging.getLogger(ProjectConfig().LOGGER_NAME)
    logger.setLevel(ProjectConfig().LOG_LEVEL)
    return logger
