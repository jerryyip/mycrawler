# coding:utf-8
import urllib2
from functools import wraps
import time


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print "[%s] time running: %fs" % (func.__name__, t1 - t0)
        return result
    return wrapper

# import sys
# req = urllib2.Request('http://www.w3school.com.cn')


req = urllib2.Request('http://www.qq.com')
# 应答对象response；方法info geturl read()
response = urllib2.urlopen(req)


@log
def crawler():
    try:
        with open('qq.txt', 'w') as qq:
            # typeEncode = sys.getfilesystemencoding()
            # decode中加入ignore忽略非法字符，默认参数是strict，代表遇到非法字符时抛出异常；replace将会用？代替非法字符；
            # 每个网站的编码都不一样，需要查看
            html = response.read().decode('gb2312', 'replace').encode('utf-8')
            qq.write(html)
    except Exception as err:
        print err


if __name__ == '__main__':
    crawler()
