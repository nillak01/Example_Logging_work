import logging

logger = logging.getLogger(__name__)


def square_number(number: int | float):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')
    # logger.critical('\n' + 'Module_3: ' + str(logger.parent) + '\n')

    return number**2
