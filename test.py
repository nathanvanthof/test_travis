from main import main


def test_main():
    assert main() == "hello world"


def test_fail():
    assert 1 == 5
