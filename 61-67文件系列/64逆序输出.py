#
# file = open('data.csv','r')
#
# for line in file:
#     line = line.replace('\n','')
#     line = line[::-1]
#     print(line,sep='')
#
# file.close()


f = open("data.csv")
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    ls = ls[::-1]
    print(",".join(ls))
f.close()