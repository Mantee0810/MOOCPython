import random

print("这是一个帮你做决定的小程序，你现在有什么纠结的事吗？\n"
      "输入1，帮你选择；输入2，帮你排序；输入其他，退出程序")

try:
    i = eval(input("请输入："))

    if i==1:
        print("你现在有几个心动选项？")
        j = eval(input("请输入："))
        print("它们分别是：（每次输入后回车）")
        c_list = []
        for k in range(j):
            alternative = input("请输入第{}个备选项：".format(k + 1))
            c_list.append(alternative)
        ans = random.choice(c_list)
        print("我的建议是选择{}".format(ans))

    elif i==2:
        print("你现在有几个备选项？")
        j = eval(input("请输入："))
        print("它们分别是：（每次输入后回车）")
        s_list = []
        for k in range(j):
            alternative = input("请输入第{}个备选项：".format(k+1))
            s_list.append(alternative)
        random.shuffle(s_list)
        print("我建议的排序是：",s_list)

except:
    print('已退出程序')





