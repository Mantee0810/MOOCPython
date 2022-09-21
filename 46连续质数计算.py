

def Su(num):
    if num==2:
        return num
    for i in range(2,num):
        if num % i == 0:
            return False
    return num

N = eval(input())
if N==int(N):
    N = N
else:
    N = int(N) + 1

list = []

while True:
    if Su(N):
        list.append(N)
    if len(list)==5:
        break
    N += 1

list = str(list)
list = list.replace(' ','')
for i in list[1:-1]:
    print(i,end='',sep='')



