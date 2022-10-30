from bs4 import BeautifulSoup
import requests
import rich


def get_num_stars(username: str, orgs: bool):
    """
    Parameters:
        username: str
    ____________________
    Return:
        html soup
    """
    name = username

    if orgs == False:
        gh_reqs = requests.get(f"https://github.com/{name}").text
        soup = BeautifulSoup(gh_reqs, "html.parser")
        num_stars = soup.select('a[data-tab-item="stars"] .Counter').get_text()
        return num_stars
    else:
        pass


def count_stars(soup):
    """Docstring for count_stars.

    :arg1: parsed html document
    :returns: num_stars: int (number of starred repos)

    """

    pass


if __name__ == "__main__":
    pass
