from googleSearch import google_search
from yahooSearch import yahoo_search
import os # needed to create directories and log files in them
import datetime # needed to assign current time to every created log file

search_query = str(input("Your search query: "))

# calling functions imported from other files to request a search in different search engines
googleResults = google_search(search_query)
yahooResults = yahoo_search(search_query)

googleResultsList = [] # needed to write google search results into a log file (used at lines 18, 40)

# printing request results and appending links into a googleResultsList
print("\nGoogle search results:")
for item in googleResults:
    print(item['link'])
    googleResultsList.append(item['link'])

print("\nYahoo search results:")
for index in range(0, 10):
    print(yahooResults[index])

#checking whether a log folders was created and create them if negative
if not os.path.exists("./logs"):
    os.mkdir("./logs")
if not os.path.exists("./logs/googleSearch"):
    os.mkdir("./logs/googleSearch")
if not os.path.exists("./logs/yahooSearch"):
    os.mkdir("./logs/yahooSearch")

# assigning a variable which will be a log file name containing current time. Replacing colons with hyphens
logFileName = search_query + " " + str(datetime.datetime.now()).replace(':', '-') + '.txt'

# logging search results in a files
with open(os.path.join('./logs/yahooSearch/', logFileName), 'w') as file:
    file.write(str(yahooResults))

with open(os.path.join('./logs/googleSearch/', logFileName), 'w') as file:
    file.write(str(googleResultsList))