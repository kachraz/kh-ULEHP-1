# Version 2 of the program 
import subprocess 
from rich import print as rprint
from src.utils import label
rom rich.console import Console
console = Console()


# Variables definition
interface = "eth0"

# Command as a list 
command_1 = ["macchanger", "-r", interface]

def mac2():
    """Second version of the progra"""
    label("machanger version 2")
    rprint(f"[green][INFO] Changing macaddress for - {interface}[/green]")
    subprocess.run(["macchanger", "-r", interface])

def mac21():
    """Second version of the progra"""
    label("machanger version 2.1")
    rprint(f"[green][INFO] Changing macaddress for - {interface}[/green]")
    subprocess.run(command_1)


comm_2 = ["curl", "ipinfo.io"]

def mac23():
    "Testing another command here"
    label("curl ipinfo.io command")
    input1 = subprocess.run(comm_2)
    subprocess.run(["jq", input=input1])


