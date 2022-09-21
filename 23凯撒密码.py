
full_upper_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
full_lower_str = full_upper_str.lower()
full_str = full_lower_str + full_upper_str
full_list = list(full_str)

def KaiSa(char):
    num_sgn = ord(char)
    if char in ['x','y','z','X','Y','Z']:
        new_num = num_sgn -23
    else:
        new_num = num_sgn + 3
    new_char = chr(new_num)
    return new_char

str = input()

old_list = list(str)
new_list = []
for i in old_list:
    if i in full_list:
        i = KaiSa(i)
    else:
        i = i
    new_list.append(i)

new_str = ''.join(new_list)
print(new_str)

