import requests
import json

# We ran this to initially get some news articles & dumped them in articles.json

API_KEY = '' # add your API KEY here 
URL = 'https://newsapi.org/v2/everything'


parameters = {
    'q': 'technology',  
    'pageSize': 20, 
    'apiKey': API_KEY
}

response = requests.get(URL, params=parameters)
data = response.json()

# Save articles to a JSON file
with open('articles.json', 'w') as f:
    json.dump(data['articles'], f, ensure_ascii=False, indent=4)

print('Fetched and saved articles successfully!')
