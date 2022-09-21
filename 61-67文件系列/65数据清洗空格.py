file = open('data.csv','r')
txt = file.read()

txt = txt.replace(' ','')

print(txt)

file.close()


