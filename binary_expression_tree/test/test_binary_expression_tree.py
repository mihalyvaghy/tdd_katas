import unittest
from src.binary_expression_tree import BinExpTree

class BinExpTreeTest(unittest.TestCase):
    def test_infix_to_postfix_conversion_no_parentheses(self):
        self.assertEqual("12+", BinExpTree.infix_to_postfix("1+2"))
        self.assertEqual("12*3+", BinExpTree.infix_to_postfix("1*2+3"))
