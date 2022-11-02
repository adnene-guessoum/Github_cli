"""
Module allowing user description update on his github account
"""
import os
from github import Github

def get_current_user_auth():
    "
    get current user object for github profile update
    "
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token)
    return g

if __name__ == "__main__":

