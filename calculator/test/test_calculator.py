import unittest
from src import calculator

class CalculatorTest(unittest.TestCase):
    def test_empty_add(self):
        self.assertEqual(0, calculator.add(""))

    def test_unary_add(self):
        self.assertEqual(1, calculator.add("1"))

    def test_binary_add(self):
        self.assertEqual(2, calculator.add("1,1"))

    def test_sum(self):
        self.assertEqual(3, calculator.add("1,1,1"))

    def test_multiple_delimiters(self):
        self.assertEqual(3, calculator.add("1,1\n1"))

    def test_changed_default_delimiter_unary(self):
        self.assertEqual(1, calculator.add("//;\n1"))

    def test_changed_default_delimiter(self):
        self.assertEqual(2, calculator.add("//;\n1;1"))

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as e:
            calculator.add("1,-1")

        self.assertEqual(("Negative numbers not allowed", -1), e.exception.args)
