
height, weight = eval(input())
BMI = weight / pow(height, 2)
if BMI<18.5:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'偏瘦',国内'偏瘦'")
if 18.5<=BMI<24:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'正常',国内'正常'")
if 24<=BMI<25:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'正常',国内'偏胖'")
if 25<=BMI<28:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'偏胖',国内'偏胖'")
if 28<=BMI<30:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'偏胖',国内'肥胖'")
if 30<=BMI:
    print("BMI数值为:{:.2f}".format(BMI))
    print("BMI指标为:国际'肥胖',国内'肥胖'")



