import re

class BinExpTree:
    @staticmethod
    def infix_to_postfix(expression):
        objects = re.split("
