
def rid_of_unit(get_str):
    get_num = get_str[:-1]
    num = float(get_num)
    return num

temp_str = input("输入想要转换的温度值（带单位C或F）：")

if 'c'==temp_str[-1] or 'C'==temp_str[-1]:
    c = rid_of_unit(temp_str)
    f = c*1.8+32
    print('将摄氏度转换为华氏度，结果为：{}F'.format(f))
elif 'f' == temp_str[-1] or 'F' == temp_str[-1]:
    f = rid_of_unit(temp_str)
    c = (f-32)/1.8
    print('将华氏度转换为摄氏度，结果为：{}C'.format(c))
elif temp_str.isdigit():
    print("重新输入时，请带单位：")
else :
    print("输入类型错误，请重试")









