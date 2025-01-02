# Main entry point

from src.utils import label

from rich.traceback import install

install(show_locals=True)


def main():
    label("Panty")


if __name__ == "__main__":
    main()
