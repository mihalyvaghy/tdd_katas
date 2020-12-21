import unittest
from src.infix_to_postfix import InfixToPostfix
from src.binary_expression_tree import BinExpTree

class BinExpTreeTest(unittest.TestCase):
    def test_infix_to_postfix_conversion_no_parentheses(self):
        self.assertEqual("12+", InfixToPostfix.convert("1+2"))
        self.assertEqual("12*3+", InfixToPostfix.convert("1*2+3"))

    def test_infix_to_postfix_conversion(self):
        self.assertEqual("abcd^e-fgh*+^*+i-", InfixToPostfix.convert("a+b*(c^d-e)^(f+g*h)-i"))

    def test_binary_expression_tree_print_no_parentheses(self):
        self.assertEqual("1+2", BinExpTree("1+2").to_string())
        self.assertEqual("1*2+3", BinExpTree("1*2+3").to_string())

    def test_binary_expression_tree_print(self):
        self.assertEqual("a+b*(c^d-e)^(f+g*h)-i", BinExpTree("a+b*(c^d-e)^(f+g*h)-i").to_string())

    def test_binary_expression_tree_evaluation(self):
        self.assertEqual(3, BinExpTree("1+2").evaluate())
        self.assertEqual(5, BinExpTree("1*2+3").evaluate())
        self.assertEqual(5, BinExpTree("1*(2+3)").evaluate())
