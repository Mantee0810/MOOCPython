
file = open('latex.log','r')
dic = {}

for line in file:
    dic[line] = dic.get(line,0)+1

count = 0
for v in dic.values():
    if v==1:
        count += 1

print('共{}独特行'.format(count))

file.close()