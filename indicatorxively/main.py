from settings import Settings
from appindicator import AppIndicator
from xivelyclient import XivelyClient

from gi.repository import Gtk
from gi.repository import GObject
import logging


class Main(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        self.settings = Settings()
        self.xively = XivelyClient(self.settings)
        self.app_ind = AppIndicator(self.settings)

    def on_timeout(self, user_data):
        self.logger.info("Updating data")
        self.app_ind.set_data(self.xively.data)

        return True  # to keep calling this function

    def run(self):
        self.timer = GObject.timeout_add(self.settings.update_interval,
                                         self.on_timeout,
                                         None)
        self.on_timeout(None)  # Update imediately after start

        Gtk.main()
