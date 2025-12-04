import unittest


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


class TriangleTestCase(unittest.TestCase):
    def test_area_base_zero(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_area_height_zero(self):
        res = area(2, 0)
        self.assertEqual(res, 0)

    def test_area_height_and_base_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_nonzero_values(self):
        res = area(2, 4)
        self.assertEqual(res, 4)

    def test_area_one_values(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_float_values(self):
        res = area(0.2, 0.2)
        self.assertAlmostEqual(res, 0.02)

    def test_perimeter_sides_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_sides_nonzero(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_perimeter_float_values(self):
        res = perimeter(0.1, 0.2, 0.3)
        self.assertAlmostEqual(res, 0.6)
