
def func(n):
    if n==0:
        return 1
    else:
        ans = n*func(n-1)
        return ans

n = eval(input("输入需要计算的阶乘数："))

print(func(n))



