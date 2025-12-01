import math


def get_S(side_1, side_2):
    s = side_1 * side_2
    return s


def getAreaCircle(radius, count):
    return round(math.pi * radius ** 2, count)
