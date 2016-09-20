#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com")

bsOBJ = BeautifulSoup(html.read(), "lxml")
#属性查找标签
#print (bsOBJ.html.h1)
print(bsOBJ)
