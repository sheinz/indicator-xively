from gi.repository import Gtk
import logging


class Settings(object):
    def __init__(self):
        self._xively_key = "OEJA1v2xXYRpKxC2fy3dfFwwDEKYU4TdAyn2gQygwD60TMrG"
        self._xively_feed = 1226691453
        self._xively_datastream = 'outdoor'
        self._update_interval = 20000

    @property
    def xively_key(self):
        return self._xively_key

    @xively_key.setter
    def xively_key(self, value):
        self._xively_key = value

    @property
    def xively_feed(self):
        return self._xively_feed

    @xively_feed.setter
    def xively_feed(self, value):
        self._xively_feed = value

    @property
    def xively_datastream(self):
        return self._xively_datastream

    @xively_datastream.setter
    def xively_datastream(self, value):
        self._xively_datastream = value

    @property
    def update_interval(self):
        return self._update_interval

    @update_interval.setter
    def update_interval(self, value):
        self._update_interval = value


class SettingsWindow(Gtk.Window):
    def __init__(self, settings):
        Gtk.Window.__init__(self, title="Indicator Xively settings",
                            modal=True)

        self.settings = settings
        self.logger = logging.getLogger(__name__)

        grid = Gtk.Grid(row_spacing=5)
        self.add(grid)

        label = Gtk.Label("Xively KEY")
        self.entry_key = Gtk.Entry(text=self.settings.xively_key)
        grid.attach(label, 0, 0, 1, 1)
        grid.attach_next_to(self.entry_key, label,
                            Gtk.PositionType.RIGHT, 1, 1)

        label = Gtk.Label("Xively feed")
        self.entry_feed = Gtk.Entry(text=self.settings.xively_feed)
        grid.attach(label, 0, 1, 1, 1)
        grid.attach_next_to(self.entry_feed, label,
                            Gtk.PositionType.RIGHT, 1, 1)

        label = Gtk.Label("Xively datastream")
        self.entry_datastream = Gtk.Entry(text=self.settings.xively_datastream)
        grid.attach(label, 0, 2, 1, 1)
        grid.attach_next_to(self.entry_datastream, label,
                            Gtk.PositionType.RIGHT, 1, 1)

        label = Gtk.Label("Update interval")
        self.entry_update_interval = Gtk.Entry(
                                    text=self.settings.update_interval)

        grid.attach(label, 0, 3, 1, 1)
        grid.attach_next_to(self.entry_update_interval, label,
                            Gtk.PositionType.RIGHT, 1, 1)

        button_ok = Gtk.Button(label="Ok")
        button_ok.connect("clicked", self._on_ok_clicked)
        button_cancel = Gtk.Button(label="Cancel")
        button_cancel.connect("clicked", self._on_cancel_clicked)

        grid.attach(button_ok, 0, 4, 1, 1)
        grid.attach_next_to(button_cancel, button_ok,
                            Gtk.PositionType.RIGHT, 1, 1)

    def _on_ok_clicked(self, widget):
        self.logger.info("Applying settings")
        self.settings.xively_key = self.entry_key.get_text()
        self.settings.xively_feed = self.entry_feed.get_text()
        self.settings.xively_datastream = self.entry_datastream.get_text()
        self.settings.update_interval = self.entry_update_interval.get_text()

        self.destroy()

    def _on_cancel_clicked(self, widget):
        self.logger.info("Discarding changes")

        self.destroy()
