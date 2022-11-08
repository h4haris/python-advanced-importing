# Python - Intermediate Importing Data in Python
Python advanced data importing experimentation for Data Science using Web and APIs.

## Importing data from the Internet
- extract various types of insights and findings from the web
- using the basics of scraping and parsing web data

### Importing Flat files from WEB
- import and locally save datasets from Web
- load datasets into pandas df
- make http requests
- scrape web data e.g. html
- parse html into useful data (BeautifulSoup) 
- using urllib and requests packages

**urllib package**
- provides interface for fetching data across web
- urlopen() - accepts URLs

#### Getting flat/non-flat files from WEB

```bash
1. Automate csv file download using urllib
==========================================
from urllib.request import urlretrieve
url = 'nttp://archive.ics.uci.edu/ml/machine-Learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')

2. Importing Excel spreadsheets
===============================
# by default it will import first sheet
# using sheet_name=None to import all sheets
xls = pd.read_excel('https://assets.datacamp.com/course/importing_data_into_r/latitude.xls', sheet_name=None)

3. Print sheet names
====================
print(xls.keys())

4. Accessing a sheet data
=========================
print(xls['1700'].head())
```

#### Using Http requests to import files

```bash
1. Get request using urllib
===========================
from urllib.request import urlopen, Request
url = "https://www.wikipedia.org/"

request = Request(url)
response = urlopen(request) # return HttpResponse Object
html = response.read() # read html as string
response.close()

2. Get request using requests
=============================
import requests
url = "https://www.wikipedia.org/"
r = requests.get(url)
text = r.text
```

### Scraping the web
- by using BeautifulSoup
    - parse and extract structured data from html
    - make **tag soup** (structurally or syntactically incorrect HTML code) beautiful and extract information

```bash
1. Using BeautifulSoup
======================
from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.prettify())

2. Extract Info
===============
print(soup.title) # return title tag e.g. <title>TITLE</title>

print(soup.get_text()) # return text

# loop thru all hyperlinks and print their href
for link in soup.find_all('a'):
    print(link.get('href'))
```

## Interacting with APIs to import data from the web

### Get Data from JSON files

```bash
1. Loading JSON from local file
===============================
import json
with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)

print(type(json_data)) # return dict

2. Printing JSON key/value pair
===============================
for key, value in json_data.items():
    print(key + ':', value)
```

NOTE: The **json.load()** is used to read the JSON document from file. Also there is another method **json.loads()** which is used to convert the JSON String document into the Python dictionary.

```bash
data_file = open('data.txt', "r")

for line in data_file:
    single_line = json.loads(line)
    print(single_line)

# Close connection to file
data_file.close()
```

### Get Data from APIs

```bash
Getting data from API using requests
====================================
import requests
url = 'http://www.omdbapi.com/?t=hackers'

r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key + ':', value)
```

## Importing from the Twitter API
- stream data from Twitter API
- filter upcoming tweets for keywords
- API Authentication and OAuth
- Using **Tweepy** python package

### Using Tweepy: Authentication

```bash
1. Importing and setting token
==============================
import tweepy, json

access_token = "..."
access_token_secret = "..."
consumer_key = "..."
consumer_secret = "..."


2. Streaming tweets
===================
# Create Streaming object
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['apples', 'oranges'])
```