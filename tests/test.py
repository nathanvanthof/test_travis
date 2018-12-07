import unittest
from main import main
import os
import ast


class TestFunctions(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "hello world")

    def test_fail(self):
        self.assertEqual(1, 5)

    def test_secure(self):
        print(os.environ['example'])
        data = ast.literal_eval(os.environ['example'])
        self.assertEqual(data['a'], 1)


if __name__ == '__main__':
    unittest.main()
