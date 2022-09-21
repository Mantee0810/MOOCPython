
def Get_Num():
    num = []
    IsNum = input("请输入数字：")
    while True:
        if IsNum!='':
            num.append(eval(IsNum))
            IsNum = input("请输入数字：")
        else:
            break
    return num

def Mean(list):
    length = len(list)
    sum = 0
    for i in range(length):
        sum += list[i]
    mean = sum/length
    return mean

def Vari(list):
    mean = Mean(list)
    length = len(list)
    sum = 0
    for i in range(length):
        sum += (list[i]-mean)**2
    vari = (sum/(length-1))**0.5
    return vari

def Median(list):
    list = sorted(list)
    length = len(list)
    if length%2==1:
        i = (length+1)/2
        return list[i]
    else:
        j = int(length/2)
        median = (list[j-1] + list[j])/2
        return median

def main():
    nums = Get_Num()
    print(Mean(nums))
    print(Vari(nums))
    print(Median(nums))

main()