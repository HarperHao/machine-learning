"""词云002"""
import wordcloud
import jieba
import imageio

mk = imageio.imread('chinamap.png')
f = open(r'K:/dou.txt', encoding='utf-8`')
text = f.read()
str1 = ''.join(jieba.lcut(text))
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='white',
                        scale=15,
                        font_path='msyh.ttc',
                        mask=mk,
                        stopwords={'quot', 'align center', 'center', 'It amp', '阅读面页章节尾部广告',
                                   'div', 'align', 'bk', 'amp it', '闻言',
                                   '片刻后', '因此', '第一更', '第三更', '第二更', '顿时',
                                   '所以', '闻言','当然'})
w.generate(str1)
w.to_file('dou2.jpg')
f.close()
