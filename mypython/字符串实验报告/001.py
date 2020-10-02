"""
检查并判断密码字符串的安全强度
"""
import string


def check(pwd):
    if not isinstance(pwd, str) or len(pwd) < 6:
        return "密码至少包含六个字符"
    d = {1: '弱', 2: '中', 3: '良', 4: '优'}
    r = [False] * 4
    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in string.punctuation:
            r[3] = True
    return d.get(r.count(True), 'Error')


pwd = input("请输入你的密码：")
level = check(pwd)
print(level)
