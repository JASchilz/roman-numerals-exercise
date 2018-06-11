import unittest

from roman_numerals.roman_to_int import RomanToInt


class TestRomanToInteger(unittest.TestCase):
    
    def test_single_x(self):
        self.assertEqual(RomanToInt.convert('X'), 10)

