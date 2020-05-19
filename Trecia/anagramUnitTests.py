import unittest
import anagram

class TestAnagram(unittest.TestCase):
    def test_string(self):
        self.assertTrue(anagram.anagram("vienas", "asnvei"))
        self.assertTrue(anagram.anagram("kaip", "ipak"))

    def test_numbers(self):
        self.assertTrue(anagram.anagram("123456", "546321"))
        self.assertTrue(anagram.anagram("215 21", "152 12"))
        self.assertFalse(anagram.anagram("215 21", "15212"))

    def test_caps(self):
        self.assertFalse(anagram.anagram("hellO", "lelho"))
        self.assertTrue(anagram.anagram("hellO", "lelhO"))


if __name__ == '__main__':
    unittest.main()