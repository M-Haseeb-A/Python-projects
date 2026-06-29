# before running the program please enter your api key in url variable.

import requests
import json
query = input("enter the category of news you want to see :")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-28&sortBy=publishedAt&apiKey= "Enter your newsapi key to use program"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print(article["url"])
  print("--------------------------------------")