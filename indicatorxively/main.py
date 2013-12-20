# coding: utf8
from settings import Settings, SettingsWindow
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
        menu_list = [{'text': "_Settings", 'callback': self.on_settings_click}]
        self.app_ind = AppIndicator(self.settings, menu_list)

    def on_data_update(self, data):
        self.app_ind.set_data(" ".join((data, "°C")))

    def on_settings_click(self, widget):
        self.logger.info("Settings is clicked")
        self.settings_win = SettingsWindow(self.settings)
        self.settings_win.show_all()

    def run(self):
        self.xively.update()
        Gtk.main()

