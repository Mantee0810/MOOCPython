#
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求
# 如果输入值是0，直接输出"Hello World"
# 如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）
# 如果输入值小于0，以垂直方式输出"Hello World"
#


num = input()
num= float(num)
str = "Hello World"
if num == 0:
    print(str)
elif num > 0:
    i,j = 0,1
    while (i <= len(str)-1)&(j <= len(str)):
        if (i < len(str)-1)&(j < len(str)):
            print(str[i],str[j],sep='')
            i += 2
            j += 2
        else:
            print(str[i])
            i += 2
elif num < 0:
    for i in str:
        print(i)



