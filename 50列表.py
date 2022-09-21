'''     序列类型的拓展
        用方括号或list（）创建
        元素类型可以不同        '''

ls = ['cat','dog','mouse','human']

# 这种方式把lt的指针指向了ls所在的列表，并没有重新创建
lt = ls

# 只有用方括号[]或者list（）函数，才算真正创建了一个新列表
ll = list(ls)

# 替换元素
ls[0] = '?'
print(ls)

# 用列表lt替换ls切片后对应子元素列表
ls[1:3] = lt
print(ls)

# 删除
del lt[1]
print(lt)

# 更新列表
ls += lt
print(ls)

# 列表乘n
print(ls*3)

ls = ['cat','dog','mouse','human']

# 插入元素
ls.append('wow')

# 生成新列表
ls.copy()

# 插入元素
ls.insert(2,'xixi')

# 取出第i个元素并删除
ls.pop(3)

# 删除第一个出现的元素x
ls.remove('dog')

# 将列表元素反转
ls.reverse()

# 删除列表所有元素
ls.clear()



