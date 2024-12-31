# Version 2 of the program 
import subprocess 
from rich import print as rprint
from src.utils import label

# Variables definition
interface = "eth0"

# Command as a list 
command_1 = ["macchanger", "-r", interface]
comm_2 = ["curl", "ipinfo.io"]

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
