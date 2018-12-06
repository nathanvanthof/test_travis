import unittest
from main import main


class TestFunctions(unittest.TestCase):

    def test_main(self):
        self.assertEqual(main(), "hello world")

    def test_fail(self):
        self.assertEqual(1, 5)


if __name__ == '__main__':
    unittest.main()
