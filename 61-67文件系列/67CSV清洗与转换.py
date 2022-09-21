file = open('data.csv','r')
txt_list = []

for line in file:
    line = line.strip('\n')
    line = line[::-1]
    txt_list.append(line)

txt_list = txt_list[::-1]

for i in range(len(txt_list)):
    txt_list[i] = txt_list[i].replace(',',';')
    txt_list[i] = txt_list[i].replace(' ', '')
    print(txt_list[i])
