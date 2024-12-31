# Utility functions
from rich import print as rprint


def label(name):
    rprint(f"""[blue]===
{name}
===[/blue]""")
