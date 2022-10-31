from .cli import *


def test_tests_success():
    assert ex_func("success") == "success"


def test_simple_user_get_num_stars():
    test_codie = get_num_stars("codie3611", False) 
    assert type(test_codie) is int
