import os

from mijiaAPI import mijiaAPI

class getDevices():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.devicesJSON = "data/devices/devices.json"
        self.basePath = "data/devices/"
        self.addedDevices = []
        self.deletedDevices = []

    def _json_reader(self, path):
        with open(path, "r") as file:
            res = json.load(file)
        return res

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

    def _updateDevices(self):
        currentDevicesFile = self._json_reader(self.devicesJSON)["list"]
        currentDevices = [curr["model"] for curr in currentDevicesFile]

        self._getDevices_all()
        newDevicesFile = self._json_reader(self.devicesJSON)["list"]
        updatedDevices = [update["model"] for update in newDevicesFile]

        self.addedDevices = [dev for dev in updatedDevices if dev not in currentDevices]
        self.deletedDevices = [dev for dev in currentDevices if dev not in updatedDevices]

        for dev in self.deletedDevices:
            os.remove(os.path.join(self.basePath, dev + ".json"))

        for dev in currentDevicesFile:
            if dev["model"] in self.addedDevices:
                devModel = dev["model"] + ".json"
                devInfo = dev
                devPath = os.path.join(self.basePath, devModel)

                if not os.path.exists(devPath):
                    self._json_writer(devPath, devInfo)
    
    def getDevices(self):
        currentDevices = self._json_reader(self.devicesJSON)
        if currentDevices == None:
            self._getDevices_all()
            self._divideDevices()
            return
        
        self._updateDevices()
        return
        
        
