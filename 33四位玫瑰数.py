
def Estimate_Rose4(num4):
    a = num4 // 1000
    num3 = num4 - a*1000
    b = num3 // 100
    num2 = num3 -b*100
    c = num2 // 10
    num1 = num2 - c*10
    d = num1
    if pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)==num4:
        return num4
    else:
        return False

for i in range(1000,10000):
    if Estimate_Rose4(i):
        print(i)



