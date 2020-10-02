f = open(r'K:\638q.txt', 'r', encoding='utf-8')
f1 = open(r"K:\638_.txt", 'w', encoding='utf-8')
for line in f.readlines():
    if len(line) > 0:
        if line[0] == '2' and line[1] == '0' or (line[0:4] == "[图片]") or (
                line[0:4] == "[表情]" or ('http' in line) or ('@' in line)) \
                or ('2019' in line) or ('群签到'in line) or ('红包'in line)\
                or ('int'in line) or ('QQ查看'in line)\
                or ('rchild'in line)or('return'in line)\
                or('struct student'in line)or('baidu'in line):
            pass
        else:
            f1.write(line)
