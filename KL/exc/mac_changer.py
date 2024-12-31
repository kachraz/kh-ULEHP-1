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
    label("mac_changer.py")


def subp1():
    """Sunprocess function test"""
    subprocess.call(["macchanger", "-r", "eth0"], shell=True)


# Excute the main function
# main()


def label(name):
    rprint("""f[blue]===
{name}
===[/blue]""")


if __name__ == "__main__":
    main()
