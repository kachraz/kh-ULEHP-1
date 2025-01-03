# scapy arp ping 2nd version
# --- Imports Section ---

from rich import print as rprint
import scapy.all as sca
from rich.console import Console

console = Console()


# --- Variables Section ---
def w2scan1(ip):
    arp_request = sca.ARP()
    arp_request.pdst = ip
    rprint(arp_request.summary())


"""
This funct
"""


def w2scan2():
    """Listing all of scapy attributes"""
    sca.ls(sca.ARP())  # Show all the attributes
