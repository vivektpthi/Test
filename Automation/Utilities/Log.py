import logging
from Config import config
import sys


logger = logging.getLogger()
#logger.level=logging.DEBUG
fhandler = logging.FileHandler(filename=config.LOG_FILE_PATH, mode='w')
shandler=logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s]->[%(levelname)s]->%(message)s')
formatter.datefmt='%a,%d-%b-%Y %H:%M:%S'
fhandler.setFormatter(formatter)
shandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.addHandler(shandler)


class Log:
    # this function will write the errors to log file
    def write_errors_to_log_file(self, msg):
        logger_error = logging.getLogger()
        logger_error.setLevel(logging.ERROR)
        logger_error.error(msg)

    # this function will write the info message to log file
    def write_info_to_log_file(self, msg):
        logger_info = logging.getLogger()
        logger_info.setLevel(logging.INFO)
        logger_info.info(msg)