from settings import Settings
from appindicator import AppIndicator
from xively import Xively
import logging

logger = logging.getLogger(__name__)


class Main(object):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.settings = Settings()
        self.app_ind = AppIndicator()
        self.xively = Xively(self.settings)

    def run(self):
        logger.info("Running")
