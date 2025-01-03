# Main entry point

from src.utils import label
from src.w1 import scan1
from src.w2 import w2scan1

from rich.traceback import install

install(show_locals=True)

# Variables that will be used int the functions
IP1 = "10.129.147.243"


# Function definitions
def main():
    w2scan1(IP1)


if __name__ == "__main__":
    main()
