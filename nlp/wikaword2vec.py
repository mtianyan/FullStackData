#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


# 加载包
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 训练模型
# sentences = LineSentence('../data/wiki.zh.word.text')
#LineSentence 将每一行读入然后存入列表,列表中每一项为一个词

# model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=2)
#size词向量维度，窗口长度，少于5次的不管，work线程

# 保存模型
# model.save('../model/word_embedding_128')

# # 加载模型
model = Word2Vec.load("../model/word_embedding_128")

# 使用模型
# items = model.most_similar(u'中国')
# for item in items:
# 	print item[0],item[1]


print model.similarity(u'男人',  u'女人')
print model.similarity(u'人', u'狗')
print model.similarity(u'人',u'猪')
