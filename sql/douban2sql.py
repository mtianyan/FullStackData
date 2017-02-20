#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import MySQLdb
import MySQLdb.cursors


# 建立连接
db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=3306, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

fr = open('../data/douban_movie_clean.txt','r')

# #create
# count = 0
# for line in fr:
# 	count +=1
# 	print count
# 	if count == 1:
# 		continue

# 	line = line.strip().split('^')

# 	cursor.execute("insert into movie(title,url,rate,length,description) values(%s, %s, %s, %s, %s)",[line[1],line[2],line[4],line[-3],line[-1]])

# fr.close()

# update
# 

cursor.execute("update movie set title =%s,length=%s where id =2",['mtianyan','999'])

# #read
# #

# cursor.execute("select title,length from movie where id =2")
# movies = cursor.fetchall()

# # movies = cursor.fetchone()

# print len(movies)
# print movies


# # CURD
#delete
#

cursor.execute("delete from movie where id =3")

# cursor.execute(sql)

# 关闭连接

cursor.close()
db.close()