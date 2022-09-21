
import wordcloud

file = open('eng.txt', 'r', encoding='utf-8')
txt = file.read()

c = wordcloud.WordCloud(max_words=60,background_color='white',font_path='msyh.ttc')
c.generate(txt)
c.to_file('eng.png')


file.close()
