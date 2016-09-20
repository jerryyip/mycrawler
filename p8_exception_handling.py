from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError

def get_title(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.script
    except AttributeError as e:
        print(e)
        return None
    return title    

mytitle = get_title("http://www.baidu.com")

if mytitle == None:
    print("Title not found")
else:
    print(mytitle)


