from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

mydict = {"class":"green", "class1":"red"}

#nameList = bsObj.findAll("", id ="text", )

for 

nameList = bsObj.findAll("", class_="red", )

for name in nameList:
    print(name)

