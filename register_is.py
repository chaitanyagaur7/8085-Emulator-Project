from global_ import *

def resister_is(temp):
    if temp == "M":
        return 7
    elif temp == "A":
        return 0
    elif temp == "B":
        return 1
    elif temp == "C":
        return 2
    elif temp == "D":
        return 3
    elif temp == "E":
        return 4
    elif temp == "H":
        return 5
    elif temp == "L":
        return 6
    else:
        return -1
