import unittest
from stringReverse import stringReverse as strReverse, error

class TestStringReverse(unittest.TestCase):
    def test_string(self):
        self.assertEqual(strReverse("abcde"), "edcba")
        self.assertEqual(strReverse("12321"), "12321")
        self.assertEqual(strReverse("12abc3"), "3cba21")

    def test_errors(self):
        self.assertRaises(error, strReverse, 123)


if __name__ == '__main__':
    unittest.main()