from settings import Settings
import logging

logger = logging.getLogger(__name__)


class Xively(object):
    def __init__(self, settings):
        try:
            from xively import XivelyAPIClient
        except ImportError:
            logger.error("ively-python is not installed")

        self.settings = settings
        logger.info("xively init")
