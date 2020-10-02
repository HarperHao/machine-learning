import wordcloud
import jieba
import imageio

mk = imageio.imread('chinamap.png')
f = open(r'K:/638_.txt', encoding='utf-8`')
text = f.read()
str1 = ''.join(jieba.lcut(text))
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='white',
                        scale=15,
                        font_path='msyh.ttc',
                        mask=mk,)
w.generate(str1)
w.to_file('638.jpg')
f.close()


