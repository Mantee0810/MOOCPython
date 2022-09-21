
file = open('latex.log','r')
txt = file.read()
print('共{}字符'.format(len(txt)),end='')

dic = {}
start = ord('a')
char_list = []

for i in range(26):
    sgn = chr(start+i)
    char_list.append(sgn)

for char in txt:
    if char in char_list:
        dic[char] = dic.get(char,0)+1

for j in range(len(dic)):
    char = chr(start+j)
    show = dic[char]
    print(',{}:{}'.format(char,show),end='')
