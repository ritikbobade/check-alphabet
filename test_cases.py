import unittest
from Restful-api import contains_all_letters

class TestContainsAllLetters(unittest.TestCase):
    
    def test_basic_positive(self):
        self.assertTrue(contains_all_letters("The quick brown fox jumps over the lazy dog"))
    
    def test_basic_negative(self):
        self.assertFalse(contains_all_letters("Hello World"))
    
    def test_empty_string(self):
        self.assertFalse(contains_all_letters(""))
    
    def test_case_insensitivity(self):
        self.assertTrue(contains_all_letters("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))
    
    def test_special_characters(self):
        self.assertTrue(contains_all_letters("The quick brown fox jumps over the lazy dog!@#$%^&*()"))
    
    def test_non_alphabetic_characters(self):
        self.assertTrue(contains_all_letters("1234567890 abcdefghijklmnopqrstuvwxyz"))
    
    def test_repeated_letters(self):
        self.assertFalse(contains_all_letters("aaaaaaa"))

if __name__ == '__main__':
    unittest.main()
