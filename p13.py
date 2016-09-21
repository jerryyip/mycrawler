#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html.read())

try:
    with open("story.txt","w") as story:
#	story.write(str(bsobj))
#find(tag, attributes, recursive, text, keywords) 
#findAll(tag, attributes, recursive, text, limit, keywords) 
#tag### 
	nameList = bsobj.findAll("the prince")
	print(len(nameList))
#        for name in nameList:
#            print(name.get_text())
#.get_text() will clear all the tags in HTML and return a string with word only. 
#            story.write(str(name.get_text()))
except Exception as e:
    print (e)
