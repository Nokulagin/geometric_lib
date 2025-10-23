
def area(a, h):
    '''
    Calculates area of a triangle using given base length a and height length h
    The formula used for calculations:
        S = a * h / 2

        Arguments:
            a (number type) : base length of a triangle
            h (number type) : height length of a triangle

        Return value:
            area (number type) : area of the triangle with base length a and height length h

        Example:
            area(5, 2) -> returns 5
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Calculates perimeter of a triangle using given side lengths a, b, c
    The formula used for calculations:
        P = a + b + c

        Arguments:
            a (number type) : side length of a triangle
            b (number type) : side length of a triangle
            c (number type) : side length of a triangle

        Return value:
            perimeter (number type) : perimeter of the triangle with side lengths a, b, c

        Example:
            perimeter(5, 2, 4) -> returns 11
    '''
    return a + b + c
