
import random

r = []

for i in range(5):
    num = random.random()
    r.append(num)

print(r)

# 范围内的随机整数
r1 = random.randint(5,100)
print(r1)

# 范围内指定步长的随机整数
r2 = random.randrange(100,400,5)
print(r2)

# 生成一个k比特长的整数
r3 = random.getrandbits(16)
print(r3)

# 生成范围内随机小数
r4 = random.uniform(1,5)
print(r4)

# 从序列中随机选取一个元素
r5 = random.choice([1,2,3,4,5,6,7,8,9])
r6 = random.choice([1,2,3,4,5,6,7,8,9])
print(r5,r6)

# 把序列随机排列后返回
s = [1,2,3,4,5,6,7,8,9]
random.shuffle(s)
print(s)

