#encoding: utf-8  
import sys   #引用sys模块进来，并不是进行sys的第一次加载  
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

# 1.变量

# 1.1数值
# 
a = 1
b = 2


# 1.2字符串
# 
c = 'hello'
d = '你好he'


# # 1.2.1字符串拼接
# print a+b
# print c +',' +d #字符串拼接用加号相连


# # 1.2.2字符串长度len()
# print len(c)
# print len(d) #一个中文字符utf8编码后是占3个字符


# 1.2.3切片
# print c[0] #位置下标从0开始
# print c[-1] #倒数第一个字符
# print d[0:3] #第0到2字符
# print c[1:5] #返回下标从1到4的片段，即第二个到第五个字符
# print c[1:-1], c[:5], c[3:] #不提供，表示从最左端开始或一直到最右端



# # 1.3列表
# # 列表好比一条队伍，里面依次存放着多个变量。列表和字符串类似，
# # 但字符串中的每个元素都是字符，而列表中的每个元素可以是任意类型的变量
# a = [] #定义一个空列表

# # 1.3.1使用append()向尾部追加
# a.append(1) 
# a.append(2.1) 
# a.append('hello')

# # 1.3.2insert()把元素插入到指定的位置
# a.insert(0,'mtianyan')
# print a
# print len(a)
# a[1] = 100
# print a

# # 1.3.3 del删除某个元素
# del a[0]
# print a

# # 1.3.4 pop() 删除某个元素
# a.pop() #默认删除list最后一个
# a.pop(1) #删除指定下标
# print a





# #1.4 元组

# # 元组和列表类似，唯一的不同是元组中的元素在初始化之后不能再更改，
# # 因此可以理解成一个只读的变量。

# a = (1,2,3)
# # 尝试修改元组中的元素会报错
# a[0] = 2
# print a





# 1.5 字典
# 

# # 1.5.1使用{}定义一个字典
# a = {}

# a = {'k1': 1,'k2':2.1,'k3':"hello"}

# # 1.5.2注释：多行注释
# '''
# 下面是一行很厉害代码
# 下面是一行很厉害代码
# 下面是一行很厉害代码
# 下面是一行很厉害代码
# '''

# # 1.5.3使用key来赋值value
# a['k4'] = 'world'
# a['k5'] = 'world2'

# print a 
# # 1.5.4此处可以看出字典是无序的，因此不能通过索引下标访问，只能通过key

# print a['k4']

# # 1.5.5使用 has_key() 判断字典中是否有某个key
# print a.has_key('k5')


# 1.6保留字符
# 保留字符赋值将报错
# import = 1 




# 1.7行和缩进

# 在Python中，代码块的边界不是通过大括号等符号进行显式划分，
# 而是通过行的缩进实现的。连续相同缩进水平的代码处于同一个代码块，
# 在使用 for 、 while 、 if 、 try 等语法时需要注意每行代码的缩进。




# 1.8运算符
a = 1
b = 2

# # 1.8.1算术运算符+，-，*，/，%，即加、减、乘、除、取余
# print a+b
# print float(a)/b


# # 1.8.2比较运算符：==，!=，>，<，>=，<=，
# # 即等于、不等于、大于、小于、大于等于、小于等于

# print a == b
# print a != b


# # 1.8.3赋值运算符：=，+=，-=，*=，/=，%=，
# # 即赋值、加赋值、减赋值、乘赋值、除赋值、取余赋值
# a +=1
# # 等价于 a = a + 1
# print a

# # 1.8.4逻辑运算符
# a1 = True
# a2 = False
# print a1 or a2




# 2 条件语句
# 在写代码的时候，
# 往往需要根据某些条件进行判断，并根据判断结果执行不同的分支代码。

# # 2.1 if 语句 elif else
# c = 1
# if c == 1:
# 	print 11111
# elif c ==2:
# 	print 3333
# else:
# 	print 2222


# # 2.2循环

# # 2.2.1while 循环

# # while 循环的思想是，
# # 只要某一条件成立，就不断执行循环体里的代码，直到条件不再成立。
# c = 1
# while c < 10:
#  # 一定要记得在循环体里修改条件变量
#  # 否则可能导致死循环
# 	print c
# 	c += 1


# # 2.2.2 for循环
# for x in xrange(1,5):
# 	print x




# 2.3for循环遍历字典和列表

a = {'k1': 1,'k2':2.1,'k3':"hello"}
b = [1,2.1,'hello']
c = (1,2,3)



# # 2.3.1 遍历列表b
# for i in b:
# 	print i
## 遍历列表，这里的i只是一个临时变量，取别的名称也行


# # 2.3.2遍历元组c
# for i in c:
# 	print i


# # 2.3.3 遍历字典

# # 同时遍历key和value
# for key,value in a.items():
# 	print key,value

# # 遍历字典的全部key，这里的key也只是一个临时变量，名称不重要
# for key in a.keys():
# 	print key

# # 遍历字典的全部value，这里的value也只是一个临时变量，名称不重要
# for value in a.values():
# 	print value


# # 3 循环控制

# # 循环控制主要包括三种： pass 、 continue 、 break 。
# # pass 表示什么也不做，只是占一行代码的位置；
# # continue 表示立即退出本轮循环，继续执行后续轮循环；
# # break 表示立即推出循环，后续循环也不再执行。


# for x in xrange(0, 10):
#     if x == 5:
#         pass
#     else:
#         print x


# for x in xrange(0, 10):
#     if x == 5:
#         continue
#     print x


# for x in xrange(0, 10):
#     if x == 5:
#         break
#     print x

#  # 4 时间
 
 
# import time

# a = int(time.time()) #获取当前时间

# print a,type(a)
# # 从1970到现在秒数



# # 时间戳转时间文本
# a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))
# print a

# # 时间文本转时间戳，精确到秒
# a = '2016-10-01 10:00:00'
# timeStamp = int(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))
# print timeStamp