# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests<3",
#     "rich",
# ]
# ///

# ---
"""
mac_changer.py - A script to change the MAC address of a network interface for kl testing
"""
# ---

from rich import print as rprint
import subprocess


def main() -> None:
    subprocess.run(["clear"], shell=True)
    subp1()


def subp1():
    label("mac_changer")
    """Sunprocess function test"""
    subprocess.run(["ifconfig"])
    subprocess.run(["macchanger", "-r", "eth0"])


# Excute the main function
# main()


def label(name):
    rprint(f"""[blue]===
{name}
===[/blue]""")


if __name__ == "__main__":
    main()
