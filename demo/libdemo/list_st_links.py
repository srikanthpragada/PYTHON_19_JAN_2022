import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com"
response = requests.get(URL)
contents = response.text  # html

bs = BeautifulSoup(contents, "html.parser")
links = bs.find_all("a")
for link in links:
    href = link['href']  # take value of href attribute
    if href == "#":
        continue   # ignore

    if not href.startswith("http"):  # relative URL
         href = URL + "/" + href

    print(href)



