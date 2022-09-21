
xingzuo = []
for i in range(12):
    sgn = chr(9800+i)
    xingzuo.append(sgn)
print('十二星座符号为：',xingzuo)

code = []
for i in range(12):
    num_sgn = ord(xingzuo[i])
    code.append(num_sgn)
print('十二星座的Unicode编码为：',code)




