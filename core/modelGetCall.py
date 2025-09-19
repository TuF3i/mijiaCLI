from .refreshCall import Call_2
from rich import Console

class Call_3(Call_2):
    def __init__(self,console):
        super().__init__(console)
        self.console:Console = console