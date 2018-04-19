from Priruba import *
from math import pi, acos
from sys import stdin
import sys

def main():
    mojePriruba = Priruba()
    mojePriruba.setProperty1(pi)
    mojePriruba.calcVolume()
    Volume = mojePriruba.getVolume()
    print(Volume)
    

if __name__ == '__main__':
    sys.exit(int(main() or 0))

    