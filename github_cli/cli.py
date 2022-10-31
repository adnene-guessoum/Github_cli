"""
Module that prompts user to indicate name and organization status for the
owner of the github account used to count total amount of stars.

returns the total number of stars in the account in a rich display.
"""
import re
import rich

from bs4 import BeautifulSoup  # type: ignore
import requests


def ex_func(example):
    """
    Useless function to test the tests
    """
    return example


def get_org_soup(name):
    """
    Function used to define the correct path in the case of an organization
    account

    args:
        name: str ; name of the organization
    --------------
    return:
        soup: bs4.BeautifulSoup object; parsed HTML document
    """
    path = f"https://github.com/orgs/{name}/repositories"
    gh_reqs = requests.get(path, timeout=10).text
    soup = BeautifulSoup(gh_reqs, "html.parser")
    return soup


def get_repo_number_pages(soup):
    """
    Extract total number of pages in repositories section of profile page
    of the queried github organization

    args:
        soup: BeautifulSoup object
    -----------------
    return:
        num_pages: int ; number of pages to inspect
    """
    num_pages_tot = soup.select_one("em[data-total-pages]")["data-total-pages"]
    num_pages = int(num_pages_tot)
    return num_pages


def count_stars(name, num_pages):
    """
    Count the stars per repos for every pages and return the sum
    """
    stars_per_repos = []

    for i in range(1, num_pages + 1):
        payload_pages = {"page": f"{i}"}

        path = f"https://github.com/orgs/{name}/repositories"
        gh_reqs = requests.get(path, payload_pages, timeout=10).text

        soup = BeautifulSoup(gh_reqs, "html.parser")

        stars_string = [
            num.text.strip()
            for num in soup.find_all(href=re.compile("stargazers"))
        ]

        stars_int = [int(x.replace(",", "")) for x in stars_string]

        stars_per_repos.append(stars_int)

    flat_stars_per_repos = [
        item for sub_list in stars_per_repos for item in sub_list
    ]

    total_num_stars = sum(flat_stars_per_repos)

    return total_num_stars


def get_num_stars(username: str, orgs: bool):
    """
    Get the number of stars for a github account

    args:
        username: str ; name of the owner of the account
        orgs: bool ; if the owner is an organization
    ____________________
    Return:
        num_stars: int ; total number of stars to display
    """
    name = username

    if orgs is False:
        gh_reqs = requests.get(f"https://github.com/{name}", timeout=10).text

        soup = BeautifulSoup(gh_reqs, "html.parser")

        num_stars_data = soup.select_one('a[data-tab-item="stars"] .Counter')
        num_stars = num_stars_data.get_text()

        return int(num_stars)

    org_soup = get_org_soup(name)
    number_of_pages = get_repo_number_pages(org_soup)
    num_stars = count_stars(name, number_of_pages)
    return num_stars


def main():
    """
    prompt the user to give the name of the owner of the github account of
    interest and its status (organization or individual user)

    display the total number of stars in a rich print in the console

    returns: print statements

    """
    name = input("Whose stars do you want to count ? ").lower()
    text = input("Is the Github account owned by an organization ? (yes/no) ")

    if (text.lower() == "yes") or (text.lower() == "y"):
        orga = True
        print("You asked for the number of stars of {name} (organization)")

    elif (text.lower() == "no") or (text.lower() == "n"):
        orga = False
        print(f"You asked for the number of stars of {name} (github user)")

    else:
        print("Type yes or no")

    print("-" * 80)
    rich.print(get_num_stars(name, orga), " stars in total (all repository). ")
    print("-" * 80)
    rich.print("Impressive, isn't it ? Hope to see you soon :)")


if __name__ == "__main__":
    main()
