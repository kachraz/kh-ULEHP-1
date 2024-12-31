# Utility functions
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console


def label(name):
    rprint(f"""[blue]===
{name}
===[/blue]""")
