import os

from mijiaAPI import mijiaAPI

class getHomes():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.homesJSON = "data/homes/homes.json"
        self.basePath = "data/homes"

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _getHomes_all(self):
        self.homes = api.get_homes_list()
        self._json_writer(self.homesJSON, homes)

    def _divideHomes(self):
        for home in self.homes["homelist"]:
            homeID = home["id"] + ".json"
            homeInfo = home
            homePath = os.path.join(self.basePath, homeID)

            if not os.path.exists(homePath):
                self._json_writer(homePath, homeInfo)

    def getHomes(self):
        self._getHomes_all()
        self._divideHomes()