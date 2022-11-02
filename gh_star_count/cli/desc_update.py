"""
Module allowing user description update on his github account
"""
import os
from github import Github

def get_user_infos():
    """
    Prompt the user to give login info 
    """
    token = input("Github account access token (if you don't have one please visit https://github.com/settings/tokens) : ")

    return token
 

def get_current_user_auth(login_info: str):
    """
    get current user object for github profile update
    """
    auth_user_obj = Github(login_info).get_user()
    return auth_user_obj

def update_user_bio(auth_user_obj: object):
    """
    update user bio with star, heart and tea emoji 
    """
    default =  ":star: :gift_heart: :tea:"
    print(f"default bio setting : {default}")
    new_str = input("New bio for your account : ") or ":star: :gift_heart: :tea:"
    auth_user_obj.edit(bio = new_str)


def update_user_status():

if __name__ == "__main__":
    login = get_user_infos() 
    authorized_user = get_current_user_auth(login) 
    update_user_bio(authorized_user)
