import sys

import requests
from bs4 import BeautifulSoup

url = "https://www.escaperoomdrachten.nl"
the_word = "drachten"
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.text, "lxml")


def contains_word(t):
    return t and the_word in t


words = soup.find_all(text=contains_word)
count = len(words)
print(f"\nUrl: {url}\nbevat {count} aantal keer het woord: {the_word}\n")

