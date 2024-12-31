# Version of macchanger program
import subprocess
from src.utils import label


def subp1():
    label("mac_changer")
    """Sunprocess function test"""
    subprocess.run(["ifconfig"])
    rprint("[cyan] Executing the macchanger three times[/cyan]")
    for i in range(3):
        subprocess.run(["macchanger", "-r", "eth0"])
        rprint("[cyan] --- [/cyan]")
