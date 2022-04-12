def triangle_perimeter(a=7, b=2, c=8):
    return a + b + c

def triangle_area(a=7, b=2, c=8):
    from math import sqrt
    p = a + b + c
    h = (2 * sqrt(p * (p - a) * (p - b) * (p - c)))/ a
    return a / 2 * h
