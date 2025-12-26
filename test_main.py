import unittest
from main import additionMethod, subtractionMethod, multiplicationMethod, divisionMethod

class TestMain(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(additionMethod(1, 2), 3)
        self.assertEqual(additionMethod(-1, 1), 0)
        self.assertEqual(additionMethod(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(subtractionMethod(2, 1), 1)
        self.assertEqual(subtractionMethod(-1, 1), -2)
        self.assertEqual(subtractionMethod(-1, -1), 0)

    def test_multiplication(self):
        self.assertEqual(multiplicationMethod(2, 3), 6)
        self.assertEqual(multiplicationMethod(-1, 3), -3)
        self.assertEqual(multiplicationMethod(-1, -3), 3)

    def test_division(self):
        self.assertEqual(divisionMethod(6, 3), 2)
        self.assertEqual(divisionMethod(-6, 3), -2)
        self.assertEqual(divisionMethod(-6, -3), 2)
        with self.assertRaises(ZeroDivisionError):
            divisionMethod(1, 0)

if __name__ == '__main__':
    unittest.main()
