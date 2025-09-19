from middleware.initAPI import initAPI
from middleware.getDevices import getDevices
from middleware.getHomes import getHomes
from middleware.getScence import getScences
from middleware.resetAll import resetAll
from rich import Console
import sys

class Call_1():
    def __init__(self, console):
        self.console:Console = console
        self.sys = sys
        self.initAPI = initAPI(self.console)

        self.api = self.initAPI.GetAPI()
        self.devices = getDevices(self.api, self.console)
        self.homes = getHomes(self.api, self.console)
        self.scences = getScences(self.api, self.console)
        self.reset = resetAll()
        
    def setupEnv(self):
        self.devices.getDevices()
        self.homes.getHomes()
        self.scences.getScence()

    def getAPI(self):
        return self.api
