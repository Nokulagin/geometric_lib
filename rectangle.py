import unittest


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


class RectangleTestCase(unittest.TestCase):
    def test_area_sides_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_diff_sides(self):
        res = area(2, 3)
        self.assertEqual(res, 6)

    def test_area_float_values(self):
        res = area(0.1, 0.2)
        self.assertAlmostEqual(res, 0.02)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-1, -1)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_one_side_zero(self):
        res = perimeter(0, 2)
        self.assertEqual(res, 2)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_diff_sides(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_perimeter_float_values(self):
        res = perimeter(0.4, 0.3)
        self.assertAlmostEqual(res, 1.4)

    def test_perimeter_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-1, -1)
