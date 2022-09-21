try:
    high,wight = eval(input("请输入身高（m）和体重（kg）[逗号隔开]："))

    bmi = wight/ pow(high,2)

    nation = [18.5,24,28]
    internation = [18.5,25,30]

    for i in range(2):
        if i==0:
            print("国内标准为：",end='')
            str = nation
        else:
            print("国际标准为：",end='')
            str = internation

        if bmi<str[0]:
            print("偏瘦")
        elif str[0]<=bmi<str[1]:
            print("标准")
        elif str[1]<=bmi<str[2]:
            print("偏胖")
        else :
            print("肥胖")
except TypeError:
    print("请输入两个数值")
except:
    print("非法输入")


