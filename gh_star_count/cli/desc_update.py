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
    print("-"*80)
    print(f"default bio update : {default}")
    new_str = input("New bio for your account : ") or default
    auth_user_obj.edit(bio = new_str)

def main_update():
    """
    main function for the update bio module
    """
    login = get_user_infos() 
    authorized_user = get_current_user_auth(login) 
    update_user_bio(authorized_user)

if __name__ == "__main__":
    main_update()
