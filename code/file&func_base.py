#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


# # 1 写文件
# # 
# # 
# # 1.1重新写模式，打开文件时会将文件内容清空
# fw = open('data.txt','w')
# for x in xrange(1,10):
# 	fw.write(str(x)+'\n')
# fw.close()

# fw = open('data.txt','w')
# for x in xrange(1,20):
# 	fw.write(str(x)+'\n')
# fw.close()




# # 1.2追加写模式，
# # 打开文件后保留原始内容，继续写入
# fw = open('data.txt','a')
# for x in xrange(1,50):
# 	fw.write(str(x)+'\n')
# fw.close()




# # 2 读文件


fr = open('douban_movie_clean.txt','r')

for line in fr:
	print line.strip()
# 	# strip()可以去掉字符串两端的空白字符

# fr.close

# # 3 异常
# # Python代码中可能会出现一些可以预知的问题，
# # 例如字典访问的key不存在。如果不加处理，发生问题的时候Python便会报错并退出，
# # 可能之前跑了很久又要重头再来。
# # 因此，我们需要对可能出现的异常进行捕捉和处理。
# # 异常的结构由 try 、 except 、 else 、 finally 四部分组成。


# try:
# 	print 1
# except Exception as e:
# 	# raise出现错误抛出并中断
# 	print e
# else:
# 	print "No Error"
# finally:
# 	print '一定会执行'



# try:
#     # 尝试执行这些代码
#     print 1 / 0
# except Exception, e:
#     # 如果出现异常就进行处理
#     # e为出现的异常类型
#     print e
# else:
#     # try里的代码没有出错
#     # 可以执行后续工作了
#     print '没有出错'
# finally:
#     # 无论是否出错，都会执行的代码
#     print '一定会执行'




# # # 函数
# # 函数

# # 函数的作用是代码模块化，将可重用的代码封装成一个函数，
# # 这样在需要使用的时候就只需调用写好的函数即可，而不用重新写一遍代码。
# # 函数的使用包括两个部分，函数的定义和函数的调用。
# # 除此之外，函数可以有一个或多个参数，
# # 参数之间以逗号分开，为函数的功能提供更多的灵活性。

# def hello():
# 	print 'hello'

# hello()
# hello()


# def hello(name,name2):
# 	print 'hello' + ','+ name +' and '+name2

# hello('python','java')
