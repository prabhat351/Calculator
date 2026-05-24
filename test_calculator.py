import unittest
from calculator import add, subtract, multiply, divide, sqrt, modulus

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 999), 0)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(25, 5), 0)
        self.assertEqual(modulus(17, 4), 1)
        self.assertEqual(modulus(-10, 3), -1)
        self.assertEqual(modulus(10, -3), 1)
        self.assertEqual(modulus(-10, -3), -1)
        self.assertEqual(modulus(0, 5), 0)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_sqrt_positive(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 2 ** 0.5)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

if __name__ == "__main__":
    unittest.main()
