# Python automated multi engine search
Currently supports 2 search engines - Google and Yahoo. More coming soon. <br>
Setup procedure:

### Step 1:
Check whether you have installed python 3.12 or above if not sure. Use a command `python` in your terminal to see its current version on your device.

### Step 2:
Install all necessary external python libraries which include:
requests - `pip install requests`
beautiful soup - `pip install beautifulsoup4`

### Step 3: 
Download this project

### Step 4:
Create a new project on a Google developer console site. Enable custom search API for that project, copy your API key into an "api_key" file. 

### Step 5:
Add a programmable search engine (Google programmable search engine site link below) and copy its ID into a "search_engine_id" file. 

### Spep 6: 
Use this project by calling it in your terminal with a command `python *path to project folder*\main.py`
Remeber that Google has daily limits on amount of requests you can send. To make more requests upgrade your rate on a Google developer console site.
Yahoo search function uses web scrapping instead of API, so it does not have that problem. 

## References:
