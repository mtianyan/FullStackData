#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
# #变量可以指向函数；
# # 2.函数名实际上就是一个指向函数的一个变量；
# 函数名和普通的而变量没有区别；
# 3.高阶函数就是可以接受一个函数作为变量的函数。
# 变量可以指向函数，函数的参数可以接收变量，
# 一个函数可以接受另一个函数作为参数。
# 

def add(x,y,f):
	return f(x)+f(y)
print add(-5,9,abs)

# map()是 Python 内置的高阶函数，
# 它接收一个函数 f 和一个 list，
# 并通过把函数 f 依次作用在 list 的每个元素上，
# 得到一个新的 list 并返回

def format_name(s):
    return s[0].upper() + s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])

# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，
# 一个函数 f，一个list，
# 但行为和 map()不同，
# reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，
# 并返回最终结果值。

#求积
def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])


# filter()函数是 Python 内置的另一个有用的高阶函数，
# filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，
# 返回 True或 False，
# filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list。



def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])


import time

def performance(f):
    def log_time(x):
        t1= time.time()
        res = f(x)
        t2=time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return res
    return log_time

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)



同名模块，放入不同包

p1.a

包必须有__init__，

包是文件夹，模块是文件。


class Person(object):

    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
  
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print Person.how_many()

p1 = Person('Bob')

print Person.how_many()

