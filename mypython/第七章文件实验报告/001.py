"""统计指定文件夹大小以及文件和子文件夹数量"""
import os.path

totalSize = 0
fileNum = 0
dirNum = 0


def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum + 1
            totalSize = totalSize + os.path.getsize(sub_path)
        elif os.path.isdir(sub_path):
            dirNum = dirNum + 1
            visitDir(sub_path)


def sizeConvert(size):
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(size / G) + 'G Bytes'
    elif size >= M:
        return str(size / M) + 'M Bytes'
    elif size >= K:
        return str(size / K) + 'K Bytes'
    else:
        return str(size) + 'Bytes'


def main(path):
    if not os.path.isdir(path):
        print("error")
        return
    visitDir(path)


def output(path):
    print('The total size of {} is:{} ({}) Bytes'.format(path, sizeConvert(totalSize), str(totalSize)))
    print("The total number of files in {} is {}".format(path, fileNum))
    print("The total number of  directories in {} is {}".format(path, dirNum))


path = r'K:\编程'
main(path)
output(path)
