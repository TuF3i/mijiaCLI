import os

from pathlib import Path

from mijiaAPI import mijiaAPI

class getScence():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.homesPath = "data/homes"
        self.basePath = "data/scences"

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _json_reader(self, path):
        with open(path, "r") as file:
            res = json.load(file)
        return res

    def _list_subdirectories(self):
        subdirectories = []
        for root, dirs, _ in os.walk(self.basePath):
            for dir_name in dirs:
                full_path = os.path.join(root, dir_name)
                subdirectories.append(full_path)
        return subdirectories
    
    def _getScence_all(self):
        self.path = Path(self.homesPath)
        for file_path in path.rglob('*'):
            if file_path.is_file() and str(file_path) != "data/homes/homes.json":
                home = self._json_reader(str(file_path))
                home_id = home["id"]
                scenes = api.get_scenes_list(home_id)
                if not os.path.exists(os.path.join(self.basePath, home_id, "all.json")):
                    try:
                        os.mkdir(os.path.join(self.basePath, home_id))
                    except:
                        pass
                    self._json_writer(os.path.join(self.basePath, home_id, "all.json"), scenes)

    def _divideScence(self):
        subdirectories = self._list_subdirectories()
        for subdirectory in subdirectories:
            scenceAll:list = self._json_reader(os.path.join(subdirectory, "all.json"))["scene_info_list"]
            for scence in scenceAll:
                scene_id = scence[scene_id]
                if not os.path.exists(os.path.join(subdirectory, scene_id + ".json")):
                    self._json_writer(os.path.join(subdirectory, scene_id + ".json"), scence)

