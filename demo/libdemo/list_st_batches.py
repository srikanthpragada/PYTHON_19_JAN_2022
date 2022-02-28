import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com"
response = requests.get(URL)
contents = response.text  # html

bs = BeautifulSoup(contents, "html.parser")
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
if table is None:
    print("Sorry! Table not found!!")
    exit()

# take rows except first one (col header)
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    name = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text

    print(f"{name:40} {timings:20} {stdate:10}")
