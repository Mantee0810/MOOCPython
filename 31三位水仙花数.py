
def  Estimate_Narcissus(num3):
    a = num3 // 100
    num2 = num3 - a*100
    b = num2 // 10
    num1 = num2 -b*10
    c = num1
    if pow(a,3)+pow(b,3)+pow(c,3)==num3:
        return num3
    else:
        return False

for i in range(100,1000):
    if Estimate_Narcissus(i):
        print(i,end=',')




