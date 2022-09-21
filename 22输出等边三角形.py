n = input()
n = eval(n)

row = int((n+1)/2)

for i in range(row):
    num = i*2+1
    output = '*' * num
    print(output.center(n,' '))
