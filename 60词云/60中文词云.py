import jieba
import wordcloud
import numpy
from PIL import Image

file = open('chi.txt','r',encoding='utf-8')
txt = file.read()
txt_list = jieba.lcut(txt)
txt_str = ' '.join(txt_list)

pic = Image.open('bg.png')
print(pic,type(pic))
mask = numpy.array(pic)

stop_words = {'的','了','和','在','对','不同','我们','大小','中','为','是','进行'}

w = wordcloud.WordCloud(background_color='white',font_path='STXINGKA.TTF',stopwords=stop_words,mask=mask)
w.generate(txt_str)
w.to_file('chi.png')

file.close()


