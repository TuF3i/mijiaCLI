import os
from mijiaAPI import mijiaAPI

class getHomes():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.homesJSON = ""
        self.basePath = ""

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _getHomes_all(self):
        pass

    def _divideHomes(self):
        pass

    def getHomes(self):
        pass