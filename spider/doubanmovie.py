#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


import urllib2
import urllib
import json
from bs4 import BeautifulSoup


tags = []


# # get爬虫模板
url = 'https://movie.douban.com/j/search_tags?type=movie'
request = urllib2.Request(url=url)#header伪装浏览器
response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read())
# print result

tags = result['tags']
print len(tags)
for item in tags:
	print item
# 
movies = []
for tag in tags:
	limit = 0
	while 1:
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start='+str(limit)
		print url
		request = urllib2.Request(url=url)#header伪装浏览器
		response = urllib2.urlopen(request, timeout=20)
		result = json.loads(response.read())
		result = result['subjects']
		if len(result) ==0:
			print "no result"
			limit +=20
			break
		for item in result:
			movies.append(item)

		
		####
		break

	break
# 两种for循环的区别，因为for item这种item为临时变量所以无法改变
# 而for xrange 可以通过指定下标改变

for x in xrange(0,len(movies)):
	item = movies[x]
	# print item
	request = urllib2.Request(url=item['url'])#header伪装浏览器
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()
	# 使用beautifulSoup进行解析
	html = BeautifulSoup(result,"lxml")
	title = html.select('h1')[0]
	title = title.select('span')[0]
	# //得到链接之类属性
	# link = get('href')
	title = title.get_text()
	# 找的的info标签第0个符合的
	# html.select('#info')[0]

	# html.find_all("span",attrs ={"property":"v:summary"})[0]

	print title

	movies[x] ['title'] = title
fw = open('../data/movies.txt','w')

for item in movies:
	tmp = ''
	for key,value in item.items():
		tmp += str(value) + ','
	fw.write(tmp[:-1] + '\n')
fw.close()




















# 	movies [x] ['title'] = title



# fw = open('movies.txt','w')

# for items in movies:
# 	tmp = ''
# 	for key,value in item.items():
# 		tmp += str(value) + ','
# 	fw.write(tmp[:-1] + '\n')
# fw.close()
	# keys = html.select("#info span.pl")
	# values = html.select('#info span.attrs')

	# for i in xrange(0,len(keys)):
	# 	print keys[i].get_text()
	# 	print values[i].get_text()
