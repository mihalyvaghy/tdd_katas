import unittest
from src.binary_expression_tree import BinExpTree

class BinExpTreeTest(unittest.TestCase):
    def test_infix_to_postfix_conversion_no_parentheses(self):
        self.assertEqual("12+", BinExpTree.infix_to_postfix("1+2"))
        self.assertEqual("12*3+", BinExpTree.infix_to_postfix("1*2+3"))

    def test_infix_to_postfix_conversion(self):
        self.assertEqual("abcd^e-fgh*+^*+i-", BinExpTree.infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))

    def test_binary_expression_tree_print_no_parentheses(self):
        self.assertEqual("1+2", BinExpTree("1+2").print())
        self.assertEqual("1*2+3", BinExpTree("1*2+3").print())
