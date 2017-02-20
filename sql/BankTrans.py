#coding:utf8
import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    
    def check_acct_available(self, acctid):
        try:           
            cursor =self.conn.cursor()
            sql = "select * from account where acctid =%s"%acctid
            cursor.execute(sql)
            print sql +"账号有效验证"
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s不存在"% acctid)
        finally:
            cursor.close()
        
        
    
    
    def reduce_money(self, acctid, money):
        try:           
            cursor =self.conn.cursor()
            sql = "update account set money=money-%s where acctid =%s"%(money,acctid)
            cursor.execute(sql)
            print sql
            rs = cursor.fetchall()
            if cursor.rowcount !=1:
            	pass
                raise Exception("账号%s减款失败"% acctid)
        finally:
            cursor.close()
    
    
    def has_enough_money(self, acctid, money):
        try:           
            cursor =self.conn.cursor()
            sql = "select * from account where acctid =%s and money>%s" % (acctid,money)
            cursor.execute(sql)
            print sql +"验证钱够不够"
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s钱不够"% acctid)
        finally:
            cursor.close()
    
    
    def add_money(self, acctid, money):
        try:           
            cursor =self.conn.cursor()
            sql = "update account set money = money+%s where acctid =%s"%(money,acctid)
            cursor.execute(sql)
            print sql
            rs = cursor.fetchall()
            if cursor.rowcount !=1:
            	raise Exception("账号%s加钱失败 "% acctid)
        finally:
            cursor.close()
    
    
    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
            


       
if  __name__== "__main__" :
    source_acctid = 11
    target_acctid = 12
    #目标人
    money = 100

    conn = MySQLdb.Connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd ='root',
            db = 'imooc',
            charset = 'utf8'
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception, e:
        print "出现问题："+ str(e)
    finally:
        conn.close()






















# # #encoding: utf-8  
# # import sys  
# # reload(sys)  
# # sys.setdefaultencoding('utf8')  
# # import MySQLdb
# # import MySQLdb.cursors

# # conn = MySQLdb.Connect(
# # 			host = '127.0.0.1',
# # 			port = 3306,
# # 			user = 'root',
# # 			passwd ='root',
# # 			db = 'imooc',
# # 			charset = 'utf8'
# # 	)
# # print conn
# # conn.autocommit(False)
# # cursor = conn.cursor()
# # print cursor


# # conn.close()
# # cursor.close()

# import sys
# import MySQLdb

# class TransferMoney(object):
# 	"""docstring for TransferMoney"""
# 	def __init__(self, conn):
# 		self.conn = conn
# 	def transfer(self,source_acctid,target_acctid,money):
# 		try:
# 			self.check_acct_available(source_acctid)
# 			self.check_acct_available(target_acctid)
# 			self.has_enough_money(source_acctid,money)
# 		    self.reduce_money(target_acctid,money)
# 		    self.conn.commit()
# 		except Exception as e:
# 			self.conn.rollback()
# 			raise e
			
# if _name_="_main_":
# 	source_acctid = sys.argv[1]
# 	target_acctid = sys.argv[2]
# 	money = sys.argv[3]

# 	conn = MySQLdb.Connect(
# 			host = '127.0.0.1',
# 			port = 3306,
# 			user = 'root',
# 			passwd ='root',
# 			db = 'imooc',
# 			charset = 'utf8'
# 	)
# 	tr_money = TransferMoney(conn)

# 	try:
# 		tr_money.transfer(source_acctid,target_acctid,money)
# 	except Exception, e:
# 		print "出现问题："+ str(e)
# 	finally:
# 		conn.close()

