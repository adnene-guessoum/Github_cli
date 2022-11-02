"""
Unit test for the description update functions of the command line interface
"""
from desc_update import get_current_user_auth


def test_get_current_user_auth():
    g = get_current_user_auth()
    assert g.get_user() = u'adnene-guessoum'
