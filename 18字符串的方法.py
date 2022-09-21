#
# 方法一定要用a.b的形式使用
# 特指其中的b
# 也是函数的一种

'''
        format函数中，大括号内容的意义和顺序
            <序号>：默认0,1,2  大括号和format内容对应顺序
            <：>：引导符号
            <填充>：用于填充的单个字符
            <对齐>：<左对齐  >右对齐  ^居中对齐
            <宽度>：设定的输出宽度
            <，>：数字的千位分隔符
            <.精度>：浮点数小数精度  或   字符串最大输出长度
            <类型>：整数类型b,c,d,o,x,X   浮点数类型e,E,f,%

'''


str = '1tDH~ kfcdhx2a'

# 大小写转换
print(str.upper())
print(str.lower())

# 分割
print(str.split('~'))

# 计数
print(str.count('d'))

# 替换
print(str.replace('2a','liangan'))

# 居中
print(str.center(2*len(str),'-'))

# 删除两侧字符
print(str.strip('112a'))

# 分隔
print('.'.join(str))
