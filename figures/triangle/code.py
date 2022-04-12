import math
__all__ = ['triangle_perimeter', 'triangle_area']
a, b, c = 7, 2, 8


def triangle_perimeter(a=7, b=2, c=8):
    return a + b + c


def triangle_area(a=7, b=2, c=8):
    return math.sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))