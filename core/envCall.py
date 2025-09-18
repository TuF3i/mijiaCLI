
from middleware.initAPI import initAPI
from middleware.getDevices import getDevices
from rich import Console

class setupEnv():
    def __init__(self):
        self.console = Console()
        self.initAPI = initAPI(self.console)
        
    def setup(self):
        self.api = self.initAPI.GetAPI()
        self.devices = getDevices(self.api, self.console)