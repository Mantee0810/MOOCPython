'''     jieba分词的三种模式
            精确模式：文本精确切开，没有冗余
            全模式：找出文本所有可能的词组，有冗余
            搜索引擎模式：在精确模式基础上，对长词再次切分
'''

import jieba
s = '婷婷是世界上最可爱的小宝贝'

# 精确模式
a = jieba.lcut(s)
print(a)

# 全模式
b = jieba.lcut(s,cut_all=True)
print(b)

# 搜索引擎模式
c = jieba.lcut_for_search(s)
print(c)

# 向词典增加新词
jieba.add_word("婷婷宝贝")



