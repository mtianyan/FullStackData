#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import urllib2
import urllib

import json
import cookielib
from bs4 import BeautifulSoup

urlbase = "http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013"

# # get爬虫模板
url = "http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013"
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
html_result = unicode(response.read())
# print html_result

url_2 ="http://kaoshi.edu.sina.com.cn/index.php?p=opencourse&s=api&a=get_courses&discipline_id=14&count_per_page=3&page=1"
## getjson模板 f12打开控制台后刷新查看
url_json ="http://kaoshi.edu.sina.com.cn/?p=college&s=api2015&a=getAllCollege"
request = urllib2.Request(url=url_json)
response = urllib2.urlopen(request, timeout=20)
json_result = unicode(response.read())
# print json_result
for key in json.loads(json_result).keys():
	print key
jsonres = json.loads(json_result)
print jsonres
fw = open('../data/xinlang_college.json','w')
fw.write(json.dumps(jsonres))
fw.close()




# #post爬虫模板
url = "http://shuju.wdzj.com/plat-info-target.html"
data = urllib.urlencode({'target1': 12, 'target2': 11, 'type': 1, 'wdzjPlatId': 59})
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request,data)
result = response.read()

# print result
for key in json.loads(result).keys():
	print key
jsonres = json.loads(result)
print jsonres
fw = open('../data/shuju_response.json','w')
fw.write(json.dumps(jsonres))
fw.close()