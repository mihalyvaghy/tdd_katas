import re

class InfixToPostfix:
    @staticmethod
    def is_operator(char):
        return char in "+-*/^"

    @staticmethod
    def is_operand(char):
        return not InfixToPostfix.is_operator(char) and char not in "()"

    @staticmethod
    def precedence(operator):
        return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": -1}[operator]

    @staticmethod
    def empty_stack(stack):
        return len(stack) == 0

    @staticmethod
    def higher_precedence(operator_1, operator_2):
        return InfixToPostfix.precedence(operator_1) >= InfixToPostfix.precedence(operator_2)

    @staticmethod
    def pop_higher_precedence(stack, postfix, operator):
        while not InfixToPostfix.empty_stack(stack) and InfixToPostfix.higher_precedence(stack[-1], operator):
            postfix.append(stack.pop())
        return stack, postfix

    @staticmethod
    def pop_parenthesis(stack, postfix):
        while stack[-1] != "(":
            postfix.append(stack.pop())
        stack.pop()
        return stack, postfix

    @staticmethod
    def convert_stack(expression):
        postfix = []
        stack = []
        tmp_operand = ""
        infix = re.split("(\+|-|\*|/|\^|\(|\))", expression)
        for word in infix:
            if word == "":
                continue
            elif InfixToPostfix.is_operand(word):
                postfix.append(word)
            elif InfixToPostfix.is_operator(word):
                if InfixToPostfix.empty_stack(stack) or stack[-1] == "(" or InfixToPostfix.higher_precedence(word, stack[-1]):
                    stack.append(word)
                else:
                    stack, postfix = InfixToPostfix.pop_higher_precedence(stack, postfix, word)
                    stack.append(word)
            elif word == "(":
                stack.append(word)
            elif word == ")":
                stack, postfix = InfixToPostfix.pop_parenthesis(stack, postfix)
        while len(stack) != 0:
            postfix.append(stack.pop())
        return postfix

    @staticmethod
    def convert(expression):
        return "".join(InfixToPostfix.convert_stack(expression))
