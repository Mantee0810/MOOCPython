
get_str = input()

dic = set(get_str)

sum = 0
for i in dic:
    sum += eval(i)

print(sum)