import math


def area(r):
    '''
    Calculates area of a circle using given radius r
    The formula used for calculations:
        S = pi * r^2

        Arguments:
            r (number type) : radius of a circle

        Return value:
            area (number type) : area of a circle of radius r

        Example:
            area(5) -> returns 78.54
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates perimeter of a circle using given radius r
    The formula used for calculations:
        P = 2 * pi * r

        Arguments:
            r (number type) : radius of a circle

        Return value:
            perimeter (number type) : perimeter of a circle of radius r

        Example:
            perimeter(5) -> returns 15.71
    '''
    return 2 * math.pi * r

