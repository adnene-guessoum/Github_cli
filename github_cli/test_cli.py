from .cli import *


def test_tests_success():
    assert ex_func("success") == "success"


def test_simple_user_get_num_stars():
    test_codie = get_num_stars("codie3611", False) 
    assert type(test_codie) is int

def test_org_get_repo_number_pages():
    test_soup = get_org_soup("facebook")
    test_facebook = get_repo_number_pages(test_soup) 
    assert type(test_facebook) is int

def test_org_get_num_stars():
    test_facebook = get_num_stars("facebook", True) 
    assert type(test_facebook) is int
