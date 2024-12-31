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
    print("Hello from mac_changer.py!")
    print_hi("world")


def print_hi(name):
    rprint(f"[green]Hi, {name}[/green]")


# Excute the main function
# main()

if __name__ == "__main__":
    main()
