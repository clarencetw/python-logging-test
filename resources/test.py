import csv
import logging

logger = logging.getLogger(__name__)

class Command:
    def console():
        logging.debug('debug')
        logging.info('info')
        logging.warning('warning')
        logging.error('error')

        return True
