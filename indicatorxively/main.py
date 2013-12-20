# coding: utf8
from settings import Settings
from appindicator import AppIndicator
from xivelyclient import XivelyClient
from gi.repository import Gtk
import logging


class Main(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        self.settings = Settings()
        self.xively = XivelyClient(self.settings, self.on_data_update)
        self.app_ind = AppIndicator(self.settings)

    def on_data_update(self, data):
        self.app_ind.set_data(" ".join((data, "°C")))

    def run(self):
        self.xively.update()
        Gtk.main()

