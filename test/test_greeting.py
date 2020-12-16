import unittest
from src import greeting

class GreetingTest(unittest.TestCase):
    def test_properName(self):
        self.assertEqual('Hello, Mitya!', greeting.greet('Mitya'))

    def test_nullName(self):
        self.assertEqual('Hello, my friend!', greeting.greet(None))

    def test_shouting(self):
        self.assertEqual('HELLO, MITYA!', greeting.greet('MITYA'))

    def test_twoNames(self):
        self.assertEqual('Hello, Bia and Mitya!', greeting.greet(['Bia', 'Mitya']))

    def test_twoShouting(self):
        self.assertEqual('HELLO, BIA AND MITYA!', greeting.greet(['BIA', 'MITYA']))

    def test_manyNames(self):
        self.assertEqual('Hello, Bia, Mitya, and Písz!', greeting.greet(['Bia', 'Mitya', 'Písz']))

    def test_manyShouting(self):
        self.assertEqual('HELLO, BIA, MITYA, AND PÍSZ!', greeting.greet(['BIA', 'MITYA', 'PÍSZ']))

if __name__ == '__main__':
    unittest.main()
