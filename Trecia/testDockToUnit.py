import unittest
import doctest
import anagram


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(anagram))
    return tests


if __name__ == '__main__':
    unittest.main()


# Run with python testDockToUnit.py -v