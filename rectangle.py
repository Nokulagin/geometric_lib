
def area(a, b):
    '''
    Calculates area of a rectangle using given side lengths a and b
    The formula used for calculations:
        S = a * b

        Arguments:
            a (number type) : side length of a rectangle
            b (number type) : side length of a rectangle

        Return value:
            area (number type) : area of the rectangle with side lengths a and b

        Example:
            area(5, 2) -> returns 10
    '''
    return a * b

def perimeter(a, b):
    '''
    Calculates perimeter of a rectangle using given side lengths a and b
    The formula used for calculations:
        P = 2 * (a + b)

        Arguments:
            a (number type) : side length of a rectangle
            b (number type) : side length of a rectangle

        Return value:
            perimeter (number type) : perimeter of the rectangle with side lengths a and b

        Example:
            perimeter(5, 2) -> returns 14
    '''
    return 2 * (a + b)
