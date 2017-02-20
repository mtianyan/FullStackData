#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  

import json
fr = open('../data/xyj.txt','r')

characters = []
# 出现过汉字
stat = {}
# 频率
# 
for line in fr:
	line = line.strip()

	if len(line) == 0:
		continue
	# print type(line)	
	line = unicode(line)
	# print type(line)
	for  x in xrange(0,len(line)):
		if line[x] in [' ','\t','\n','。','？','！','，','、','：','“','”','‘','’','（','）','──','……','—','·','《','》','〈' ,'〉']:
			continue

		if not line[x] in characters:
			characters.append(line[x])
		if not stat.has_key(line[x]):
			stat[line[x]] = 0
		stat[line[x]] += 1


print len(characters)
# print characters
# for key,values in stat.items():
# 	print key,values
# 	
# 	
fw = open('xiyou.json','w')
fw.write(json.dumps(stat))
fw.close()
stat = sorted(stat.iteritems(),key= lambda d:d[1],reverse=True)

# print type(stat),len(stat)
# 
# 
# for x in xrange(0,20):
# 	print characters[x]

print "*" * 20

# for x in xrange(0,20):
# 	# print stat[x][0],stat[x][1]
	
print len(stat)
fw =  open('xiyou.csv','w')
for item in stat:
	fw.write(item[0]+','+str(item[1])+'\n')
fw.close()



fr.close()