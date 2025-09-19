from .modelPostCall import Call_4
from rich import Console

class Call_5(Call_4):
    def __init__(self,console):
        super().__init__(console)
        self.console:Console = console