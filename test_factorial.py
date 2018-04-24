import unittest
from factor import factorial

class FactTestCase(unittest.TestCase):

    def test_function_validates_input(self):
        f = factorial(5)
        self.assertEqual(f, 126)

if __name__ == '__name__':
    unittest.main()
