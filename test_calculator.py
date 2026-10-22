import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(8, 3, "-"), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(4, 3, "*"), 12)

    def test_division(self):
        self.assertEqual(calculate(9, 3, "/"), 3)

    def test_square_root(self):
        self.assertEqual(calculate(9, None, "sqrt"), 3)
        self.assertEqual(calculate(16, None, "√"), 4)

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    def test_unknown_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "%")


if __name__ == "__main__":
    unittest.main()
