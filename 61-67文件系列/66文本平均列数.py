def Quit4Add5(num):
    if num-int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

file = open('latex.log','r')

row_num = 0
char_sum = 0
for line in file:
    line = line.strip('\n')
    if len(line) != 0:
        row_num += 1
        char_sum += len(line)

mean = Quit4Add5(char_sum/row_num)

file.close()

print(mean)
