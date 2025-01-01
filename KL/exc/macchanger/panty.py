# main python which executes functtions

from src.testa import *
from rich.traceback import install

install(show_locals=True)


def main():
    animal_sound()


if __name__ == "__main__":
    main()
