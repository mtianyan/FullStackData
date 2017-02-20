#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
f =open('ucr.py',"ab+")
# 以二进制a+方式打开
print type(f)
# print f.read().strip()
# only read one line
# print f.readline()
# readmanylines去除格式
print f.readlines()

#写入
#文件打开方式，r只读（read），
#w只写（write），
#a追加（append），
#r+/w+ 读写方式打开，
#r+可以从头写去替换，
#w+是全部删掉去替换，
#a+追加和读写方式，
#感觉以后a+用得更多
#d选项二进制方式打开
#
f.close()
f.readline() //默认读取一行
f.readline(100)  //若这行超过100个字节，则返回这行的100个字节。
                 //如果这行小于100个字节，则全部返回
f.readline(2) //读取'ww'
f.readline(2) //追加读取'w.'
f.readline()  //剩下返回


readlines([size]) -> size==>buff
import io
io.DEFAULT_BUFFER_SIZE

iter:使用迭代器读取大文件

f = open('imooc.txt')
iter_f = iter(f)
line = 0
for line in iter_f:
    line += 1

lines
writes（str）字符串写入文件
writelins 写多行到文件
# 当使用open的写操作时，
# 会先写到内核的缓冲区，
# 当缓冲区写满的时候才会自动写到磁盘。
# 如果没满，那么需要使用flush或者close操作来写入f
f.flush()
ps
cat /proc/pid/limits

f.fileno()
file.fileno 属性
如果打开一个文件，这个属性+1
Python文件为什么要关闭
1：将写缓存同步到磁盘；
2：linux系统中每个进程打开的文件个数是有限的；
3：如果打开文件数到了系统限制，在打开文件就会失败；
ps
cat /proc/pid/limits

print f.tell() 文件指针当前位置
f.seek(0,os.SEEK_SET) 改变文件指针当前位置 
第一个参数是相对偏移量 第二个参数是
os.SEEK_SET 文件起始位置
os.SEEK_CUR 文件当前位置 
os.SEEK_END 文件结束位置
相对值
file.fileno 属性