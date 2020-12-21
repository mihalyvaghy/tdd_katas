from .infix_to_postfix import InfixToPostfix
from abc import ABC, abstractmethod

class BinExpTree:
    class Node(ABC):
        def __init__(self, **kwargs):
            self.word = kwargs.get("word")
            self.left = kwargs.get("left")
            self.right = kwargs.get("right")

        @abstractmethod
        def to_string(self, parent_precedence):
            pass

        @abstractmethod
        def evaluate(self):
            pass

    class Operator(Node):
        def __init__(self, operator, left, right):
            super().__init__(word=operator, left=left, right=right)

        def to_string(self, parent_precedence):
            result = ""
            if parent_precedence > InfixToPostfix.precedence(self.word):
                result += "("
            result += self.left.to_string(InfixToPostfix.precedence(self.word))
            result += self.word
            result += self.right.to_string(InfixToPostfix.precedence(self.word))
            if parent_precedence > InfixToPostfix.precedence(self.word):
                result += ")"
            return result

        def evaluate(self):
            operand_1 = self.left.evaluate()
            operand_2 = self.right.evaluate()
            if self.word == "+":
                return operand_1 + operand_2
            elif self.word == "-":
                return operand_1 - operand_2
            elif self.word == "*":
                return operand_1 * operand_2
            elif self.word == "/":
                return operand_1 / operand_2
            elif self.word == "^":
                return operand_1 ** operand_2

    class Operand(Node):
        def __init__(self, operand):
            super().__init__(word=operand)

        def to_string(self, parent_precedence):
            return self.word

        def evaluate(self):
            return float(self.word)

    def __init__(self, expression):
        postfix = InfixToPostfix.convert_stack(expression)
        stack = []
        for word in postfix:
            if InfixToPostfix.is_operand(word):
                stack.append(BinExpTree.Operand(word))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(BinExpTree.Operator(word, left, right))
        self.root = stack.pop()

    def to_string(self):
        return self.root.to_string(0)
    
    def evaluate(self):
        return self.root.evaluate()
