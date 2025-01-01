# Macchanger that accepts arguments

import subprocess
from rich import print as rprint
from src.utils import label


def mac31():
    """Testing macchanger which will accept args"""
    label("machanger version 3.1")
    subprocess.run(["ifconfig"])
    interface = "eth0"
    rprint(f"[green][INFO] Changing macaddress for - {interface}[/green]")
    subprocess.run(["macchanger", "-r", interface])
