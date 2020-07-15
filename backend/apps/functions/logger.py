import logging
import os
from logging.handlers import RotatingFileHandler


def get_logger():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(BASE_DIR, 'logs')
    log_fname = os.path.join(log_dir, 'app.log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                                  datefmt="%d/%b/%Y %H:%M:%S")
    logger = logging.getLogger('app')
    logging.basicConfig(format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                        datefmt="%d/%b/%Y %H:%M:%S")
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_fname, maxBytes=5000, backupCount=4)
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger
