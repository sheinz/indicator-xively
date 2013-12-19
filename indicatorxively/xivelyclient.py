import logging
import xively


class XivelyClient(object):
    def __init__(self, settings):
        self.logger = logging.getLogger(__name__)

#         try:
#             from xively import XivelyAPIClient
#         except ImportError:
#             self.logger.error("xively-python is not installed", exc_info=True)

        self.settings = settings
        self.logger.info("Creating xively api with key=%s",
                         self.settings.xively_key)

        self.api = xively.XivelyAPIClient(self.settings.xively_key)

    @property
    def data(self):
        feed = self.api.feeds.get(self.settings.xively_feed)
        datastream = feed.datastreams[self.settings.xively_datastream_index]
        return str(round(float(datastream.current_value), 1))
