
from middleware.initAPI import initAPI
from middleware.getDevices import getDevices
from rich import Console

class setupEnv():
    def __init__(self):
        self.console = Console()
        self.api = initAPI(self.console)
        self.devices = getDevices(self.api, self.console)
        
    def setup(self):
        pass
