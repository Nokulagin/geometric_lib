import unittest


def area(a):
    '''
    Calculates area of a square using given side length a
    The formula used for calculations:
        S = a * a

        Arguments:
            a (number type) : side length of a square

        Return value:
            area (number type) : area of the square with side length a

        Example:
            area(5) -> returns 25
    '''
    return a * a


def perimeter(a):
    '''
    Calculates perimeter of a square using given side length a
    The formula used for calculations:
        P = 4 * a

        Arguments:
            a (number type) : side length of a square

        Return value:
            perimeter (number type) : perimeter of the square with side length a

        Example:
            perimeter(5) -> returns 20
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_side_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_side_nonzero(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_side_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_float_value(self):
        res = area(0.1)
        self.assertAlmostEqual(res, 0.01)

    def test_perimeter_side_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_side_nonzero(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_side_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_float_value(self):
        res = perimeter(0.1)
        self.assertAlmostEqual(res, 0.4)
