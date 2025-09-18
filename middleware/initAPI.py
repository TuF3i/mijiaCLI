from mijiaAPI import mijiaAPI
from mijiaAPI import mijiaLogin

class initAPI():
    def __init__(self, console):
        self.authJSON = "data/auth/auth.json"   #认证文件路径
        self.loginStatusJSON = "data/auth/loginCheck.json"  #认证状态文件路径
        self.RetryMax = 5   #最大重试次数
        self.console = console
        self.api = None

    def _json_reader(self, path):
        with open(path, "r") as file:
            res = json.load(file)
        return res

    def _json_writer(self, path, item):
        with open(path, "w") as file:
            json.dump(item, file, indent=4)
        return None

    def _loginChecker(self):
        data = self._json_reader(self.loginStatusJSON)
        if data["ifLogin"]:
            return True
        else:
            return False

    def _QRLogin(self):
        try:
            api = mijiaLogin()
            auth = api.QRlogin()
            self._json_writer(self.authJSON, auth)
            data = self._json_reader(self.loginStatusJSON)
            data["ifLogin"] = True
            self._json_writer(self.loginStatusJSON,data)
        except Exception as err:
            console.log(err)

    def GetAPI(self):
        RetryCount = 0
        while (not self._loginChecker() and RetryCount <= self.RetryMax):
            self._QRLogin()
            RetryCount += 1
        self.api = mijiaAPI(self._json_reader())
        return self.api
