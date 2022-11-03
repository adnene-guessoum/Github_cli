"""
    unit test module for the functions in the cli module used to prompt a
    search for the number of stars in a specific repo by the user of this
    package.
"""
from .count_stars_scrapping import ex_func, get_num_stars, get_org_soup
from .count_stars_scrapping import get_repo_number_pages


def test_tests_success():
    """
    simple test to test the tests
    """
    assert ex_func("success") == "success"


def test_simple_user_get_num_stars():
    """
    type check of return value
    """
    test_codie = get_num_stars("codie3611", False)
    assert isinstance(test_codie, int)


def test_org_get_repo_number_pages():
    """
    type check of return value
    """
    test_soup = get_org_soup("facebook")
    test_facebook = get_repo_number_pages(test_soup)
    assert isinstance(test_facebook, int)


def test_big_org_get_num_stars():
    """
    type check of return value for organization with mutiple pages
    """
    test_facebook = get_num_stars("facebook", True)
    assert isinstance(test_facebook, int)


def test_small_org_get_num_stars():
    """
    type check of return value for organization with only one page
    """
    test_psf = get_num_stars("psf", True)
    assert isinstance(test_psf, int)
