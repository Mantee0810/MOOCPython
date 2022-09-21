
def reverse(str):
    if str=='':
        return str
    else:
        ans = reverse(str[1:]) + str[0]
        return ans

str = input("输入需要反转的字符串：")
ans = reverse(str)
print("反转后的结果为：",ans)

