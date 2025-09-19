import shutil
import os

class resetAll():
    def __init__(self):
        self.devicesPath = "data/devices"
        self.homesPath = "data/homes"
        self.scencePath = "data/scences"

        self.devicesJSON = "data/devices/devices.json"
        self.homesJSON = "data/homes/homes.json"
        self.scencesJSON = "data/scences/scences.json"

        self.authJSON = "data/auth/auth.json"
        self.ifLoginJSON = "data/auth/loginCheck.json"

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
        return None

    def _delete_all_in_directory(self,directory_path):
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            os.makedirs(directory_path)
        else:
            os.makedirs(directory_path)

    def reset_devices(self):
        self._delete_all_in_directory(self.devicesPath)
        self._json_writer(self.devicesJSON, None)
        
    def reset_homes(self):
        self._delete_all_in_directory(self.homesPath)
        self._json_writer(self.homesJSON, None)

    def reset_scences(self):
        self._delete_all_in_directory(self.scencePath)
        self._json_writer(self.scencesJSON, None)

    def reset_login(self):
        os.remove(self.authJSON)
        os.remove(self.ifLoginJSON)

        self._json_writer(self.authJSON, None)
        self._json_writer(self.ifLoginJSON, {"ifLogin":false})