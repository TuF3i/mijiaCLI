import os

from mijiaAPI import mijiaAPI

class getDevices():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.devicesJSON = "data/devices/devices.json"
        self.basePath = "data/devices/"

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _getDevices_all(self):
        self.devices = self.api.get_devices_list()
        self._json_writer(self.devicesJSON, self.devices)

    def _divideDevices(self):
        for device in self.devices["list"]:
            devModel = device["model"] + ".json"
            devInfo = device
            devPath = os.path.join(self.basePath, devModel)

            if not os.path.exists(devPath):
                self._json_writer(devPath, devInfo)
    
    def getDevices(self):
        self._getDevices_all()
        self._devideDevices()