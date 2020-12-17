import unittest
from src import roman

class RomanToDecimalTest(unittest.TestCase):
    def test_single_characters(self):
        self.assertEqual(1, roman.roman_to_decimal("I"))
        self.assertEqual(5, roman.roman_to_decimal("V"))
        self.assertEqual(10, roman.roman_to_decimal("X"))
        self.assertEqual(50, roman.roman_to_decimal("L"))
        self.assertEqual(100, roman.roman_to_decimal("C"))
        self.assertEqual(500, roman.roman_to_decimal("D"))
        self.assertEqual(1000, roman.roman_to_decimal("M"))

    def test_only_addition(self):
        self.assertEqual(2, roman.roman_to_decimal("II"))
        self.assertEqual(2020, roman.roman_to_decimal("MMXX"))

    def test_substraction(self):
        self.assertEqual(4, roman.roman_to_decimal("IV"))
        self.assertEqual(900, roman.roman_to_decimal("CM"))
