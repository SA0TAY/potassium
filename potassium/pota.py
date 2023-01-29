import requests
from threading import Thread
from time import sleep

class POTA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.activators = []
        self.daemon = True
        self.start()

    def run(self):
        while True:
            apidata = requests.get("https://api.pota.app/spot/activator").json()
            self.activators = [x["activator"] for x in apidata]
            sleep(60)
