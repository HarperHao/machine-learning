"""判断一个文件是否为GIF图像文件"""


def isGif(fname):
    with open(fname, 'rb')as fp:
        first4 = fp.read(4)
    return first4 == b'GIF8'


print(isGif(r'K:\1.jpg'))
