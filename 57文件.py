'''         文件的两种形式
            文本文件（全文统一编码）、二进制文件
            处理文件步骤：打开-操作-关闭
            txt.open()和txt.close()转换文件的存储状态和占用状态
            变量名 = open（文件名，打开模式）
            文件打开模式          描述
            r               只读模式，默认
            w               覆盖写
            x               创建写
            a               追加写
            b               二进制文件模式
            t               文本文件模式
            +               在原功能基础上增加同时读写功能
                                                         '''

'''
            file = open(...)
                file.read(size=-1)         
                    以字符串的形式读入全部内容，有参数则读取前size长度
                file.readline(size=-1)
                    以字符串的形式读入一行内容，有参数则读取前size长度
                file.readlines(hint=-1)
                    每行是一个字符串，所有行的字符串形成一个列表，有参数则读入前hint行
                    
                file.write(str)
                    向文件写入字符串或字节流
                file.writelines(list)
                    将一个元素全为字符串的列表写入文件
                file.seek(offset)
                    调整指针位置（0开头，1当前，2结尾）
                    
'''

