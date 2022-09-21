
def func(n):
    if n==1 or n==2:
        return 1
    else:
        ans = func(n-1)+func(n-2)
        return ans

n = eval(input("输入值："))
ans = func(n)
print('输出值{}'.format(ans))
