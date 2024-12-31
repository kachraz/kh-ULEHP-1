# Utility functions
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
console = Console()


def label(name):
    panel = Panel("""
Learning Conditionals Here
""",title="Main",subtitle="This One", style="Italic", border_style="magenta")
# Print the Panel
console.print(panel)
