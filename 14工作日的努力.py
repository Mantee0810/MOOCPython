# 工作日的力量

factor = input('输入每天的变化量：')
factor = float(factor)
power = 1
for i in range(365):
    if i%7 in [0,1,2,3,4]:
        power *= (1+factor)
    if i%7 in [5,6]:
        power *= (1-factor)
print("一年之后，power值为：{:.2f}".format(power))


