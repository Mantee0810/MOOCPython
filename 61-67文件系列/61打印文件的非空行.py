
file = open('latex.log','r',encoding='utf-8')
count = 0
for line in file:
    line = line.strip('\n')
    if len(line)!= 0:
        count += 1

file.close()

print(count)