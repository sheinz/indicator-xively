import logging
from gi.repository import GObject
import requests
from requests.exceptions import ConnectionError
from requests.auth import AuthBase


class DataNotAvailable:
    pass


class XivelyAuth(AuthBase):
    def __init__(self, key):
        self.key = key

    def __call__(self, r):
        r.headers['X-ApiKey'] = self.key
        return r


class XivelyClient(object):
    def __init__(self, settings, on_data_update):
        self.logger = logging.getLogger(__name__)

        self.settings = settings
        self.on_data_update = on_data_update

        self.timer = GObject.timeout_add(self.settings.update_interval,
                                         self._on_timeout,
                                         None)

    @property
    def data(self):
        result = "NA"
        url = "https://api.xively.com/v2/feeds/{feed}/datastreams/"\
              "{datastream}.json".format(
                            feed=self.settings.xively_feed,
                            datastream=self.settings.xively_datastream)
        self.logger.info("Requesting url: %s", url)
        try:
            r = requests.get(url, auth=XivelyAuth(self.settings.xively_key))
        except ConnectionError:
            self.logger.warn("Connection error")
            raise DataNotAvailable

        if r.status_code != 200:
            self.logger.warn("Error status code: %d", r.status_code)
            raise DataNotAvailable
        else:
            data = r.json()
            str_val = data['current_value']
            result = str(round(float(str_val), 1))

        return result

    def _on_timeout(self, user_data):
        try:
            data = self.data
            self.on_data_update(data)
            self.logger.info("Updating data. Data=%s", data)
        except DataNotAvailable:
            self.logger.info("Data not available")

        return True  # to keep calling this function

    def update(self):
        self._on_timeout(None)
