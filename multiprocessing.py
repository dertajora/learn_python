import multiprocessing
import logging
import sys

logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)
logger.warning('doomed')