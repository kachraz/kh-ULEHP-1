# Using scapy

from rich.traceback import install

import scapy.all as sca

install(show_locals=True)


# Functions are written here
def scan1(ip):
    """Using scan with scapy"""
    sca.arping(ip)
