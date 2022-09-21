
'''     集合的核心作用：数据去重
        放入集合中的元素是不可变数据类型
        无序，元素唯一，
        不可变组合数据类型：整数、浮点数、复数、字符串、元组 '''

t = {99,8,10,'y','m','t'}
c = {99,1,28,'llc'}

# 并集
print(t|c)

# 差
print(t-c)

# 交集
print(t&c)

# 补集
print(t^c)

# 子集关系
print(t<=c)

# 添加元素
t.add('mt')

# 移除，不会报错
t.discard(99)

# 移除，无则报错
try:
    t.remove(1999)
except:
    pass

# 随机取出一个元素
print(c.pop())

# 拷贝
t1 = t.copy()
print(t1)

# 清除所有元素
t1.clear()
print(t1)

# 长度
print(len(t))

# 判断元素与集合
print(8 in t)

# 判断元素与集合
print(99 not in t)

# 强制集合
ly = [1999,1999,8,10,1,28]
print(set(ly))



