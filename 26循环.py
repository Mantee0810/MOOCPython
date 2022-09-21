
s = 'life sucks'
#
# while s!= '':
#     for c in s:
#         if c=='s':
#             break
#         print(c,end='')
#     s = s[:-1]
# else:
#     print("suck!")

for c in s:
    if c=='f':
        continue
    print(c,end='')
else:
    print("正常退出")
