# API requests


# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=the+social+network&apikey=APIKEY'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)



# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])







# Checking out the Wikipedia API


# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

