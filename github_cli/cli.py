import re
import rich

from bs4 import BeautifulSoup  # type: ignore
import requests


def ex_func(example):
    return example

def get_org_soup(name):
    gh_reqs = requests.get(f"https://github.com/orgs/{name}/repositories").text
    soup = BeautifulSoup(gh_reqs, "html.parser")
    return soup

def get_repo_number_pages(soup):
    num_pages = soup.find(attrs={"name":"data-total-pages"})
    return int(num_pages)

def count_stars(name, num_pages):
    """Docstring for count_stars.

    :arg1: parsed html document
    :returns: num_stars: int (number of starred repos)

    """
    stars_per_repos = []

    for i in range(1, num_pages+1):
        payload_pages = {"page" : "{}".format(i)}

        gh_reqs = requests.get(f"https://github.com/orgs/{name}/repositories",
                payload_pages).text
        soup = BeautifulSoup(gh_reqs, "html.parser")

        stars_string = [num.text for num in soup.find_all(href=re.compile("stargazers"))]
       
        stars_int = [int(x) for x in stars_strings]

        stars_per_repos.append(stars_int)

    flat_stars_per_repos = [item for sub_list in stars_per_repos for item in sub_list] 
    total_num_stars = sum(flat_stars_per_repos) 

    return total_num_stars

def get_num_stars(username: str, orgs: bool):
    """
    Parameters:
        username: str
    ____________________
    Return:
        html soup
    """
    name = username

    if orgs is False:
        gh_reqs = requests.get(f"https://github.com/{name}").text
        soup = BeautifulSoup(gh_reqs, "html.parser")
        num_stars = soup.select_one('a[data-tab-item="stars"] .Counter').get_text()
        #find('data-tab-item="stars"').get_text()
        return int(num_stars)

    else:
        org_soup = get_org_soup(name)
        number_of_pages = get_repo_number_pages(org_soup)
        num_stars = count_stars(name, number_of_pages)
        return num_stars
    
if __name__ == "__main__":
    print("-"*100)
    rich.print(get_num_stars("codie3611", False))
    print("-"*100)
    rich.print(get_num_stars("facebook", True))
    print("-"*100)

