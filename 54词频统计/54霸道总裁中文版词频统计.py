
import jieba

txt = open("异瞳断天机.txt",'r',encoding='utf-8').read()

# 输出word_list为列表格式，里面包含各种符号
word_list = jieba.lcut(txt)
print(word_list)
counts = {}

for w in word_list:
    if len(w)==1:
        continue
    else:
        counts[w] = counts.get(w,0)+1
item = list(counts.items())
item.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = item[i]
    print("{:<10}{:>5}".format(word,count))


