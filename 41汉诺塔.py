
count = 0
def Hanoi(n,start,mid,end):
    global count
    if n==1:
        print("第{}个圆盘：{}->{}".format(1,start,end))
        count += 1
    else:
        Hanoi(n-1,start=start,mid=end,end=mid)
        print("第{}个圆盘：{}->{}".format(n,start,end))
        count +=1
        Hanoi(n-1,start=mid,end=end,mid=start)

Hanoi(5,'a','b','c')
print(count)



