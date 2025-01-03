# scapy arp ping 2nd version
# --- Imports Section ---

from rich import print as rprint
import scapy.all as sca
from rich.console import Console

console = Console()


# --- Variables Section ---
def w2scan1(ip):
    arp_request = sca.ARP(pdst=ip)
