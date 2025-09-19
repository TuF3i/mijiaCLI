from .modelGetCall import Call_3
from rich import Console

class Call_4(Call_3):
    def __init__(self,console):
        super().__init__(console)
        self.console:Console = console