'''     w = wordcloud.WordCloud()
        方法：w.generate(txt)  向词云中加载文本txt
             w.to_file(filename)  将词云输出为图像文件，后缀.png或.jpg
        步骤：
            1.配置对象参数
            2.加载词云文本
            3.输出词云文件

        wordcloud.WordCloud()的参数：
            1.width -- 生成图片的宽度
            2.height-- 生成图片的高度
            3.min_font_size -- 词云中字体的最小字号
            4.max_font_size -- 词云中字体的最大字号
            5.font_step -- 字号的步进间隔
            6.font_path -- 字体文件路径    以.tcc或.TTF结尾的字符串
            7.max_words -- 显示的最大单词数
            8.stop_words -- 词云的排除词列表    以字典形式输入
            9.background_color -- 词云的背景颜色
            10.mask -- 指定词云形状
                eg.
                    from scipy.misc import imread
                    mk = imread('pic.png')
                    w = wordcloud.WordCloud(mask=mk)
'''