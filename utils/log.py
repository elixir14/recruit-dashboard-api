import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(app_name, screen_log=False, txt_log=True, elastic_log=False,
                  log_level=logging.DEBUG):
    log_dir = os.path.abspath('logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log = logging.getLogger(app_name)
    log.setLevel(log_level)

    log_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s %(process)d %(filename)s:%(lineno)d  :: %(message)s"
    )

    if txt_log:
        txt_handler = RotatingFileHandler(
            os.path.join(log_dir, 'app.txt'),
            mode='a',
            maxBytes=1024 * 1024 * 5,
            backupCount=50
        )
        txt_handler.setFormatter(log_formatter)
        log.addHandler(txt_handler)
        log.info("Logger initialized for app %s.", app_name)

    if screen_log:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        log.addHandler(console_handler)
