"""
使用正则表达式提取字符串中的电话号码
"""
import re

telNumber = 'Suppose my Phone No.is 0123-4566893,yours if 011-99816674'
pattern = re.compile(r'(\d{3,4})-(\d{7,8})')
index = 0
while True:
    matchResult = pattern.search(telNumber, index)
    if not matchResult:
        break
    print('-' * 30)
    print('Success:')
    for i in range(2):
        print("匹配到的内容:", matchResult.group(i), '开始位置:', matchResult.start(i), "结束位置：", matchResult.end(i), "前后间隔：",
              matchResult.span(i))
        index = matchResult.end(2)
