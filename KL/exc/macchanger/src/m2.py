# Version 2 of the program 
import subprocess 
from rich import print as rprint
from src.utils import label

# Variables definition
interface = "eth0"

def mac2():
    """Second version of the progra"""
    label("machanger version 2")
    rprint(f"[magenta] [INFO]Changing macaddress for - {interface}[/magenta]")
    subprocess.run(["macchanger", "-r", interface])
