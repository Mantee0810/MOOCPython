

def cal(a,*b):
    ans = a
    for i in b:
        ans *= i
    return ans

nums = input()

print(eval("cal{}".format(eval(nums))))


