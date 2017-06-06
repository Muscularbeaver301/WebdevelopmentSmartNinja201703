"""
Example unittest:
more in detail on: https://docs.python.org/2/library/unittest.html
"""
import unittest
from calc import add

class TestCases(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)
