import logging


class ErrorLogFilter(logging.Filter):
    # Создаем фильтр на пропуск только ERROR логов
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == "ERROR"


class CriticalLogFilter(logging.Filter):
    # Создаем фильтр на пропуск только CRITICAL логов
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == "CRITICAL"


class DebugWarningLogFilter(logging.Filter):
    # Создаем фильтр на пропуск только DEBUG или WARNING логов
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG', 'WARNING')


class NotDebugLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname != "DEBUG"


class NotInfoLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname != "INFO"
