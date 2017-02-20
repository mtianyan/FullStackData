#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import urllib2
import urllib

import json

from bs4 import BeautifulSoup

# # get爬虫模板
# url = "http://www.baidu.com"
# request = urllib2.Request(url=url)
# response = urllib2.urlopen(request, timeout=20)
# result = response.read()
# print result

# # # post爬虫模板(已失效)
# data = urllib.urlencode({'type1': 2, 'type2': 0, 'status': 0, 'wdzjPlatId': int(platId)})
# request = urllib2.Request(url, headers)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
# response = opener.open(request, data) 
# result = response.read()

# # # post爬虫模板修改版
url = "http://shuju.wdzj.com/plat-info-target.html"
data = urllib.urlencode({'target1': 12, 'target2': 11, 'type': 1, 'wdzjPlatId': 59})
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request,data)
result = response.read()
print result