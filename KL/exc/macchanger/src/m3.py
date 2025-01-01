# Macchanger that accepts arguments

import subprocess
from rich import print as rprint
from rich.prompt import Prompt as Pr
from src.utils import label
from rich.traceback import install
from rich import inspect
import re

install(show_locals=True)


def mac31():
    """Testing macchanger which will accept args"""
    label("machanger version 3.1")
    subprocess.run(["ifconfig"])
    interface = "eth0"
    rprint(f"[green][INFO] Changing macaddress for - {interface}[/green]")
    subprocess.run(["sudo", "macchanger", "-r", interface])


def mac32():
    """Testing macchanger which will accept args"""

    label("machanger version 3.2")
    subprocess.run(["ifconfig"])

    interface = Pr.ask("What interface do you want to rape")

    rprint(f"[green][INFO] Changing macaddress for - {interface}[/green]")

    subprocess.run(["sudo", "macchanger", "-r", interface])


def mac33():
    """Testing macchanger which will accept args"""

    label("Tresting Regex")

    ifco = subprocess.check_output(["ifconfig"])

    re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifco)
