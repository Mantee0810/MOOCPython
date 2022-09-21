
def Su(num):
    if num==2:
        return num
    for i in range(2,num):
        if num % i == 0:
            return False
    return num

sum = 0

for i in range(2,100):
    if Su(i):
        sum += i

print(sum)
