from .cli import ex_func


def test_tests_success():
    assert ex_func("success") == "success"
