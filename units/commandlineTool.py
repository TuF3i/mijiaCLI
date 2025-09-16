from rich.console import Console

class commandLine():
    def __init__(self):
        self.console = Console()
        self.input = self.console.input
        self.print = self.console.print
        self.log = self.console.log

        self.userCommand = ""

    def userCommandProcesser(self):
        self.userCommand = self.input("[bold green][MiJiaAPI]>[/bold green]")