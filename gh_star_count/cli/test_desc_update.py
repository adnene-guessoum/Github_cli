"""
Unit test for the description update functions of the command line interface
"""
from .desc_update import get_current_user_auth


def test_get_current_user_auth():
    """
    Unittest fetching user auth token in env
    """
    g_object = get_current_user_auth()
    assert g_object.get_user() == None
