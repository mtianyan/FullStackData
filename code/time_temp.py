#encoding: utf-8  
import sys   #引用sys模块进来，并不是进行sys的第一次加载  
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

# 时间戳指的是从1970年1月1日0时0分0秒开始，
# 到某一时刻所经历的秒数，可以是整数或者小数，后者的精度更高
import time
a = time.time()
print a
# 时间戳转时间文本
a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))
print a

# %Y 、 %m 等都是时间字段，前者表示四位的年份，后者表示两位的月份

# 时间文本转时间戳，精确到秒
a = '2016-10-01 10:00:00'
timeStamp = int(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))
print timeStamp