import unittest


class TestFunctions(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(0, 0)

    def test_fail(self):
        self.assertEqual(1, 5)


if __name__ == '__main__':
    unittest.main()
