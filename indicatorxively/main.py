from settings import Settings
from appindicator import AppIndicator


class Main(object):

    def __init__(self):
        self.settings = Settings()
        self.app_ind = AppIndicator()

    def run(self):
        print("Run")
