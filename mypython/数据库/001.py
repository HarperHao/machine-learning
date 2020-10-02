"""
sqlite3数据库创建表
"""
import sqlite3

# 创建连接
con = sqlite3.connect(r'K:\SQLite3\first_DB.db')
# 创建游标对象
cur = con.cursor()
# 创建表
sql = """create table t_person(
    pno INTEGER primary key autoincrement,
    pname VARCHAR not null,
    age INTEGER
)
"""
# 执行
try:
    cur.execute(sql)
    print('创造成功')
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    cur.close()
    con.close()
