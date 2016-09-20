#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html.read())

try:
    with open("story.txt","w") as story:
        story.write(str(bsobj))
        nameList = bsobj.findAll("span", {"class":"green"})
        for name in nameList:
            story.write(str(name.get_text()))
except Exception as e:
    print (e)
