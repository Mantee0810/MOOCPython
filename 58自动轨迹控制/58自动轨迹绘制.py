'''   基本思路：
            1.定义数据文件格式（接口）
            2.编写程序，根据文件接口解析参数绘制图形
            3.编制数据文件
                                                    '''

import turtle

# 绘画环境
turtle.title('自动轨迹绘制')
turtle.setup(800,600)
turtle.pensize(3)

f = open('58数据文件.txt','r')

def Get_Row(file):
    row = 0
    while True:
        line = file.readline()
        if line=='':
            break
        row += 1
    return row

def Get_Line_Matrix(file):
    line_matrix = []
    for line in file:
        if line=='':
            break
        line = line.replace('\n','')
        line = line.split(',')
        line = list(map(eval,line))
        line_matrix.append(line)
    return line_matrix

row = Get_Row(f)
f.seek(0)
line_matrix = Get_Line_Matrix(f)

f.close()
for i in range(row):
    turtle.pencolor(int(line_matrix[i][3]),int(line_matrix[i][4]),int(line_matrix[i][5]))
    turtle.forward(int(line_matrix[i][0]))
    if int(line_matrix[i][1])==0:
        turtle.left(int(line_matrix[i][2]))
    else:
        turtle.right(int(line_matrix[i][2]))

turtle.hideturtle()
turtle.done()




