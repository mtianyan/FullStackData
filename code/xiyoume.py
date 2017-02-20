#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import json

fr = open('../data/xyj.txt','r')

characters = []
# 出现过汉字
stat = {}
# 出现过汉字的频率

for line in fr:
	line = line.strip()#去掉空白符号
	if len(line)== 0:
		continue
	# print type(line)
	line = unicode(line)
	# print type(line)
	# 
	for x in xrange(0,len(line)):
		if line[x] in ['','-','‘','’','/','[','*','〕','【','〔','{',':','…','】','','．','—','','　',' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# print line[x]
		# 如果这个字没出现过那么将其加入character中
		if not line[x] in characters:
			characters.append(line[x])
		if not stat.has_key(line[x]):
			stat[line[x]]=0
		stat[line[x]] +=1
		
print len(characters)
print len(stat)
# print characters
# for key,value in stat.items():
	# print key,value
fw = open('../data/xyj_result.json','w')
fw.write(json.dumps(stat))
fw.close()

stat = sorted(stat.iteritems(),key = lambda d:d[1],reverse= True)

for x in xrange(0,20):
	print characters[x]
print '*'*20


fw = open('../data/xyj_sorted.csv','w')
for item in stat:
	fw.write(item[0] + ',' + str(item[1]) + '\n')
fw.close()

fw = open('../data/xyj_sorted.json','w')
fw.write(json.dumps(stat))
fw.close()

print "hello"

fr.close()













































	
fr.close