import requests

# making a custom function to use it in a main.py file
def google_search(google_search_query):

    # opening files to read applicable google api key and search engine id. Do not forget to paste yours in these!
    api_key = open('api_key').read()
    search_engine_id = open('search_engine_id').read()

    url = 'https://www.googleapis.com/customsearch/v1'

    # assigning parameters as a payload for a Google request
    params = {
        'q': google_search_query,
        'key': api_key,
        'cx': search_engine_id,
    }

    # sending a request and formatting a response in a json format
    response = requests.get(url, params=params)
    results = response.json()['items']

    return results