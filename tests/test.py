from main import main
import unittest


class TestFunctions(unittest.TestCase):

    def test_main(self):
        assert main() == "hello world"

    def test_fail(self):
        assert 1 == 5


if __name__ == '__main__':
    unittest.main()
