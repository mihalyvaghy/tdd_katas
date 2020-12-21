import re

class BinExpTree:
    @staticmethod
    def __is_operator(char):
        return char in "+-*/^"

    @staticmethod
    def __is_operand(char):
        return not BinExpTree.__is_operator(char) and char not in "()"

    @staticmethod
    def __precedence(operator):
        return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": -1}[operator]

    @staticmethod
    def __empty_stack(stack):
        return len(stack) == 0

    @staticmethod
    def __higher_precedence(operator_1, operator_2):
        return BinExpTree.__precedence(operator_1) >= BinExpTree.__precedence(operator_2)

    @staticmethod
    def __pop_higher_precedence(stack, postfix, operator):
        while not BinExpTree.__empty_stack(stack) and BinExpTree.__higher_precedence(stack[-1], operator):
            postfix.append(stack.pop())
        return stack, postfix

    @staticmethod
    def __pop_parenthesis(stack, postfix):
        while stack[-1] != "(":
            postfix.append(stack.pop())
        stack.pop()
        return stack, postfix

    @staticmethod
    def infix_to_postfix_stack(expression):
        postfix = []
        stack = []
        tmp_operand = ""
        infix = re.split("(\+|-|\*|/|\^|\(|\))", expression)
        for word in infix:
            if word == "":
                continue
            elif BinExpTree.__is_operand(word):
                postfix.append(word)
            elif BinExpTree.__is_operator(word):
                if BinExpTree.__empty_stack(stack) or stack[-1] == "(" or BinExpTree.__higher_precedence(word, stack[-1]):
                    stack.append(word)
                else:
                    stack, postfix = BinExpTree.__pop_higher_precedence(stack, postfix, word)
                    stack.append(word)
            elif word == "(":
                stack.append(word)
            elif word == ")":
                stack, postfix = BinExpTree.__pop_parenthesis(stack, postfix)
        while len(stack) != 0:
            postfix.append(stack.pop())
        return postfix

    @staticmethod
    def infix_to_postfix(expression):
        return "".join(BinExpTree.infix_to_postfix_stack(expression))

    def __init__(self, expression):
        pass

    def print(self):
        pass
