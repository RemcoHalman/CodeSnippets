import sys
import pandas as pd

import requests
from bs4 import BeautifulSoup

folder_path = "/Users/Remco/csv/escaperoomwebsites"

url_base = "https://"
url_site = "mysteryhouse"
url_ext = ".nl"

url = url_base + url_site + url_ext
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, "lxml")

heading_tag_1 = soup.findAll("h1")
heading_tag_2 = soup.findAll("h2")
heading_tag_3 = soup.findAll("h3")
heading_tag_4 = soup.findAll("h4")
heading_tag_5 = soup.findAll("h5")
heading_tag_6 = soup.findAll("h6")

tag_a = soup.findAll("a")

header_list = {
    "h1 :": [heading.text for heading in heading_tag_1],
    "h2 :": [heading.text for heading in heading_tag_2],
    "h3 :": [heading.text for heading in heading_tag_3],
    "h4 :": [heading.text for heading in heading_tag_4],
    "h5 :": [heading.text for heading in heading_tag_5],
    "h6 :": [heading.text for heading in heading_tag_6],
    "a :": [a.text for a in tag_a],
}

heading_tag_1.append(header_list)
df_ = pd.DataFrame.from_dict(header_list, orient="index")

print(df_)
df_.to_csv(f"{folder_path}/{url_site}.csv")
