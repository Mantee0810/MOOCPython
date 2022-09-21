# 输入3  输出星期三

# 方法1
# weekid = input("输入数字（1-7）：")
# week = '星期一星期二星期三星期四星期五星期六星期日'
# pos = (eval(weekid)-1)*3
# output = week[pos:pos+3]
# print(output)

# 方法2
weekid = input("输入数字（1-7）：")
weekstr = '一二三四五六日'
print('星期'+weekstr[eval(weekid)-1])

