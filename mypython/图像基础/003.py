"""Pillow库学习"""
# from PIL import Image
#
# # img = Image.open('3.jpg')
# # img.show()
# # 透明度混合
# # img2 = Image.new("RGB", img.size, "red")
# # Image.blend(img, img2, alpha=0.5).show()
# # 遮罩混合处理
# # img3 = Image.open('4.jpg')
# # img3.resize(img.size)
# # r, g, b = img3.split()
# # Image.composite(img3, img, g).show()
# # 图片的缩放
# # img = Image.open('3.jpg')
# # img2 = img.copy()
# # img2.thumbnail((200, 200))
# # img2.show()
# # 图片的剪切复制
# # img = Image.open('3.jpg')
# # img1 = img.copy()
# # img2 = img1.crop((200, 200, 320, 320))
# # img1.paste(img2, (30, 30))
# # img1.show()
# # 图片的转换
# # img = Image.open('3.jpg')
# # img.transpose(Image.FLIP_LEFT_RIGHT).show()
# # 图片的分割和合并
# # img = Image.open('3.jpg')
# # img1 = Image.open('4.jpg')
# # img1 = img1.resize(img.size)
# # r1, g1, b1 = img.split()
# # r2, g2, b2 = img1.split()
# # mode = [r1, g2, b2]
# # img3 = Image.merge("RGB", mode)
# # img3.show()
# #PIL滤镜
# from PIL import Image, ImageFilter
#
# img = Image.open('4.jpg')
# w, h = img.size
# img_output = Image.new('RGB', (2 * w, h))
# img_output.paste(img, (0, 0))
# img_filter1 = img.filter(ImageFilter.GaussianBlur)  # 高斯模糊
# img_filter2 = img.filter(ImageFilter.EDGE_ENHANCE)  # 边缘增强
# img_filter3 = img.filter(ImageFilter.FIND_EDGES)  # 寻找边缘滤镜
# filters = []
# filters.append(img_filter1)
# filters.append(img_filter2)
# filters.append(img_filter3)
# for i in filters:
#     img_output.paste(i, (w, 0))
#     img_output.show()
#添加文字
from PIL import Image, ImageFont, ImageDraw

img = Image.open('4.jpg')
# print(img.size)
draw_pen = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw_pen.text((100, 100), 'Hao', font=font, fill='red')
#font = ImageFont.truetype('STXINGKA.TTF', 30)
draw_pen.text((100, 200), "Hao", font=font, fill="red")
img.show()
