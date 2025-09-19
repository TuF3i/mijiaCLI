import os
import json

from mijiaAPI import mijiaAPI

class getHomes():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.homesJSON = "data/homes/homes.json"
        self.basePath = "data/homes"
        self.addedHomes = []
        self.deletedHomes = []

    def _json_reader(self, path):
        with open(path, "r") as file:
            res = json.load(file)
        return res

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _getHomes_all(self):
        self.homes = self.api.get_homes_list()
        self._json_writer(self.homesJSON, self.homes)

    def _divideHomes(self):
        for home in self.homes["homelist"]:
            homeID = home["id"] + ".json"
            homeInfo = home
            homePath = os.path.join(self.basePath, homeID)

            if not os.path.exists(homePath):
                self._json_writer(homePath, homeInfo)

    def _updateHomes(self):
        currentHomesFile = self._json_reader(self.homesJSON)["homelist"]
        currentHomes = [curr["id"] for curr in currentHomesFile]

        self._getHomes_all()
        newHomesFile = self._json_reader(self.homesJSON)["homelist"]
        updatedHomes = [update["id"] for update in newHomesFile]

        self.addedHomes = [home for home in updatedHomes if home not in currentHomes]
        self.deletedHomes = [home for home in currentHomes if home not in updatedHomes]

        for home in self.deletedHomes:
            homePath = os.path.join(self.basePath, home + ".json")
            if os.path.exists(homePath):
                os.remove(homePath)

        for home in newHomesFile:
            if home["id"] in self.addedHomes:
                homeID = home["id"] + ".json"
                homeInfo = home
                homePath = os.path.join(self.basePath, homeID)

                if not os.path.exists(homePath):
                    self._json_writer(homePath, homeInfo)

    def getHomes(self):
        try:
            currentHomes = self._json_reader(self.homesJSON)
            if currentHomes == None:
                self._getHomes_all()
                self._divideHomes()
                return
            
            self._updateHomes()
            return
        except FileNotFoundError:
            # 如果文件不存在，创建并初始化
            self._getHomes_all()
            self._divideHomes()
            return