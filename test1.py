import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

quotes = []  # a list to store quotes

table = soup.find(
    'a', attrs={'class': 'cb-lv-scrs-well cb-lv-scrs-well-complete'})

print(table)
result = table.find('div', attrs={'class': 'cb-text-complete'})
print(type(result))
