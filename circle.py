import math
import unittest


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


class CircleTestCase(unittest.TestCase):
    def test_area_radius_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_radius_one(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_radius_nonzero(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    def test_area_float_value(self):
        res = area(0.1)
        self.assertAlmostEqual(res, math.pi * 0.01)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_radius_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_radius_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, math.pi * 2)

    def test_perimeter_radius_nonzero(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, math.pi * 4)

    def test_perimeter_float_value(self):
        res = perimeter(0.1)
        self.assertAlmostEqual(res, math.pi * 0.2)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            perimeter(-1)