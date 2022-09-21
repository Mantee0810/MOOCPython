#
# 获得用户输入的一个正整数输入，输出该数字对应的中文字符表示
# 0到9对应的中文字符分别是：零一二三四五六七八九
#
# 输入示例1
# 123
# 输出示例1
# 一二三
#
# 输入示例2
# 9876543210
# 输出示例2
# 九八七六五四三二一零

keys = ['0','1','2','3','4','5','6','7','8','9']
values = ['零','一','二','三','四','五','六','七','八','九']
dic = dict( zip(keys, values) )

nb_str = input()
nb_list = list(nb_str)
ans_list = []
for i in nb_list:
    ans_list.append(dic[i])
ans_str = ""
for j in ans_list:
    ans_str += j
print(ans_str)

