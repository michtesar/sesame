import logging

from sesame.settings import log_level

logger = logging.getLogger("sesame")
logging.basicConfig(level=log_level)
