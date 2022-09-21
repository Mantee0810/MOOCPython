'''     组合数据类型的三种表达形式
        集合、序列、映射（字典）
        字典是键值对的集合，键值对之间是无序的
        采用大括号{}或dict（）创建
        键值对用冒号：表示
        注意：集合和字典都是用{}表示
        但是d = {}默认用来生成字典类型
        所以只能用set（）生成空集合            '''

d = {'China':'Beijing','American':'Washington','Japan':'Tokyo'}

# 删除键k对应的数据值
del d['Japan']
print(d)

# 判断元素是否在字典中
print('China' in d)

# 返回所有键的信息
print(d.keys())

# 返回所欲值的信息
print(d.values())

# 返回所有键值对信息
print(list(d.items()))

# key存在则返回相应值，否则返回default
d.get('Australia','None')

# key存在则取出并删除相应值，否则返回default
d.pop('American','None')

# 以元组形式随机取出一个键值对
d.popitem()

# 返回元素个数
print(len(d))

c = {'China':'Beijing','American':'Washington','Japan':'Tokyo'}
for k in c:
    print(c[k])

print(c.get('Ababa','Who knows'))

# 删除所有键值对
c.clear()



