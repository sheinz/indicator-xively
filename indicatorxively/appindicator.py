from settings import Settings
from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
import logging
import os


class AppIndicator(object):

    def __init__(self, settings, menu_list):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        icon_path = os.path.join(os.path.dirname(__file__), 'temp-icon.png')
#         icon_path = os.path.abspath("indicatorxively/temp-icon.png")
        self.ind = appindicator.Indicator.new(
                      "xively indicator",
                      icon_path,
                      appindicator.IndicatorCategory.APPLICATION_STATUS)

        self.ind.set_status(appindicator.IndicatorStatus.ACTIVE)

        menu = Gtk.Menu()

        for item in menu_list:
            menu_item = Gtk.MenuItem(item['text'], use_underline=True)
            menu_item.connect("activate", item['callback'])
            menu_item.show()
            menu.append(menu_item)

        menu_quit = Gtk.MenuItem("_Quit", use_underline=True)
        menu_quit.connect("activate", self.on_quit_click)
        menu_quit.show()
        menu.append(menu_quit)

        self.ind.set_menu(menu)

    def on_test_click(self, widget):
        self.ind.set_label("-13.0", "")

    def on_quit_click(self, widget):
        self.logger.info("Quitting")
        Gtk.main_quit()

    def set_data(self, data):
        self.ind.set_label(data, "")
