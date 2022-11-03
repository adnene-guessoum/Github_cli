"""
Module retrieving user requested info about a github account
"""
import requests
import rich
from github import Github


def get_user_name_token():
    """
    Prompt the user to give login info

    Check API response for valid token
    """
    username = input("Your Github username : ")
    token = input(
        (
            "Github account access token "
            "(if you don't have one please visit:"
            " https://github.com/settings/tokens) : "
        )
    )

    response = requests.get('https://api.github.com', auth= ( username , token ))

    if response.status_code == requests.codes.ok :
        return username, token
    else:
        raise Exception("Invalid token or username")

def create_github_instance(token:str):
    """
    Instanciate github object for querying github
    """
    gh_object = Github(token)
    return gh_object

def get_target_starcount(gh_object):
    """
    Prompt user for github account of interest
    """
    target_account = input(("Whose stars do you want to count ? "
        "(target github username, including your own) : "))
    total_stars = []
    for repo in gh_object.get_user(target_account).get_repos():
        number_stars_per_repo = repo.stargazers_count
        total_stars.append(number_stars_per_repo) 
        
    total = sum(total_stars)
    return total, target_account

def main_starcount():
    """
    main function for total star count of a target user
    """
    username, token = get_user_name_token()
    gh_instance = create_github_instance(token)
    total_starcount, target_account = get_target_starcount(gh_instance)

    print("-" * 80)

    rich.print((f"{total_starcount} stars in total "
        f"(all repository from {target_account}). "))

    print("-" * 80)
    rich.print("Impressive, isn't it ? Hope to see you soon :)")


if __name__ == "__main__":
    main_starcount()
