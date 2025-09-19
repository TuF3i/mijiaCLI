import os

import json

from pathlib import Path

from mijiaAPI import mijiaAPI

class getScences():
    def __init__(self, api, console):
        self.api: mijiaAPI = api
        self.console = console
        self.homesPath = "data/homes"
        self.basePath = "data/scences"
        self.addedScences = []
        self.deletedScences = []

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
        for file_path in self.path.rglob('*'):
            if file_path.is_file() and str(file_path) != "data/homes/homes.json":
                home = self._json_reader(str(file_path))
                home_id = home["id"]
                scenes = self.api.get_scenes_list(home_id)
                scene_dir = os.path.join(self.basePath, home_id)
                if not os.path.exists(scene_dir):
                    try:
                        os.makedirs(scene_dir)
                    except:
                        pass
                self._json_writer(os.path.join(scene_dir, "all.json"), scenes)

    def _divideScence(self):
        subdirectories = self._list_subdirectories()
        for subdirectory in subdirectories:
            try:
                scenceAll = self._json_reader(os.path.join(subdirectory, "all.json"))
                if "scene_info_list" in scenceAll:
                    for scence in scenceAll["scene_info_list"]:
                        # 使用正确的键获取scene_id
                        scene_id = scence.get("id", "unknown")
                        scene_file = os.path.join(subdirectory, f"{scene_id}.json")
                        if not os.path.exists(scene_file):
                            self._json_writer(scene_file, scence)
            except Exception as e:
                # 处理可能的错误
                if hasattr(self.console, 'log'):
                    self.console.log(f"处理场景时出错: {e}")

    def _updateScence(self):
        subdirectories = self._list_subdirectories()
        
        # 对每个家庭目录进行处理
        for subdirectory in subdirectories:
            home_id = os.path.basename(subdirectory)
            
            try:
                # 获取当前存储的场景
                current_scenes_file = self._json_reader(os.path.join(subdirectory, "all.json"))
                if "scene_info_list" in current_scenes_file:
                    current_scenes = {scene.get("id", "unknown"): scene for scene in current_scenes_file["scene_info_list"]}
                else:
                    current_scenes = {}
                
                # 获取最新的场景
                self._getScence_all()
                new_scenes_file = self._json_reader(os.path.join(subdirectory, "all.json"))
                if "scene_info_list" in new_scenes_file:
                    new_scenes = {scene.get("id", "unknown"): scene for scene in new_scenes_file["scene_info_list"]}
                else:
                    new_scenes = {}
                
                # 检测新增和删除的场景
                self.addedScences = [scene_id for scene_id in new_scenes if scene_id not in current_scenes]
                self.deletedScences = [scene_id for scene_id in current_scenes if scene_id not in new_scenes]
                
                # 删除不再存在的场景文件
                for scene_id in self.deletedScences:
                    scene_file = os.path.join(subdirectory, f"{scene_id}.json")
                    if os.path.exists(scene_file):
                        try:
                            os.remove(scene_file)
                        except Exception as e:
                            if hasattr(self.console, 'log'):
                                self.console.log(f"删除场景文件失败: {e}")
                
                # 添加新的场景文件
                for scene_id in self.addedScences:
                    scene_file = os.path.join(subdirectory, f"{scene_id}.json")
                    self._json_writer(scene_file, new_scenes[scene_id])
            except Exception as e:
                if hasattr(self.console, 'log'):
                    self.console.log(f"更新家庭 {home_id} 的场景时出错: {e}")

    def getScence(self):
        try:
            # 检查是否存在任何场景目录
            if not os.path.exists(self.basePath) or len(os.listdir(self.basePath)) == 0:
                # 如果没有场景数据，初始化
                self._getScence_all()
                self._divideScence()
                return
            
            # 检查是否有家庭目录
            home_directories = self._list_subdirectories()
            if not home_directories:
                self._getScence_all()
                self._divideScence()
                return
            
            # 更新场景数据
            self._updateScence()
            return
        except Exception as e:
            # 捕获所有异常并记录
            if hasattr(self.console, 'log'):
                self.console.log(f"获取场景时出错: {e}")
            # 出错时重新初始化
            self._getScence_all()
            self._divideScence()
            return

