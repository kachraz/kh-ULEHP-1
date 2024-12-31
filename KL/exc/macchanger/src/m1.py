# Version of macchanger program
import subprocess
from rich import print as rprint


def subp1():
    label("mac_changer")
    """Sunprocess function test"""
    subprocess.run(["ifconfig"])
    rprint("[cyan] Executing the macchanger three times[/cyan]")
    for i in range(3):
        subprocess.run(["macchanger", "-r", "eth0"])
        rprint("[cyan] --- [/cyan]")
