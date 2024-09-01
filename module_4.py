import logging

logger = logging.getLogger(__name__)
logger.propagate = False


def cookie():
    logger.debug("Ааааа куки проблись в Дебаги")
    logger.info("Ты этого видеть не должен")
    logger.warning("Они уже в ворингах, берегись Куки!")
    logger.error("Они захватили Erorr")
    logger.critical("Логер пал под натиском куки. Это конец")
    print("Куки - везде")
