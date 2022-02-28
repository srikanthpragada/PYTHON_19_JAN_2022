import requests
from bs4 import BeautifulSoup

with open("courses.xml") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")
courses = bs.find_all("course")
for course in courses:
    title = course.find("title").text
    duration = course.find("duration").text
    fee = course.find("fee").text

    print(f"{title:30} {duration:3} {fee:5}")
