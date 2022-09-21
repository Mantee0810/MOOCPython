
sgn = -1
sum = 0

for i in range(1,967):
    if i%2==0:
        add = i*sgn
        sum += add
    else:
        add = i
        sum += add

print(sum)



