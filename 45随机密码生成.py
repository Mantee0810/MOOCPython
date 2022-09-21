
# 输入N ，输出三个以N为长度的密码
import random

N = eval(input())

random.seed(17)
min = 10**(N-1)
max = 10**N
for i in range(3):
    print(random.randint(min,max))


