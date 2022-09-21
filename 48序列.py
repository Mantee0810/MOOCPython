
'''     具有先后关系的一组元素
        元素之间可以相同，类型可以不同
        序列是一个基类：衍生出了字符串、元组、列表         '''

s = [123,'py','thon']
x = 'py'
t = [456,222,606,135,606]

# 元素是否在序列中
print(x in s)
print(x not in t)

# 连接
print(s+t)

# 将序列复制n次
print(s*3)
print(5*t)

# 索引
print(s[2])

# 切片
print(s[::-1])

# 序列长度
print(len(s))

# 可比较前提下，返回最大最小
print(min(t))

# s.index（x） 索引x出现的位置
print(t.index(606,3))

# s.count(x) 计算x出现的总次数
print(t.count(606))
