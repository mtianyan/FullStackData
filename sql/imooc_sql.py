#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import MySQLdb
import MySQLdb.cursors


# connection（数据库连接对象）占用网络资源，需要不适用关闭，占用数据库和应用程序的资源
# cursor(数据库交互对象)
# exceptions(数据库异常类)
# 

# print MySQLdb
#

conn = MySQLdb.Connect(
			host = '127.0.0.1',
			port = 3306,
			user = 'root',
			passwd ='root',
			db = 'imooc',
			charset = 'utf8'
	)
conn.autocommit(False)
cursor = conn.cursor()
# sql = 'select * from user'
# cursor.execute(sql)

# print cursor.rowcount

# rs = cursor.fetchone()
# print rs

# print conn
# print cursor
# 
# 

# 开发中怎样使用事务
# -关闭自动commit：设置conn.autocommit(False)
# -正常结束事务：conn.commit()
# -异常结束事务：conn.rollback()


sql_insert = "insert into user(userid,username) values(4,'name3')"
sql_update = "update user set username ='mtianyan' where userid =10"
sql_delete = "delete from user where userd<3"


try:
	cursor.execute(sql_insert)
	print cursor.rowcount
	cursor.execute(sql_update)
	print cursor.rowcount
	cursor.execute(sql_delete)
	print cursor.rowcount

	conn.commit()
except Exception, e:
	print e
	conn.rollback()

conn.commit()
conn.close()
cursor.close()