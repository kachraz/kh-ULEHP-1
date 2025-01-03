# Main entry point

from src.utils import label
from src.w1 import scan1

from rich.traceback import install

install(show_locals=True)

# Variables that will be used int the functions
IP1 = "10.129.49.1/24"


# Function definitions
def main():
    scan1(IP1)


if __name__ == "__main__":
    main()
