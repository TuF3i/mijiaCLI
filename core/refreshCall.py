from .envCall import Call_1
from rich import Console

class Call_2(Call_1):
    def __init__(self,console):
        super().__init__(console)
        self.console:Console = console

    def refreshDevices(self):
        self.reset.reset_devices()
        self.devices.getDevices()

    def refreshHomes(self):
        self.reset.reset_homes()
        self.homes.getHomes()

    def refreshScence(self):
        self.reset.reset_scences()
        self.scences.getScence()

    def refreshAll(self):
        self.refreshDevices()
        self.refreshHomes()
        self.refreshScence()

        self.reset.reset_login()
        self.console.print("[green]data已重置，重启以重新登录！[/green]")
        self.sys.exit(0)