import logging.config
import yaml

from logging_settings import logging_config
from module_1 import main


with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
# Загружаем настройки логирования из словаря `logging_config`
logging.config.dictConfig(config)

# Исполняем функцию `main` из модуля `module_1.py`
main()
