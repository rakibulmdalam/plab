import logging
from logging.handlers import TimedRotatingFileHandler

from configs.project_config import ProjectConfig


class LogHandler(TimedRotatingFileHandler):
    def __init__(
        self,
        filename,
        when=ProjectConfig().LOG_ROTATE_WHEN,
        interval=ProjectConfig().LOG_ROTATE_INTERVAL,
        backup_count=ProjectConfig().LOG_ROTATE_BACKUPCOUNT,
    ):
        super().__init__(
            filename=filename, when=when, interval=interval, backupCount=backup_count
        )
        self.set_formatter()

    def set_formatter(self, formatter=ProjectConfig().LOG_FORMATTER):
        self.formatter = formatter
        super().setFormatter(logging.Formatter(self.formatter))

    def set_level(self, level=logging.INFO):
        self.level = level
        super().setLevel(self.level)

    def rotate(self, source, dest):
        super().rotate(source, dest)
