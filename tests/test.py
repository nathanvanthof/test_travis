import unittest
from main import main
import os
import json


class TestFunctions(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "hello world")

    def test_fail(self):
        self.assertEqual(1, 5)

    def test_secure(self):
        data = json.loads(os.environ['example'])
        self.assertEqual(data['a'], 1)


if __name__ == '__main__':
    unittest.main()
