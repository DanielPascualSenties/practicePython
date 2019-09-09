from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find_all(class_="story-heading")



print(title)


