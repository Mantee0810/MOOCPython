import jieba
import wordcloud


def Cwordcloud(file):
    # 第一步：获取文本字符串
    file = open(file,'r',encoding='utf-8')
    txt = file.read()
    txt_list = jieba.lcut(txt)
    txt_str = ' '.join(txt_list)
    file.close()
    # 第二步：制作词云
    stop_words = {'的', '了', '和', '在', '对', '不同', '我们', '大小', '中', '为', '是', '进行'}
    w = wordcloud.WordCloud(background_color='white',font_path='STXINGKA.TTF',stopwords=stop_words)
    w.generate(txt_str)
    w.to_file('词云绘制.png')


def Ewordcloud(file):
    file = open(file,'r',encoding='utf-8')
    txt = file.read()
    file.close()
    w = wordcloud.WordCloud(background_color='white')
    w.generate(txt)
    w.to_file('词云绘制.png')


language = eval(input('制作中文词云输入1，制作英文词云输入2：'))
file_name = input('请带后缀地输入文本名称：')

if language==1:
    Cwordcloud(file_name)
elif language==2:
    Ewordcloud(file_name)
else:
    print("请重新输入")
