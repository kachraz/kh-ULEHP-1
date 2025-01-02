# Main entry point

from src.utils import label

from rich.traceback import install

install(show_locals=True)


def main():
    print("Hello from netsca!")


if __name__ == "__main__":
    main()
