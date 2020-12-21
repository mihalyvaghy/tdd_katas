import unittest
from src import prime_factors

class PrimeFactorTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([], prime_factors.prime_factors(1))

    def test_2(self):
        self.assertEqual([2], prime_factors.prime_factors(2))

    def test_3(self):
        self.assertEqual([3], prime_factors.prime_factors(3))

    def test_4(self):
        self.assertEqual([2,2], prime_factors.prime_factors(4))

    def test_5(self):
        self.assertEqual([5], prime_factors.prime_factors(5))

    def test_6(self):
        self.assertEqual([2,3], prime_factors.prime_factors(6))

    def test_7(self):
        self.assertEqual([7], prime_factors.prime_factors(7))

    def test_8(self):
        self.assertEqual([2,2,2], prime_factors.prime_factors(8))

    def test_9(self):
        self.assertEqual([3,3], prime_factors.prime_factors(9))

    def test_4620(self):
        self.assertEqual([2,2,3,5,7,11], prime_factors.prime_factors(4620))
