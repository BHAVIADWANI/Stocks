from serpapi import GoogleSearch
import json
params = {
  "engine": "google_news",
  "q": "axis bank stock",
  "api_key": "fcb0576f34b33696c89221e6eb0dadd1754c9f9373a9a1f946848ebbf6de2030"
}

search = GoogleSearch(params)
results = search.get_dict()
news_results = results["news_results"]
# Store news results in a JSON file
with open("C:/Users/BHAVESH/OneDrive/Documents/GitHub/stocks-master/pages/static/json_data/axis.json", "w") as file:
    json.dump(news_results, file)