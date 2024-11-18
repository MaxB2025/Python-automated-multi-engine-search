import requests
from bs4 import BeautifulSoup

#making a custom function to use it in a main.py file
def yahoo_search(yahoo_search_query):

    all_links = [] # list used to contain found results. yahoo_search function will return this list (used at lines 18, 22-24, 28)
    delete_count = 0 # int value used to count all deleted useless items to precisely call for any needed items in a list by their altered indices (used at lines 23-25)

    url = "https://api.search.yahoo.com/search?p=%s"
    # getting results of a request and searching for links in them
    r = requests.get(url % yahoo_search_query)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all('a')

    # Appending all found links in "all_links" list
    for link in links:
        all_links.append(link.get('href'))

    # there are a lot of useless links to several "yahoo" services or just a single "#" symbol in a list for unexpected reason
    # this loop gets rid of these items
    for item in range(len(all_links)):
        if all_links[item - delete_count].find("yahoo") != -1 or all_links[item - delete_count] == "#":
            all_links.pop(item - delete_count)
            delete_count = delete_count + 1

    return all_links