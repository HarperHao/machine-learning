import hashlib
import os
import sys

filename = sys.argv[1]
if os.path.isfile(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    data = ''.join(lines)
a=(hashlib.md5(data.encode()).hexdigest())
print(a)
