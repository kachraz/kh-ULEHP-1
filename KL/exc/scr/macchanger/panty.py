# main python which executes functtions 

from src.m1 import mac1
from src.m2 import mac2, mac21, mac23
from rich.traceback import install
install(show_locals=True)

def main():
    mac23()


if __name__ == "__main__":
    main()
