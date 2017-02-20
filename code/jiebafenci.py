#encoding: utf-8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import jieba


#基于规则，与基于统计
#jieba：基于前缀词典进行词图扫描，构成全部可能分词结果的有向无环图，
#动态规划查找最大概率路径


# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
# # # 使用
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut(u'他来到了网易杭研大厦')  # 默认是精确模式
# # # print(", ".join(seg_list))

# # #遍历数组方式

# for i in seg_list:
# 	print i




# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所, 后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))




# 关键词提取
import jieba.analyse
# 基于TF-IDF：
# TF词频，反向文档词频。100份文档都出现过这词是很普通的词
content = u'中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'
# keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
# for item in keywords:
# 	print item[0],item[1]
#topk返回前多少个，withweight权重，允许返回词性






# 基于TextRank：
# 词的共性关系。在某一个视窗范围内，上海和自来水出现就有关系。如果某一词词和其他词都有关系
# 那么说明该词关键
# 


# keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# for item in keywords:
# 	print item[0],item[1]




# 词性标注
# 
import jieba.posseg as pseg
words = pseg.cut(content)
for word, flag in words:
	print('%s, %s' % (word, flag))

# 词性列表
# 1. 名词 (1个一类，7个二类，5个三类)
# n 名词
# nr 人名
# nr1 汉语姓氏
# nr2 汉语名字
# nrj 日语人名
# nrf 音译人名
# ns 地名
# nsf 音译地名
# nt 机构团体名
# nz 其它专名
# nl 名词性惯用语
# ng 名词性语素

# 2. 时间词(1个一类，1个二类)
# t 时间词
# tg 时间词性语素

# 3. 处所词(1个一类)
# s 处所词 (家中、门外、境内、西方……)

# 4. 方位词(1个一类)
# f 方位词

# 5. 动词(1个一类，9个二类)
# v 动词
# vd 副动词
# vn 名动词
# vshi 动词“是”
# vyou 动词“有”
# vf 趋向动词
# vx 形式动词
# vi 不及物动词（内动词）
# vl 动词性惯用语
# vg 动词性语素

# 6. 形容词(1个一类，4个二类)
# a 形容词
# ad 副形词
# an 名形词
# ag 形容词性语素
# al 形容词性惯用语

# 7. 区别词(1个一类，2个二类)
# b 区别词 (主要、整个、所有……)
# bl 区别词性惯用语

# 8. 状态词(1个一类)
# z 状态词

# 9. 代词(1个一类，4个二类，6个三类)
# r 代词
# rr 人称代词
# rz 指示代词
# rzt 时间指示代词
# rzs 处所指示代词
# rzv 谓词性指示代词
# ry 疑问代词
# ryt 时间疑问代词
# rys 处所疑问代词
# ryv 谓词性疑问代词
# rg 代词性语素

# 10. 数词(1个一类，1个二类)
# m 数词
# mq 数量词

# 11. 量词(1个一类，2个二类)
# q 量词
# qv 动量词
# qt 时量词

# 12. 副词(1个一类)
# d 副词

# 13. 介词(1个一类，2个二类)
# p 介词
# pba 介词“把”
# pbei 介词“被”

# 14. 连词(1个一类，1个二类)
# c 连词
# cc 并列连词

# 15. 助词(1个一类，15个二类)
# u 助词
# uzhe 着
# ule 了 喽
# uguo 过
# ude1 的 底
# ude2 地
# ude3 得
# usuo 所
# udeng 等 等等 云云
# uyy 一样 一般 似的 般
# udh 的话
# uls 来讲 来说 而言 说来
# uzhi 之
# ulian 连 （“连小学生都会”）

# 16. 叹词(1个一类)
# e 叹词

# 17. 语气词(1个一类)
# y 语气词(delete yg)

# 18. 拟声词(1个一类)
# o 拟声词

# 19. 前缀(1个一类)
# h 前缀

# 20. 后缀(1个一类)
# k 后缀

# 21. 字符串(1个一类，2个二类)
# x 字符串
# xx 非语素字
# xu 网址URL

# 22. 标点符号(1个一类，16个二类)
# w 标点符号
# wkz 左括号，全角：（ 〔 ［ ｛ 《 【 〖 〈 半角：( [ { <
# wky 右括号，全角：） 〕 ］ ｝ 》 】 〗 〉 半角： ) ] { >
# wyz 左引号，全角：“ ‘ 『
# wyy 右引号，全角：” ’ 』
# wj 句号，全角：。
# ww 问号，全角：？ 半角：?
# wt 叹号，全角：！ 半角：!
# wd 逗号，全角：， 半角：,
# wf 分号，全角：； 半角： ;
# wn 顿号，全角：、
# wm 冒号，全角：： 半角： :
# ws 省略号，全角：…… …
# wp 破折号，全角：—— －－ ——－ 半角：--- ----
# wb 百分号千分号，全角：％ ‰ 半角：%
# wh 单位符号，全角：￥ ＄ ￡ ° ℃ 半角：$